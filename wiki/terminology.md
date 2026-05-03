# Terminology

## Official Statistics

Used as the institutional frame for the whole corpus. The term carries strong normative weight: quality, comparability, methodological rigor, confidentiality, transparency, and public trust.

## National Statistical Institutes (NSIs)

The recurring organizational subject. These institutions are described as needing to modernize production and dissemination while preserving their authoritative role.

## Semantic search

A core methodological term. In the corpus it usually means embedding-based retrieval that matches free-text queries or documents to statistical metadata or classification descriptors in a shared semantic space.

## Automatic coding

Assignment of official statistical codes to free-text descriptions. Most often discussed for ATECO, NACE, ISCO, and PRODCOM.

## ICD-10 cause-of-death coding

Assignment of ICD-10 codes to medical expressions reported on death certificates, followed by rule-based selection of multiple and underlying causes of death. In the corpus, AI is framed as support for the medical-text recognition phase of the Iris workflow, especially for lines that dictionary-based recognition fails to code.

## Iris

Cause-of-death coding software used for automated and manual coding. Its first module performs dictionary-based recognition of medical expressions; subsequent rule-based modules support the selection of multiple and underlying causes. The newer health-statistics paper treats Iris as an existing production system to be complemented, not displaced.

## CP2021

The 2021 Italian classification of professions. In this workspace it matters as a hierarchical target structure for profession-related tasks and as institutional context for any paper on semantic retrieval in the professions domain.

## FOL / Labour Force Survey context

Useful as survey background when profession information is discussed in an Official Statistics setting. Its role in the workspace is not to define the method, but to anchor profession-related tasks in a concrete Istat data-collection environment.

## Navigatore delle professioni

A legacy Istat tool for exploring and searching the profession classification. In the current workspace it is important both as institutional baseline and as evidence that profession coding already combines hierarchy, profession labels, descriptive text, and search support.

## Profession coding

In the profession-related sources, coding is explicitly framed as interpretation of the work actually performed, not mere normalization of a job title. This distinction is especially important for queries containing generic titles such as `impiegato`, `operaio`, or `imprenditore`.

## Embeddings / sentence embeddings

Dense vector representations used to encode semantic meaning and support retrieval, similarity ranking, or downstream classification.

## Conformal prediction

A preferred uncertainty-quantification framework for classification tasks in Official Statistics. Its rhetorical role in the corpus is important: it helps translate model outputs into statistically valid and institutionally defensible decisions.

## Semantic confidence

A simpler uncertainty notion used in the patent-to-sector work. It refers to the margin or separation between top-ranked candidates in embedding-based retrieval.

## Deterministic or rule-based systems

Used mainly as a contrast class. These systems are valued for transparency and historical usefulness, but often described as hard to maintain and less adaptable than semantic approaches.

## Non-traditional data sources

A recurring umbrella term covering websites, patents, sensors, satellite data, balance sheets, and other sources outside classical survey or administrative pipelines.

## Document-to-structure extraction

Transformation of heterogeneous textual documents into structured statistical information. In the anti-violence-network paper, this means extracting institutions, signatories, promoters, involved actors, and governance roles from formal agreements, while avoiding roles or attributes not explicitly supported by the text.

## Promoting subjects / involved actors / governance actors

Role distinction used in the anti-violence-network work. Promoting subjects initiate or formally promote a network; involved actors participate operationally; governance actors exercise coordination, monitoring, or strategic oversight when these responsibilities are explicitly stated in the document.

## Trustworthy AI

Not merely an ethical slogan. In the corpus it refers to a concrete package of validation, transparency, privacy protection, governance, robustness, and alignment with Official Statistics principles.

## User-centred dissemination

The idea that statistical information must be discoverable and usable by non-experts through natural-language interfaces, semantic search, interactive tools, and AI-assisted reporting.
