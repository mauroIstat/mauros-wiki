# AGENTS.md

## Purpose

This repository is a writing workspace designed to help Codex support the drafting of scientific papers.

Its main function is not to build a generic knowledge archive. Its main function is to provide structured, source-grounded context that helps Codex write new papers in a style that is consistent with the user's existing work.

The repository should help Codex understand:
- recurring research themes
- preferred methodological framing
- recurring terminology and distinctions
- the user's scientific voice
- reusable structures and formulations from past writing

The primary use case is paper writing. Other uses are secondary.

---

## Core idea

The repository has four distinct layers:

- `raw/` = original source materials
- `sources_md/` = markdown versions of source materials
- `wiki/` = compact structured context derived from the sources
- `paper/` = active workspace for a new manuscript

These layers must stay conceptually distinct.

`raw/` is the archive.
`sources_md/` is the readable text layer.
`wiki/` is the synthesis layer.
`paper/` is the drafting layer.

---

## Directory roles

### `raw/`

`raw/` contains the original source files.
These may include papers, slides, notes, project descriptions, emails, bios, and other materials.

Rules:
- Never modify files in `raw/`
- Treat `raw/` as immutable
- Use it only as the original source archive

### `sources_md/`

`sources_md/` contains clean markdown versions of the source documents found in `raw/`.

This layer exists because Codex usually works better with markdown than with PDFs or other binary formats.

For each relevant source file in `raw/`, create a corresponding markdown file in `sources_md/` whenever possible.

The goal of `sources_md/` is to preserve the textual content of the corpus in a form that is easy for Codex to read, compare, quote, and reuse.

A `sources_md/` file should usually contain:
- title
- source filename
- document type if known
- a clean markdown rendering of the text
- light structural organization when recoverable

Do not over-engineer this layer.
Its purpose is readability and reuse, not heavy annotation.

### `wiki/`

`wiki/` is the compact contextual layer built on top of `sources_md/`.

It should not be a full archive of everything in the corpus.
It should be a selective, structured, high-value synthesis that helps Codex write better papers.

The wiki should capture things like:
- recurring themes
- research identity
- methodological framing
- important distinctions
- preferred tone and vocabulary
- reusable argument patterns
- key projects and use cases
- recurring references or conceptual anchors

The wiki must remain compact, navigable, and useful.
Avoid turning it into a dump of source content.

### `paper/`

`paper/` is the active workspace for a new article.

Typical contents may include:
- `outline.md`
- `intro.md`
- `related_work.md`
- `methods.md`
- `results.md`
- `discussion.md`
- `conclusion.md`
- `figures/`

This is the place where drafting and revision happen.

---

## Main objective

When supporting the writing of a new paper, Codex should use:
- `wiki/` for voice, framing, concepts, and recurring distinctions
- `sources_md/` for concrete wording, structure, and prior formulations from the user's corpus
- `paper/` for the current manuscript and its local objective

The goal is not just to produce fluent academic English.
The goal is to produce text that sounds compatible with the user's established scientific voice.

Every new paragraph should be:
- clear
- compact
- source-aware
- stylistically compatible with the corpus
- conceptually aligned with recurring themes in the wiki

If a sentence is fluent but sounds generic or unlike the user's usual framing, revise it.

---

## Generation policy

All useful higher-level structure must be grounded in the actual corpus.

Do not invent themes, terminology, or writing conventions that are not supported by the source materials.
Do not use generic background knowledge to populate the wiki unless explicitly requested.

When evidence is weak or ambiguous:
- stay cautious
- prefer a smaller grounded output
- mark uncertainty explicitly if needed
- if you do not have enough information about a topic, or you are not confident about what to write, ask the user for more context before proceeding

Grounded, partial structure is better than polished but generic structure.

---

## Recommended workflow

When asked to build or refresh the workspace:

1. Inspect `raw/`
2. Create or update markdown source files in `sources_md/`
3. Build or update `wiki/` using `sources_md/` as the main input
4. Keep `wiki/` compact and writing-oriented
5. Use the resulting structure to support drafting in `paper/`

