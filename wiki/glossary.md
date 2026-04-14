---
title: Glossary
type: analysis
created: 2026-04-14
updated: 2026-04-14
sources: [2026-book-chapter-semantic-search-ateco.pdf, 2025-note-official-statistics-ai.pdf, 2026-conference-paper-patents-semantic-confidence.pdf, 2026-conference-paper-trustworthy-ai.pdf, 2026-slides-neural-networks-unveiled.pdf, 2025-slides-automatic-coding.pdf, 2026-slides-ai-reliability.pdf, 2026-slides-ai-webscraping.pdf, 2025-book-chapter-big-data-machine-learning.pdf, 2025-conference-paper-language-models.pdf, 2025-conference-paper-patents-occupational-exposure.pdf]
tags: [glossary, terminology]
status: draft
---

This glossary records terminology that recurs in the current corpus and the way the documents use it.

## Terms

### ATECO

Italian classification of economic activities used in the corpus as a concrete target taxonomy for automatic coding tasks.

### Conformal prediction

Method used in the ATECO chapter to calibrate retrieval scores and support statistically valid uncertainty statements.

### Deterministic coding

Rule- and dictionary-based assignment of classification codes using lexical overlap, parsing, and normalization. In the corpus, this is often contrasted with semantic retrieval.

### Embeddings

Numerical vector representations of text. In teaching and methodological material, embeddings are the main mechanism for moving from word matching to meaning matching.

### IstatData

The dissemination platform discussed as a vehicle for AI-enabled access to official statistics, especially natural-language search and interactive analysis support.

### ISCO-08

International Standard Classification of Occupations, used in the corpus as the occupational taxonomy for patent-based AI-exposure analysis.

### Prediction sets

Reliability device mentioned in workshop material as a way to move beyond single-label outputs.

### Public trust

Institutional outcome repeatedly tied to methodological soundness, validation, transparency, and privacy protection.

### Trusted Smart Statistics

Programmatic frame used in the big-data chapter for integrating new data sources and ML methods into official-statistics production while preserving official-statistics principles.

### Semantic confidence

Confidence signal derived from semantic retrieval rankings, especially the margin between top candidates in the patents paper. Not interchangeable with generic model confidence.

### Semantic integration

Corpus-level term for linking unstructured textual data to structured statistical categories through embeddings and retrieval workflows.

### Semantic search

Retrieval approach that matches user or source text to relevant information or codes through meaning rather than exact keywords.

### Trustworthy AI

In this corpus, AI use compatible with official-statistics requirements for validation, transparency, privacy, quality, and public trust.

### Uncertainty quantification

Umbrella term for methods that help judge whether AI outputs are reliable enough for operational use in official statistics.

## Terminology notes

- "Reliability", "confidence", and "uncertainty" overlap in the corpus but are not identical.
- "Trustworthy AI" is used more institutionally than philosophically.
- "Semantic integration" is broader than automatic coding; it also covers search and web-derived classification workflows.

## Related pages

- [[concepts/semantic-confidence-and-reliability]]
- [[concepts/trustworthy-ai-in-official-statistics]]
- [[concepts/deterministic-vs-semantic-coding]]
