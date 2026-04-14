# AGENTS.md

## Purpose

This repository contains a personal LLM-maintained wiki built from source documents stored in `raw/`.

The goal is to transform papers, chapters, slide decks, project notes, bios, emails, and other materials into a structured markdown knowledge base under `wiki/`.

This wiki is intended to support:
- research synthesis
- writing reuse
- teaching preparation
- conference preparation
- institutional communication
- long-term knowledge accumulation

The wiki is a persistent artifact.
It must become more useful over time as new sources are ingested and linked to existing knowledge.

---

## Source-grounded generation

This wiki must be generated from the actual contents of `raw/`.

The wiki is not a generic template and must not be populated with plausible but ungrounded content.
Its structure may start from a light scaffold, but its actual pages, terminology, summaries, hierarchy, and cross-links must emerge from the source materials.

This rule applies especially to:
- `wiki/index.md`
- `wiki/overview.md`
- `wiki/glossary.md`
- all section indexes or overview pages
- pages under `wiki/sources/`
- pages under `wiki/topics/`
- pages under `wiki/projects/`
- pages under `wiki/concepts/`
- pages under `wiki/snippets/`
- pages under `wiki/style/`
- pages under `wiki/analyses/`

### Required behavior

- Always inspect `raw/` before creating or substantially revising wiki content.
- Infer the wiki taxonomy from the actual source materials, not from generic prior knowledge.
- Use source documents as the primary grounding for terminology, themes, distinctions, and reusable formulations.
- When creating summaries, overviews, snippets, or glossary entries, derive them from one or more real source documents.
- Preserve traceability to source files in frontmatter and/or page body.
- If evidence is weak or ambiguous, explicitly mark the page or section as `needs-review`.

### Forbidden behavior

- Do not create generic placeholder summaries that are not supported by `raw/`.
- Do not fill `index.md`, `overview.md`, or `glossary.md` with abstract content disconnected from the sources.
- Do not invent recurring themes, concepts, or writing conventions unless they are supported by actual documents.
- Do not use web knowledge or general background knowledge to define the wiki unless explicitly requested by the user.

### Practical interpretation

- `wiki/index.md` must reflect the real structure and real contents of the wiki pages derived from `raw/`.
- `wiki/overview.md` must summarize the main themes that genuinely emerge from the source corpus.
- `wiki/glossary.md` must collect terms that actually appear in the source documents or are clearly needed to normalize recurring terminology found there.
- `wiki/snippets/` must contain reusable writing blocks distilled from real formulations, patterns, and arguments found across the source materials.

### Default workflow

1. Inspect `raw/`
2. Identify document types, recurring themes, projects, concepts, and tones
3. Create or update source pages
4. Create or update higher-level thematic pages
5. Update `wiki/index.md`, `wiki/overview.md`, `wiki/glossary.md`, and `wiki/log.md`
6. Report what was grounded strongly, what was inferred, and what needs human review

The wiki must be source-driven, not template-driven.

---

## Ground rules

- `raw/` is immutable. Never edit files under `raw/`.
- `wiki/` is the maintained knowledge layer. You may create and update files there.
- Prefer incremental updates over destructive rewrites.
- Do not delete existing wiki pages unless they are clearly obsolete and replaced by better grounded pages.
- Do not invent unsupported claims.
- Clearly distinguish extraction, synthesis, and inference.
- When uncertain, mark content explicitly for review rather than guessing.
- Prefer grounded stubs over polished but generic pages.

---

## Directory policy

### RAW

`raw/` stores immutable source materials.

Expected high-level structure:

- `raw/papers/`
- `raw/chapters/`
- `raw/slides/`
- `raw/projects/`
- `raw/notes/`
- `raw/bios/`
- `raw/emails/`
- `raw/reports/`
- `raw/misc/`

Possible second-level organization includes:
- source subtype
- context of use
- project grouping
- year, if useful

Examples:
- `raw/papers/conference/`
- `raw/papers/journal/`
- `raw/slides/teaching/`
- `raw/slides/conference/`
- `raw/slides/institutional/`

