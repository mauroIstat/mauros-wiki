# Mauro's Writing Wiki

This repository is a writing workspace for building source-grounded context from an existing corpus and using it to support new scientific papers.

The repository has four distinct layers:

- `raw/` stores the original source documents and should be treated as immutable.
- `sources_md/` stores readable markdown conversions of those sources.
- `wiki/` stores compact synthesis pages derived from the corpus.
- `paper/` is the active drafting area for the current manuscript.

## Current structure

```text
raw/
  chapters/
  notes/
  papers/
  teaching/
  workshop/

sources_md/
  chapters/
  notes/
  papers/
  teaching/
  workshop/

wiki/
  index.md
  overview.md
  recurring_themes.md
  methodological_framing.md
  writing_voice.md
  key_projects.md
  terminology.md

paper/
  abstract.md
  introduction.md
  text-classification-in-official-statistics.md
  figures/
```

## Purpose

The main goal is not to build a generic encyclopedia. The goal is to maintain a compact, useful context layer that helps future drafting stay aligned with the source corpus in:

- recurring themes
- methodological framing
- preferred terminology
- project examples
- scientific voice

## Workflow

1. Add new source files under `raw/`.
2. Convert them into markdown under `sources_md/`.
3. Refresh the compact synthesis pages in `wiki/`.
4. Use `wiki/` and `sources_md/` to support drafting in `paper/`.

## Notes

- `raw/` should never be edited.
- `wiki/` should stay selective and writing-oriented.
- `sources_md/` should prioritize readability over heavy annotation.
- All synthesis in `wiki/` should stay grounded in the actual corpus.
