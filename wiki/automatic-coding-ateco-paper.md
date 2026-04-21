# Automatic Coding ATECO Paper

This page summarizes the current JOS paper on semantic coding for ATECO as a writing aid for revision work. It should be read together with the broader project context in [key_projects.md](/home/mauro/projects/mauros-wiki/wiki/key_projects.md) and the source markdown in [2026-paper-automatic-coding-ateco.md](/home/mauro/projects/mauros-wiki/sources_md/papers/2026-paper-automatic-coding-ateco.md).

## Core contribution in the submitted version

The submitted paper argues that embedding-based semantic retrieval is a viable alternative to rule-based coding systems such as CIRCE for the assignment of ATECO codes from short natural-language activity descriptions. The contribution is framed empirically rather than theoretically: the manuscript compares several embedding models and several ways of constructing the representation of the taxonomy, then measures agreement with CIRCE on a large corpus of real-world queries.

## Task as it currently appears in the paper

The practical task is not a strict single-label classification problem. The paper's strongest applied justification appears when coding is presented as shortlist support for users, interviewers, or statistical staff. This is especially clear in the conclusion, where the central outcome is not only top-1 accuracy but the usefulness of top-k candidate codes for interactive coding tools and possible offline deployment.

This point is present in the submitted paper but underdeveloped. For revision work, it is one of the most reusable conceptual anchors because it aligns the methodology with operational NSI requirements.

## Data and evidence base

The paper relies on three ingredients:

- the official ATECO 2022 classification, including notes and hierarchy
- 33,544 CIRCE-labelled real-world queries at the 5-digit level
- 12,400 synthetic queries generated with GPT-5-mini from 6-digit descriptors

The synthetic data are used mainly to enrich lexical coverage and to build centroid representations. The real-world CIRCE queries remain the operational benchmark. One recurring tension in the paper is that the benchmark is realistic and large, but it is not a perfect gold standard because CIRCE itself can produce ambiguous or questionable assignments.

## Main methodological objects

Three representation strategies structure the paper:

- naïve: one consolidated descriptor per code
- disentangled: multiple text fragments per code, scored with max pooling
- centroid-based: one centroid vector per code built from multiple sub-text embeddings

This triad is a strong reusable element. It gives the paper a clear methodological spine and should remain central in the revision. The most useful argumentative move is not simply to say that several methods were tested, but to explain why each representation strategy encodes a different assumption about how official classifications should be represented in semantic space.

## Main empirical findings

The current paper supports four robust claims:

- semantic retrieval can achieve high top-k agreement with CIRCE, especially at shortlist level
- centroid-based and disentangled representations outperform a single-descriptor baseline
- medium-sized models can offer a strong balance between performance and deployability
- longer, semantically richer queries are easier to code reliably than very short ones

The short-query issue is one of the most important discussion anchors. It connects model performance, realistic user behaviour, and operational limits of semantic retrieval in official settings.

## Writing value for the revision

This paper is useful not only as a direct source but also as a corpus anchor for future sections:

- For the introduction: contrast between rule-based maintenance burden and semantic flexibility.
- For methods: modular presentation of representation strategy, dataset role, and top-k evaluation.
- For discussion: medium-model deployability, shortlist logic, and the short-query problem.
- For limitations: benchmark dependence on CIRCE, ambiguity of some queries, and the simplified nature of synthetic data.

Primary source for this page:

- [2026-paper-automatic-coding-ateco.md](/home/mauro/projects/mauros-wiki/sources_md/papers/2026-paper-automatic-coding-ateco.md)
