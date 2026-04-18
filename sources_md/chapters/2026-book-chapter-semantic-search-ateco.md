# Semantic Search Techniques for Automatic Coding of Economic Activity in Official

- Source file: `raw/chapters/2026-book-chapter-semantic-search-ateco.pdf`
- Document type: `chapter`

## Extracted Text

Semantic Search Techniques for Automatic Coding of Economic Activity in Official
Statistics
Francesco Ortame 0009-0007-8672-872X, Mauro Bruno 0009-0004-7003-3242
Abstract: This chapter examines embedding -based semantic search as a method to automate
the coding of free-text economic activity descriptions into official statistical taxonomies, while
respecting the quality requirements of Official Statistics (OS), particularly r egarding robust
uncertainty quantification. We focus on Sentence Transformers combined with retrieval and
optional cross -encoder reranking. Using the Italian ATECO 2022 taxonomy of economic
activities as a case study, we evaluate three knowledge base design strategies on a reproducible
synthetic dataset of 12,410 user -like queries. Approaches based on creating centroid
embeddings that represent ATECO codes achieve the best performance (Hit@5: 92.6% with
over 1241 labels), while reranking mainly benefits simpler knowledge -base representations.
To meet OS requirements for defensible decisions, we integrate conformal prediction to
calibrate similarity scores and provide statistically valid uncertainty estimates.
Keywords: Automatic Classification, Semantic Search, Sentence Transformers, Conformal
Prediction, Official Statistics
INTRODUCTION
Over the past decade, the environment in which National Statistical Institutes (NSIs) operate
has changed significantly (Dumpert, 2025). Society’s digitization, the growth of platform -
mediated services, and the rapid advancement of Artificial Intelligence (AI), particularly Large
Language Models (LLMs), have transformed how information is produced and accessed. At
the same time, data ecosystems have become more complex. Consequently, expectations for
Official Statistics (OS) have grown: users increasingly d emand more timely releases, greater
detail and, most importantly, simpler ways to access and interact with statistical data (European
Commission, 2018). Citizens, policymakers, journalists, and researchers increasingly interact
with information through con versational systems and search methods that minimize the need
for technical skills or specialized vocabulary. Traditional dissemination models in OS may no
longer align with the cultural habits of modern users, since they mainly rely on static tables,
keyword-based searches, and metadata -driven navigation. When OS are difficult to interpret,
their public value is diminished, risking to widen the gap between NSIs and society (United
Nations, 2014).

At the same time, the mission of OS is guided by a core set of essential principles:
methodological soundness , quality assurance , transparency, protection of privacy and
confidentiality, and institutional accountability . These principles support trust in OS and
distinguish NSIs from other information providers. The current challenge is therefore twofold:
(1) NSIs must modernize their production and dissemination systems to remain relevant and
accessible, while (2) maintaining the trust and rigor that legitimizes their role as authoritative
producers of public information. The tension between innovation and trust becomes especially
clear in the context of modern AI, where powerful methods also b ring opacity and new risks.
In this context, NSIs have a responsibility to modernize the way OS are produced and
disseminated while preserving their public value, and to frame AI within its core principles,
which should be viewed as the foundation that makes innovation reliable and trustworthy rather
than as obstacles to it (Ricciato et al., 2019).
Across the statistical production chain, AI, and language models (LMs) in particular,
offer opportunities in data collection , managing interactions with respondents, assist
interviewers and explore new collection strategies, in data processing , automating
classification and coding tasks, transforming unstructured non -traditional data sources into
statistical information, and in data dissemination, improving how users access OS, making it
easier to retrieve relevant information and supporting users in inter acting with statistical
content. Importantly, the role of AI in OS is not to replace expert work, but to strengthen it by
improving efficiency and accessibility while preserving methodological quality (CCS -UNS,
2017; UNECE, 2025).
Among recent advancements in Machine Learning (ML), the most significant was the
introduction of Transformer -based LMs (Vaswani et al., 2017), which demonstrated
unprecedented capabilities for representing and generating natural language. Within the
approaches enabled by such models, semantic search has emerged as a particularly promising
methodology for NSIs. Its value lies in enabling systems that can understand the meaning of
user queries expressed in natural language, rather than relying on exact keywo rd matching.
This, in turn, reduces reliance on high-maintenance search and automatic classification systems
based on manually curated rule sets. As a result, semantic search has the potential to enhance
access to and interaction with OS, provided that quality and trust requirements are adequately
ensured (HLG-MOS, 2023).
This chapter contributes to this agenda by examining semantic search as a
methodological and operational approach for the modernization of OS. In recent years, the
Italian National Institute of Statistics (Istat) has invested in research projects that imp lement

