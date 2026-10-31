#!/usr/bin/env python3
"""Course state machine for the learn-anything skill.

Owns progress.json, enforces the gate that stops a learner skipping ahead,
schedules spaced-repetition reviews, tracks study time, and re-renders
progress.html after every change. The tutor agent should never edit
progress.json by hand -- go through this script so the log and the dashboard
stay honest.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
TEMPLATE = SKILL_DIR / "assets" / "dashboard-template.html"

LOCKED, UNLOCKED, GENERATED, PASSED = "locked", "unlocked", "generated", "passed"

# Spaced repetition ladder, in days. A confident review moves one rung up.
INTERVALS = [1, 3, 7, 16, 35, 90, 180]
CONFIDENT = 85          # review score at or above this advances the interval
SESSION_CAP_MIN = 240   # a single sitting is never credited more than this
SESSION_STALE_H = 8     # an open session older than this is auto-closed


# ---------------------------------------------------------------- utilities

def now_dt() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def now() -> str:
    return now_dt().isoformat()


def parse_ts(s):
    if not s:
        return None
    try:
        d = datetime.fromisoformat(s)
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def slug(text: str, maxlen: int = 40) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")
    if len(s) > maxlen:
        s = s[:maxlen].rstrip("-")
    return s or "item"


def as_text(md: str, ext: str) -> str:
    """Strip markdown so `.txt` courses read as plain text."""
    if ext != "txt":
        return md
    out = []
    for line in md.splitlines():
        h = re.match(r"^(#{1,6})\s+(.*)$", line)
        if h:
            title = re.sub(r"[*`]", "", h.group(2))
            out.append(title.upper() if len(h.group(1)) == 1 else title)
            out.append(("=" if len(h.group(1)) == 1 else "-") * len(title))
            continue
        line = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
        line = re.sub(r"`([^`]+)`", r"\1", line)
        out.append(line)
    return "\n".join(out)


def die(msg: str, code: int = 1):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def read_json(path: Path):
    if not path.exists():
        die(f"no course found at {path.parent} (missing {path.name}). "
            f"Run `course.py init` first.", 2)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        die(f"{path} is not valid JSON: {e}", 2)


def write_json(path: Path, data) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)


def load(root: Path):
    course = read_json(root / "course.json")
    progress = read_json(root / "progress.json")
    if reap_stale_session(progress):
        write_json(root / "progress.json", progress)
    return course, progress


def save(root: Path, progress) -> None:
    progress["updated"] = now()
    write_json(root / "progress.json", progress)


def log(progress, event: str, detail: str) -> None:
    progress.setdefault("log", []).append({"ts": now(), "event": event, "detail": detail})


# ------------------------------------------------------------ state helpers

def find_module(progress, module_id: str):
    for m in progress["modules"]:
        if m["id"] == module_id:
            return m
    return None


def find_lesson(progress, module_id: str, lesson_id: str):
    m = find_module(progress, module_id)
    if not m:
        return None, None
    for l in m["lessons"]:
        if l["id"] == lesson_id:
            return m, l
    return m, None


def parse_ref(ref: str):
    """'02-locators/04-waiting' -> ('02-locators', '04-waiting')"""
    parts = [p for p in str(ref).split("/") if p]
    if len(parts) != 2:
        die(f"--lesson expects <module-id>/<lesson-id>, got {ref!r}")
    return parts[0], parts[1]


def module_complete(m) -> bool:
    return all(l["status"] == PASSED for l in m["lessons"]) and m["test"]["status"] == PASSED


def module_status(m) -> str:
    if module_complete(m):
        return "complete"
    if any(l["status"] != LOCKED for l in m["lessons"]) or m["test"]["status"] != LOCKED:
        return "active"
    return "locked"


def next_action(progress):
    """First thing the learner still owes, as (kind, module, item)."""
    for m in progress["modules"]:
        for l in m["lessons"]:
            if l["status"] != PASSED:
                return ("lesson", m, l)
        if m["test"]["status"] != PASSED:
            return ("test", m, m["test"])
    fp = progress["finalProject"]
    if fp["status"] != PASSED:
        return ("final", None, fp)
    return ("done", None, None)


def cascade_unlock(progress) -> None:
    """Open exactly what has been earned, and nothing further."""
    prev_module_done = True
    for m in progress["modules"]:
        prev_lesson_done = prev_module_done
        for l in m["lessons"]:
            if prev_lesson_done and l["status"] == LOCKED:
                l["status"] = UNLOCKED
            prev_lesson_done = prev_lesson_done and l["status"] == PASSED
        lessons_done = all(l["status"] == PASSED for l in m["lessons"])
        if prev_module_done and lessons_done and m["test"]["status"] == LOCKED:
            m["test"]["status"] = UNLOCKED
        prev_module_done = prev_module_done and lessons_done and m["test"]["status"] == PASSED
    fp = progress["finalProject"]
    if prev_module_done and fp["status"] == LOCKED:
        fp["status"] = UNLOCKED


def lesson_parts(l):
    """The graded components this lesson needs, as {name: score-or-None}."""
    parts = {"quiz": l.get("quizScore")}
    if l.get("requiresAssignment", True):
        parts["assignment"] = l.get("assignmentScore")
    if l.get("requiresExplain", True):
        parts["explain"] = l.get("explainScore")
    return parts


# --------------------------------------------------- spaced repetition

def new_review(due_days: int = 1):
    return {"due": (now_dt() + timedelta(days=due_days)).isoformat(), "interval": due_days,
            "reps": 0, "lapses": 0, "last": None, "lastScore": None}


def schedule_review(l, score: int) -> None:
    """SM-2-lite: confident recall climbs the ladder, a lapse resets to one day."""
    r = l.get("review") or new_review()
    if score >= CONFIDENT:
        r["reps"] = min(r.get("reps", 0) + 1, len(INTERVALS) - 1)
    elif score < 70:
        r["lapses"] = r.get("lapses", 0) + 1
        r["reps"] = 0
    r["interval"] = INTERVALS[r["reps"]]
    r["due"] = (now_dt() + timedelta(days=r["interval"])).isoformat()
    r["last"] = now()
    r["lastScore"] = score
    l["review"] = r


def review_queue(progress, course=None):
    """Passed lessons whose review is due, most overdue first."""
    out = []
    cmods = {m["id"]: m for m in (course or {}).get("modules", [])}
    for m in progress["modules"]:
        cl = {l["id"]: l for l in cmods.get(m["id"], {}).get("lessons", [])}
        for l in m["lessons"]:
            r = l.get("review")
            if l["status"] != PASSED or not r or not r.get("due"):
                continue
            due = parse_ts(r["due"])
            if due is None or due > now_dt():
                continue
            out.append({
                "module": m["id"], "moduleTitle": m["title"],
                "lesson": l["id"], "title": l["title"],
                "objectives": cl.get(l["id"], {}).get("objectives", []),
                "due": r["due"],
                "daysOverdue": max(0, (now_dt() - due).days),
                "reps": r.get("reps", 0), "lapses": r.get("lapses", 0),
                "lastScore": r.get("lastScore"),
                "testedOut": bool(l.get("testedOut")),
            })
    out.sort(key=lambda x: x["due"])
    return out


# -------------------------------------------------------- session time

def reap_stale_session(progress) -> bool:
    """Close an open session someone forgot about. Returns True if it changed."""
    op = progress.get("openSession")
    if not op:
        return False
    start = parse_ts(op.get("start"))
    if start is None:
        progress["openSession"] = None
        return True
    if (now_dt() - start) < timedelta(hours=SESSION_STALE_H):
        return False
    progress.setdefault("sessions", []).append({
        "start": op["start"], "end": now(),
        "minutes": min(SESSION_CAP_MIN, int((now_dt() - start).total_seconds() // 60)),
        "note": "auto-closed (left open)", "auto": True,
    })
    progress["openSession"] = None
    log(progress, "session_autoclosed", f"open since {op['start']}")
    return True


def time_stats(progress, items_total: int, items_passed: int):
    sessions = progress.get("sessions", [])
    total = sum(s.get("minutes", 0) for s in sessions)
    open_min = 0
    op = progress.get("openSession")
    if op and parse_ts(op.get("start")):
        open_min = min(SESSION_CAP_MIN,
                       int((now_dt() - parse_ts(op["start"])).total_seconds() // 60))

    # daily minutes for the last 21 days, oldest first
    today = now_dt().date()
    buckets = {(today - timedelta(days=i)).isoformat(): 0 for i in range(20, -1, -1)}
    for s in sessions:
        d = parse_ts(s.get("end") or s.get("start"))
        if d and d.date().isoformat() in buckets:
            buckets[d.date().isoformat()] += s.get("minutes", 0)
    if op and parse_ts(op.get("start")):
        k = today.isoformat()
        if k in buckets:
            buckets[k] += open_min
    daily = [{"date": k, "minutes": v} for k, v in buckets.items()]

    starts = [parse_ts(s.get("start")) for s in sessions if parse_ts(s.get("start"))]
    span_days = max(1, (now_dt() - min(starts)).days + 1) if starts else 1
    recent = sum(s.get("minutes", 0) for s in sessions
                 if parse_ts(s.get("end") or s.get("start"))
                 and (now_dt() - parse_ts(s.get("end") or s.get("start"))).days < 28)
    pace = round(recent * 7 / min(28, span_days)) if starts else 0

    per_item = round((total + open_min) / items_passed) if items_passed else None
    remaining = per_item * (items_total - items_passed) if per_item else None
    finish = None
    if remaining and pace > 0 and len(sessions) >= 3:
        finish = (now_dt() + timedelta(days=remaining * 7 / pace)).date().isoformat()

    return {
        "totalMinutes": total + open_min,
        "sessionCount": len(sessions),
        "openMinutes": open_min if op else None,
        "minutesPerItem": per_item,
        "estRemainingMinutes": remaining,
        "pacePerWeek": pace,
        "estFinish": finish,
        "daily": daily,
    }


# --------------------------------------------------------- momentum

STUDY_EVENTS = {
    "session_start", "session_end", "generated", "review",
    "lesson_passed", "lesson_failed", "lesson_partial",
    "test_passed", "test_failed", "final_passed", "final_failed",
    "testout_passed", "testout_failed",
}


def study_days(progress):
    """Every calendar day the learner actually did something, as a set of dates."""
    days = set()
    for s in progress.get("sessions", []):
        d = parse_ts(s.get("end") or s.get("start"))
        if d:
            days.add(d.date())
    op = progress.get("openSession")
    if op and parse_ts(op.get("start")):
        days.add(parse_ts(op["start"]).date())
    for e in progress.get("log", []):
        if e.get("event") in STUDY_EVENTS:
            d = parse_ts(e.get("ts"))
            if d:
                days.add(d.date())
    return days


def streaks(progress):
    """Current and best run of consecutive study days.

    Today not yet studied does not break the streak — yesterday still counts, so the
    streak is lost only after a full day off.
    """
    days = sorted(study_days(progress))
    if not days:
        return {"current": 0, "best": 0, "lastStudyDay": None, "studyDays": 0}
    best = run = 1
    for prev, day in zip(days, days[1:]):
        run = run + 1 if (day - prev).days == 1 else 1
        best = max(best, run)
    today = now_dt().date()
    gap = (today - days[-1]).days
    current = 0
    if gap <= 1:
        current = 1
        for prev, day in zip(reversed(days[:-1]), reversed(days[1:])):
            if (day - prev).days != 1:
                break
            current += 1
    return {"current": current, "best": best,
            "lastStudyDay": days[-1].isoformat(), "studyDays": len(days)}


def wins(progress, st):
    """Earned badges. Every one is derived from a real score — none are participation."""
    lessons = [l for m in progress["modules"] for l in m["lessons"]]
    out = []

    def add(icon, label, detail):
        out.append({"icon": icon, "label": label, "detail": detail})

    if st["lessonsPassed"] >= 1:
        add("🚀", "Off the mark", "first lesson passed")
    if st["modulesComplete"] >= 1:
        add("📦", f"{st['modulesComplete']} module{'s' if st['modulesComplete'] > 1 else ''} cleared",
            "boss fight won")
    flawless = sum(1 for l in lessons if l["status"] == PASSED
                   and all(s is not None and s >= 90 for s in lesson_parts(l).values()))
    if flawless:
        add("💎", f"{flawless} flawless", "90%+ on every component")
    comeback = sum(1 for l in lessons if l["status"] == PASSED and l.get("attempts", 1) > 1)
    if comeback:
        add("🔁", f"{comeback} comeback{'s' if comeback > 1 else ''}", "failed it, then passed it")
    solid = sum(1 for l in lessons if (l.get("review") or {}).get("reps", 0) >= 3)
    if solid:
        add("🧠", f"{solid} stuck", "survived three spaced reviews")
    if st["testedOut"]:
        add("⚡", f"{st['testedOut']} tested out", "credited from a cold placement test")
    if progress["finalProject"]["status"] == PASSED:
        add("🏆", "Course complete", "final project passed")
    return out


# ------------------------------------------------------------------ stats

def stats(progress):
    lessons = [l for m in progress["modules"] for l in m["lessons"]]
    tests = [m["test"] for m in progress["modules"]]
    done = sum(1 for x in lessons + tests if x["status"] == PASSED)
    total = len(lessons) + len(tests) + 1
    if progress["finalProject"]["status"] == PASSED:
        done += 1
    scored = [x["score"] for x in lessons + tests if x.get("score") is not None]
    q = review_queue(progress)
    st = {
        "lessonsTotal": len(lessons),
        "lessonsPassed": sum(1 for l in lessons if l["status"] == PASSED),
        "modulesTotal": len(progress["modules"]),
        "modulesComplete": sum(1 for m in progress["modules"] if module_complete(m)),
        "itemsTotal": total,
        "itemsPassed": done,
        "percent": round(done * 100 / total) if total else 0,
        "averageScore": round(sum(scored) / len(scored)) if scored else None,
        "overrides": sum(1 for x in lessons + tests if x.get("overridden")),
        "testedOut": sum(1 for l in lessons if l.get("testedOut")),
        "reviewsDue": len(q),
        "reviewsOverdue": sum(1 for r in q if r["daysOverdue"] > 0),
    }
    st.update({"time": time_stats(progress, total, done),
               "momentum": streaks(progress)})
    st["wins"] = wins(progress, st)
    return st


# ------------------------------------------------------------------ render

def render(root: Path) -> Path:
    course, progress = load(root)
    payload = {
        "course": course,
        "progress": progress,
        "stats": stats(progress),
        "moduleStatus": {m["id"]: module_status(m) for m in progress["modules"]},
        "reviewQueue": review_queue(progress, course),
        "renderedAt": now(),
    }
    if not TEMPLATE.exists():
        die(f"dashboard template missing at {TEMPLATE}")
    # `</` only ever occurs inside JSON strings, so escaping it keeps the blob
    # from closing the <script> tag it is embedded in.
    blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8").replace("__PROGRESS_DATA__", blob)
    out = root / "progress.html"
    out.write_text(html, encoding="utf-8")
    return out


# -------------------------------------------------------------------- init

COURSE_README = """# {topic}

