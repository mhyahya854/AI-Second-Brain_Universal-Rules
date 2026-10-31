# Writing assessments people can actually answer

The most common way a good course goes cold: every question is written at exam altitude,
each one bundles three sub-answers, and the learner opens the quiz to a wall of essay
prompts. They get four right, feel stupid, and stop.

**Target: the learner should get roughly 8 in 10 of the main-body questions right.** Not
because the questions are soft — because they were taught the material and the questions
ask one clear thing each. If they're scoring below that consistently, the quiz is
miscalibrated or the teaching was thin. Either way it's yours to fix, not theirs.

---

## The ramp — never open with the hardest question

Order questions by difficulty, always. A quiz of 6–8 questions:

| Slot | Questions | What it does | Answer length |
|---|---|---|---|
| **Warm-up** | 1–2 | Straight recall from the lesson's takeaways. They should get these instantly. | a phrase or one line |
| **Core** | 3–4 | Applied. Read code, predict output, spot the bug, pick between two options. **This is the real quiz.** | one or two sentences |
| **Stretch** | 1 | Judgment, synthesis, or a case not covered verbatim. Clearly marked. | a short paragraph |

The warm-ups are not filler. They are the on-ramp that gets someone answering instead of
staring, and a learner who has answered two questions correctly will attempt the third.

**The stretch question is marked `(stretch)` and is not required to pass.** Weight it so
that missing it entirely still leaves a pass available. Getting it right is a flourish, not
a toll gate. Say this in the quiz file so they can attempt it without dread.

## One question, one thing

This is the fix for "the quiz is too hard" more often than difficulty is.

> **Bad:** "A team has 400 E2E tests and 30 unit tests. CI takes 50 minutes and developers
> re-run failed jobs until green. Name two distinct problems and what you'd do about each."

Four answers in one question, and a zero if they only see one. Instead:

> **Good:** "CI takes 50 minutes with 400 E2E tests. Name the single biggest cause."
> **Good:** "Developers re-run failed jobs until they go green. What habit is that hiding?"

Two questions, each with one answer, each independently scoreable. Same coverage, half the
intimidation, and the grading tells you far more precisely what they missed.

If a question contains "and", "as well as", or "for each of the following", check whether
it should be two questions. Usually it should. When a multi-part question is genuinely the
right shape, **number the parts (a, b, c) and score them separately** so partial credit is
automatic rather than a judgment call.

## Mix the formats

Eight open-ended prompts in a row is an exam paper. Rotate — most of these are faster to
answer *and* better at exposing understanding:

| Format | Example |
|---|---|
| **Predict the output** | "What does this print? One line." |
| **Spot the bug** | "One line here is wrong. Which, and what happens?" (say how many bugs) |
| **This or that** | "`getByRole` or `locator('.btn')` here — which, and why in one line?" |
| **Fix the line** | "Rewrite line 3 so this stops flaking." |
| **True and why** | "True or false: X. One sentence on why." |
| **Fill the blank** | "`await expect(page).____('/dashboard')`" |
| **Order these** | "Put these four lifecycle steps in the order they run." |
| **Which layer** | "Unit, integration or E2E for this feature? One line." |
| **Read the error** | Show a real stack trace: "what happened?" |
| **Open** | "Explain why X works that way." — at most **two** of these per quiz |

Code-reading questions are the workhorse: fast to answer, impossible to bluff, and they
feel like a puzzle rather than a test.

## Rules for every question

- **It must be answerable from this lesson.** If the answer needs something you never
  taught, cut it — that's the definition of an unfair question. Trace every question to a
  section.
- **No trick questions.** A detail mentioned once in passing is not a fair target. The
  question should test whether they understood the main idea, not whether they were
  scanning closely at the right moment.
- **No guessing what's in your head.** "What are the three costs?" is fair only if you
  taught exactly three and labelled them. Otherwise ask "name a cost of X."
- **Say how many things you want.** "Name two" — not "name the problems."
- **Show the code inline.** Never make them go and find a file to answer a question.
- **Keep the answer budget honest.** If the model answer runs past three sentences, the
  question is too big for a quiz. Move it to the explain-back or the assignment.
- **Aim the wrong answers at real misconceptions.** The best question is one where the
  plausible wrong answer *is* the misconception you most want to catch.

## Deliver it conversationally

The file is the record. You are the quiz.

Ask **one question at a time** in chat, react to the answer, then move on. This is a
completely different experience from being handed eight questions and told to write. It
lets you hint when they stall, follow up when an answer is half-right, and stop early when
they've clearly got it.

Keep the pace up. React in a sentence — "yep, that's it" / "close, one word off" — not a
paragraph of praise. Save the real feedback for the end.

## The hint ladder

**Getting stuck must never be a dead end.** This is the single biggest lever on "this feels
hard". When they stall or answer wrong, don't mark it and move on — climb the ladder, one
rung at a time, letting them try again after each:

| Rung | You say | Cap on the score for that question |
|---|---|---|
| **0** | "Take another run at it." | full credit |
| **1** | Point at the area: "Think about *when* the browser is ready, not what's on it." | full credit |
| **2** | Narrow it: "It's about the `await` on line 3." | ~80% of the question |
| **3** | Near-answer: "The click fires before the handler is attached — so what does that make the assertion?" | ~50% of the question |
| **4** | Tell them, explain the mechanism, and **ask them to say it back in their own words.** | 0 for that question, but they leave understanding it |

Hints one and two are free — a learner who needed a nudge and then got it has demonstrated
the understanding, and pretending otherwise just makes the number less honest, not more.
Only rungs three and four cost, and even then the lesson can still pass on the rest.

This is not softening the standard. The gate still holds, the explain-back still has to be
in their own words, and rung 4 still scores zero. What changes is that a stall becomes a
conversation instead of a wall.

## When someone is struggling

A learner missing the core questions is a teaching problem. Stop quizzing and fix it:

1. **Stop the quiz.** Finishing a quiz someone is failing teaches nothing and costs a lot
   of morale.
2. **Find the actual gap** — it's usually one misconception generating every wrong answer,
   not five separate holes.
3. **Reteach it differently.** New analogy, smaller example, or have them work one case
   with you. Repeating the original explanation more slowly does not work.
4. **Requiz on the same objectives with fresh questions.** Never the failed paper again.
5. Say plainly that a retry is normal and costs them nothing. It's true, and the belief
   that a fail is terminal is what makes people quit.

## Module tests — the boss fight

Same rules, bigger scope, plus:

- **Frame it as a boss fight, not an exam.** "Everything from module 2, one run." Stakes
  make it fun; dread makes it a chore.
- **Still ramp it.** A cumulative test that opens with its hardest question wastes the
  first five minutes on panic.
- **Tell them what it covers** before they sit it. Surprise scope is not rigour, it's just
  unfair.
- **Include one practical task** — something they build or fix, not just answer.
- **Draw a third of it from earlier modules.** That's the point of cumulative, and it's why
  reviews exist.
- Hints on a module test cost more than on a lesson quiz (cap at rung 2), and it stays
  closed-book. Rigour lives here; it doesn't need to live in every warm-up question too.