advanced ML methods and data-driven approaches (Bruno et al., 2025), expanding its effort to
include several approaches based on LMs, with the explicit goal of integrating them into
production environments in a controlled, feasible, and quality-assured manner. In the following
sections, we present a case study based on semantic search methods for the automatic
classification of free-text descriptions into a complex official taxonomy of economic activities.
We show how this approach can support production workflows by improving the efficiency of
classification processes in OS, and how its outputs can be evaluated within statistical
frameworks that ensure reliable uncertainty estimates.
Traditional Methods for Automatic Classification into Official Taxonomies
Traditional methods for automated coding in OS rely on string-matching techniques and
manually curated rule sets to assign classification codes to textual descriptions , with early
systems already explored in the literature (Wenzowski, 1988). Their long-standing use within
NSIs reflects the need for transparent and reproducible methodologies.
Within this context, Istat developed CIRCE 1, a general-purpose rule-based system for
automated coding across several statistical classifications and languages (D’Orazio & Macchia,
2002; Macchia et al., 2007). CIRCE assigns classification codes by comparing user queries to
structured lexical resources. Input texts are first parsed and normalized, then matched against
classification-specific vocabularies and synonym lists that encode expert knowledge (Figure
1.1). CIRCE remains extensively used at Istat, primarily to support the assignment of ATECO
codes (Istat, 2022), the Italian version of NACE.
[Figure 1.1]
Figure 1.1. Workflow of the CIRCE system. The process is organized into two main phases: (1)
construction of a classification dictionary from the taxonomy via rule -based parsing and text
preprocessing, and (2) matching and rule -based scoring of free -text descriptions to produce
coding outcomes. (Source: own)
While rule-based systems like CIRCE offer reliability and interpretability, their reliance
on manually curated rule sets introduces scalability constraints, particularly as classifications
evolve and linguistic variability in queries increases. These limitations motivate exploring
semantic search approaches that reduce manual effort while maintaining quality.

1 https://www.istat.it/wp-content/uploads/2023/12/Manuale-circe-2-0.pdf

METHODOLOGY
In this section, we explore the use of modern, non -generative LLMs, specifically, Sentence
Transformers, to build semantic search tools for automatic classification of user queries based
on semantic similarity measures. Then, we describe methods for reliably quantifying the
uncertainty of such classifications.
Sentence Transformers and Semantic Search for Automated Coding
Sentence Transformers are language models that map sentences to fixed-size numeric vectors,
called sentence embeddings, such that semantically similar sentences are geometrically close
in the resulting space (Reimers & Gurevych, 2019). Unlike generative models, they produce a
vector representation rather than generated text. This property enables semantic search: instead
of relying on rule-based text matching, the most relevant codes for a user query can be retrieved
by identifying the nearest embedding in a pre-built index.
Sentence transformers are derived from token-level encoder models such as BERT
(Devlin et al., 2019) and multilingual extensions (Conneau et al., 2020), which produce one
vector per input token rather than a single sentence-level representation (Figure 2.1). A
pooling step, typically averaging all token embeddings (mean pooling) or extracting the
representation of a special classification token (CLS pooling), converts these variable-length
outputs into a single fixed-size vector. Applied directly to a pretrained BERT model,
however, these simple pooling strategies tend to yield sentence representations that are poorly
informative, not suited for semantic similarity tasks. Sentence Transformers address this
through a dedicated fine-tuning procedure that adapts the embedding space so that similar
sentences are mapped to nearby vectors and yields substantially better performance on
retrieval and similarity tasks.
[Figure 2.1]
Figure 2.1. Simplified flow to obtain sentence embeddings from token embeddings via pooling
strategies. (Source: own)
To build a semantic search system for automated coding, we construct a knowledge
base, i.e., a structured collection of textual descriptors representing each classification code. In
our setting, each ATECO code can be associated with its official title, of ficial description,
taxonomy notes, and labeled example queries.
The knowledge base is encoded into embeddings and indexed. User queries are then
encoded and matched against the knowledge base via cosine similarity to retrieve the top

