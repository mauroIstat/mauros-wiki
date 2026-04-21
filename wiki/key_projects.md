# Key Projects

## Semantic search for ATECO automatic coding

This is one of the clearest anchor projects in the corpus. The task is to assign official economic-activity codes to free-text descriptions. The recurring contrast is between deterministic rule systems such as CIRCE and embedding-based semantic retrieval systems using sentence transformers, centroid representations, reranking, and conformal prediction.

The new JOS paper sharpens this strand in a more directly paper-oriented form. Its current empirical core is the comparison among three ways of representing the taxonomy in embedding space: a naïve single-descriptor representation, a disentangled one-to-many representation, and a centroid-based representation. It also clarifies the operational evidence base: official ATECO notes, 33,544 CIRCE-labelled real-world queries, and 12,400 synthetic queries generated from 6-digit ATECO descriptors.

The strongest reusable findings from this paper are practical rather than purely technical:

- top-k shortlist quality matters more than only top-1 assignment
- medium-sized models can be attractive because they balance performance and deployability
- short queries are structurally harder than semantically richer descriptions
- centroid-based representations are a strong baseline for official classification retrieval

For drafting work, this project is especially useful when the paper needs to connect model design with NSI use cases such as interactive coding tools, offline deployment, or transition costs when taxonomies change.

Key sources:

- [2026-paper-automatic-coding-ateco.md](/home/mauro/projects/mauros-wiki/sources_md/papers/2026-paper-automatic-coding-ateco.md)
- [2026-book-chapter-semantic-search-ateco.md](/home/mauro/projects/mauros-wiki/sources_md/chapters/2026-book-chapter-semantic-search-ateco.md)
- [2025-conference-paper-language-models.md](/home/mauro/projects/mauros-wiki/sources_md/papers/2025-conference-paper-language-models.md)
- [2025-slides-automatic-coding.md](/home/mauro/projects/mauros-wiki/sources_md/workshop/2025-slides-automatic-coding.md)

## Profession classification and semantic retrieval

This emerging project extends the same general logic of semantic search to the domain of professions. The relevant context is more explicitly tied to Official Statistics survey infrastructure: the FOL questionnaire provides the survey setting, while CP2021 provides the target classification structure. The likely writing value of this cluster is to connect occupation coding, profession descriptions, and hierarchical classification levels within a clearly institutional Istat frame.

An important part of this cluster is the presence of a legacy institutional tool, the Navigatore delle professioni. The new paper can be framed not as a generic search application, but as a methodology meant to overcome some residual limitations of a search-and-navigation system already used to support codification.

Another key source is the codification note that explains how the taxonomy should be interpreted. This matters because the corpus evidence suggests that profession coding cannot rely on titles alone: it depends on the concrete tasks performed, the work context, and the distinction between profession, employment status, position in the profession, and economic activity.

Key sources:

- [cp2021.md](/home/mauro/projects/mauros-wiki/sources_md/professioni/cp2021.md)
- [nota-codifica-delle-professioni.md](/home/mauro/projects/mauros-wiki/sources_md/professioni/nota-codifica-delle-professioni.md)
- [navigatore-delle-professioni.md](/home/mauro/projects/mauros-wiki/sources_md/professioni/navigatore-delle-professioni.md)
- [focus-classificazione-professioni-2021.md](/home/mauro/projects/mauros-wiki/sources_md/professioni/focus-classificazione-professioni-2021.md)
- [questionario-fol-2026.md](/home/mauro/projects/mauros-wiki/sources_md/professioni/questionario-fol-2026.md)

## Trustworthy AI in Official Statistics

This strand is broader than a single model. It frames AI adoption as an institutional programme involving validation protocols, quality-framework adaptation, privacy protection, governance, infrastructure, and capacity building. It provides the strongest anchor for high-level framing and discussion sections.

Key sources:

- [2026-conference-paper-trustworthy-ai.md](/home/mauro/projects/mauros-wiki/sources_md/papers/2026-conference-paper-trustworthy-ai.md)
- [2026-conference-paper-ai-governance-framework.md](/home/mauro/projects/mauros-wiki/sources_md/papers/2026-conference-paper-ai-governance-framework.md)
- [2025-note-official-statistics-ai.md](/home/mauro/projects/mauros-wiki/sources_md/notes/2025-note-official-statistics-ai.md)

## AI governance for automatic coding

This paper connects a production-oriented methodological theme with an explicitly institutional governance perspective. Its distinctive contribution within the corpus is to show that automatic coding is not only a modelling task, but also a governance problem involving validation procedures, responsibilities, traceability, and operational safeguards. It is particularly useful when a draft needs to connect semantic-search applications with broader organizational arguments about responsible AI adoption at Istat.

Key sources:

- [2026-conference-paper-ai-governance-framework.md](/home/mauro/projects/mauros-wiki/sources_md/papers/2026-conference-paper-ai-governance-framework.md)
- [2026-conference-paper-trustworthy-ai.md](/home/mauro/projects/mauros-wiki/sources_md/papers/2026-conference-paper-trustworthy-ai.md)
- [2025-note-official-statistics-ai.md](/home/mauro/projects/mauros-wiki/sources_md/notes/2025-note-official-statistics-ai.md)

## AI-enhanced dissemination and IstatData

Another recurring application is user-facing access to statistics. The key idea is that natural-language search, semantic retrieval, and AI-assisted analysis can make official data more discoverable and usable for non-experts, provided that traceability and quality remain explicit.

Key sources:

- [2025-note-official-statistics-ai.md](/home/mauro/projects/mauros-wiki/sources_md/notes/2025-note-official-statistics-ai.md)

## Patent-based mapping of AI exposure

This project uses patent abstracts plus occupational or sector taxonomies to estimate how AI-related innovation connects to labor and economic structure. The methodological core is embedding-based similarity between patent text and structured classification descriptions. One branch emphasizes policy-relevant occupational exposure; another emphasizes semantic confidence and ranking structure.

Key sources:

- [2025-conference-paper-patents-occupational-exposure.md](/home/mauro/projects/mauros-wiki/sources_md/papers/2025-conference-paper-patents-occupational-exposure.md)
- [2026-conference-paper-patents-semantic-confidence.md](/home/mauro/projects/mauros-wiki/sources_md/papers/2026-conference-paper-patents-semantic-confidence.md)

## PRODCOM classification from company websites

This project focuses on product statistics and business surveys. It combines website discovery, page filtering, product extraction, retrieval, and supervised or unsupervised code assignment. The framing is strongly operational: reducing reporting burden, supporting questionnaire pre-filling, and building digital assistants for statistical offices.

Key sources:

- [2026-conference-paper-prodcom.md](/home/mauro/projects/mauros-wiki/sources_md/papers/2026-conference-paper-prodcom.md)
- [2026-slides-ai-webscraping.md](/home/mauro/projects/mauros-wiki/sources_md/workshop/2026-slides-ai-webscraping.md)

## Big data and machine learning at Istat

This broader background project gives institutional continuity to the corpus. It situates current semantic-search and AI work within a longer trajectory of experimentation with satellite data, sensor data, web intelligence, remote sensing, and trusted smart statistics.

Key sources:

- [2025-book-chapter-big-data-machine-learning.md](/home/mauro/projects/mauros-wiki/sources_md/chapters/2025-book-chapter-big-data-machine-learning.md)
