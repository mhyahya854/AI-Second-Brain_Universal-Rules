# Depth levels

Ask the learner which one they want. Never assume — a person who wanted a
two-hour orientation will abandon a 12-module course, and a person preparing for
a job will resent a tour.

| Level | Modules | Lessons/module | Rough time | What it buys them |
|---|---|---|---|---|
| **Tour** | 3 | 2–3 | 3–6 h | Vocabulary, mental model, one working thing. Enough to decide whether to go deeper or to talk about it credibly. |
| **Practitioner** | 5–6 | 3–4 | 20–40 h | Can do real work unsupervised. Knows the happy path, the common failure modes, and the tooling. **The right default for most people.** |
| **Deep** | 8–10 | 3–5 | 60–120 h | Internals, performance, edge cases, architecture decisions. Can review other people's work and justify trade-offs. |
| **Mastery** | 12–15 | 4–6 | 200 h+ | Source-level understanding, history, ecosystem, contributing back. Extends the tool, not just uses it. |

## Rules

- **Adjust down for narrow topics.** "CSS Grid" at Deep is 6 modules, not 10. Padding a
  small topic to hit a module count produces filler, and filler is what makes people quit.
- **Adjust for prior knowledge.** Someone who knows React learning Next.js should not sit
  through the JavaScript module — but do not delete it from the plan. Keep the module and
  let them **test out** of it (`course.py test-out`), so the skip is evidence-based and the
  material stays there if the placement test says otherwise.
- **Time estimates assume they do the assignments.** Say so. Passive reading is not
  what this course measures.
- **State the level in the plan** and put it on the dashboard. If the learner asks to go
  deeper mid-course, extend with new modules at the end rather than rewriting what they
  already passed.
