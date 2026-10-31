# learn-anything

A Claude Code skill that turns any topic into a **gated, hands-on course** with an AI tutor
who won't let you skip ahead — and won't let you forget what you already passed.

You say what you want to learn and how deep you want to go. It builds a folder-based
curriculum — modules, lessons, quizzes, worked examples, explain-back checks, assignments,
module tests, and a final project — then teaches it to you one lesson at a time, grades
your work, schedules spaced-repetition reviews of old material, and refuses to unlock the
next thing until you've earned it.

```
  Playwright end-to-end testing  ·  practitioner
  [############################] 86%   6/7 items   avg 89%
  time 13h 00m over 12 sessions   pace 5h 21m/wk   est. finish 2026-09-14
  6-day streak (best 9)   🚀 Off the mark   📦 1 module cleared   💎 2 flawless

  DONE    01-foundations  Foundations
          [x] 01-why-end-to-end-tests  Why end-to-end tests  85%
          [x] 02-your-first-test       Your first test       90%
          [x] module-test              Foundations check     84%
  ACTIVE  02-locators-and-assertions  Locators and assertions
          [x] 01-role-based-locators   Role-based locators   91%  (tested out)
          [ ] 02-auto-waiting          Auto-waiting
           .  module-test              Locators check

  REVIEWS DUE (2):
          01-foundations/01-why-end-to-end-tests  Why end-to-end tests  (4d overdue)
          01-foundations/02-your-first-test       Your first test       (1d overdue)
```

## Why it's different from asking a chatbot to teach you

A chatbot will happily explain module 7 when you're on module 2, will tell you your answer
was great when it wasn't, and will never ask you about module 1 again. None of that helps
you learn.

- **The gate is code, not vibes.** [`scripts/course.py`](scripts/course.py) owns the state
  machine. The tutor runs `gate` before every lesson and gets a non-zero exit if you
  haven't earned it. It can't talk itself into being lenient.
- **Three components per lesson, weakest link wins.** Quiz, hands-on assignment, and an
  **explain-back check** where you close the file and teach the idea in your own words. A
  perfect quiz won't carry a weak explain-back — that's the one that catches
  recognise-but-don't-understand.
- **Spaced repetition, enforced.** Every passed lesson comes back on a 1 → 3 → 7 → 16 → 35
  → 90 → 180 day ladder. Let three pile up and new lessons stop unlocking until you clear
  them.
- **Skip honestly or not at all.** Already know a module? Take a cold placement test at a
  **higher** bar (85%) and test out of the whole thing. No hand-waving.
- **Grades are recorded, not remembered.** Scores, attempts, lapses and study time live in
  `progress.json`. Close the session, come back next week, pick up exactly where you were.
- **Answer keys are hidden from you.** Rubrics and keys live in `.grading/`. You get
  feedback, not solutions.
- **A dashboard you can actually look at.** `progress.html` is regenerated after every
  graded item — review queue, per-component scores, study-time chart, day streak, badges,
  projected finish date. No server, no dependencies, just open the file.
- **Written to be worth reading.** Lessons open on a mystery or a war story rather than a
  definition, make you predict outputs before revealing them, and are set in one running
  product built across the whole course — ideally your own. A boring lesson is treated as
  a bug, not a style preference.
- **Quizzes you can actually answer.** Questions ramp from warm-up to stretch, ask one
  thing each, and mix formats — predict the output, spot the bug, this-or-that — instead of
  eight essay prompts. Stuck? Ask for a hint: a nudge costs you nothing, and only a
  near-answer costs points. The pass mark doesn't move.

## Install

Requires [Claude Code](https://claude.com/claude-code) and Python 3.8+ (already on macOS
and most Linux; on Windows, install from python.org).

```bash
git clone https://github.com/naeemdev360/learn-anything-skill.git ~/.agents/skills/learn-anything
ln -s ~/.agents/skills/learn-anything ~/.claude/skills/learn-anything
```

Or drop it straight into `~/.claude/skills/learn-anything` (personal) or
`.claude/skills/learn-anything` inside a project.

## Use

```
> teach me Rust
> I want to learn Figma auto-layout properly
> /learn-anything
```

The tutor asks five things — topic, **how deep you want to go**, what you already know,
`md` or `txt` files, and where to put the course — then shows you a roadmap before it
writes anything.

### Depth levels

| Level        | Modules | Rough time | For                                           |
| ------------ | ------- | ---------- | --------------------------------------------- |
| Tour         | 3       | 3–6 h      | Orientation, vocabulary, one working thing    |
| Practitioner | 5–6     | 20–40 h    | Doing real work unsupervised _(default)_      |
| Deep         | 8–10    | 60–120 h   | Internals, trade-offs, reviewing others' work |
| Mastery      | 12–15   | 200 h+     | Source-level, extending the tool              |

