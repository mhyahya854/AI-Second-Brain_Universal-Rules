# GSAP Animation Helper Skill

[![npm version](https://badge.fury.io/js/gsap-animation-helper-skill.svg)](https://www.npmjs.com/package/gsap-animation-helper-skill)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modular AI skill for creating professional animations with GSAP (GreenSock Animation Platform). Works with Claude, ChatGPT, Gemini, Cursor, and other AI assistants.

## What is This?

This is a Claude AI skill that extends Claude's knowledge for GSAP animations. It's designed with a **modular structure** for efficient agent usage - loading only the specific documentation needed for each query.

## Structure

```
gsap-skill/
├── SKILL.md                 # Entry point with decision tree
├── plugins/
│   ├── scroll-trigger.md    # ScrollTrigger plugin
│   ├── scroll-smoother.md   # ScrollSmoother plugin
│   ├── split-text.md        # SplitText plugin
│   ├── flip.md              # Flip plugin
│   ├── draggable.md         # Draggable + Inertia
│   ├── observer.md          # Observer plugin
│   ├── draw-svg.md          # DrawSVG plugin
│   ├── morph-svg.md         # MorphSVG plugin
│   ├── motion-path.md       # MotionPath plugin
│   ├── text-plugins.md      # Text + ScrambleText
│   └── physics.md           # Physics2D + PhysicsProps
├── frameworks/
│   ├── react.md             # React + useGSAP hook
│   ├── nextjs.md            # Next.js SSR handling
│   └── vanilla.md           # Vanilla JS patterns
├── reference/
│   ├── core-methods.md      # gsap.to, set, timeline, etc.
│   ├── utilities.md         # gsap.utils methods
│   └── easing.md            # All easing functions
└── examples/                # Code examples
```

## Why Modular?

1. **Efficient** - Load only what's needed (e.g., ScrollTrigger query → read `plugins/scroll-trigger.md` only)
2. **Maintainable** - Update individual plugins without touching everything
3. **Scalable** - Easy to add new plugins/frameworks
4. **Token-efficient** - ~150 lines per file instead of 1000+ in one file

## How It Works

1. Agent reads `SKILL.md` (entry point with decision tree)
2. Based on user's question, agent reads the relevant file(s)
3. Agent provides targeted, accurate answer

### Example Flow

**User**: "How do I use ScrollTrigger with React?"

**Agent**:
1. Reads `SKILL.md` → sees decision tree
2. Reads `plugins/scroll-trigger.md` for ScrollTrigger info
3. Reads `frameworks/react.md` for React patterns
4. Combines knowledge to answer

## Quick Reference

| Topic | File |
|-------|------|
| Basic animations | `reference/core-methods.md` |
| Scroll animations | `plugins/scroll-trigger.md` |
| Smooth scrolling | `plugins/scroll-smoother.md` |
| Text effects | `plugins/split-text.md` |
| SVG drawing | `plugins/draw-svg.md` |
| Shape morphing | `plugins/morph-svg.md` |
| Path animation | `plugins/motion-path.md` |
| Layout animation | `plugins/flip.md` |
| Drag & drop | `plugins/draggable.md` |
| Input handling | `plugins/observer.md` |
| Physics | `plugins/physics.md` |
| React | `frameworks/react.md` |
| Next.js | `frameworks/nextjs.md` |
| Vanilla JS | `frameworks/vanilla.md` |
| Easing | `reference/easing.md` |
| Utilities | `reference/utilities.md` |

## Installation

### Install This Skill

```bash
npm install gsap-animation-helper-skill
```

Or clone from GitHub:

```bash
git clone https://github.com/kxwxn/gsap-animation-helper-skill.git
```

### Install GSAP (for your project)

```bash
npm install gsap
```

## Usage

This skill is a collection of markdown documentation files. Use it with your AI assistant:

| AI Tool | How to Use |
|---------|------------|
| **Claude Projects** | Upload files to your Project |
| **ChatGPT (GPTs)** | Upload files to your custom GPT |
| **Cursor** | Include in your project folder |
| **Other AI** | Provide files as context |

The AI will read `SKILL.md` as the entry point and navigate to specific documentation based on your questions.

## GSAP Resources

- **Official Docs**: https://gsap.com/docs/v3/
- **Cheatsheet**: https://gsap.com/cheatsheet
- **Easing Visualizer**: https://gsap.com/docs/v3/Eases/
- **Community**: https://gsap.com/community/

## License

This skill is MIT licensed.

**Note**: GSAP itself has its own licensing - core is free, some plugins require Club GSAP membership. See https://gsap.com/pricing/