A gated, hands-on course generated by the **learn-anything** skill.
Depth: **{depth}**{goal_line}  ·  Pass mark: **{threshold}%**

## How this works

1. Open `progress.html` in a browser to see where you are.
2. Work through modules **in order**. Lessons unlock one at a time.
3. Each lesson gives you content, worked examples, a quiz, an assignment, and a
   spoken explain-back check. Your tutor grades all three — you need **{threshold}%**
   on each to move on.
4. Passed lessons come back as **spaced-repetition reviews** days and weeks later.
   Let too many pile up and new lessons stop unlocking until you clear them.
5. Each module ends with a cumulative test. Passing it unlocks the next module.
6. Finish every module to unlock the final project.

You cannot skip ahead. That is the point. If you already know a module, ask to be
**tested out** of it — you take the module test cold at a higher bar ({testout}%).

## Modules

{modules}

## Final project

**{final_title}** — {final_summary}

## Files

- `progress.json` — the source of truth for your progress (don't edit by hand)
- `progress.html` — the dashboard, regenerated after every graded item
- `course.json` — the fixed curriculum plan
- `.grading/` — answer keys and rubrics. **Tutor only. Reading these is cheating yourself.**
"""


def cmd_init(args):
    root = Path(args.root).expanduser().resolve()
    if (root / "progress.json").exists() and not args.force:
        die(f"a course already exists at {root}. Resume it, or pass --force to overwrite.", 3)

    plan = read_json(Path(args.plan).expanduser())
    for key in ("topic", "modules"):
        if key not in plan:
            die(f"plan is missing required key {key!r}")
    if not plan["modules"]:
        die("plan has no modules")

    ext = plan.get("format", "md")
    if ext not in ("md", "txt"):
        die("format must be 'md' or 'txt'")
    threshold = int(plan.get("passThreshold", 70))
    testout = int(plan.get("testOutThreshold", 85))
    review_gate = int(plan.get("reviewGate", 3))

    course = {
        "topic": plan["topic"],
        "depth": plan.get("depth", "practitioner"),
        "goal": plan.get("goal", ""),
        "format": ext,
        "passThreshold": threshold,
        "testOutThreshold": testout,
        "reviewGate": review_gate,
        "created": now(),
        "modules": [],
        "finalProject": {},
    }
    progress = {
        "topic": plan["topic"],
        "created": now(),
        "updated": now(),
        "passThreshold": threshold,
        "testOutThreshold": testout,
        "reviewGate": review_gate,
        "format": ext,
        "modules": [],
        "finalProject": {},
        "sessions": [],
        "openSession": None,
        "log": [],
    }

    for mi, pm in enumerate(plan["modules"], 1):
        mid = f"{mi:02d}-{slug(pm['title'])}"
        cmod = {
            "id": mid,
            "title": pm["title"],
            "summary": pm.get("summary", ""),
            "objectives": pm.get("objectives", []),
            "lessons": [],
            "test": {
                "id": "module-test",
                "title": pm.get("test", {}).get("title", f"{pm['title']} — module test"),
                "summary": pm.get("test", {}).get("summary", ""),
            },
        }
        pmod = {"id": mid, "title": pm["title"], "lessons": [],
                "test": {"title": cmod["test"]["title"], "status": LOCKED,
                         "score": None, "attempts": 0, "generated": False,
                         "completedAt": None, "overridden": False, "testedOut": False}}

        for li, pl in enumerate(pm.get("lessons", []), 1):
            lid = f"{li:02d}-{slug(pl['title'])}"
            cmod["lessons"].append({
                "id": lid,
                "title": pl["title"],
                "summary": pl.get("summary", ""),
                "objectives": pl.get("objectives", []),
                "requiresAssignment": bool(pl.get("assignment", True)),
                "requiresExplain": bool(pl.get("explain", True)),
            })
            pmod["lessons"].append({
                "id": lid, "title": pl["title"], "status": LOCKED,
                "quizScore": None, "assignmentScore": None, "explainScore": None,
                "score": None, "attempts": 0, "generated": False, "completedAt": None,
                "requiresAssignment": bool(pl.get("assignment", True)),
                "requiresExplain": bool(pl.get("explain", True)),
                "overridden": False, "testedOut": False, "review": None,
            })
            (root / mid / lid).mkdir(parents=True, exist_ok=True)
            (root / ".grading" / mid / lid).mkdir(parents=True, exist_ok=True)

        if not cmod["lessons"]:
            die(f"module {pm['title']!r} has no lessons")

        course["modules"].append(cmod)
        progress["modules"].append(pmod)

        obj = "\n".join(f"- {o}" for o in cmod["objectives"]) or "- (to be filled in)"
        lessons_list = "\n".join(
            f"{i}. **{l['title']}** — {l['summary']}" for i, l in enumerate(cmod["lessons"], 1)
        )
        (root / mid / f"module.{ext}").write_text(
            as_text(
                f"# Module {mi}: {pm['title']}\n\n{cmod['summary']}\n\n"
                f"## By the end of this module you can\n\n{obj}\n\n"
                f"## Lessons\n\n{lessons_list}\n\n"
                f"## Module test\n\n{cmod['test']['title']}\n\n"
                f"Cumulative and closed-book. You need {threshold}% to unlock the next module.\n"
                f"Already know this material? Ask to test out — same test, cold, at {testout}%.\n",
                ext,
            ),
            encoding="utf-8",
        )

    fp = plan.get("finalProject", {})
    course["finalProject"] = {
        "title": fp.get("title", f"{plan['topic']} capstone"),
        "summary": fp.get("summary", ""),
        "requirements": fp.get("requirements", []),
        "stretch": fp.get("stretch", []),
    }
    progress["finalProject"] = {
        "title": course["finalProject"]["title"], "status": LOCKED,
        "score": None, "attempts": 0, "generated": False,
        "completedAt": None, "overridden": False,
    }
    (root / "final-project").mkdir(parents=True, exist_ok=True)
    (root / ".grading" / "final-project").mkdir(parents=True, exist_ok=True)

    (root / ".grading" / "DO-NOT-READ.txt").write_text(
        "Answer keys and grading rubrics live here.\n"
        "They are for the tutor agent. Reading them only cheats you out of the course.\n",
        encoding="utf-8",
    )

    modules_md = "\n".join(
        f"{i}. **{m['title']}** — {m['summary']} ({len(m['lessons'])} lessons)"
        for i, m in enumerate(course["modules"], 1)
    )
    goal_line = f"  ·  Goal: **{course['goal']}**" if course["goal"] else ""
    (root / f"README.{ext}").write_text(
        as_text(COURSE_README.format(
            topic=plan["topic"], depth=course["depth"], threshold=threshold,
            testout=testout, goal_line=goal_line, modules=modules_md,
            final_title=course["finalProject"]["title"],
            final_summary=course["finalProject"]["summary"] or "briefed when you get there",
        ), ext),
        encoding="utf-8",
    )

    cascade_unlock(progress)
    log(progress, "course_created",
        f"{plan['topic']} · {course['depth']} · {len(course['modules'])} modules")
    write_json(root / "course.json", course)
    save(root, progress)
    out = render(root)

    print(f"Course created at {root}")
    print(f"  {len(course['modules'])} modules, "
          f"{sum(len(m['lessons']) for m in course['modules'])} lessons, "
          f"pass mark {threshold}%, test-out bar {testout}%")
    print(f"  dashboard: {out}")
    first_m = progress["modules"][0]
    print(f"  unlocked:  {first_m['id']}/{first_m['lessons'][0]['id']}")


# ------------------------------------------------------------------ status

def fmt_mins(m):
    if not m:
        return "0m"
    return f"{m // 60}h {m % 60:02d}m" if m >= 60 else f"{m}m"


def cmd_status(args):
    root = Path(args.root).expanduser().resolve()
    course, progress = load(root)
    st = stats(progress)
    q = review_queue(progress, course)

    if args.json:
        kind, m, item = next_action(progress)
        print(json.dumps({
            "topic": progress["topic"], "stats": st,
            "next": {"kind": kind,
                     "module": m["id"] if m else None,
                     "item": item["id"] if item and "id" in item else (
                         "final-project" if kind == "final" else None),
                     "title": item["title"] if item else None},
            "reviewQueue": q,
            "modules": progress["modules"],
            "finalProject": progress["finalProject"],
        }, indent=2))
        return

    t = st["time"]
    bar_len = 28
    filled = round(st["percent"] * bar_len / 100)
    print(f"\n  {progress['topic']}  ·  {course['depth']}")
    print(f"  [{'#' * filled}{'.' * (bar_len - filled)}] {st['percent']}%   "
          f"{st['itemsPassed']}/{st['itemsTotal']} items"
          + (f"   avg {st['averageScore']}%" if st["averageScore"] is not None else ""))
    line = f"  time {fmt_mins(t['totalMinutes'])} over {t['sessionCount']} sessions"
    if t["pacePerWeek"]:
        line += f"   pace {fmt_mins(t['pacePerWeek'])}/wk"
    if t["estFinish"]:
        line += f"   est. finish {t['estFinish']}"
    print(line)
    if progress.get("openSession"):
        print(f"  session OPEN — {fmt_mins(t['openMinutes'])} so far")
    mo = st["momentum"]
    if mo["current"] >= 2 or st["wins"]:
        bits = []
        if mo["current"] >= 2:
            bits.append(f"{mo['current']}-day streak (best {mo['best']})")
        bits += [f"{w['icon']} {w['label']}" for w in st["wins"]]
        print("  " + "   ".join(bits))
    print()

    marks = {PASSED: "[x]", GENERATED: "[~]", UNLOCKED: "[ ]", LOCKED: " . "}
    for m in progress["modules"]:
        ms = module_status(m)
        head = {"complete": "DONE  ", "active": "ACTIVE", "locked": "LOCKED"}[ms]
        print(f"  {head}  {m['id']}  {m['title']}")
        if ms == "locked":
            continue
        for l in m["lessons"]:
            score = f"  {l['score']}%" if l.get("score") is not None else ""
            flag = "  (override)" if l.get("overridden") else ""
            flag += "  (tested out)" if l.get("testedOut") else ""
            print(f"          {marks[l['status']]} {l['id']}  {l['title']}{score}{flag}")
        t2 = m["test"]
        score = f"  {t2['score']}%" if t2.get("score") is not None else ""
        print(f"          {marks[t2['status']]} module-test  {t2['title']}{score}")
    fp = progress["finalProject"]
    score = f"  {fp['score']}%" if fp.get("score") is not None else ""
    print(f"  {'DONE  ' if fp['status'] == PASSED else 'LOCKED' if fp['status'] == LOCKED else 'OPEN  '}"
          f"  final-project  {fp['title']}{score}")

    if q:
        print(f"\n  REVIEWS DUE ({len(q)}):")
        for r in q[:8]:
            od = f"{r['daysOverdue']}d overdue" if r["daysOverdue"] else "due today"
            print(f"          {r['module']}/{r['lesson']}  {r['title']}  ({od})")
        if len(q) > 8:
            print(f"          … and {len(q) - 8} more")

    kind, m, item = next_action(progress)
    print()
    if kind == "done":
        print("  Course complete. Nothing left to unlock.")
    elif kind == "final":
        print(f"  Next: the final project — {item['title']}")
    else:
        print(f"  Next: {m['id']}/{item.get('id', 'module-test')} — {item['title']}"
              f"  [{item['status']}]")
    gate_n = progress.get("reviewGate", 3)
    if gate_n and len(q) >= gate_n:
        print(f"  BLOCKED: {len(q)} reviews due (limit {gate_n}). Clear reviews to keep going.")
    if st["overrides"]:
        print(f"  note: {st['overrides']} item(s) were force-unlocked.")
    if st["testedOut"]:
        print(f"  note: {st['testedOut']} lesson(s) were tested out of.")
    print()


# -------------------------------------------------------------------- gate

def resolve_target(progress, args):
    if args.lesson:
        mid, lid = parse_ref(args.lesson)
        m, l = find_lesson(progress, mid, lid)
        if not m:
            die(f"no module {mid!r}. Run `status` to see the real ids.")
        if not l:
            die(f"no lesson {lid!r} in module {mid!r}.")
        return "lesson", m, l
    if args.test:
        m = find_module(progress, args.test)
        if not m:
            die(f"no module {args.test!r}.")
        return "test", m, m["test"]
    if args.final:
        return "final", None, progress["finalProject"]
    die("specify one of --lesson <m>/<l>, --test <m>, or --final")


def blocking_reason(progress, kind, module, item) -> str:
    nk, nm, ni = next_action(progress)
    where = (f"{nm['id']}/{ni.get('id', 'module-test')} — {ni['title']}"
             if nm else (ni["title"] if ni else "nothing"))
    target = (f"{module['id']}/{item.get('id', 'module-test')}" if module
              else "the final project")
    if nk == "lesson":
        need = [k for k, v in lesson_parts(ni).items() if v is None] or ["a passing re-attempt"]
        return (f"{target} is LOCKED.\n"
                f"Current position: {where}\n"
                f"Outstanding: {' and '.join(need)}"
                + (f" (last score {ni['score']}%, pass mark {progress['passThreshold']}%)"
                   if ni.get("score") is not None else ""))
    if nk == "test":
        return (f"{target} is LOCKED.\n"
                f"Current position: the module test for {nm['id']} — {ni['title']}\n"
                f"Outstanding: pass that test at {progress['passThreshold']}% or better.")
    return f"{target} is LOCKED.\nCurrent position: {where}"


def cmd_gate(args):
    root = Path(args.root).expanduser().resolve()
    course, progress = load(root)
    kind, module, item = resolve_target(progress, args)
    label = f"{module['id']}/{item.get('id', 'module-test')}" if module else "final-project"

    if item["status"] == LOCKED:
        print(blocking_reason(progress, kind, module, item), file=sys.stderr)
        print("\nBLOCKED — do not teach or reveal this material.", file=sys.stderr)
        sys.exit(4)

    # Reviews block starting something new, never finishing what is underway.
    gate_n = progress.get("reviewGate", 3)
    q = review_queue(progress, course)
    if gate_n and len(q) >= gate_n and item["status"] == UNLOCKED:
        print(f"{label} is unlocked, but {len(q)} spaced-repetition reviews are due "
              f"(limit {gate_n}).", file=sys.stderr)
        print("Run the reviews first — old material is slipping:", file=sys.stderr)
        for r in q[:6]:
            od = f"{r['daysOverdue']}d overdue" if r["daysOverdue"] else "due today"
            print(f"  {r['module']}/{r['lesson']}  {r['title']}  ({od})", file=sys.stderr)
        print("\nBLOCKED PENDING REVIEW — run `course.py review --root <root>`.",
              file=sys.stderr)
        sys.exit(5)

    print(f"OK — {label} is {item['status']}. Cleared to teach.")
    if q:
        print(f"  ({len(q)} review(s) due — worth clearing before the next new lesson.)")


# ---------------------------------------------------------------- mutations

def cmd_mark_generated(args):
    root = Path(args.root).expanduser().resolve()
    _, progress = load(root)
    kind, module, item = resolve_target(progress, args)
    if item["status"] == LOCKED:
        die("that item is locked — run `gate` first; content must not be written ahead of time.", 4)
    item["generated"] = True
    if item["status"] == UNLOCKED:
        item["status"] = GENERATED
    label = f"{module['id']}/{item.get('id', 'module-test')}" if module else "final-project"
    log(progress, "generated", label)
    save(root, progress)
    render(root)
    print(f"marked generated: {label}")


def _pass_fail(progress, item, score, threshold, label, kind):
    item["attempts"] = item.get("attempts", 0) + 1
    item["score"] = score
    if score >= threshold:
        item["status"] = PASSED
        item["completedAt"] = now()
        log(progress, f"{kind}_passed", f"{label} — {score}% (attempt {item['attempts']})")
        return True
    if item["status"] == PASSED:
        item["status"] = GENERATED
        item["completedAt"] = None
    log(progress, f"{kind}_failed", f"{label} — {score}% (attempt {item['attempts']})")
    return False


def cmd_grade(args):
    root = Path(args.root).expanduser().resolve()
    _, progress = load(root)
    threshold = progress["passThreshold"]

    for v in (args.quiz, args.assignment, args.explain, args.score, args.final):
        if v is not None and not (0 <= v <= 100):
            die("scores must be between 0 and 100")

    if args.lesson:
        mid, lid = parse_ref(args.lesson)
        m, l = find_lesson(progress, mid, lid)
        if not l:
            die(f"no lesson {args.lesson!r}")
        if l["status"] == LOCKED:
            die("that lesson is locked — you cannot grade work that was never unlocked.", 4)
        if args.quiz is None and args.assignment is None and args.explain is None:
            die("give at least one of --quiz, --assignment, --explain")
        if args.quiz is not None:
            l["quizScore"] = args.quiz
        if args.assignment is not None:
            l["assignmentScore"] = args.assignment
        if args.explain is not None:
            l["explainScore"] = args.explain

        parts = lesson_parts(l)
        label = f"{mid}/{lid} — {l['title']}"
        missing = [k for k, v in parts.items() if v is None]

        if missing:
            l["attempts"] = l.get("attempts", 0) + 1
            log(progress, "lesson_partial", f"{label} — {', '.join(missing)} still outstanding")
            cascade_unlock(progress)
            save(root, progress)
            render(root)
            print(f"recorded, but NOT passed: {label}")
            print("  " + "  ".join(f"{k}={v}" for k, v in parts.items()))
            print(f"  still outstanding: {', '.join(missing)}. The next lesson stays locked.")
            return

        vals = list(parts.values())
        avg = round(sum(vals) / len(vals))
        ok = min(vals) >= threshold
        l["attempts"] = l.get("attempts", 0) + 1
        l["score"] = avg
        if ok:
            l["status"] = PASSED
            l["completedAt"] = now()
            if not l.get("review"):
                l["review"] = new_review()
            log(progress, "lesson_passed", f"{label} — {avg}% (attempt {l['attempts']})")
        else:
            if l["status"] == PASSED:
                l["status"] = GENERATED
                l["completedAt"] = None
            weak = [k for k, v in parts.items() if v < threshold]
            log(progress, "lesson_failed",
                f"{label} — {avg}% (attempt {l['attempts']}, weak: {', '.join(weak)})")

    elif args.test:
        m = find_module(progress, args.test)
        if not m:
            die(f"no module {args.test!r}")
        t = m["test"]
        if t["status"] == LOCKED:
            die("that module test is locked — finish the module's lessons first.", 4)
        if args.score is None:
            die("module tests need --score")
        label = f"{m['id']} module test"
        ok = _pass_fail(progress, t, args.score, threshold, label, "test")

    elif args.final is not None:
        fp = progress["finalProject"]
        if fp["status"] == LOCKED:
            die("the final project is locked — every module must be complete first.", 4)
        ok = _pass_fail(progress, fp, args.final, threshold, fp["title"], "final")
        label = fp["title"]

    else:
        die("specify --lesson <m>/<l>, --test <module-id>, or --final <score>")

    if args.note:
        log(progress, "feedback", f"{label}: {args.note}")

    cascade_unlock(progress)
    save(root, progress)
    render(root)

    print(("PASSED: " if ok else "NOT PASSED: ") + label)
    if ok:
        kind, m2, item2 = next_action(progress)
        if kind == "done":
            print("  Course complete. Everything is unlocked and graded.")
        elif kind == "final":
            print(f"  Unlocked: the final project — {item2['title']}")
        else:
            print(f"  Unlocked: {m2['id']}/{item2.get('id', 'module-test')} — {item2['title']}")
        if args.lesson:
            r = find_lesson(progress, *parse_ref(args.lesson))[1]["review"]
            print(f"  First review scheduled for {parse_ts(r['due']).date().isoformat()}.")
    else:
        print(f"  Below the {threshold}% pass mark. Nothing new unlocks — reteach and retry.")
    print(f"  dashboard: {root / 'progress.html'}")


# ------------------------------------------------------------------ review

def cmd_review(args):
    root = Path(args.root).expanduser().resolve()
    course, progress = load(root)

    if args.lesson and args.score is not None:
        mid, lid = parse_ref(args.lesson)
        m, l = find_lesson(progress, mid, lid)
        if not l:
            die(f"no lesson {args.lesson!r}")
        if l["status"] != PASSED:
            die("that lesson has not been passed yet — there is nothing to review.")
        if not (0 <= args.score <= 100):
            die("scores must be between 0 and 100")
        before = (l.get("review") or {}).get("reps", 0)
        schedule_review(l, args.score)
        r = l["review"]
        verdict = ("solid" if args.score >= CONFIDENT
                   else "shaky" if args.score >= progress["passThreshold"] else "lapsed")
        log(progress, "review", f"{mid}/{lid} — {args.score}% ({verdict})")
        if args.note:
            log(progress, "feedback", f"review {mid}/{lid}: {args.note}")
        save(root, progress)
        render(root)
        print(f"review recorded: {mid}/{lid} — {args.score}% ({verdict})")
        print(f"  interval {before} -> {r['reps']} rung  ·  next due "
              f"{parse_ts(r['due']).date().isoformat()} ({r['interval']}d)")
        if verdict == "lapsed":
            print("  Reset to a 1-day interval. Reteach this before moving on.")
        left = review_queue(progress, course)
        print(f"  {len(left)} review(s) still due." if left else "  Review queue is clear.")
        return

    if args.lesson or args.score is not None:
        die("recording a review needs both --lesson <m>/<l> and --score N")

    q = review_queue(progress, course)
    if args.json:
        print(json.dumps(q, indent=2))
        return
    if not q:
        nxt = []
        for m in progress["modules"]:
            for l in m["lessons"]:
                r = l.get("review")
                if l["status"] == PASSED and r and r.get("due"):
                    nxt.append((r["due"], f"{m['id']}/{l['id']}", l["title"]))
        print("\n  Review queue is clear.")
        if nxt:
            nxt.sort()
            print(f"  Next up: {nxt[0][1]} — {nxt[0][2]} on "
                  f"{parse_ts(nxt[0][0]).date().isoformat()}\n")
        else:
            print("  Nothing scheduled yet — pass a lesson first.\n")
        return

    print(f"\n  {len(q)} review(s) due — ask these before any new material.\n")
    for r in q:
        od = f"{r['daysOverdue']}d overdue" if r["daysOverdue"] else "due today"
        print(f"  {r['module']}/{r['lesson']}  {r['title']}")
        print(f"      {od}  ·  rung {r['reps']}/{len(INTERVALS) - 1}"
              f"  ·  lapses {r['lapses']}"
              + (f"  ·  last {r['lastScore']}%" if r["lastScore"] is not None else "")
              + ("  ·  tested out" if r["testedOut"] else ""))
        for o in r["objectives"][:3]:
            print(f"      - {o}")
    gate_n = progress.get("reviewGate", 3)
    if gate_n and len(q) >= gate_n:
        print(f"\n  New lessons are BLOCKED until this drops below {gate_n}.")
    print("\n  Record each with: course.py review --root <root> "
          "--lesson <m>/<l> --score N\n")


# ---------------------------------------------------------------- test-out

def cmd_test_out(args):
    root = Path(args.root).expanduser().resolve()
    _, progress = load(root)
    m = find_module(progress, args.module)
    if not m:
        die(f"no module {args.module!r}")
    if not (0 <= args.score <= 100):
        die("scores must be between 0 and 100")

    idx = progress["modules"].index(m)
    for earlier in progress["modules"][:idx]:
        if not module_complete(earlier):
            die(f"module {earlier['id']} is not complete — test out of modules in order.", 4)
    if module_complete(m):
        die(f"module {m['id']} is already complete.")

    bar = progress.get("testOutThreshold", 85)
    if args.score < bar:
        log(progress, "testout_failed", f"{m['id']} — {args.score}% (bar {bar}%)")
        cascade_unlock(progress)
        save(root, progress)
        render(root)
        print(f"NOT TESTED OUT: {m['id']} — {m['title']}")
        print(f"  {args.score}% is below the {bar}% test-out bar. Take the module normally.")
        print("  The wrong answers show exactly which lessons to pay attention to.")
        return

    for l in m["lessons"]:
        if l["status"] != PASSED:
            l["status"] = PASSED
            l["score"] = args.score
            l["testedOut"] = True
            l["completedAt"] = now()
            l["attempts"] = l.get("attempts", 0) + 1
            # Tested-out material is the likeliest to be shaky, so review it soon.
            l["review"] = new_review(due_days=2)
    t = m["test"]
    t["status"] = PASSED
    t["score"] = args.score
    t["testedOut"] = True
    t["completedAt"] = now()
    t["attempts"] = t.get("attempts", 0) + 1

    log(progress, "testout_passed",
        f"{m['id']} — {args.score}% (bar {bar}%), {len(m['lessons'])} lessons credited")
    if args.note:
        log(progress, "feedback", f"test-out {m['id']}: {args.note}")
    cascade_unlock(progress)
    save(root, progress)
    render(root)

    print(f"TESTED OUT: {m['id']} — {m['title']} at {args.score}%")
    print(f"  {len(m['lessons'])} lesson(s) + the module test credited.")
    print("  All of them are queued for review in 2 days — tested-out material is the "
          "likeliest to be thin.")
    kind, m2, item2 = next_action(progress)
    if kind == "done":
        print("  Course complete.")
    elif kind == "final":
        print(f"  Unlocked: the final project — {item2['title']}")
    else:
        print(f"  Unlocked: {m2['id']}/{item2.get('id', 'module-test')} — {item2['title']}")


# ----------------------------------------------------------------- session

def cmd_session(args):
    root = Path(args.root).expanduser().resolve()
    _, progress = load(root)
    t = stats(progress)["time"]

    if args.action == "start":
        if progress.get("openSession"):
            start = parse_ts(progress["openSession"]["start"])
            mins = int((now_dt() - start).total_seconds() // 60)
            print(f"a session is already open ({fmt_mins(mins)} so far, "
                  f"started {progress['openSession']['start']})")
            return
        progress["openSession"] = {"start": now()}
        log(progress, "session_start", "")
        save(root, progress)
        render(root)
        print(f"session started at {progress['openSession']['start']}")
        print(f"  lifetime study time so far: {fmt_mins(t['totalMinutes'])}")
        return

    if args.action == "end":
        op = progress.get("openSession")
        if not op:
            print("no session is open — nothing to end.")
            return
        start = parse_ts(op["start"])
        raw = int((now_dt() - start).total_seconds() // 60)
        mins = min(SESSION_CAP_MIN, raw)
        progress.setdefault("sessions", []).append({
            "start": op["start"], "end": now(), "minutes": mins,
            "note": args.note or "", "auto": False,
        })
        progress["openSession"] = None
        log(progress, "session_end", f"{fmt_mins(mins)}" + (f" — {args.note}" if args.note else ""))
        save(root, progress)
        render(root)
        t2 = stats(progress)["time"]
        print(f"session ended: {fmt_mins(mins)}"
              + (f" (capped from {fmt_mins(raw)})" if raw > mins else ""))
        print(f"  total {fmt_mins(t2['totalMinutes'])} over {t2['sessionCount']} sessions")
        if t2["pacePerWeek"]:
            print(f"  pace {fmt_mins(t2['pacePerWeek'])}/week", end="")
            print(f"  ·  est. finish {t2['estFinish']}" if t2["estFinish"] else "")
        return

    # status
    print(f"\n  study time: {fmt_mins(t['totalMinutes'])} over {t['sessionCount']} sessions")
    if progress.get("openSession"):
        print(f"  session OPEN since {progress['openSession']['start']} "
              f"({fmt_mins(t['openMinutes'])})")
    if t["minutesPerItem"]:
        print(f"  {fmt_mins(t['minutesPerItem'])} per completed item")
    if t["estRemainingMinutes"]:
        print(f"  ~{fmt_mins(t['estRemainingMinutes'])} of work left")
    if t["pacePerWeek"]:
        print(f"  pace {fmt_mins(t['pacePerWeek'])}/week")
    if t["estFinish"]:
        print(f"  estimated finish {t['estFinish']}")
    print()


# ------------------------------------------------------------------- misc

def cmd_unlock(args):
    root = Path(args.root).expanduser().resolve()
    _, progress = load(root)
    kind, module, item = resolve_target(progress, args)
    label = f"{module['id']}/{item.get('id', 'module-test')}" if module else "final-project"

    if item["status"] != LOCKED:
        print(f"{label} is already {item['status']} — nothing to do.")
        return
    if not args.force:
        die("that item is locked. Force-unlocking defeats the point of the course.\n"
            "Only pass --force when the learner has explicitly asked to override the gate, "
            "and always with --reason.", 4)

    item["status"] = UNLOCKED
    item["overridden"] = True
    item["overrideReason"] = args.reason or "no reason given"
    log(progress, "override", f"{label} force-unlocked — {item['overrideReason']}")
    save(root, progress)
    render(root)
    print(f"OVERRIDE: {label} unlocked without being earned.")
    print(f"  reason: {item['overrideReason']}")
    print("  This is permanently recorded in the log and shown on the dashboard.")


def cmd_note(args):
    root = Path(args.root).expanduser().resolve()
    _, progress = load(root)
    log(progress, "note", args.text)
    save(root, progress)
    render(root)
    print("note recorded")


def cmd_render(args):
    root = Path(args.root).expanduser().resolve()
    print(f"wrote {render(root)}")


# --------------------------------------------------------------------- cli

def main():
    p = argparse.ArgumentParser(
        prog="course.py", description="Course state machine for the learn-anything skill.")
    sub = p.add_subparsers(dest="cmd", required=True)

    def with_root(sp):
        sp.add_argument("--root", required=True, help="course root directory")
        return sp

    sp = with_root(sub.add_parser("init", help="scaffold a course from a plan JSON file"))
    sp.add_argument("--plan", required=True)
    sp.add_argument("--force", action="store_true", help="overwrite an existing course")
    sp.set_defaults(func=cmd_init)

    sp = with_root(sub.add_parser("status", help="where the learner is"))
    sp.add_argument("--json", action="store_true")
    sp.set_defaults(func=cmd_status)

    def with_target(sp):
        sp.add_argument("--lesson", help="<module-id>/<lesson-id>")
        sp.add_argument("--test", help="<module-id>")
        sp.add_argument("--final", action="store_true")
        return sp

    sp = with_target(with_root(sub.add_parser(
        "gate", help="check whether an item may be taught (exit 4 locked, 5 reviews due)")))
    sp.set_defaults(func=cmd_gate)

    sp = with_target(with_root(sub.add_parser(
        "mark-generated", help="record that content has been written")))
    sp.set_defaults(func=cmd_mark_generated)

    sp = with_root(sub.add_parser("grade", help="record scores and unlock what was earned"))
    sp.add_argument("--lesson", help="<module-id>/<lesson-id>")
    sp.add_argument("--test", help="<module-id>")
    sp.add_argument("--quiz", type=int, help="lesson quiz score 0-100")
    sp.add_argument("--assignment", type=int, help="lesson assignment score 0-100")
    sp.add_argument("--explain", type=int, help="lesson explain-back (Feynman) score 0-100")
    sp.add_argument("--score", type=int, help="module test score 0-100")
    sp.add_argument("--final", type=int, help="final project score 0-100")
    sp.add_argument("--note", help="one-line feedback for the log")
    sp.set_defaults(func=cmd_grade)

    sp = with_root(sub.add_parser(
        "review", help="list due spaced-repetition reviews, or record one"))
    sp.add_argument("--lesson", help="<module-id>/<lesson-id> to record a review for")
    sp.add_argument("--score", type=int, help="recall score 0-100")
    sp.add_argument("--note", help="one-line feedback for the log")
    sp.add_argument("--json", action="store_true")
    sp.set_defaults(func=cmd_review)

    sp = with_root(sub.add_parser(
        "test-out", help="credit a whole module from a cold placement test"))
    sp.add_argument("--module", required=True)
    sp.add_argument("--score", type=int, required=True)
    sp.add_argument("--note")
    sp.set_defaults(func=cmd_test_out)

    sp = with_root(sub.add_parser("session", help="track study time"))
    sp.add_argument("action", choices=["start", "end", "status"])
    sp.add_argument("--note", help="what you worked on")
    sp.set_defaults(func=cmd_session)

    sp = with_target(with_root(sub.add_parser(
        "unlock", help="force-unlock an item (learner override only)")))
    sp.add_argument("--force", action="store_true")
    sp.add_argument("--reason")
    sp.set_defaults(func=cmd_unlock)

    sp = with_root(sub.add_parser("note", help="append a note to the log"))
    sp.add_argument("--text", required=True)
    sp.set_defaults(func=cmd_note)

    sp = with_root(sub.add_parser("render", help="rebuild progress.html"))
    sp.set_defaults(func=cmd_render)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