Never modify files under `raw/`.

### wiki

`wiki/` stores the maintained markdown knowledge base.

Expected structure:

- `wiki/index.md`
- `wiki/log.md`
- `wiki/overview.md`
- `wiki/glossary.md`

Main directories:
- `wiki/sources/`
- `wiki/topics/`
- `wiki/projects/`
- `wiki/concepts/`
- `wiki/snippets/`
- `wiki/style/`
- `wiki/analyses/`

Suggested second-level organization:

- `wiki/sources/papers/`
- `wiki/sources/chapters/`
- `wiki/sources/slides/`
- `wiki/sources/projects/`
- `wiki/sources/notes/`
- `wiki/sources/bios/`
- `wiki/sources/emails/`
- `wiki/sources/reports/`

- `wiki/snippets/bios/`
- `wiki/snippets/conference-intros/`
- `wiki/snippets/institutional-paragraphs/`
- `wiki/snippets/methodological-blocks/`
- `wiki/snippets/project-descriptions/`
- `wiki/snippets/teaching-explanations/`
- `wiki/snippets/abstracts/`
- `wiki/snippets/email-blocks/`

- `wiki/style/scientific-tone/`
- `wiki/style/institutional-tone/`
- `wiki/style/teaching-tone/`
- `wiki/style/terminology/`
- `wiki/style/recurring-formulations/`

If a page does not fit existing categories, prefer proposing a new subdirectory rather than misfiling it.

---

## Main priorities

Prioritize extracting and organizing content related to:
- AI for Official Statistics
- semantic search
- text classification
- embeddings and retrieval
- governance and methodological constraints
- trustworthy / explainable AI
- modernization of official statistics
- conference talks and scientific dissemination
- teaching narratives and recurring lecture material
- project descriptions and institutional communication

---

## Important distinctions to preserve

Pay attention to recurring distinctions such as:
- rule-based vs semantic approaches
- generic AI vs AI for Official Statistics
- innovation vs methodological safeguards
- statistical usefulness vs operational constraints
- research tone vs institutional tone vs teaching tone

When multiple source documents express the same idea in different tones, preserve that distinction rather than collapsing them into a single generic summary.

---

## Page types

Use these page types:

- `source` — summary of one raw document
- `topic` — cross-document theme or recurring subject
- `project` — project, use case, system, or initiative
- `concept` — methodological or conceptual idea
- `snippet` — reusable writing block derived from multiple documents
- `analysis` — synthesized output created in response to a question or exploration
- `style` — tone, terminology, naming, or rhetorical convention

---

## Frontmatter

Every wiki page must include YAML frontmatter:

```yaml
---
title: <page title>
type: source | topic | project | concept | snippet | analysis | style
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [list of raw source filenames]
tags: [relevant tags]
status: draft | reviewed | needs-review
---
```

Rules:
- `sources` must contain actual source filenames where possible.
- `status` should be `needs-review` when grounding is weak, parsing failed, or interpretation is uncertain.
- Use stable, descriptive titles.
- Keep filenames in `kebab-case`.

---

## Page format

Each page should contain:
1. one-line summary
2. structured body
3. related pages section at the bottom

Use internal markdown links in this format:

`[[path/to/page-without-extension]]`

Each page should be understandable on its own, but also connected to related pages.

---

## Index policy

`wiki/index.md` is a required navigational artifact and the main entry point to the wiki.

Treat it as:
- the homepage of the knowledge base
- the top-level navigation map
- the first file to read when answering queries

Whenever pages are created, renamed, significantly updated, or reorganized:
- update `wiki/index.md`
- add links to major pages
- include a one-line description for each major page
- place each page under the correct section

Without `wiki/index.md`, the repository is only a collection of markdown files.
With `wiki/index.md`, it is a navigable wiki.

Whenever helpful, create local section indexes or overview pages, for example:
- `wiki/sources/papers/index.md`
- `wiki/projects/ateco/overview.md`
- `wiki/snippets/conference-intros/index.md`