candidate codes. We explore three strategies for mapping knowledge base texts to class
embeddings, illustrated in Figure 2.2:
a) Concatenating all texts for a class into a string and encoding them into a single
embedding (one-to-one mapping).
b) Storing each text separately for each class and aggregating per-text similarity scores at
retrieval time (one-to-many mapping).
c) Averaging embeddings of individual texts into a single centroid per class (one -to-one
mapping).
Each approach involves trade-offs between compactness, retrieval granularity, and robustness
to heterogeneous class descriptions, and the best choice depends on the specific use case.
[Figure 2.2]
Figure 2.2. Illustration of three different knowledge base creation and mapping strategies.
Different shades represent classes in the taxonomy and circles represent sentence embedding
vectors. (Source: own)
As an optional final step, candidate codes retrieved by the sentence transformer (acting
as a fast first-stage retriever) can be re-ranked using specialized cross-encoder models, which
score each query -candidate pair more precisely. While computationally more expensive, re -
ranking can improve the ordering of candidates when accurate top-k ranking matters.
Calibrating Uncertainty around Black-box Similarity Scores
Similarity scores produced by sentence transformers are informative but not calibrated
probabilities and can exhibit overconfidence, a well -known issue in neural models (Pearce et
al., 2021). That is, they can be overconfident or biased for rare classes or out -of-distribution
queries. In OS contexts, where decisions must be defensible and error rates controllable, a
single score does not provide a robust basis for setting automatic-accept thresholds.
Conformal Prediction (CP) addresses this by wrapping any black -box predictor and
producing prediction sets, subsets of possible class labels, with a formal, finite -sample
coverage guarantee (Vovk et al., 2005; Angelopoulos & Bates, 2021). Specifically, gi ven a
desired miscoverage level α (the statistical confidence level, e.g., α = 0.10 for 90% coverage),
CP guarantees that the true class will be included in the prediction set at least 1 -α of the time,
regardless of the underlying model. This guarantee hol ds under the mild assumption that
calibration data are exchangeable with test data.
In practice, CP requires a held-out set to compute nonconformity scores – measures of
how unexpected the true label is given the model’s output – and derives a threshold from their

empirical distribution. Prediction sets are then built for new queries by including all labels
whose nonconformity score falls below this threshold. Algorithms such as Adaptive Prediction
Sets (APS) and its regularized variant (RAPS) (Romano et al., 2020; Angelopoulos et al., 2020)
improve on simpler approaches by producing sets that are small when the model is confident
and larger when it is uncertain.
In our setting, CP allows us to define an automatic -accept policy: when the prediction
set is a singleton, the system's assignment can be accepted automatically; when the set contains
multiple candidates, the item is flagged for manual review. This provide s a statistically
grounded mechanism for controlling the trade-off between automation and human oversight.
USE CASE: CLASSIFYING USER QUERIES INTO THE OFFICIAL ATECO
TAXONOMY VIA SEMANTIC SEARCH
Now that we have explained all the necessary theoretical concepts to build a semantic search
classification system, we can present Istat’s use case. Specifically, it involves classifying user
queries, which contain short descriptions of economic activity, into a specific ATECO code to
help them find the right fit within a complex taxonomy.
First, we present the dataset we used and the processing steps we applied. Second, we
go through the actual implementation, including Python code for each section. Last, we show
preliminary results.
It should be noted that, in the actual use case, we also compute an agreement score
between our semantic search-based method and the traditional CIRCE method for a set of real
user queries. However, due to privacy constraints, we can’t publish that dataset . Therefore, to
make this use case publicly available and reproducible, we use a synthetic version that contains
queries generated by an LLM, each labelled with the correct ATECO code. This generation
process is detailed in the following sections.
Datasets
This use case draws on two complementary datasets that jointly capture economic activity
descriptions and their associated ATECO codes. The first dataset is the official ATECO 2022
classification, which provides a hierarchical structure, textual definitions, and additional notes
underpinning all coding tasks. The second dataset is a synthetic corpus of user -like queries
obtained via GPT-5-mini. We describe both in detail in the following paragraphs.

