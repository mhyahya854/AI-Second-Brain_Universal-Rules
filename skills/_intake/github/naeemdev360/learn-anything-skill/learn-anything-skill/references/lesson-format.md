# Lesson files

Generate these **only for the current unlocked lesson**, into
`<root>/<module-id>/<lesson-id>/`. Use the learner's chosen extension (`md` or `txt`).
For `txt`, drop the markdown syntax and use plain headings, blank lines and indentation —
the structure stays identical.

Templates to copy and fill: `templates/`. Read `engagement.md` before you write a word of
it, and `quiz-design.md` before the quiz — this file gives the required beats, those two
give the difference between a course someone finishes and one they abandon.

## `lesson.<ext>` — the content

Required beats, in this order:

- **Cold open** (2–4 sentences): a mystery, a bet, a war story, a broken demo — never a
  definition. See the cold-open table in `engagement.md`, and rotate which kind you use.
- **What you'll be able to do**: 2–4 observable outcomes from the plan. One line each.
- **The body**, in short sections with question headings ("Why does this pass locally and
  fail in CI?" beats "Auto-waiting"). Rules:
  - **Nothing longer than ~150 words without something happening** — code, a table, a
    diagram, a question.
  - **At least one runnable thing in the first 90 seconds**, before the theory.
  - **At least two predict-then-run moments**, answer folded into `<details>`. At least
    one should be a trap most people fall for.
  - Prefer a diagram or a table over a third paragraph. For flows and hierarchies, ASCII
    beats prose.
  - **One checkpoint micro-question** every couple of sections — one-line answer, folded
    away, ungraded. Momentum, not assessment.
- **Try this now** — one 60-second experiment, with the expected output stated so they can
  self-check. Include one "now break it on purpose and read the error."
- **Gotchas**: 2–4 real traps, ideally with the cost attached ("this is a two-hour bug").
- **Key takeaways**: 3–5 bullets — what they should still know in six months.

Aim for **350–700 words of prose**, plus code. Density beats length, and the file is the
record — you are teaching in conversation as well. If it reads like documentation, it is
too long and too flat: cut the exposition, keep the demos.

**Vary the format between lessons** (mystery / build-along / teardown / versus / speedrun /
time travel — see `engagement.md`) and never run the same one twice in a row. Set examples
in the course's running world rather than in `foo` and `TodoItem`.

## `examples.<ext>` — worked examples

2–3 examples, each traced step by step: the starting point, each change, **what happens
and why**. Make them detective work rather than transcription:

- State the goal, then ask them to **predict the outcome before each reveal**.
- At least one example is a *wrong* version debugged into a right one — the error message
  quoted verbatim, then read line by line. Diagnosing an error teaches more than admiring
  correct code, and it is the skill that transfers.
- Build on the same artifact across examples where you can, so the file tells one story.

## `quiz.<ext>` — checks understanding

**Read `quiz-design.md` first.** In short: 6–8 questions, no answers in this file, ramped
easy → hard, one question asking exactly one thing, mixed formats (predict-the-output,
spot-the-bug, this-or-that, fix-the-line — at most two open prompts), the last one marked
`(stretch)` and not required to pass. Every question traceable to a section of the lesson.
Say up front that hints are available and cost little.

## `explain.<ext>` — the explain-back (Feynman) check

Three or four prompts, in this order:

1. **"Explain {the core concept} in your own words"** — give them a *specific* audience,
   which makes it concrete and lowers the stakes: a new teammate on day one, a rubber duck,
   your PM who doesn't code, a tweet.
2. **"Give me an example of your own"** — not one from the lesson.
3. **"Why does it work that way?"** or **"when would this break?"** — one probe that
   recitation cannot answer.
4. Optional: **"where would you *not* use this?"** — knowing the boundary is knowing the
   thing.

Keep the file short; this happens in conversation and the file is a prompt sheet, not a
worksheet. Tell them it's closed-book, and that stumbling while thinking out loud is
expected and costs nothing — you are scoring the understanding, not the fluency.

## `assignment.<ext>` — the hands-on task

- **The mission**, stated as a goal in the course's running world, not a click-by-click
  recipe. A ticket someone would plausibly be handed.
- **Three tiers**, so nobody stalls out and nobody coasts:
  - **Bronze** — the required core. This is what's graded, and it should be genuinely
    achievable in the stated time.
  - **Silver** — the natural next step. Graded if attempted, never penalised if not.
  - **Gold** — the show-off version. Ungraded, there for the keen.
- **Acceptance criteria** as a checklist, so they can self-assess before submitting.
- **Constraints** — what they may not use, so they practise the thing being taught.
- **Time estimate**, honestly, for bronze.
- **Hints in `<details>`**, aimed at the likely sticking points. A learner who is stuck at
  11pm with nobody to ask needs an exit that isn't quitting.

Never include the solution. Hints are fine; solutions live in `.grading/`.

## `submission.<ext>` — where the learner answers

A skeleton with a numbered slot per quiz question and a section for the assignment: what
they built, where it lives, how they tested it. Pre-filling this removes the friction of a
blank page.

## Grading files — `.grading/<module-id>/<lesson-id>/`

**Never show these to the learner and never reference their contents verbatim.**

- `quiz-key.<ext>` — per question: the answer, the point value, **the hint ladder** (the
  three escalating nudges you'll give if they stall), and *what a wrong answer reveals*
  about the misconception, so you can reteach precisely.
- `explain-rubric.<ext>` — what a passing explanation must contain: the two or three ideas
  that must appear, the misconceptions that cap the score, and the jargon that does *not*
  count as understanding unless they can unpack it.
- `assignment-rubric.<ext>` — weighted criteria totalling 100 **for bronze alone**, each
  with what full, partial and zero credit look like. Silver adds nothing to the score if
  skipped; it is a place to put excellence, not a hidden requirement.

## Module tests

Same idea at module scope, in `<root>/<module-id>/`:

- `module-test.<ext>` — 10–15 questions plus one small practical task, cumulative across
  this module *and* earlier ones. Ramped like a quiz, closed book (say so at the top), and
  framed as the module's boss fight. State what it covers before they sit it.
- `module-test-submission.<ext>` — the skeleton.
- `.grading/<module-id>/module-test-key.<ext>` — key with per-question point values and,
  for each, **which lesson to send them back to** when they get it wrong.

## Final project

In `<root>/final-project/`: `brief.<ext>` (requirements, constraints, what "done" means,
how it will be assessed) and `submission.<ext>`.
In `.grading/final-project/`: `rubric.<ext>`.

## Placement tests (test-out)

When a learner claims prior knowledge, generate `placement-test.<ext>` into the module
folder from `templates/placement-test.md`. It looks like the module test but is written
**before** any teaching: cover every lesson objective in the module, closed book, and
include at least one applied task so recall alone cannot carry it. The key goes in
`.grading/<module-id>/placement-key.<ext>` and must map each question to the lesson it
comes from, so a fail turns straight into a study plan.