These local indexes must also be grounded in actual source-derived content.

---

## Glossary policy

`wiki/glossary.md` is the canonical terminology file.

Rules:
- Add new terms when they genuinely recur in source materials.
- Record preferred terminology and important distinctions.
- Flag conflicting usage explicitly.
- Note deprecated, variant, or context-specific terms when relevant.
- Prefer canonical terms across the rest of the wiki.

Never build the glossary from generic background knowledge alone.

---

## Overview policy

`wiki/overview.md` is a high-level synthesis of the whole corpus.

It should summarize:
- major themes
- major projects
- recurring distinctions
- dominant writing/use contexts
- major tensions or unresolved questions

It must be grounded in the actual source corpus, not in a generic abstract description of the field.

---

## Snippet policy

`wiki/snippets/` is a high-value reuse layer.

Create snippets only when they are grounded in recurring formulations, arguments, or patterns found in source documents.

Typical snippet families include:
- conference intros
- short bios
- institutional paragraphs
- methodological blocks
- project descriptions
- teaching explanations
- abstract skeletons
- email blocks

A snippet should be:
- compact
- reusable
- clearly scoped
- traceable to the source corpus

Avoid generic “marketing-style” snippets.

---

## Ingest workflow

When asked to ingest sources:

1. Inspect relevant files in `raw/`
2. Identify file type, context, probable year, topic, and likely relevance
3. Create or update source pages under `wiki/sources/`
4. Extract:
   - title
   - source filename
   - document type
   - probable context/year if recoverable
   - short summary
   - key messages
   - reusable formulations
   - related topics
   - related projects
   - terminology worth adding to the glossary
5. Update or create affected pages in:
   - `wiki/topics/`
   - `wiki/projects/`
   - `wiki/concepts/`
   - `wiki/style/`
   - `wiki/snippets/`
6. Update:
   - `wiki/index.md`
   - `wiki/overview.md`
   - `wiki/glossary.md`
7. Append to `wiki/log.md`
8. Report:
   - files created
   - files updated
   - themes strongly grounded
   - inferred connections
   - ambiguities needing human review

A single source may update many pages. This is expected.

---

## Query workflow

When the user asks a question:

1. Read `wiki/index.md` first
2. Identify relevant wiki pages
3. Read those pages
4. Synthesize the answer from the wiki, not from raw rediscovery, unless raw verification is necessary
5. If the answer creates durable value, file it into `wiki/analyses/`
6. Append a query entry to `wiki/log.md`

When filing an answer as analysis:
- give it a stable descriptive filename
- connect it to relevant topics/projects/concepts
- keep traceability to consulted wiki pages and source files

---

## Log policy

`wiki/log.md` is append-only and chronological.

Use entries like:

```md
## [YYYY-MM-DD] ingest | <source title>
Pages created: ...
Pages updated: ...
Key additions: ...
Open issues: ...
```

```md
## [YYYY-MM-DD] query | <question summary>
Pages consulted: ...
Output filed: yes/no
Filed page: ...
Notes: ...
```

```md
## [YYYY-MM-DD] lint
Issues found: ...
Fixes applied: ...
Open questions: ...
```

Keep the log compact but informative.

---

## Lint workflow

When asked to lint the wiki:

1. Inspect the wiki structure and major pages
2. Look for:
   - contradictions
   - stale claims
   - orphan pages
   - missing cross-references
   - missing concept/topic/project pages
   - terminology inconsistencies
   - duplicate or near-duplicate pages
3. Propose concrete fixes
4. Apply fixes only when requested, unless the instruction explicitly asks for autonomous maintenance
5. Append a lint entry to `wiki/log.md`

---

## Style expectations

Write clearly, compactly, and professionally.

Preferred qualities:
- precise
- calm
- reusable
- well-structured
- faithful to source nuance

Avoid:
- flashy prose
- inflated summaries
- generic background filler
- unnecessary repetition
- collapsing distinct tones into one bland formulation

When a source formulation is especially strong and reusable, preserve it or stay close to it