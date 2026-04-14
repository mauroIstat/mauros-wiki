# Mauro's Personal LLM Wiki

This repository contains a personal, LLM-maintained markdown wiki built from source documents stored in `raw/`.

The goal is to turn papers, chapters, notes, teaching slide decks, and workshop materials into a persistent knowledge base under `wiki/` that supports:

- research synthesis
- writing reuse
- teaching preparation
- conference preparation
- institutional communication
- long-term knowledge accumulation

## Core idea

Instead of re-reading the source corpus from scratch every time, the wiki is incrementally maintained as a reusable knowledge layer.

The repository has two roles:

- `raw/` stores immutable source materials
- `wiki/` stores the maintained markdown knowledge base derived from those materials

The wiki is meant to compound over time: new sources refine or extend existing pages rather than replacing the whole structure.

## Current structure

```text
raw/
  chapters/
  notes/
  papers/
  teaching/
  workshop/

wiki/
  index.md
  log.md
  overview.md
  glossary.md
  sources/
    chapters/
    notes/
    papers/
    teaching/
    workshop/
  topics/
  projects/
  concepts/
  snippets/
  style/
  analyses/

AGENTS.md
README.md
```

## Repository principles

- `raw/` is immutable. Never edit files under `raw/`.
- `wiki/` is the maintained knowledge layer.
- Wiki pages must be source-grounded and traceable to real documents.
- The wiki should emerge from the corpus, not from a generic template.
- Incremental updates are preferred over destructive rewrites.

## What the wiki captures

The wiki is not just a set of source summaries. It is intended to preserve and organize:

- recurring ideas and arguments
- methodological positions
- project and use-case descriptions
- reusable formulations
- terminology
- distinctions between scientific, institutional, and teaching tones

## Key wiki files

### `wiki/index.md`

The main entry point and navigation map for the wiki.

### `wiki/overview.md`

High-level synthesis of the corpus: major themes, projects, distinctions, and tensions.

### `wiki/glossary.md`

Canonical terminology grounded in the source materials.

### `wiki/log.md`

Append-only record of ingests and maintenance work.

## Typical workflow

### 1. Add new source files

Place documents in the appropriate subdirectory under `raw/`.

Current source categories:

- `raw/chapters/`
- `raw/notes/`
- `raw/papers/`
- `raw/teaching/`
- `raw/workshop/`

### 2. Ingest the new material

Ask the LLM agent to inspect the new sources and update the wiki incrementally.

Typical outputs:

- source pages in `wiki/sources/`
- updated or new topic/project/concept pages
- snippet and style pages when clearly grounded
- updates to `wiki/index.md`, `wiki/overview.md`, `wiki/glossary.md`, and `wiki/log.md`

### 3. Query the wiki

Questions should normally be answered from the maintained wiki first, not by rediscovering the raw corpus each time.

If a query yields something durable, it can be filed into `wiki/analyses/`.

### 4. Maintain and refine

Periodically review the wiki for:

- missing cross-links
- weakly grounded summaries
- terminology inconsistencies
- missing higher-level synthesis pages
- pages that should be split or merged

## Current thematic focus

The current corpus is centered on:

- AI for Official Statistics
- semantic search and semantic integration
- automated coding and classification
- trustworthy AI, governance, and methodological safeguards
- uncertainty, semantic confidence, and conformal prediction
- big data and machine learning projects at Istat
- teaching explanations of AI concepts

## Grounding rules

The operational rules for the LLM agent are defined in `AGENTS.md`.

That file specifies:

- source-grounding requirements
- directory and page conventions
- page types and frontmatter
- ingest, query, and lint workflows
- policies for `index.md`, `overview.md`, `glossary.md`, and `log.md`

## Notes

- Prefer stable, descriptive filenames.
- Prefer `kebab-case` for wiki pages.
- When grounding is weak, prefer a stub marked `needs-review`.
- Avoid generic content that is not supported by the source corpus.

## Summary

This repository is not just a document archive.
It is a maintained system for turning a growing set of source documents into a navigable, reusable personal knowledge base.
