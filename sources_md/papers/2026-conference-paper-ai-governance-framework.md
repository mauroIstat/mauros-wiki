# AI-Based Automatic Coding in Official Statistics:

- Source file: `raw/papers/2026-conference-paper-ai-governance-framework.pdf`
- Document type: `paper`

## Abstract

Artificial Intelligence (AI) is becoming increasingly relevant for official statistics, particularly in tasks that require transforming unstructured textual information into structured statistical variables. In this context, automatic coding represents a key methodological step for linking heterogeneous textual data from administrative and non-traditional sources to official statistical classifications. Compared with traditional rule-based approaches, recent advances in natural language processing, including sentence embeddings, semantic search, and large language models (LLMs), offer greater flexibility in handling evolving classifications and noisy textual descriptions.

This paper presents Istat's approach to AI-based automatic coding through two use cases: the classification of economic activity descriptions into ATECO categories and the assignment of PRODCOM codes to enterprise products using company websites as auxiliary data sources. Together, these cases show how AI-based methods can reduce reliance on manually maintained vocabularies and support more scalable coding workflows, while also raising methodological issues related to validation, statistical quality, transparency, and integration into production processes.

The paper argues that the adoption of AI for automatic coding in official statistics cannot be treated solely as a matter of model performance or technological efficiency. It also requires a governance framework capable of defining responsibilities, validation procedures, and operational safeguards for the design and deployment of AI systems. From this perspective, Istat's experience illustrates how methodological innovation can be aligned with the quality principles and institutional requirements of official statistics.

## 1. Introduction

In Official Statistics (OS), many core production tasks depend on transforming free-text descriptions into structured variables consistent with official classifications. This need arises whenever heterogeneous textual inputs, such as enterprise activity descriptions, product descriptions, administrative records, or web content, must be linked to formal statistical categories. In this sense, automatic coding is not a marginal technical task, but a key operational function for ensuring consistency, comparability, and integration within statistical production.

Over the past decade, the environment in which National Statistical Institutes (NSIs) operate has changed profoundly, driven by the digitalization of society, the growing complexity of data ecosystems, and the rapid progress of Artificial Intelligence (AI). At the same time, the volume and heterogeneity of textual data relevant to statistical production have increased, making traditional rule-based coding systems more difficult to maintain and less adaptable to evolving terminology and new data sources. These limitations have encouraged the exploration of AI-based approaches such as semantic search and machine learning (ML) for automatic coding tasks.

Recent advances in natural language processing offer new opportunities in this context. Embedding-based models, semantic retrieval, and large language models can support coding on the basis of meaning rather than exact lexical overlap, thereby improving flexibility when textual descriptions are short, noisy, or only partially aligned with the formal wording of official classifications. However, for NSIs the adoption of AI is not merely a technological choice. It is also a methodological and governance issue that directly affects the integrity, reliability, and legitimacy of OS.

When adopting AI, NSIs must consider not only the model's ability to represent and process natural language, but also the reliability and institutional defensibility of its outputs, for instance through confidence thresholds, uncertainty quantification, validation procedures, and expert review. AI-based coding systems must therefore be embedded within controlled statistical processes in which their outputs can be evaluated, documented, and, when necessary, revised. From this perspective, automatic coding provides a concrete use case for examining how AI can be integrated into OS while preserving quality and accountability.

Against this background, the aim of this paper is to present Istat's approach to AI-based automatic coding through two use cases, highlighting both methodological opportunities and governance challenges. More specifically, the contribution of the paper is twofold: first, it discusses two text-based coding applications that show how semantic and AI-based methods can support statistical classification tasks in practice; second, it frames these applications within an emerging governance perspective aimed at ensuring responsible use, validation, and integration into production processes.

## 2. AI-Based Coding in Official Statistics

In OS, coding is a core function that enables the transformation of textual descriptions into structured variables consistent with official classifications such as ATECO, NACE, ISCO, or PRODCOM. This task arises in multiple contexts, for example when assigning an ATECO code to a free-text description of an enterprise's economic activity or a PRODCOM code to a product reported by an enterprise in a business survey. As statistical production increasingly relies on heterogeneous and unstructured textual data, the ability to assign codes accurately and consistently becomes essential.

Traditionally, these tasks have been addressed through deterministic systems based on lexical rules and manually curated vocabularies. While effective in stable environments, such systems are difficult to maintain as classifications evolve or when new data sources introduce more variable and less standardized language. AI-based approaches, including embedding-based models and semantic search, make it possible to move beyond exact word matching and support coding on the basis of semantic similarity in a shared representation space. This is particularly relevant when textual descriptions are short, noisy, or only partially aligned with the formal wording of statistical classifications.