ATECO Taxonomy
The Italian ATECO taxonomy organizes economic activities into progressively detailed
classifications, grouping together entries that share comparable characteristics while adhering
to the principles of completeness and full coverage. Each category is stric tly exclusive: every
activity must be assigned to one (and only one) ATECO code. The categories must also retain
practical relevance, meaning the level of detail cannot be so fine -grained as to jeopardize the
feasibility of data collection. The structure c onsists of six hierarchical layers: (1) Sections,
identified by single letters from A to U; (2) Divisions, marked by two-digit codes ranging from
01 to 99; (3) Groups, with three-digit codes; (4) Classes, with four-digit codes; (5) Categories,
using five -digit codes; and (6) Sub-categories, identified by six -digit codes. Table 3.1
summarizes this hierarchy and the scope associated with each level.
Table 3.1. ATECO 2022 hierarchical structure
Section Division Group Class Category Sub-category
Digits 1 2 3 4 5 6
Size 21 87 270 615 919 1240
Example A, U 05, 73 46.7, 74.2 46.73 46.73.4 46.73.40
Beyond its system of numeric codes and titles, ATECO is supplemented with a comprehensive
set of textual explanatory notes designed to guide accurate classification (Figure 3.1 illustrates
the corresponding structure for NACE, the English equivalent of ATE CO). These notes serve
distinct functions:
● Central notes outline the overarching scope and intent of each code.
● Inclusion notes supply concrete examples of the activities encompassed within a
category.
● Exclusion notes delineate the limits of a code by indicating related activities that should
be placed elsewhere.
● Operational notes offer practical instructions to ensure uniform and consistent
application of the classification in real-world contexts.
[Figure 3.1]
Figure 3.1. Example of a NACE group (01.1) and class (01.11) along with inclusion notes
(blue) and exclusion notes (orange). Both inclusion and exclusion notes located in class 01.11
apply to all nested categories and sub -categories. The text has been shortened for cl arity
purposes. (Source: own)

The integration of a hierarchical framework with comprehensive explanatory notes makes
ATECO both thorough and intricate. While these notes improve clarity and precision for
human coders, they also introduce challenges for automated classification: a singl e enterprise
description can correspond to multiple potential codes across different levels of the hierarchy,
and selecting the correct code often hinges on small distinctions expressed in natural language.
This complexity poses difficulties for traditiona l string-matching approaches but presents an
advantage for contemporary semantic search methods based on Language Models, where rich
semantic context can significantly enhance performance.
Synthetic Dataset
To get an idea of our system's performance, we use GPT -5-mini2 to generate 10 queries for
each ATECO sub-category, for a total of 12,410 labelled queries. To obtain the most accurate
results, we pass information from the latter as context and include some query examples to help
the LLM better match the actual tone an d style of real -world user queries, as few -shot
prompting often improves performance (Brown et al., 2020). We prompt GPT-5-mini via its
API using the following instruction (translated from Italian):
“You are a generator of descriptions of activities carried out by companies and professionals.
Here’s what you need to do:
- You receive as input an economic classification (title + details).
- You generate 10 examples of very brief descriptions of activities carried out by
companies, consistent with the classification.
- Do not generate any text that is not one of the descriptions.
Important information:
- Focus on the indicated activity; do not generate descriptions with different activities
(you may use synonyms).
Some examples of descriptions:
[6 REAL-WORLD QUERY EXAMPLES]
Format the output as a Python list.
[ATECO CATEGORY TITLE + DESCRIPTION]”

2 Temperature is set to 1.0. As of writing, OpenAI’s API does not allow custom temperatures for GPT -5 models.

