---
title: Semantic Search Techniques for Automatic Coding of Economic Activity in Official Statistics
type: source
created: 2026-04-14
updated: 2026-04-14
sources: [2026-book-chapter-semantic-search-ateco.pdf]
tags: [official-statistics, semantic-search, automatic-coding, ateco, conformal-prediction, uncertainty]
status: draft
---

Embedding-based semantic retrieval is presented as a practical route for automatic coding in official statistics, provided that uncertainty is quantified in a statistically defensible way.

## Source details

- Source filename: `raw/chapters/2026-book-chapter-semantic-search-ateco.pdf`
- Document type: book chapter
- Probable context/year: 2026; chapter focused on ATECO 2022 coding
- Tone/use context: scientific and methodological

## Extracted content

- The chapter studies automatic coding of free-text economic activity descriptions into official classifications.
- The main technical pipeline is Sentence Transformers retrieval, with optional cross-encoder reranking.
- Three knowledge-base design strategies are compared on a synthetic dataset of 12,410 user-like queries.
- Centroid embeddings representing ATECO codes are reported as the strongest approach in the evaluated setup.
- Conformal prediction is introduced to calibrate similarity scores and provide statistically valid uncertainty estimates.

## Key messages

- Semantic search is useful when text descriptions do not align cleanly with exact classification vocabulary.
- Retrieval quality alone is not enough for official statistics; defensible uncertainty handling is part of the method.
- The chapter frames semantic coding as a replacement for purely lexical matching, not as a justification for unvalidated automation.

## Reusable formulations

- Official statistics need simpler access methods without weakening methodological safeguards.
- Semantic retrieval can support coding decisions, but statistical validity remains a separate requirement.
- Human expertise shifts from vocabulary construction toward validation, calibration, and quality control.

## Related topics

- [[topics/ai-in-official-statistics]]
- [[topics/semantic-integration-of-textual-data]]
- [[topics/trustworthy-ai-and-governance]]

## Related concepts

- [[concepts/deterministic-vs-semantic-coding]]
- [[concepts/conformal-prediction-for-official-statistics]]
- [[concepts/semantic-confidence-and-reliability]]

## Related projects

- [[projects/ateco-automatic-coding]]

## Terminology notes

- Recurring terms: semantic search, automatic coding, ATECO, centroid embeddings, reranking, conformal prediction.
- Glossary candidate: the corpus uses uncertainty quantification as a methodological requirement, not as a generic confidence label.

## Related pages

- [[glossary]]
- [[overview]]
- [[snippets/methodological-block-semantic-retrieval-for-coding]]