The following use cases illustrate how Istat is applying AI-based coding in practice, combining semantic methods with validation procedures and controlled integration into statistical production processes.

### 2.1 Use Case: ATECO Automatic Coding

One relevant use case concerns the automatic coding of free-text descriptions of economic activity into ATECO categories. This task is challenging because these descriptions are often short, heterogeneous, and only partially aligned with the formal vocabulary of the classification.

Recent work has therefore explored semantic-search-based approaches in which textual descriptions and official category definitions are represented in a shared semantic space through sentence embeddings. This allows candidate codes to be retrieved on the basis of meaning rather than exact keyword overlap, improving robustness when descriptions are short or linguistically variable. In this scenario, the key challenge lies in the gap between the formal language of official classifications and the variability of real-world textual descriptions, which makes purely lexical matching fragile and motivates the use of semantic representations.

At the same time, the ATECO use case shows that semantic retrieval generates candidate codes, but an additional step is needed to assess whether these outputs can be considered reliable. This requires methods for defining confidence thresholds, constructing prediction sets, and quantifying the uncertainty associated with the prediction, so that similarity scores can be translated into coding decisions in a controlled way. In this sense, semantic search must be complemented by a decision layer that allows the uncertainty associated with the model output to be quantified.

### 2.2 Use Case: From Company Websites to Official Product Codes

A second relevant use case concerns the coding of industrial products into PRODCOM categories using company websites as auxiliary information sources. In business surveys, product coding is often burdensome because descriptions are heterogeneous, incomplete, and highly context-dependent. In this context, web data can provide additional evidence on the goods and services associated with an enterprise, thereby supporting more reliable coding. Recent work has explored modular pipelines in which company websites are identified, filtered to retain product-relevant pages, and then used to extract textual information for coding through methods such as embedding-based retrieval and LLM-assisted coding.

The PRODCOM use case is methodologically important because it shows that coding may depend on prior information extraction. Rather than assigning codes to isolated text inputs, the system must first identify relevant sources, detect informative content, and extract relevant textual evidence before coding. As a result, coding becomes part of a multi-step pipeline rather than a single prediction task. This highlights that coding quality depends not only on the model itself, but also on the relevance and quality of the underlying workflow. At the same time, the modular structure improves traceability, as each stage can be inspected, evaluated, and refined independently.

## 3. Istat's Governance Framework for AI

Within NSIs, innovation must be supported by a robust governance framework capable of ensuring that new methods and tools remain aligned with the principles of OS. In the case of AI, this need is even more pressing because its adoption occurs within a complex and continuously evolving national and international regulatory landscape. More broadly, the responsible use of AI requires legal, ethical, and methodological dimensions to be addressed jointly rather than separately.

For these reasons, the adoption of AI at Istat requires a governance framework that translates general principles into operational rules, processes, and responsibilities. The framework, currently being developed at Istat, is structured around three fundamental and closely interconnected pillars:

- Innovation: procedures for overseeing use case implementation and lifecycle management, with centralized coordination and knowledge reuse.
- Data & Rules: regulatory requirements, data quality, availability, organizational arrangements, and best practices for managing AI systems.
- People: training, capacity building, and structured knowledge sharing to strengthen internal capabilities.

To support the central governance of AI, Istat has established a multidisciplinary Strategic Committee tasked with translating these pillars into concrete operational activities. Within the Data & Rules pillar, the Committee is working on both general policies for all personnel and more specific guidelines for technical staff operating in areas such as development, procurement, and methodology. Activities associated with the Innovation pillar focus on the systematic collection of information, support for developers throughout the lifecycle of AI solutions, and the monitoring of use cases and their performance. The People pillar focuses on strengthening Istat's internal capabilities through training and capacity building in AI technologies, machine learning, deep learning, Python programming, and the implications of the AI Act.

## 4. Conclusion

This paper shows that AI-based automatic coding in official statistics requires not only robust and controlled methodological innovation, but also a governance framework capable of ensuring reliability, validation, and integration into production processes.

From a methodological perspective, future work includes improving benchmark and annotated datasets, refining uncertainty-aware approaches, and developing evaluation procedures that consider not only predictive accuracy, but also consistency, traceability, and suitability for production use. Further work is also needed to better integrate coding models within end-to-end workflows, especially when coding depends on upstream stages of information extraction and data selection.

From the perspective of AI governance, future initiatives will build on the current implementation of Istat's governance framework, including an evaluation questionnaire under development to assess awareness of AI use within the Institute and identify the skills required for targeted strengthening of internal competencies. More broadly, the paper argues that the challenge is not simply to adopt more advanced models, but to embed them within statistical processes that remain reliable, transparent, and fully aligned with the principles of Official Statistics.