### What gets created

```
rust-course/
├── progress.html              ← the dashboard, open it in a browser
├── progress.json              ← state: scores, attempts, reviews, sessions
├── course.json                ← the fixed curriculum plan
├── README.md
├── 01-foundations/
│   ├── module.md
│   ├── 01-ownership/
│   │   ├── lesson.md          ← content, code, gotchas, takeaways
│   │   ├── examples.md        ← worked examples, including one debugged
│   │   ├── quiz.md            ← 6–8 questions, easy → hard, no answers
│   │   ├── explain.md         ← the explain-back prompts
│   │   ├── assignment.md      ← the mission: bronze / silver / gold
│   │   └── submission.md      ← you fill this in
│   └── module-test.md         ← cumulative, closed book
├── final-project/
└── .grading/                  ← keys and rubrics. tutor only.
```

Lesson content is written **just in time**, when you unlock the lesson — so it can adapt
to how you've actually been doing. The full roadmap exists from day one.

## Rules of the gate

- A lesson passes only when **quiz, explain-back and assignment** are all ≥ the pass mark
  (70% by default).
- Passing every lesson unlocks the module test. Passing the test unlocks the next module.
- Finishing every module unlocks the final project.
- **Three or more reviews due blocks new lessons** — but never interrupts one already
  underway.
- Only **bronze** on an assignment is graded. Silver and gold are there if you want them
  and cost nothing if you skip them.
- Failing doesn't punish you — the tutor reteaches the specific weak component differently
  and retests you on the same objectives. A fail means *not yet*, and retries are free.
- If you really need to skip, say **"override the gate"**. It's permanently logged and
  flagged on your dashboard. If what you actually want is to skip material you know, ask
  to be tested out instead.

## Reviews

Passing a lesson schedules its first review for tomorrow. A review is 2–3 _fresh_ recall
questions — never the original quiz, always closed book:

| Your score | What happens                                                   |
| ---------- | -------------------------------------------------------------- |
| ≥ 85%      | Interval climbs a rung — longer gap before it returns          |
| 70–84%     | Repeats at the same interval                                   |
| < 70%      | Resets to 1 day, counts a lapse, and gets retaught on the spot |

## Testing out

Claim prior knowledge and the tutor writes a cold placement test for module 1 — every
lesson objective, closed book, plus an applied task so recall alone can't carry it. Clear
**85%** and the whole module is credited. It runs in order and stops at the first module
you don't clear. Everything you test out of is queued for review two days later, because
tested-out knowledge is the likeliest to be thin.

## Study time

The tutor starts a clock when you begin and ends it when you stop. The dashboard shows
total hours, a 21-day activity chart, time per completed item, your weekly pace, and —
once there are a few sessions — a projected finish date. Forget to stop and the session
auto-closes, capped, rather than corrupting the numbers.

## Streaks and badges

Any day you study counts toward a **streak**, shown on the dashboard and in `status`. Miss
a single day and it survives; miss two and it resets — no guilt-tripping either way.

Badges are earned, never given for showing up: *off the mark* (first lesson passed),
*flawless* (90%+ on all three components), *comeback* (failed it, then passed it), *stuck*
(survived three spaced reviews), *module cleared*, *tested out*, *course complete*. They
are all derived from real scores, so none of them can be farmed.

## Resuming

Point Claude Code at the course folder and say you want to continue. The skill finds
`progress.json`, starts a session, and shows you what's due for review before anything new.

## Driving it yourself

The state machine is a plain CLI — useful for scripting or for checking progress without
starting a session:

```bash
python3 scripts/course.py status  --root ./rust-course
python3 scripts/course.py review  --root ./rust-course
python3 scripts/course.py session status --root ./rust-course
python3 scripts/course.py status  --root ./rust-course --json
```

Full reference: [`references/commands.md`](references/commands.md).

## Layout

| Path                             | What                                                                   |
| -------------------------------- | ---------------------------------------------------------------------- |
| `SKILL.md`                       | The tutor's instructions — the workflow Claude follows                 |
| `scripts/course.py`              | State machine: gating, grading, reviews, sessions, rendering           |
| `assets/dashboard-template.html` | Self-contained dashboard, data injected at render                      |
| `references/`                    | Curriculum design, engagement, quiz design, depth levels, lesson format, grading, CLI reference |
| `templates/`                     | Skeletons for lessons, quizzes, explain-backs, assignments, rubrics    |
| `example/plan.json`              | A worked example of the curriculum plan format                         |

## License

MIT — see [LICENSE](LICENSE).