We sample 80% of this dataset, balancing by ATECO sub-category, for a total of 9920 queries,
to create the knowledge base in scenarios (b) and (c), while the remaining, non -overlapping
20% (2480 queries) is used for evaluation.
Implementation
Now we can detail the processes of knowledge base creation, retrieval and reranking of
candidates. We use BGE-M3 as our multilingual sentence encoder, and the BGE-reranker-v2-
m3, as out multilingual reranker (Chen et al., 2024).
Knowledge base creation
Here, we explore the three different knowledge base creation methods explained in the previous
sections. In particular, (a) a concatenation method, where we put all the available information
about an ATECO sub-category into an individual string, which we call descriptor, and encode
it into a single vector; (b) a separation method, where we keep all the information about an
ATECO sub-category separate and encode each text into its own vector; (c) a centroid method,
where we encode each text separately and compute the ATECO code-wise centroid averaging
all the embeddings.
(a) Concatenated descriptor per ATECO sub -category (one -to-one mapping) . In this
scenario, we extract all relevant information from the ATECO classification and
concatenate it into a single string ( descriptor), which we then encode with a Sentence
Transformer. This results in a knowledge base with 1241 embeddings, each
corresponding to an ATECO sub-category.
(b) Store and encode each text separately (one-to-many mapping). To create a knowledge
base with a one-to-many mapping between ATECO codes and representative texts, we
simply encode each representative text separately and store its corresponding ATECO
code. We have data from both the official taxonomy and synthetic queries, and we
concatenate them to create a single dataset. Each row contains a single text along its
assigned code, and the knowledge base is created exactly as in (a).
This results in a knowledge base with 14,724 embeddings, meaning that each
ATECO code is, on average, represented by approximately 12 separate texts. In the
results, we analyze the effect of including synthetic queries in the knowledge base
compared to kee ping only the official texts. For simplicity, we use a “max score”
retrieval strategy to assign individual scores to ATECO sub-categories.
(c) Centroid class embedding (one -to-one mapping) . The centroid -based approach at
knowledge base creation is slightly trickier, as we first need to encode each text

separately and only then average the embeddings by ATECO sub -category. Like (a),
this results in a knowledge base with 1241 embeddings, each corresponding to an
ATECO sub-category.
Performance
Here, we show the results of our experiment. Specifically, we compare basic retrieval via
semantic search with further reranking. It should be noted that, in case (a) and (c), reranking is
performed via a pairwise comparison between the user query and the descriptors from the top
5 extracted ATECO sub -categories, while in case (b), reranking is performed via a pairwise
comparison between the user query and the extracted most similar individual text for each of
the top 5 extracted ATECO sub-categories.
Table 3.2 presents the results for each approach using Hit@k metrics, which measure
the number of times the correct ATECO code appears among the top k results.
Table 3.2. Retrieval and reranking performance
Metric Knowledge Base Retrieval Reranking
Hit@1 Descriptor (one-to-one) 49.03% 55.12%
Hit@1 Separated (one-to-many) 55.40% 55.12%
Hit@1 Centroid (one-to-one) 69.90% 62.57%
Hit@3 Descriptor (one-to-one) 68.21% 72.36%
Hit@3 Separated (one-to-many) 74.01% 75.66%
Hit@3 Centroid (one-to-one) 88.36% 84.97%
Hit@5 Descriptor (one-to-one) 75.54% 75.54%
Hit@5 Separated (one-to-many) 81.79% 81.79%
Hit@5 Centroid (one-to-one) 92.63% 92.63%
The centroid-based approach clearly outperforms both other approaches by a large margin.
However, we need to keep in mind that the descriptor approach does not use synthetic data,
which, coming from the same distribution as the evaluation data, might inflate the performance.
It is also interesting to notice that reranking the results only really improves the performance
in the descriptor scenario, while in other scenarios it is indifferent or detrimental. This could
stem from the fact that the reranker finds it easier to handle clearly worse candidates compared
to better ones.

