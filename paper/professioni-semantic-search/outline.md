# Outline

## Working title

A Semantic Search Approach to Occupation Coding in Official Statistics

## Core sections

- 1. Introduction
- 2. Data
- 3. Methodology
- 4. Results
- 5. Conclusion
- References

## Narrative logic

The paper should tell a compact but methodologically strong story:

1. profession coding is an important institutional task in Official Statistics
2. in practice, coding starts from free-text occupation descriptions that may be generic, ambiguous, or lexically distant from the official taxonomy
3. Istat already provides a legacy support tool, the Navigatore delle professioni, which is useful but highlights the residual gap between user language and classification language
4. the codification note clarifies that coding cannot rely on profession titles alone, because profession, employment status, position in the profession, and economic activity must remain conceptually distinct
5. this motivates a semantic-search formulation in which the central methodological question is how to represent the target occupational classes
6. the empirical contribution of the paper is to show that descriptor enrichment produces a robust gain across embedding models

## 1. Introduction

### Goal

Frame the institutional problem, introduce the legacy baseline, and motivate semantic retrieval as the methodological contribution of the paper.

### Paragraph structure

- Paragraph 1:
  importance of profession classification in Official Statistics and relevance of coding free-text job descriptions into CP2021 categories
- Paragraph 2:
  FOL as a major Istat survey and free-text work-activity field as a concrete setting in which the coding problem emerges
- Paragraph 3:
  Navigatore delle professioni as an existing Istat support tool; likely lexical or string-based orientation; distance between taxonomy wording and natural-language user queries
- Paragraph 4:
  codification note as conceptual anchor; coding must reflect the work actually performed and keep key conceptual distinctions separate; semantic search is introduced as a way to reduce the mismatch between query language and classification language

### Key points to include

- profession coding is institutionally important, not just technically interesting
- free-text occupational descriptions create a difficult alignment problem
- the paper does not present semantic search in a vacuum; it builds on a real institutional setting and a legacy tool already in use
- the methodological focus is on retrieval over a semantically structured label space
- the contribution is not only model comparison, but also descriptor design

## 2. Data

### Goal

Describe the resources used in the benchmark and explain how they support the semantic-search formulation.

### Suggested internal flow

- institutional context of CP2021 as the official target classification
- short mention of FOL as motivating context for free-text occupational descriptions
- labelled dataset of query and gold-standard CP2021 code pairs
- official 5-digit CP2021 descriptors
- enriched 6-digit occupational entries aggregated to the 5-digit level
- query-derived lexical enrichment used in the strongest descriptor setting

### Key points to include

- CP2021 defines the official label space at the 5-digit level
- the benchmark uses a labelled dataset of Italian occupation descriptions
- descriptor enrichment is grounded in real class-related textual material
- the data section should prepare the reader to understand why descriptor construction is central in the methodology

### Material that may be mentioned briefly

- screenshot of the FOL questionnaire section on main work activity
- screenshot or brief mention of the Navigatore only if it helps bridge Introduction and Data without turning this section into system description

## 3. Methodology

### Goal

Formally define the semantic retrieval task and show how descriptor construction is treated as a methodological variable.

### Current structure to preserve

- problem formulation as retrieval over class descriptors
- sentence embeddings and cosine similarity
- descriptor design:
  - `5digit`
  - `5_6digit`
  - `5_6_enriched`
- query-side representation
- benchmark design across multilingual embedding models
- ranking-based evaluation
- analytical strategy

### Main claim of the section

The paper does not treat class descriptors as fixed inputs. It treats their textual formulation as part of the method.

## 4. Results

### Goal

Show that descriptor enrichment produces clear and stable gains across models, and identify the best-performing configuration.

### Current structure to preserve

- `Accuracy@k` curves in the best descriptor setting
- progressive descriptor enrichment analysis
- compact benchmark table
- short synthesis of main findings

### Main messages

- `Qwen/Qwen3-Embedding-4B` is the best overall configuration in the benchmark
- descriptor enrichment improves results for all models
- the gain is visible not only in `Top-1`, but across the ranking profile
- descriptor design is a major driver of performance in retrieval-based occupation coding

## 5. Conclusion

### Goal

Summarize the methodological contribution and leave a clear path toward the extended journal version.

### Points to include

- semantic retrieval is a viable approach for occupation coding in an Official Statistics setting
- the strongest result of the paper concerns descriptor enrichment rather than model choice alone
- the current paper is a benchmark-oriented methodological contribution
- the journal extension can add richer analysis:
  - error analysis
  - subgroup analysis
  - qualitative inspection of failures
  - comparison with stronger baselines or interactive systems
  - possible extension toward conversational or assisted coding tools

## Writing constraints for the short paper

- keep the Introduction compact: ideally four paragraphs
- let `Data` stay operational and avoid turning it into a second introduction
- keep the paper methodologically focused
- avoid overclaiming about the Navigatore, since we only have interface evidence and not technical documentation
- use the codification note to justify the conceptual complexity of the task, not as a long documentary digression
