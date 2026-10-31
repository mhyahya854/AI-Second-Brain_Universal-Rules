# Designing the curriculum

## Pick the world before you pick the modules

Before you write a single module title, decide **what you are building together** and
**where it lives**. One product, one story, all course long — see "The running world" in
`engagement.md`.

- Take it from their real goal wherever possible: their app, their job, the portfolio piece
  they want at the end. A course set inside the learner's own problem never has to justify
  itself.
- Otherwise invent something concrete and a bit odd. Not "an e-commerce site" — *Ferry*, a
  bike-rental app with one endpoint that has been broken since 2019.
- Then every example, assignment and quiz question is a ticket from that world, and the
  final project is its launch. Continuity across modules is what turns a syllabus into a
  story, and a story is the thing people come back to.

Run the world past them with the roadmap. If it doesn't appeal, change it — it costs
nothing now and it flavours everything after.

## The shape of a good course

Each module answers one question the learner can feel, and its **title should be that
question or the mission it unlocks**. Not "Chapter 4: Advanced Configuration" — "How do I
make this fast enough to ship?" A contents page of noun phrases promises a textbook; a
contents page of questions promises answers.

Order modules so that **every module depends on the one before it and nothing after
it.** That dependency chain is what makes the gate honest rather than arbitrary. If you
cannot say why module 5 needs module 4, reorder them.

A reliable arc:

1. **Foundations** — the mental model and one thing that works end to end on day one.
   Never start with theory alone; start with something running. **Lesson 1 must produce a
   visible win inside the first sitting** — the single strongest predictor of whether
   someone comes back for lesson 2.
2. **Core mechanics** — the 20% of the API or concepts used in 80% of real work.
3. **Real-world shape** — structure, patterns, project layout, how professionals organise it.
4. **Failure and debugging** — what breaks, how to read the errors, how to diagnose.
   Most courses omit this. It is the module that separates someone who can use a tool
   from someone who can rely on it.
5. **Performance / scale / advanced** — depth appropriate to the level.
6. **Integration** — testing, CI, deployment, working with the rest of the stack.

## Per-module checklist

- 3–5 lessons. More than 6 means the module is really two modules.
- **Objectives are observable.** "Understand promises" is not testable. "Rewrite a
  callback chain as async/await and explain what happens on rejection" is.
- Every lesson builds something or changes something. If a lesson has no assignment
  that produces an artifact, ask what it is actually for.
- **No two consecutive lessons should feel the same.** Vary the format across the module —
  a mystery, then a build-along, then a teardown (see `engagement.md`). Uniformity is what
  a learner experiences as boredom, even when every individual lesson is good.
- **Give at least one lesson per module some teeth** — a genuinely hard puzzle, a nasty bug
  to hunt, a "most people get this wrong" trap. Courses that are uniformly gentle are as
  forgettable as courses that are uniformly brutal.
- The module test is **cumulative**: it must draw on earlier modules too, otherwise the
  learner forgets module 1 by module 4.

## Lesson sizing

One lesson = one sitting = 30–90 minutes including the assignment. If a lesson needs
three new concepts to make sense, it is three lessons.

## The final project

This is the piece most learners actually remember, so make it real:

- It must require **most modules at once**, not just the last one.
- It should be something they would plausibly show someone — a portfolio piece, a tool
  they will use, a contribution to their actual work.
- Tie it to the goal they gave you at intake. A learner automating tests at work should
  build a suite for something like their real app, not a to-do demo.
- Give 4–7 hard requirements and 2–3 stretch goals. Stretch goals are not graded.

## Adapting mid-course

The plan in `course.json` is fixed, but you are not. If a learner keeps failing quizzes
on a prerequisite, **add remediation inside the current lesson** rather than pushing
them forward. If they are blowing through everything at 95%+, raise the difficulty of
the assignments rather than skipping lessons — the gate stays intact either way.