Conformalizing similarity scores
To obtain a statistically grounded measure of uncertainty for the predicted ATECO codes
associated with an input query, we apply a standard split conformal prediction procedure. We
do not employ adaptive prediction sets procedures as they tend to underperform or collapse to
a single prediction set size when the distribution of nonconformity scores is flat rather than
concentrated, which is often the case with cosine similarity scores.
We split our evaluation set into two equal -sized sets: a calibration set to calibrate the
empirical quantile and a test set to analyze the procedure's outcome. We set 𝛼 = 0.1 and obtain
an empirical coverage of 92.3%, meaning that, on average, the correct label was found inside
a prediction set 92.3% of the time. Figure 3.2 shows the distribution of the prediction set size
across the entire test set, i.e., the number of candid ate labels that the procedure considers
relevant.
[Figure 3.2]
Figure 3.2. Prediction set size distribution over the test set for the split conformal prediction
procedure. (Source: own)
As we can see, most of the mass lies in the 1 -9 range, which is a promising result given the
high dimensionality of the label space (1241 labels in total). Such procedures are useful as they
provide statistically valid coverage guarantees while also calibr ating an inclusion threshold,
which is fundamental in semantic search systems that aim to aid users to find a correct code in
a complex taxonomy, greatly restricting the range of options.
CONCLUSION
This chapter examined semantic search as a practical method based on modern Language
Models (LMs) to support production tasks in Official Statistics (OS), focusing on automated
coding into official taxonomies. Starting with the institutional goals and constraints that define
OS, such as privacy protection, transparency, reproducibility, quality, and accountability, we
argued that some Artificial Intelligence (AI) solutions, especially generative models, require
greater prudence than others when implemented in National Statistical Institutes (NSIs). In this
regard, non -generative embedding -based semantic search is particularly well-suited, as it
enhances users’ ability to express their information needs in natural language while keeping
the retrieval process transparent.
The ATECO case study shows the potential of this method in a field where complexity
and language differences are natural. Modern LMs such as Sentence Transformers can support

the identification of candidate codes with high accuracy levels suitable for interactive coding
tools, where the aim is often to produce a short, ranked list of candidate codes rather than a
fully automated decision. Importantly, the results suggest that p erformance strongly depends
on how the classification is represented in the knowledge base (in particular, naïve descriptors
versus separate texts and centroid -based representations). The implementation of Conformal
Prediction (CP) techniques in semantic s earch can lead to the desired outcome of calibrating
an inclusion threshold that guarantees marginal coverage with statistical validity and provides
a reliable filter to shortlist candidate labels.
The methodology outlined in this chapter can be extended to virtually any use case
where free -text descriptions need to be classified within a pre -defined classification or
taxonomy, both for dissemination systems and user interfaces, providing easier interaction with
OS via natural language queries, and for actual statistical processes, where information needs
to be extracted from unstructured data sources such as administrative data.
References
Angelopoulos, A., Bates, S., Malik, J., & Jordan, M. I. (2020). Uncertainty Sets for Image
Classifiers using Conformal Prediction (Version 5). arXiv.
https://doi.org/10.48550/ARXIV.2009.14193
Angelopoulos, A. N., & Bates, S. (2021). A Gentle Introduction to Conformal Prediction and
Distribution-Free Uncertainty Quantification (Version 6). arXiv.
https://doi.org/10.48550/ARXIV.2107.07511
Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A.,
Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G.,
Henighan, T., Child, R., Ramesh, A., Ziegler, D. M., Wu, J., Winter, C., … Amodei,
D. (2020). Language Models are Few-Shot Learners (Version 4). arXiv.
https://doi.org/10.48550/ARXIV.2005.14165
Bruno, M., Catanese, E., Cerasti, E., De Cubellis, M., De Fausti, F., Di Zio, M., Grippo, G.,
Lancioni, G., Massacci, G., Mugnoli, S., Ortame, F., Pappagallo, A., Pugliese, F.,
Righi, A., Sabbi, A., Sisti, F., Summa, D., & Valentino, L. (2025). Big Data and

