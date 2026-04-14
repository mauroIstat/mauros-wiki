---
title: Beyond String Matching
type: source
created: 2026-04-14
updated: 2026-04-14
sources: [2025-slides-automatic-coding.pdf]
tags: [workshop, automatic-coding, statistical-integration, embeddings, web-scraping, ateco]
status: draft
---

This workshop deck positions embeddings as a step beyond deterministic coding and links semantic methods to several statistical integration tasks.

## Source details

- Source filename: `raw/workshop/2025-slides-automatic-coding.pdf`
- Document type: workshop slide deck
- Probable context/year: ITACOMS 2025
- Tone/use context: workshop/tutorial with applied examples

## Extracted content

- The deck spans AI in official statistics, ATECO classification, deterministic coding, AI-based coding, and future work.
- It presents non-traditional data sources including administrative text, company websites, and social media.
- Semantic search is framed as a way to improve retrieval and coding beyond exact keyword dependence.
- The slides explicitly warn about semantic failure modes such as confusion between near-opposite formulations like "including rice" and "excluding rice".
- Planned next steps include baseline comparison, human-labeled evaluation, fine-tuning with CIRCE vocabulary, and continuous learning from feedback.

## Key messages

- The contrast with string matching is one of the strongest recurring motifs in the corpus.
- Domain specificity and evaluation are presented as practical bottlenecks for deployment.
- Human expertise is repositioned toward validation and improvement rather than manual rule construction alone.

## Reusable formulations

- These systems match words, but they do not capture meaning.
- Domain expertise remains necessary even when semantic methods outperform deterministic ones.
- Validation must cover both benchmark comparison and human-labeled evidence.

## Related topics

- [[topics/semantic-integration-of-textual-data]]
- [[topics/ai-in-official-statistics]]

## Related concepts

- [[concepts/deterministic-vs-semantic-coding]]
- [[concepts/semantic-confidence-and-reliability]]

## Related projects

- [[projects/ateco-automatic-coding]]
- [[projects/enterprise-website-analysis]]

## Terminology notes

- Recurring terms: string matching, semantic search, CIRCE, ATECO, retrieval-augmented workflows.
- Glossary candidate: deterministic coding refers to dictionary/rule-based approaches anchored in lexical overlap.

## Related pages

- [[snippets/methodological-block-semantic-retrieval-for-coding]]
- [[style/teaching-tone]]
