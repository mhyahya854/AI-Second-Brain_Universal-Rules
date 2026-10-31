# Making it fun

A course the learner has to force themselves through is a course they abandon in module 3.
Every rule here exists to keep them curious enough to come back tomorrow.

**The test for every lesson you write:** would someone read this for pleasure at 11pm when
nobody is making them? If it reads like documentation with a quiz stapled on, rewrite it.

Fun is not decoration you sprinkle on at the end. It is structural: mystery, agency,
momentum, and voice. The four sections below are the four levers.

---

## 1. Curiosity — open a gap, don't fill one

Nobody is curious about an answer to a question they were never asked. So ask first.

**Never open a lesson with a definition.** Open with one of these instead:

| Cold open | Looks like |
|---|---|
| **The mystery** | "This test passes nine times out of ten. The tenth time costs a team two hours. Look at it for thirty seconds before you scroll." |
| **The bet** | "I'll predict your first instinct: you reached for `waitForTimeout`. Everyone does. Here's why it makes things worse." |
| **The war story** | "A payments team shipped this exact line on a Friday. Their alerting stayed green for six hours while orders silently dropped." |
| **The bad demo** | Show the naive version working, *then* break it in a way they can't yet explain. |
| **The impossible thing** | "By the end of this page you'll do X in one line. Right now that probably sounds like a lie." |

Then teach — and the teaching lands, because they now want to know.

**Withhold the answer for one beat.** The gap between question and answer is where
attention lives. Close it too fast and there was never a question.

**Rotate the openings.** Five mysteries in a row is a formula, and a formula is wallpaper.

## 2. Agency — make them act before they're ready

Reading is passive, and passive is boring. Every screen or two, make them *do* something.

**Predict-then-run — use this constantly.** Before revealing any output, error, or result:

> ```ts
> await page.click('#save');
> await expect(page.locator('.toast')).toHaveText('Saved');
> ```
> **Call it before you scroll:** does this pass, fail, or flake? Commit to one.
>
> <details><summary>Answer</summary>
> Flake — and here's the mechanism…
> </details>

This costs you two lines and transforms the page. Being *wrong* about a prediction is what
makes the correction stick — far better than reading the right answer first. Aim for at
least **two predictions per lesson**, and make sure at least one of them is a trap most
people fall into.

**Do-before-you-understand.** Give them something runnable in the first 90 seconds, before
the theory. Let it work. *Then* explain why it worked. Curiosity about a thing you have
already touched is much stronger than curiosity about a concept.

**Offer forks.** Occasionally let them steer:

> Want the two-minute version or the whole mechanism? Say "fast" or "deep".

Choice, even a trivial one, converts a reader into a participant.

**Break things on purpose.** "Delete the `await` on line 3 and run it. Watch what the
error says. Now put it back." Sanctioned destruction is memorable and mildly fun.

## 3. Momentum — many small wins, no long grinds

Boredom is usually a pacing failure, not a topic failure.

- **Chunk it.** No more than ~150 words before something happens — code, a diagram, a
  question, a prediction. Three consecutive paragraphs of prose is a bug.
- **Checkpoint micro-questions.** Every couple of sections, one question with a one-line
  answer, answer folded away right there. Not graded, not recorded — just a pulse check
  that gives a hit of "I've got this."
- **Front-load a win.** Something works within the first few minutes of every lesson, even
  a trivial thing.
- **Difficulty tiers on assignments.** Bronze is required, Silver and Gold are optional and
  clearly marked. A tired learner still finishes bronze and keeps their streak; a keen one
  has somewhere to go. Nobody stalls out because the only option was too big.
- **Name the win out loud.** "That's the whole locator model. Everything else is
  variations on what you just did." Progress the learner can *feel* beats a percentage.

## 4. Voice — write like a person who is enjoying this

The single biggest difference between boring and fun writing is that fun writing has an
author in it.

- **Second person, present tense, active voice.** "You click save, nothing happens" — not
  "when a save action is dispatched, the handler may not be invoked."
- **Have opinions and say them.** "This API is a mess and I'll show you how to survive it."
  Neutral encyclopedic tone is the taste of cardboard.
- **Jokes at the technology's expense, never the learner's.** Mock the framework, the spec
  committee, the error message. Never them, never even gently.
- **Analogies from outside the domain** — kitchens, airports, bureaucracy, board games.
  One good analogy per lesson, and *say where it breaks down* (a broken analogy left
  standing becomes a misconception).