Machine Learning at Istat. In F. Dumpert (Ed.), Foundations and Advances of
Machine Learning in Official Statistics (pp. 239–298). Springer Nature Switzerland.
https://doi.org/10.1007/978-3-032-10004-7_12
Chen, J., Xiao, S., Zhang, P., Luo, K., Lian, D., & Liu, Z. (2024). M3-Embedding: Multi-
Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-
Knowledge Distillation. Findings of the Association for Computational Linguistics
ACL 2024, 2318–2335. https://doi.org/10.18653/v1/2024.findings-acl.137
Committee of the Chief Statisticians of the United Nations System (CCS-UNS) (Ed.). (2017).
UN Statistics Quality Assurance Framework. UNSYSTEM/2017/3.
https://unstats.un.org/unsd/unsystem/Documents-March2017/UNSystem-2017-3-
QAF.pdf
Conneau, A., Khandelwal, K., Goyal, N., Chaudhary, V., Wenzek, G., Guzmán, F., Grave, E.,
Ott, M., Zettlemoyer, L., & Stoyanov, V. (2020). Unsupervised Cross-lingual
Representation Learning at Scale. Proceedings of the 58th Annual Meeting of the
Association for Computational Linguistics, 8440–8451.
https://doi.org/10.18653/v1/2020.acl-main.747
Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of Deep
Bidirectional Transformers for Language Understanding. Proceedings of the 2019
Conference of the North, 4171–4186. https://doi.org/10.18653/v1/N19-1423
D’Orazio, M., & Macchia, S. (2002). A system to monitor the quality of automated coding of
textual answers to open questions. Research in Official Statistics (ROS), 2, 7–21.
Dumpert, F. (Ed.). (2025). Foundations and advances of machine learning in official
statistics. Springer. https://doi.org/10.1007/978-3-032-10004-7

European Commission (Ed.). (2018). European statistics code of practice: For the national
statistical authorities and Eurostat (EU statistical authority). Publications Office.
https://doi.org/10.2785/914491

HLG-MOS White Paper (Ed.). (2023). Large Language Models in Official Statistics.
Modernstats. https://unece.org/sites/default/files/2023-
12/HLGMOS%20LLM%20Paper_Preprint_1.pdf
Italian National Institute of Statistics. (2022). ATECO 2007—2022 Revision: Classification of
Economic Activities. https://www.istat.it/classificazione/classificazione-delle-attivita-
economiche-ateco-2007-aggiornamento-2022/
Macchia, S., Giovani, P., Perrone, D., Degortes, M., & Mazza, L. (2007). Metodi e software
per la codifica automatica dei dati. Tecniche e Strumenti.
Pearce, T., Brintrup, A., & Zhu, J. (2021). Understanding Softmax Confidence and
Uncertainty (Version 1). arXiv. https://doi.org/10.48550/ARXIV.2106.04972
Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese
BERT-Networks. Proceedings of the 2019 Conference on Empirical Methods in
Natural Language Processing and the 9th International Joint Conference on Natural
Language Processing (EMNLP-IJCNLP), 3980–3990.
https://doi.org/10.18653/v1/D19-1410
Ricciato, F., Wirthmann, A., Giannakouris, K., Reis, F., & Skaliotis, M. (2019). Trusted
smart statistics: Motivations and principles. Statistical Journal of the IAOS, 35(4),
589–603. https://doi.org/10.3233/SJI-190584
Romano, Y., Sesia, M., & Candès, E. J. (2020). Classification with Valid and Adaptive
Coverage. https://doi.org/10.48550/ARXIV.2006.02544

UNECE Statistics Division (Ed.). (2025). Generic Statistical Business Process Model
(GSBPM) version 5.2. https://unece.org/sites/default/files/2025-
07/GSBPM%20v5.2%20%28CES%20endorsed%29.pdf
United Nations (Ed.). (2014). Fundamental Principles of Official Statistics. General
Assembly Resolution 68/261.
https://unece.org/fileadmin/DAM/stats/documents/technical_coop/2014/mtg3/Implem
entation_Guidelines_FOC_state_of_the_art_September_2014.pdf
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł.
ukasz, & Polosukhin, I. (2017). Attention is All you Need. Advances in Neural
Information Processing Systems, 30.
https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845
aa-Abstract.html
Vovk, V., Gammerman, A., & Shafer, G. (2005). Algorithmic learning in a random world
(Second edition). Springer.
Wenzowski, M. (1988). ACTR - A Generalised Automated Coding System. Survey
Methodology, 14(2), 299–308.