When asked to work on a new paper:

1. Ask the user which section or file in `paper/` they want to work on
2. Ask whether there is any extra material outside `wiki/` and `sources_md/` that should be read first for additional context
3. Read `paper/outline.md` if it exists
4. Read the most relevant pages in `wiki/`
5. Read relevant files in `sources_md/` when concrete prior wording, structure, or framing is useful
6. Read any additional user-provided draft or supporting material if available
7. Draft or revise the target file in `paper/`
8. Work collaboratively and incrementally: one section at a time, and when useful one paragraph or one sentence at a time
9. Prefer continuity with the user's corpus over generic academic phrasing

Do not assume the task is to write the whole paper from scratch unless the user explicitly asks for that.
The default mode is collaborative, section-based, and iterative writing.

## PAPER REVISION WORKFLOW (CRITICAL)

When the task is to revise an existing paper after peer review, do not treat it as a paper-from-scratch workflow.

### Revision inputs
The agent should use:
1. the existing manuscript in `raw/` or its markdown version if available
2. reviewer comments in `sources_md/`
3. the current `paper/outline.md`
4. relevant conceptual material in `wiki/`

### Required process
1. Read the existing manuscript
2. Read the reviewer comments carefully
3. Extract the main criticisms, required changes, and open issues
4. Update the wiki with revision-relevant context:
   - current paper contribution
   - structural weaknesses
   - reviewer concerns
   - revision strategy
5. Propose or update the paper structure before drafting new text
6. Only then start rewriting sections

### Writing objective
The goal is not only to improve prose, but to resolve reviewer concerns and transform the manuscript into a stronger scientific article.

### Important rules
- Do not rewrite blindly
- Do not preserve the original structure if it is part of the problem
- Prioritize conceptual and structural fixes before stylistic polishing
- Explicitly connect new text to reviewer concerns when relevant

---

## What to generate

### In `sources_md/`

Create one markdown file per relevant source document whenever possible.

Use simple, stable filenames in kebab-case.
Try to preserve a meaningful title and readable section structure.

The purpose of these files is to make the original corpus directly usable during drafting.

### In `wiki/`

Prefer a small number of high-value pages over a large taxonomy.

Useful pages may include:
- `wiki/index.md`
- `wiki/overview.md`
- `wiki/writing_voice.md`
- `wiki/methodological_framing.md`
- `wiki/recurring_themes.md`
- `wiki/key_projects.md`
- `wiki/terminology.md`
- additional focused pages only when clearly useful

Do not create many category folders unless the corpus clearly requires them.

The wiki should feel like a compact map of the user's research and writing habits.

---

## Writing-oriented principles

When building or updating the wiki, prioritize information that helps future writing.

High-value content includes:
- how introductions are framed
- how methods are described
- how limitations are qualified
- how contributions are positioned
- how institutional and scientific tones differ
- which distinctions recur across papers
- which formulations are reused or adapted often

Low-value content includes:
- generic summaries of the field
- background filler that does not reflect the user's corpus
- long descriptions that are not useful during drafting
- excessive duplication from the sources

The wiki should help answer questions like:
- How does the user usually frame a methodological contribution?
- Which distinctions recur in their papers?
- What kind of tone appears in scientific writing versus teaching materials?
- Which past paper is the best stylistic reference for a new introduction?

---

## What to avoid

Avoid the following:
- turning the wiki into a generic encyclopedia
- copying large amounts of raw text into `wiki/`
- creating rigid taxonomies too early
- over-designing folder structures
- inventing unsupported abstractions
- writing summaries that are polished but detached from the corpus
- optimizing for completeness instead of usefulness

This repository is not meant to be an abstract knowledge system.
It is a practical writing environment for Codex.

---

## Default behavior

At the start of any substantial task:
- inspect the relevant files
- ground yourself in `wiki/` and `sources_md/`
- then act

When in doubt:
- prefer source-grounded markdown
- prefer compact synthesis
- prefer writing usefulness over taxonomy expansion

The repository should become more useful over time because it becomes a better writing context, not because it becomes larger.
