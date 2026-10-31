# `scripts/course.py` reference

Every mutating command rewrites `progress.json` and re-renders `progress.html`.
Never edit `progress.json` by hand.

```bash
python3 scripts/course.py <command> --root <course-root> [options]
```

| Command | Options | Does |
|---|---|---|
| `init` | `--plan <file.json>` `[--force]` | Scaffolds folders, `course.json`, `progress.json`, module overviews, `README`, `.grading/`, dashboard. Unlocks module 1 lesson 1 only. |
| `status` | `[--json]` | Progress, per-lesson state, study time, reviews due, what's next. |
| `gate` | `--lesson <m>/<l>` \| `--test <m>` \| `--final` | **0** = teach it. **4** = locked. **5** = unlocked but too many reviews are due. Run before every lesson. |
| `mark-generated` | same targets | Records that content has been written. Refuses on locked items. |
| `grade` | `--lesson <m>/<l> [--quiz N] [--assignment N] [--explain N]`<br>`--test <m> --score N`<br>`--final N`<br>`[--note "…"]` | Records scores 0–100, decides pass/fail, unlocks what was earned, schedules the first review. |
| `review` | *(no args)* → list the queue<br>`--lesson <m>/<l> --score N [--note]` → record one<br>`[--json]` | Spaced repetition over passed lessons. |
| `test-out` | `--module <m> --score N [--note]` | Credits a whole module from a cold placement test, at the higher `testOutThreshold`. |
| `session` | `start` \| `end [--note]` \| `status` | Study-time clock. |
| `unlock` | target + `--force --reason "…"` | Learner override. Logged permanently and flagged on the dashboard. |
| `note` | `--text "…"` | Appends a note to the activity log. |
| `render` | — | Rebuilds `progress.html` from `progress.json`. |

## Exit codes

`0` fine · `1` bad arguments · `2` no course at that path · `3` course already exists ·
`4` **locked by the gate** · `5` **blocked pending review**

## Grading a lesson across a session

Quiz, explain-back and assignment usually happen at different times. Grade whichever you
have; the lesson stays open until all three are in.

```bash
course.py grade --root ./course --lesson 02-locators/01-roles --quiz 85
# -> "recorded, but NOT passed: … still outstanding: assignment, explain"
course.py grade --root ./course --lesson 02-locators/01-roles --explain 78 --assignment 90
# -> "PASSED … Unlocked: 02-locators/02-waiting. First review scheduled for 2026-08-24."
```

Set `"assignment": false` or `"explain": false` on a lesson in the plan to drop that
component; it then passes on the remaining ones.

## Spaced repetition

Passing a lesson schedules its first review for tomorrow. Each review moves it along the
ladder **1 → 3 → 7 → 16 → 35 → 90 → 180 days**: ≥85% climbs a rung, 70–84% repeats the
current interval, <70% resets to 1 day and counts a lapse.

```bash
course.py review --root ./course
# 4 review(s) due — ask these before any new material.
#   01-foundations/01-why-e2e  Why end-to-end tests
#       4d overdue · rung 0/6 · lapses 0
#       - Compare unit/integration/E2E
course.py review --root ./course --lesson 01-foundations/01-why-e2e --score 92
```

When the queue reaches `reviewGate` (default 3), `gate` returns **5** for anything not
already in progress. Lessons underway are never interrupted; only starting something new
is blocked. Set `"reviewGate": 0` in the plan to disable.

## Testing out

```bash
course.py test-out --root ./course --module 01-foundations --score 88
```

Requires every earlier module to be complete — placement runs in order. On a pass, all
lessons plus the module test are credited and queued for review in 2 days. On a fail
(below `testOutThreshold`, default 85), nothing changes and they take the module normally.

## Session time

```bash
course.py session start  --root ./course
course.py session end    --root ./course --note "module 2 lessons 1-2"
course.py session status --root ./course
```

A single session is credited at most 4 hours. A session left open more than 8 hours is
auto-closed and capped on the next command, and marked `auto` in the log. Once there are
three or more sessions, the dashboard projects a finish date from the observed pace and
the average time per completed item.

## `plan.json`

```json
{
  "topic": "string, required",
  "depth": "tour | practitioner | deep | mastery",
  "goal": "why they are learning it",
  "format": "md | txt",
  "passThreshold": 70,
  "testOutThreshold": 85,
  "reviewGate": 3,
  "modules": [{
    "title": "string, required",
    "summary": "one line",
    "objectives": ["..."],
    "lessons": [{
      "title": "string, required",
      "summary": "one line",
      "objectives": ["..."],
      "assignment": true,
      "explain": true
    }],
    "test": { "title": "...", "summary": "..." }
  }],
  "finalProject": {
    "title": "...", "summary": "...",
    "requirements": ["..."], "stretch": ["..."]
  }
}
```

Ids are derived from titles — module `01-foundations`, lesson `02-your-first-test`.
