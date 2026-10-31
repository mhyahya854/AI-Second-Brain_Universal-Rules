# Learn Anything · by Nar

**English** · [简体中文](README.zh-CN.md)

> **Help AI teach you to truly learn—not just explain things to you.**

Learn Anything is an adaptive learning Skill for agent environments. It turns a serious learning goal into a source-grounded, adjustable course, then uses practice, feedback, transfer, and delayed review to test whether the learner can actually use what they learned.

It runs inside Codex, Claude Code, Cursor, and other environments that support Agent Skills. It is a Skill, not a standalone agent or application.

**Created by [Nar / 那不然](https://github.com/Nar101)** · Official repository: [`Nar101/learn-anything`](https://github.com/Nar101/learn-anything)

> Learn Anything was designed and open-sourced by **Nar / 那不然**. You may use, modify, and redistribute it under the MIT License. When redistributing all or a substantial part of the project, keep the original copyright notice and license.

## Choose your learning scenario

After installation, describe your goal in natural language. You do not need to learn a complex command system.

### You already have learning material

Upload a PDF, article, lecture note, transcript, or your own notes, or share an accessible web link. The Tutor treats the material as the boundary of the course, explains what it says, and then connects it to your use case.

```text
Use learn-anything to help me systematically learn the PDF I uploaded.
I want to apply its methods independently to real cases.
First show me the structure and learning route,
then teach only one lesson segment at a time.
```

For long material, the Tutor reads only the sections needed for the current lesson instead of loading the entire document into the conversation.

### You are starting from a goal

Tell the Tutor what you want to learn and where you will use it. It researches reliable sources for the current lesson and builds a course route instead of asking you to collect a complete textbook first.

```text
Use learn-anything to teach me OAuth 2.0 from scratch.
I want to independently review a third-party login design.
I have no textbook in mind, so research reliable sources for the current lesson.
```

### You have studied it and want to test yourself

```text
Use learn-anything to check whether I really understand opportunity cost.
Do not tell me the answer first. Give me a realistic case,
then decide from my response whether I need a refresher.
```

### You want to continue a long-term course

If a course state has already been saved, say:

```text
Continue my previous course.
Check for any due reviews first,
then resume from where I stopped or from the earliest unstable concept.
```

## Start in 30 seconds

```bash
npx skills add Nar101/learn-anything
```

Then tell your Agent what you want to learn. The shortest useful prompt is:

```text
I uploaded some material. Use learn-anything to help me truly learn it.
Start with an adjustable course map, then teach one lesson segment at a time.
```

## What makes it different from ordinary AI Q&A?

Ordinary AI is good at making an answer clear. Learn Anything goes further: it builds a route, asks you to apply ideas, corrects misconceptions, and checks whether you can use the knowledge in a new context and after a delay.

- **With material, stay faithful to the source:** distinguish the author's claims, the Tutor's synthesis, and your application assumptions.
- **Without material, research the current lesson:** do not require a complete reading list before starting.
- **Freeze the standard before the answer:** define the expected answer or rubric before asking you to respond.
- **Do not confuse exposure with mastery:** track prompted performance, independent performance, transfer, and delayed recall separately.
- **Do not rush unstable knowledge:** when a core misconception remains, “continue” means strengthening it before moving on.

Evidence of learning progresses through:

```text
seen → can do with hints → can do independently → can transfer → can recall later
```

## How it works

```text
Learning goal
→ mastery standard
→ adjustable course map
→ current lesson only
→ navigation and source-grounded teaching
→ application to your context
→ pre-committed assessment
→ feedback, retry, and mastery gate
→ immediate recall and transfer
→ delayed review
```

The detailed protocol is documented in [`SKILL.md`](./SKILL.md).

## Manual installation

Clone this repository into a Skills directory that your Agent can read, or copy the repository into a project-level `.agents/skills/learn-anything/` directory. Do not copy only `SKILL.md`: the course templates, evaluation rubrics, and validator are part of the Skill.

## Compatibility

This repository follows the Agent Skills `SKILL.md` structure and can be used by Codex, Claude Code, Cursor, and other compatible Agents. Capabilities differ by environment: when an environment cannot write files, the Skill can still follow the teaching protocol in the current conversation, but it will not pretend that cross-session state was saved.

## Validation

Validate the Skill structure:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py .
```

Run the course-validator regression tests:

```bash
python3 -B scripts/test_validate_course.py
```

Validate a persisted course package:

```bash
python3 -B scripts/validate_course.py /path/to/course
```

## Design boundaries

- This is a learning Tutor, not a forced router for every quick question; one-off questions can be answered directly.
- It does not pre-generate every lesson just to look complete.
- Saying “I understand” or finishing an explanation does not count as mastery.
- Practice in a high-risk domain is not a professional qualification or permission for real-world action.
- When the source text was not read, the Tutor does not present its own interpretation as the author's intent.

## Author

**[Nar / 那不然](https://github.com/Nar101)**

I am exploring how AI can move beyond one-off answers and participate in real learning, thinking, and work. Learn Anything is one open-source result of that practice.

This repository is the official source for Learn Anything: [`Nar101/learn-anything`](https://github.com/Nar101/learn-anything). If you find Learn Anything in another repository, website, or package, return here to verify the original author and latest version.

## License

[MIT](./LICENSE)