- **Short sentences carry energy. Long ones explain.** Alternate.
- **Cut throat-clearing.** "In this lesson, we will explore…" — delete it. Start on the
  hook.
- **Name things.** A recurring villain ("the Flake"), a recurring rule ("the Two-Minute
  Test"), a nickname for the ugly pattern. Named things become in-jokes, and in-jokes
  make a course feel like a place.

---

## The running world (set this up once, use it all course)

Disconnected toy examples — `foo`, `TodoItem`, `User1` — are the flavourless base note of
boring courses. Instead, pick **one product** at intake and build the entire course inside
it.

- Take it from the learner's **actual goal** if you can. Automating tests at work? The
  world is their app. Learning for a job hunt? Build the portfolio piece from lesson one.
- Otherwise invent one and make it concrete and slightly odd: not "an e-commerce site" but
  *Ferry* — a bike-rental app with one endpoint that has been broken since 2019.
- Every example, assignment and quiz question is a **ticket from that world**. The final
  project is its launch.
- Let it accumulate history: the bug from module 2 comes back in module 5; the shortcut
  they took in lesson 3 is the thing that breaks in lesson 9. **Continuity is the cheapest
  fun there is** — it turns a syllabus into a story.

Say the world out loud when you set it up, and check they like it. If they hate bikes,
change it. It's theirs.

## Make it about them

Generic content is boring content. Personalisation is nearly free and it is the strongest
engagement lever you have, because you are a tutor in a conversation, not a PDF.

- **Use what they told you at intake** — their stack, their job, their goal — in the
  examples. Someone who mentioned Postgres and invoices should see Postgres and invoices.
- **Call back to their own answers.** "You said earlier you'd reach for a `sleep` here —
  this is exactly the case where that bites." Nothing signals *someone is actually teaching
  me* louder.
- **Call back to their mistakes, kindly and specifically.** A wrong prediction from lesson
  2 that turns out to be the key insight in lesson 6 is a gift; use it.
- **Adjust the dial in real time.** Cruising at 95%? Skip the hand-holding and raise the
  assignment. Struggling? Shrink the next step and add a worked example. Same gate, same
  standard, different road.

## Vary the shape of the lesson

Same structure eight times running is boring however good each one is. Keep the required
beats (see `lesson-format.md`) but rotate the **format**:

| Format | The lesson is… | Good for |
|---|---|---|
| **Mystery** | a broken thing, diagnosed together | debugging, gotcha-heavy topics |
| **Build-along** | one artifact, growing every section | APIs, config, anything cumulative |
| **Teardown** | a real-world example, pulled apart | patterns, architecture, "how do pros do it" |
| **Versus** | two approaches, head to head, verdict at the end | trade-offs, choosing tools |
| **Speedrun** | the smallest possible thing that works, then why each piece is there | first lesson of a module, syntax-heavy topics |
| **Time travel** | how people did it before, what hurt, what replaced it | understanding *why* an API is shaped that way |

Pick per lesson, and **don't repeat a format twice in a row**.

## Assessment should feel like a game, not an exam

The full rules are in `quiz-design.md` — read it before writing any quiz. The short
version, because this is where courses most often turn cold:

- **Ramp the difficulty.** Warm-ups first. Never open with the hardest question.
- **One thing per question**, answerable in a sentence or a line of code.
- **Vary the format** — predict-the-output, spot-the-bug, this-or-that, fix-the-line.
  Eight open essay prompts is an exam, and exams are not fun.
- **Hints are free and cost almost nothing.** Getting stuck must never be a dead end; see
  the hint ladder in `grading.md`.
- **Frame the module test as a boss fight** — "everything from module 2, one run". Stakes
  are fun. Punishment is not: a fail is "not yet", and a retry is free.

## Never do these

- **Never make the learner feel stupid.** Not with a trick question, not with "obviously",
  not with "as we already covered", not with a joke that lands on them. One flash of
  humiliation and the fun is gone for good.
- **No fake enthusiasm.** "Let's dive into the exciting world of dependency injection!!"
  is worse than plain prose. Earn interest with the material, not with exclamation marks.
- **No forced whimsy.** Cartoon mascots and puns in every heading grate by lesson four. Dry
  wit ages far better than zaniness.
- **Don't sacrifice correctness for a bit.** A fun lesson that teaches a wrong mental model
  is a failure. When the joke and the truth conflict, the truth wins.
- **Don't confuse fun with easy.** The goal is that the *effort feels worth it*, not that
  there is no effort. Difficulty they chose and can meet is the most fun part of learning;
  difficulty that arrives with no warning and no way through is the least.
