# Review Matrix

This file translates the referee and AE comments into concrete editorial actions for the revised JOS manuscript.

| Comment / Issue | Why it matters | Editorial action | Target sections |
| --- | --- | --- | --- |
| The paper reads like a technical report rather than a scientific article. | The manuscript currently emphasizes experiments before conceptual framing. | Rebuild the paper around a scientific argument: problem, literature, methods, evaluation logic, results, implications. | Whole manuscript |
| Encoding approaches are introduced without justification. | The three representation strategies look ad hoc if their rationale is not made explicit. | Explain naïve, disentangled, and centroid-based representations as alternative ways of encoding official classifications in semantic space, with strengths and limitations stated before results. | `2.background-related-work.md`, `4.methods.md` |
| Connection to the literature is weak. | Without related work, the contribution appears isolated and insufficiently scientific. | Add a proper background section on automatic coding in official statistics, semantic retrieval, and practical challenges in real coding systems. | `2.background-related-work.md` |
| The task is not formally defined. | Readers cannot tell whether this is classification, retrieval, ranking, or decision support. | Define the task as ranking ATECO codes from free-text descriptions, with top-k shortlist generation as the operational output. | `3.problem-formulation.md` |
| The shortlist use case appears too late. | The practical value of top-k metrics is under-motivated. | Introduce shortlist support early, as the operational use case for NSIs, respondents, or interviewers. | `1.introduction.md`, `3.problem-formulation.md` |
| Claims about replacing rule-based systems are too strong. | The current wording risks overclaiming and underplaying institutional constraints. | Reframe the contribution as a viable semantic alternative or complement to rule-based systems, not an unqualified replacement. | `1.introduction.md`, `8.discussion.md`, `9.conclusion.md` |
| Metrics are introduced only in the results section. | This weakens methodological transparency and makes the evaluation look post hoc. | Move all evaluation definitions to methods and experimental design. Define `match@k`, rationale for `k`, hierarchy levels, and model-selection logic before presenting results. | `4.methods.md`, `6.experimental-design.md` |
| There is no clear decision rule for selecting the preferred model/method. | Readers cannot infer what "best" means operationally. | State explicit selection criteria combining shortlist quality, robustness, and deployability. | `6.experimental-design.md`, `8.discussion.md` |
| Some figures are overcrowded or unclear. | Visual clutter makes interpretation weaker. | Keep only figures that change the argument; simplify division-wise and threshold visualizations; move secondary detail into text or appendix if needed. | `7.results.md` |
| Threshold analysis is underinterpreted. | Raw threshold curves do not explain how deployment decisions would be made. | Reinterpret thresholds as a decision-policy problem: coverage versus confidence versus manual review. | `7.results.md`, `8.discussion.md` |
| The purpose of the synthetic dataset is unclear. | Synthetic data currently look auxiliary and partially ad hoc. | State clearly that synthetic queries are used to enrich lexical coverage and support centroid construction, while acknowledging realism limits. | `5.data.md`, `6.experimental-design.md`, `8.discussion.md` |
| Synthetic data lack realistic noise such as typos and abbreviations. | This limits external validity. | Add an explicit limitation paragraph and avoid overselling synthetic data as a full substitute for real queries. | `5.data.md`, `8.discussion.md` |
| Short queries are not discussed enough. | This is one of the most policy-relevant constraints for real-world deployment. | Promote the short-query problem into a central discussion point and link it to subgroup robustness and user behavior. | `2.background-related-work.md`, `7.results.md`, `8.discussion.md` |
| Uneven performance across divisions is not contextualized. | Subgroup results need interpretation, not just reporting. | Discuss division-level heterogeneity as a function of linguistic similarity, data imbalance, and semantic ambiguity. | `7.results.md`, `8.discussion.md` |
| Data and methods are not clearly separated. | The current organization blurs what is observed data and what is methodological design. | Separate `Data`, `Methods`, and `Experimental Design` into distinct sections. | `5.data.md`, `4.methods.md`, `6.experimental-design.md` |
| Some references are missing or too thin. | Missing references weaken credibility and framing. | Add explicit references for CIRCE, ACTR, sentence transformers, multilingual retrieval models, and official-statistics coding context. | `2.background-related-work.md`, `references.md` |

## Revision Priorities

1. Fix scientific framing before touching fine-grained prose.
2. Define the problem and evaluation framework before rewriting results.
3. Use results selectively: only what supports the revised argument should remain in the main text.
4. Keep the main applied message, but qualify claims in a more institutionally cautious way.
