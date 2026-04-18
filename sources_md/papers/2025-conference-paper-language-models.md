# 4rd WORKSHOP ON METHODOLOGIES FOR OFFICIAL STATISTICS | PROCEEDINGS

- Source file: `raw/papers/2025-conference-paper-language-models.pdf`
- Document type: `paper`

## Extracted Text

4rd WORKSHOP ON METHODOLOGIES FOR OFFICIAL STATISTICS | PROCEEDINGS
Language Models for Automated Coding in Official Statistics:
Risks and Opportunities
Francesco Ortame, Mauro Bruno Marco Di Zio 1
Abstract
Statistical classifications, such as NACE, are especially important for National Statistical
Offices (NSOs). Automating the classification process has been a focal point for NSOs in
recent decades, and deterministic, rule-based methods that directly assign codes to natural
language queries have been widely implemented. While accurate, these systems are labour-
intensive and generalise poorly across domains, as each classification requires its own rule
set. Recent advancements in natural language processing, particularly language modelling,
offer an opportunity to improve the efficiency and scalability of the automatic coding process
via semantic search systems. However, they come with their own set of challenges, most
notably Uncertainty Quantification (UQ). We address UQ by employing robust statistical
frameworks based on conformal prediction.
Keywords:Automatic Coding, Language Models, Conformal Prediction
1. Introduction
Large language models (LLMs) represent a recent and significant advancement in the field
of Artificial Intelligence (AI), particularly in natural language processing (NLP). These mod-
els, usually based on Transformer architectures (Vaswaniet al.2017), are trained on large
amounts of text to learn language patterns, semantic relationships, and contextual dependen-
cies across various domains. Through this training, LLMs acquire the ability to understand
and generate (in the case of auto-regressive transformers) text with impressive fluency and
coherence.
Prominent examples, including the GPT series (Brownet al.2020), LLaMA models
(Touvronet al.2023), and more recent reasoning models such as DeepSeek (Team 2024)
and Qwen (Baiet al.2024), demonstrate the increasing scale and capability of such systems,
often involving hundreds of billions of parameters (Raffelet al.2020). Unlike traditional
machine learning models designed for narrowly defined predictive tasks, modern language
models generalise across diverse linguistic applications, ranging from summarisation, trans-
lation, and question answering to text classification and representation. In the context of
1Francesco Ortame (francesco.ortame@uniroma1.it), Sapienza University of Rome, Italy; Italian National Insti-
tute of Statistics (Istat), Italy;
Mauro Bruno (mbruno@istat.it), Italian National Institute of Statistics (Istat), Italy;
Marco Di Zio (dizio@istat.it), Italian National Institute of Statistics (Istat), Italy.
The views and opinions expressed are those of the author and do not necessarily reflect the official policy or
position of the Italian National Institute of Statistics - Istat.
ISTITUTO NAZIONALE DI STATISTICA 1

SESSION 2 | AI/ML FOR OFFICIAL STATISTICS
generative models, their capacity to produce contextually relevant and human-like responses
positions them as valuable tools for enhancing information retrieval, automation, and deci-
sion support in data-intensive environments.
However, the probabilistic nature of LLMs poses challenges for interpretability, bias, and
reliability. These models may reproduce social and linguistic biases from their training data
and produce inaccurate or fabricated content, a phenomenon known as “hallucination” (Ji
et al.2023). Such issues highlight the importance of careful fine-tuning, human oversight,
and ethical governance to ensure that LLMs are used responsibly, especially in public-sector
settings such as official statistics.
Language models are not always generative. Text representation models, such as BERT
(Devlinet al.2019), S-BERT (Reimers and Gurevych 2019), and GTE (Li, Lin,et al.2023),
encode text into dense, high-dimensional vectors. This can be done at the token level (word
or sub-word), where a sentence is represented as a variable-length sequence of dense vectors
(token-level embeddings), or at the sentence level, where each sentence is represented as a
single dense vector (sentence-level embedding). These representations are typically used for
text classification and clustering tasks, where text generation is not required.
The introduction of LLMs presents significant opportunities for national statistical offices
(Buonoet al.2024). Within statistical organisations, LLMs can automate routine adminis-
trative tasks such as drafting correspondence, writing reports, and preparing documentation,
thereby improving operational efficiency (UNECE HLG-MOS 2025). This automation en-
ables skilled personnel to focus on analytical and methodological tasks that require expert
judgement and contextual understanding.
At the production level, LLMs can potentially be integrated into various phases of the
Generic Statistical Business Process Model (GSBPM) (UNECE 2025). They can support
questionnaire design, text classification, data validation, and the production of narrative in-
terpretations of statistical outputs. Additionally, LLMs can facilitate metadata management,
translate programming code between languages (e.g., SAS to R), and generate synthetic
datasets for testing and methodological development. Conversational AI interfaces that use
retrieval-augmented generation (RAG) can also transform data dissemination by allowing
users to query statistical databases in natural language and receive context-specific explana-
tions or visualisations.
However, these opportunities must be weighed against the associated risks. The opaque
and data-dependent design of LLMs raises concerns about the accuracy, neutrality, and con-
fidentiality of AI-generated outputs — principles that underpin official statistics (United Na-
tions 2014). To protect these principles, human review and clear governance mechanisms
are essential. Establishing robust ethical frameworks, transparency standards, and validation
protocols is crucial to ensuring that the integration of LLMs enhances rather than undermines
institutional credibility.
Finally, as public engagement with information increasingly occurs through AI-driven
interfaces, statistical agencies face a strategic need to maintain their role as trusted sources
of data. Collaborative partnerships among statistical organisations, academia, and AI devel-
opers can foster the development of reliable and verifiable generative AI applications that
broaden access to official data while ensuring accuracy, accountability, and public trust (UN-
ECE HLG-MOS 2023).
In this paper, we examine the use of LLMs to assign ATECO codes to economic activities
2 ISTITUTO NAZIONALE DI STATISTICA

4rd WORKSHOP ON METHODOLOGIES FOR OFFICIAL STATISTICS | PROCEEDINGS
based on user-provided descriptions. The current tool used by Istat is CIRCE (Istat 2016),
developed in R. It mainly relies on a thesaurus that has been manually updated year by year
by dedicated staff. Users’ descriptions are compared with the thesaurus content, and one or
more ATECO codes are generated using string matching algorithms.
The transition to the new ATECO 2025 (Istat 2025) classification would require revising
the thesaurus, which is both costly and time-consuming. LLMs could potentially provide a
more flexible alternative for this transition.
In this work, we use two different kind of language models for different purposes: (1)
generativeLLMs to create a dataset of synthetic user queries labelled with ATECO codes,
and (2)non-generativeLLMs, in particular sentence encoders, to encode these texts into a
high dimensional representation space where we can perform retrieval/classification based
on user queries. Results obtained via language models are assessed against CIRCE-assigned
labels; therefore, each performance measure is to be interpreted as concordance with CIRCE
rather than plain accuracy. We explore two different retrieval/classification strategies to as-
sign ATECO codes to natural language queries:cosine-based retrieval, typical of retrieval-
augmented generation (RAG) applications (Lewiset al.2020), andlinear discriminant anal-
ysis. Moreover, we address the issue of uncertainty quantification with language models
applying Conformal Prediction techniques (V ovket al.2005; Angelopoulos, Bates,et al.
2023).
This paper aims to assess the feasibility of using LLMs for ATECO classification and to
determine whether they represent a viable alternative to the traditional approach. It is impor-
tant to note that we focus on ATECO 2007 rev. 2022 (hereafter referred to as ATECO 2022)
rather than ATECO 2025, as we have CIRCE-labelled data for ATECO 2022. Additionally,
we focus on 2-digit codes, specifically ATECOdivisions. However, given the flexibility of
our proposed approach, this system can be easily extended to the ATECO 2025 classification
and other statistical classifications with relatively low effort.
2. Data
This study relies on three complementary datasets that together provide a comprehen-
sive view of economic activity descriptions and their corresponding ATECO codes. The first
dataset contains theofficial ATECO 2022 classification, which defines the hierarchical struc-
ture and textual descriptors used for coding. The second dataset consists ofCIRCE-labelled
queries, representing real-world user inputs collected through Istat’s online classification ser-
vice. Finally, asynthetic datasetwas generated using a large language model (GPT-5-mini)
starting from the official classification. Table 2.1 summarises the main features of these
datasets.
2.1 ATECO Official Classification (2007 rev. 2022)
The ATECO classification groups economic activities that are assumed to be similar, fol-
lowing the principles of completeness and mutual exclusivity (Istat 2022). Each category
belongs to a single branch, ensuring an exhaustive and coherent representation of the national
production system. The hierarchy comprises six levels — Sections (letters A–U), Divisions
ISTITUTO NAZIONALE DI STATISTICA 3

SESSION 2 | AI/ML FOR OFFICIAL STATISTICS
Table 2.1 – Summary of datasets used in the study.
Dataset Source Size / Scope Purpose in study
ATECO 2022 Istat, official classification 21 Sections, 87 Divisions,
∼1,200 Sub-categories
Hierarchical reference and base for
data augmentation
CIRCE-labelled
queries
Istat, classification tool 33,544 user-generated queries Benchmark for evaluating semantic
vs. rule-based classification
Synthetic dataset GPT -5-mini (OpenAI, 2025) 12,400 generated examples Data augmentation, balancing and
knowledge base creation
(2 digits), Groups (3 digits), Classes (4 digits), Categories (5 digits), and Sub-categories (6
digits) — covering 21 sections, 87 divisions, and more than 1,200 sub-categories in total.
Beyond numeric codes and titles, ATECO includes explanatory, inclusion, and exclusion
notes that define the scope and boundaries of each code. General notes describe the overall
domain of a branch; inclusion notes list typical activities covered by a code; and exclusion
notes indicate those classified elsewhere. This detailed documentation supports consistency
and comparability across statistical domains but also increases the linguistic complexity of
the classification, posing challenges for automatic coding systems.
Figure 2.1 - Distribution of active businesses in Italy by ATECO division (2-digit code) as of December 2024. Shaded
background areas and capital letters indicate ATECO sections.
Source: Own computation based on Istat Business Register.
Figure 2.1 shows the distribution of active businesses in Italy by ATECO division (2-
digit level) as of December 2024. The figure highlights a highly unbalanced structure: for
instance, Division 47 (Retail trade) accounts for more than 680,000 enterprises, whereas Di-
vision 99 (Activities of extraterritorial organisations and bodies) includes only a few cases.
This imbalance has direct implications for the design of classification models, motivating the
4 ISTITUTO NAZIONALE DI STATISTICA

4rd WORKSHOP ON METHODOLOGIES FOR OFFICIAL STATISTICS | PROCEEDINGS
use of complementary data sources to ensure adequate representation across the entire taxon-
omy. Although this study focuses on the 2022 version, the proposed methods are designed to
support the transition to ATECO 2025 (Istat 2025).
2.2 CIRCE-labelled Real-world Queries
To evaluate the proposed semantic-search approach, we rely on real-world data collected
through CIRCE, the rule-based system currently used by the Italian National Institute of
Statistics (Istat) to assist businesses and professionals in identifying the appropriate ATECO
category from short natural-language descriptions (Istat 2016). CIRCE has been publicly
available since 2016 and is accessible through the Istat classification portal.2
The dataset consists of 33,544 user queries, each processed through the CIRCE algo-
rithm to obtain a predicted 5-digit ATECO code. This output constitutes a labelled corpus
that reflects authentic user interactions with the system. The corpus is used as a benchmark
to assess the alignment between traditional rule-based classification and embedding-based
Semantic Search.
Figure 2.2 - Distribution of CIRCE-assigned labels across ATECO divisions (2-digit codes). Shaded background areas
and capital letters indicate ATECO sections.
Source: Own computation based on CIRCE system outputs (Istat).
Figure 2.2 shows the distribution of CIRCE-assigned labels by ATECO division (2-digit
level). The shape of this distribution broadly mirrors the overall population of Italian enter-
prises (see Figure 2.1), with Division 47 dominating the dataset and low-frequency divisions,
such as Division 99, appearing only marginally. This imbalance is a key factor considered in
the experimental design described in the following section.
2https://www.istat.it/classificazione/classificazione-delle-attivita-economiche-ateco-2007-aggiornamento-2022/
ISTITUTO NAZIONALE DI STATISTICA 5

SESSION 2 | AI/ML FOR OFFICIAL STATISTICS
2.3 Synthetic Dataset
Sentence encoder models are trained to encode semantically similar sentences close in
the sentence representation space. These models process large amounts of data during train-
ing and may contain inherent encoding biases. For instance, sentences that are similar in
thematic content but differ in length, style, or overall tone can be projected into quite distant
regions of the representation space. For this reason, it is ideal that, when classifying a nat-
ural language input query, the reference sentences (representative of the ATECO divisions)
are somewhat similar to the input query. In theory, we could directly encode the official de-
scriptions of ATECO codes, but this yields empirically lower performance. Moreover, some
ATECO divisions include only a few codes, leading to a significant imbalance in the dataset.
For these reasons, we generated a synthetic dataset of business activity descriptions using
a generative LLM,GPT-5-mini(OpenAI 2025). The model was instructed to create ten short
queries for each ATECO sub-category (6-digit level), resulting in a total of 12,400 synthetic
examples. Each prompt combined the official ATECO descriptors (including titles, explana-
tory notes, and inclusion/exclusion rules) to ensure semantic coherence with the taxonomy.
Moreover, the model was given several real-world queries as examples to better reproduce
their style and tone.
For each sub-category, the model generated realistic free-text descriptions of economic
activities, mirroring the type of input provided by enterprises and professionals through the
CIRCE platform. These synthetic queries were then grouped by the 2-digit division level.
3. Methodology
In this section, we will first briefly outline the idea behind CIRCE, then move onto de-
scribing Sentence Embeddings, describing different ways to use them for semantic similarity
search, and finally show a way to ground our predictions in statistical frameworks.
3.1 CIRCE
Traditional automatic coding systems in official statistics rely on deterministic rule sets
and weighted keyword matching. These approaches use dictionaries derived from the clas-
sification, where entries and user queries are pre-processed through tokenisation, stop-word
removal, and synonym replacement, then represented as sets of weighted n-grams. Systems
such as CIRCE (ACTR v3 engine) compare parsed queries with all dictionary entries and
compute similarity scores to determine whether a match is unique, multiple, possible, or
failed, based on score thresholds. While transparent and easily tuned by domain experts,
these methods face key limitations: they lack semantic understanding, depend on constant
maintenance of tokenisation and synonym rules, enforce rigid token-level matching, and
scale poorly to new taxonomies. These issues, made evident during Italy’s transition from
ATECO 2022 to ATECO 2025, underscore the need for more flexible, language model–based
approaches that capture meaning and context beyond surface-level tokens.
6 ISTITUTO NAZIONALE DI STATISTICA

4rd WORKSHOP ON METHODOLOGIES FOR OFFICIAL STATISTICS | PROCEEDINGS
3.2 Sentence Embeddings
Token-level embeddings assign vectors to individual words or subwords, capturing local
lexical and morphological information. Sentence-level embeddings, by contrast, compress
the whole text into a single vector that captures global semantics and context, i.e., the overall
meaning or intent of the sentence rather than the meaning of each token in isolation. For
our task (classifying economic activities), this global view is often more useful, treating an
activity description as a single semantic unit rather than a bag of token features.
es =π(s), e s ∈R d
Our approach builds a representation space for the economic activity taxonomy, theknowl-
edge base, in which each activity code is mapped to a dense, high-dimensional vector. We
create these embeddings using sentence-level models (Reimers and Gurevych 2019), which
produce a single fixed-length vector for an entire piece of text. This lets each code be rep-
resented as a compact semantic fingerprint in the shared vector space. In particular, we rely
on the pre-trainedgte-multilingual-baseembedding model (Li, Lin,et al.2023), which
maps sentences to768−dimensional embedding vectors.
Since we have multiple sentences assigned to each ATECO division, we end up with a
one-to-many (division-to-vectors) mapping.
Retrieval strategiesOnce activity codes are embedded in the shared vector space, seman-
tic similarity between them can be efficiently measured usingcosine similarity. This metric
evaluates the cosine of the angle between two embedding vectors, effectively capturing how
close their meanings are, regardless of vector magnitude. In this framework, retrieval be-
comes a geometric search problem: identifying the codes whose embeddings are most sim-
ilar (i.e., closest in angle) to a given query vector, enabling intuitive, meaning-based lookup
and matching across the taxonomy. Considering our one-to-many mapping, we define the
similarity scores assigned to each ATECO divisionD j, for input queryx i, as:
score(Dj) = max (sim(π(x i), e1,j)), . . . , sim(π(xi), eM,j ))
whereπ(x i)is the embedding vector assigned to queryx i, and{e n}M
i=1 are theMembedding
vectors (corresponding toMsentences) that characterise divisionD j. That is, each division
is assigned the highest similarity score between all scores extracted from the corresponding
vectors.
Another alternative approach we explore is Linear Discriminant Analysis (LDA) to re-
trieve relevant codes from the knowledge base. The LDA model is fit on the labelled Sentence
Embeddings, and the probabilities of each ATECO division are retrieved.
3.3 Conformalising Semantic Search
To obtain valid and interpretable uncertainty estimates for semantic classification of eco-
nomic activities, we employ Conformal Prediction (CP) procedures. Conformal prediction
provides a distribution-free framework for constructing prediction sets, i.e., collections of
ISTITUTO NAZIONALE DI STATISTICA 7

SESSION 2 | AI/ML FOR OFFICIAL STATISTICS
candidate labels that contain the true class with a user-specified probability1−α. We will
explore both direct CP implementations, such as Split Conformal Prediction and Adaptive
Prediction Sets, and Conformal Risk Control, which extends CP to any monotone loss func-
tion (Angelopoulos, Bates,et al.2024).
3.3.1 Split Conformal Prediction and Adaptive Prediction Sets
Given a nonconformity score (or “uncertainty”) score functions(x, y)that quantifies how
atypical a labelyis given an inputx, the conformal algorithm calibrates a threshold on these
scores using a held-out calibration set. For a new queryx new, the conformal predictor then
outputs all labelsywhose scores do not exceed this calibrated threshold, hence guaranteeing
coverage under exchangeability assumptions. While CP guaranteesmarginalcoverage, it
cannot guaranteeconditionalcoverage in any of its forms. However, if best practices are
followed, one can get close to it in practice (Angelopoulos, Bates,et al.2023).
Formally, let(x, y)denote a random query and its true class, withy∈ {1, . . . , N}. We
assume we have an embedding mapx7→e(x)∈R d (our sentence encoder), and a finite
calibration setD cal ={(x i, yi)}n
i=1 drawn exchangeably with the test query. The goal is
to turn a score functions(x, y)(low score=plausible label) into a set-valued prediction
Cα ⊆ {1, . . . , N}that satisfies the usual marginal coverage guarantee:
Pr(y∈C α(x))≥1−α
for a user-chosen miscoverage levelα∈(0,1).
In our setting, each query is a natural-language description of an economic activity,
and each possible class corresponds to an ATECO division (Npre-defined labels). Recalling
previous paragraphs, we can define two alternative heuristics for the nonconformity score:
1. Cosine similarity, measuring semantic alignment between the query and class embed-
dings (lower similarity implies higher nonconformity);
2. Calibrated posterior probability from the Linear Discriminant Analysis (LDA) clas-
sifier, trained in the same embedding space, where uncertainty (or nonconformity) is
represented as1−p(y|x).
As for ourcalibrationD cal andvalidationD val sets, used for calibrating the procedure
and computing coverage and diagnostics, respectively, we split the CIRCE-labelled dataset
in half, leading to16,772observations for each set. Note that the CIRCE dataset is never part
of either the knowledge base creation or training processes.
The quality of CP procedures, beyond the coverage guarantee, is usually assessed via two
properties:efficiencyandadaptivity. The former depends on the overall size of prediction
sets, where smaller sizes are associated with higher efficiency, while the latter refers to the
procedure’s ability to create larger prediction sets for harder examples, and smaller prediction
sets for easier examples. Different CP algorithms lead to different efficiency and adaptivity
properties. We apply both Split Conformal Prediction (SCP) and Adaptive Prediction Sets
(APS) procedures (Leiet al.2018; Romanoet al.2020).
8 ISTITUTO NAZIONALE DI STATISTICA

4rd WORKSHOP ON METHODOLOGIES FOR OFFICIAL STATISTICS | PROCEEDINGS
Split Conformal PredictionDefine a nonconformity scoreq i =s(x i, yi)for each
calibration pair inD cal. Sort thencalibration scores in increasing order and letq (k) denote
thek−th smallest.
For finite-sample marginal coverage, we use the quantile index
k∗ = ⌈(n+ 1)(1−α)⌉
n , τ=q (k∗).
The Split Conformal Prediction set for a new queryx new is
Cα (xnew) ={y∈ {1, . . . , N}:s(x new, y)≤τ}
Under the exchangeability assumption, this guarantees
Pr(y∈C α(x))≥1−α.
The efficiency of this procedure can be measured by the average set size
AvgSize(α) =E[|C α(x)|].
Adaptive Prediction Sets (APS)When the model provides a probability distribution
{pk(x)}N
k=1 over labels, APS constructs Adaptive Prediction Sets that reflect the model’s
uncertainty. For each calibration example, define the APS score for the true labelyas the cu-
mulative probability mass up to and includingy, when classes are sorted in decreasing order
ofp k(x):
S(x, y) =
X
k:pk(x)≥py(x)
pk(x).
Intuitively,S(x, y)is the total probability mass of all labels ranked above (and including) the
true one: smallSmeansylies among the top-probability labels.
Compute calibration scoresS i =S(x i, yi)onD cal, then take the
τAPS =S (k∗), k ∗ =⌈(n+ 1)(1−α)⌉.
For a new inputx, the APS prediction set is
C α
APS(x) ={y:S(x, y)≤τ APS}.
Equivalently,C APS
α (x)is the smallest set of top-ranked labels whose cumulative probability
mass is at mostτ APS.
APS typically yields smaller, more informative sets on confident examples (wherepis con-
centrated) and larger sets on ambiguous ones, while maintaining coverage at level1−α.
ISTITUTO NAZIONALE DI STATISTICA 9

SESSION 2 | AI/ML FOR OFFICIAL STATISTICS
3.3.2 Conformal Risk Control
We also consider a Conformal Risk Control formulation to control the false negative rate
(FNR) rather than the usual marginal miscoverage. In this setting, the goal is to produce set-
valued predictionsC(x)⊆ {1, . . . , N}such that, with high confidence, the population FNR
(probability that the true label is not included in the returned set) does not exceed a user-
specified targetα. Concretely, lets(x, y)be a conformity score where larger values indicate
greater conformity (e.g., cosine similarity or a calibrated class probability). For a thresholdτ
the set predictor is:
Cτ (x) ={y:s(x, y)≥τ}
Using a held-out calibration set of sizen, we compute the empirical FNR at candidate thresh-
olds as:
ˆF N R(τ) = 1
n
nX
i=1
1{s(xi, yi)< τ},
and apply a one-sided concentration correctionε=
p
log(1/δ)/(2n)for confidence level
1−δ. To guarantee (with probability≥1−δ) that the true FNR is at mostα, we select
the largest thresholdτsatisfying ˆF N R(τ)≤α−ε(ifα−ε <0we require ˆF N R(τ) =
0). This procedure produces the smallest prediction sets that still satisfy the risk control
guarantee. The method, like CP, only requires data exchangeability and can be applied with
any monotone conformity score.
4. Results
In this section, we first present the results obtained using cosine similarity-based retrieval
of correct labels and LDA-based label prediction. Then, we apply Conformal Prediction al-
gorithms to both cosine similarity values and LDA output probabilities to build statistically
valid prediction sets.
Table 4.1 – Performance of different retrieval strategies (matching with CIRCE labels).
Strategy Hit@1 Hit@3 Hit@5
Cosine similarity 0.549 0.8270.902
LDA probabilities0.630 0.8310.881
Table 4.1 shows hit@1, hit@3, and hit@5 metrics. These are computed by checking whether
the correct label is found inside thetop k extracted labels. We can see how LDA-based pro-
duces better results (i.e., more in line with CIRCE labels) at the first retrieved positions, while
cosine similarity-based retrieval achieves higher performance when considering the first five
extracted labels. However, producing fixed-size prediction sets, i.e., top 5 results, is not op-
timal for such applications. Therefore, we proceed to calibrate threshold values to create
dynamically sized prediction sets.
10 ISTITUTO NAZIONALE DI STATISTICA

4rd WORKSHOP ON METHODOLOGIES FOR OFFICIAL STATISTICS | PROCEEDINGS
4.1 Experiment A. Cosine Similarity as Conformity Score
In this first experiment, we use pair-wise cosine similarity scores, computed between
each possible pair of query-code embedding vectors, as heuristic notions of uncertainty. In
particular, lower cosine similarity scores indicate higher levels of nonconformity, while the
contrary is true for higher cosine similarity values. Since we have a one-to-many mapping in
our knowledge base, i.e., multiple embedding vectors represent the same ATECO division,
we take the maximum cosine similarity for each division. This way, for each query, we
end up with a score for each ATECO division. Figure 4.1 shows the distribution of cosine
similarity values assigned to true labels (CIRCE-assigned labels) for each division. We can
observe how cosine similarity scores can differ significantly across divisions. This is due to
the pre-training of the language model (sentence encoder) and its inherent biases.
Figure 4.1 - Distribution of cosine similarity scores assigned to correct labels across ATECO divisions.
4.1.1 Standard Split CP Algorithm
We first apply a standard Split Conformal Prediction algorithm, one of the simplest CP
applications. In this case, the nonconformity score is computed simply as1−cos_sim(ytrue).
Using these scores, we extract a calibrated90 th percentileˆqSCP of0.313, which we use to
construct the prediction sets: each observation with a nonconformity score lower thanˆq SCP
is included in the prediction set. This yields an average empirical coverage of89.9%.
To inspect the label-stratified coverage (LSC) of our procedure, we plot the average cov-
erage for each ATECO division (Figure 4.2). We order the divisions by their prevalence in the
validation set, as we give more importance to more populated divisions. As for prediction set
ISTITUTO NAZIONALE DI STATISTICA 11

SESSION 2 | AI/ML FOR OFFICIAL STATISTICS
Figure 4.2 - Average coverage for the split CP procedure (left axis) by ATECO division, ordered by normalised count
(right axis). Cosine similarities as conformity scores
size, the average extracted set size is8.09. This means that, on average, a query is assigned
∼9%of the whole label space, which is a fairly large share.
4.1.2 Adaptive Prediction Sets (APS)
Here, we use a different CP procedure, namely Adaptive Prediction Sets (APS). This time,
the score function considers the entire cumulative distribution of cosine similarity values up
to the correct label. In general, this should improve the procedure’s adaptivity, i.e., its ability
to adjust the set size to the complexity of the query and produce smaller sets on average. The
extracted90 th calibrated percentileˆqAP S is14.04: labels are included in the prediction set up
until the cumulative distribution of their ordered cosine similarity scores reaches1−ˆq AP S,
yielding an average empirical coverage of90.1%. Figure 4.3 shows the label-stratified cover-
age across ATECO divisions. Indeed, the average prediction set size for the APS procedure is
4.98, much lower than with Split Conformal Prediction, making the procedure substantially
much more efficient.
4.1.3 Conformal Risk Control
Finally, we apply a Conformal Risk Control procedure using cosine similarity scores as
conformity measures. The Conformal Risk Control attains the target FNR with the calibrated
threshold, with an empirical coverage on the validation set of0.909(achieved FNR= 0.091)
andτ= 0.682. The average set size is fairly large (8.76labels) and a small fraction of queries
yield empty sets, which in practice would require a fallback. The label-stratified distribution
of coverage (Figure 4.4) closely mimics the one obtained with Split Conformal Prediction,
especially for the most frequent labels.
12 ISTITUTO NAZIONALE DI STATISTICA

4rd WORKSHOP ON METHODOLOGIES FOR OFFICIAL STATISTICS | PROCEEDINGS
Figure 4.3 - Average coverage for the APS procedure (left axis) by ATECO division, ordered by normalised count
(right axis). Cosine similarities as conformity scores.
4.2 Experiment B. LDA Probabilities as Conformity Scores
In this second experiment, we fit a linear discriminant analysis (LDA) model on
the ATECO divisions’ knowledge base. Each embedding dimension represents a feature
(nf eatures = 768) and the GPT-generated dataset is split into a training and a test set, with a
80 : 20ratio. The output probabilities are calibrated using isotonic regression. We experi-
mented with dimensionality reduction methods, such as PCA and UMAP, but they negatively
impacted performance. We keep the same experimental design as in paragraph 4.1, utilising
calibrated output probabilities as heuristic notions of uncertainty in place of cosine similarity
scores.
Figure 4.5 shows the label-stratified distribution of the probabilities assigned to the correct
ATECO divisions by the LDA model. As we can see, the values greatly vary both between
and within labels.
4.2.1 Standard Split CP Algorithm
Mirroring the previous paragraphs, the nonconformity scores for the SCP algorithm are
computed as1−ˆp(y true|x). We extract a90%calibrated percentileˆq LDA
SCP = 0.984, meaning
that labels that are assigned a probability higher than1−ˆq LDA
SCP . This yields an average
empirical coverage of90.1%prediction sets with an average size of5.2, which is close to
APS on cosine similarity scores. The label stratified coverage is shown in Figure 4.6.
4.2.2 Adaptive Prediction Sets (APS)
We can now apply an APS procedure using the LDA output probabilities. The extracted
calibrated90%percentile is0.977, yielding an average empirical coverage of90.2%and an
ISTITUTO NAZIONALE DI STATISTICA 13

SESSION 2 | AI/ML FOR OFFICIAL STATISTICS
Figure 4.4 - Average coverage for the Conformal Risk Control procedure (left axis) by ATECO division, ordered by
normalised count (right axis). Cosine similarities as conformity scores.
average set size of7.36, which is closer to the standard CP procedure using cosine similarity
scores. Figure 4.8 shows the label-stratified coverage for the APS procedure.
4.2.3 Conformal Risk Control
As for Conformal Risk Control, LDA probabilities produce smaller average prediction
sets compared to cosine similarity scores (6.02labels) and no empty sets on the validation
split, while still satistfying the FNR control guarantee (empirical coverage= 0.91,τ= 0.01).
As for cosine similarity scores, the label-stratified distribution of coverage (Figure) is very
similar to the Split Conformal Prediction procedure.
5. Conclusion
In this study, we examined language modelling-based methods for automatically classi-
fying user queries into an official statistical taxonomy (ATECO, Istat). We used generative
LLMs to create a synthetic dataset of labelled user queries and non-generative LLMs to
encode these queries as embedding vectors in a high-dimensional semantic space. This
allowed us to classify new queries using various strategies, such as cosine similarity-based
retrieval and linear discriminant analysis. When evaluating our approach, we found relatively
high agreement with the rule-based CIRCE method, exceeding 90% across the top five
results. To set calibrated thresholds on cosine similarities and LDA output probabilities, and
to extract prediction sets for each query with statistically guaranteed coverage, we employed
Conformal Prediction (CP) techniques, namely split CP and Adaptive Prediction Sets (APS),
as well as Conformal Risk Control using the false negative rate (FNR) as the loss function.
We analysed the results in each scenario and found that APS procedures tend to yield better
14 ISTITUTO NAZIONALE DI STATISTICA

4rd WORKSHOP ON METHODOLOGIES FOR OFFICIAL STATISTICS | PROCEEDINGS
Figure 4.5 - Distribution of output probabilities assigned to correct labels across ATECO divisions.
results as they produce smaller prediction sets while still guaranteeing marginal coverage.
Although additional work is needed, especially to develop retrieval strategies and fit dis-
criminant models, these preliminary results are encouraging and suggest that the cumbersome
process of defining deterministic rule sets can be simplified by using language models. This
can greatly improve efficiency and scalability without sacrificing statistical robustness, thanks
to modern model-agnostic and distribution-free uncertainty quantification techniques.
References
Angelopoulos, A., S. Bates, A. Fisch, L. Lei, and T. Schuster. 2024. “Conformal Risk Control”. In
Kim, B., Y . Yue, S. Chaudhuri, K. Fragkiadaki, M. Khan, and Y . Sun (eds.).International Conference
on Learning Representations, V olume 2024: 55198–55218.URL: https://proceedings.iclr.cc/paper_
files/paper/2024/file/f3549ef9b5ff520a7e41ff3cc306ab2b-Paper-Conference.pdf.
Angelopoulos, A. N., S. Bates,et al.2023. “Conformal prediction: A gentle introduction”.Foun-
dations and trends® in machine learning, V olume 16, N. 4: 494–591.
Bai, J., J. Chen, L. Chen,et al.2024. “Qwen2: A Family of Open Language Models by Alibaba
Cloud”.arXiv preprint arXiv:2407.10671.
Brown, T. B., B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam,
G. Sastry, A. Askell,et al.2020. “Language Models are Few-Shot Learners”.Advances in Neural
Information Processing Systems, V olume 33: 1877–1901.
Buono, D., M. Felecan, and C. Tessitore. 2024. “An Introduction to Large Language Models and
their Relevance for Statistical Offices: 2024 Edition”.Report. Eurostat.URL: %7Bhttps://ec.europa.
eu/eurostat/web/products-statistical-working-papers/-/ks-tc-24-006%7D.
ISTITUTO NAZIONALE DI STATISTICA 15

SESSION 2 | AI/ML FOR OFFICIAL STATISTICS
Figure 4.6 - Average coverage for the split CP procedure (left axis) by ATECO division, ordered by normalised count
(right axis). LDA probabilities as conformity scores.
Devlin, J., M.-W. Chang, K. Lee, and K. Toutanova. 2019. “BERT: Pre-training of Deep Bidirec-
tional Transformers for Language Understanding”.Proceedings of NAACL-HLT: 4171–4186.
Istat. 2025.ATECO 2025. https : / / www. istat . it / classificazione / ateco - 2025/. Italian National
Institute of Statistics.
Istat. 2022.ATECO 2022. https : / / www. istat . it / classificazione / classificazione - delle - attivita -
economiche-ateco-2007-aggiornamento-2022/. Italian National Institute of Statistics.
Istat. 2016.CIRCE. https://www.istat.it/classificazioni- e- strumenti/metodi- e- software- del-
processo - statistico / fase - di - elaborazione / codifica - delle - risposte - testuali / circe/. Italian National
Institute of Statistics.
Ji, Z., N. Lee, R. Frieske, T. Yu, D. Su, Y . Xu, E. Ishii, Y . Bang, A. Madotto, and P. Fung. 2023.
“Survey of Hallucination in Natural Language Generation”.ACM Computing Surveys, V olume 55,
N. 12: 1–38.
Lei, J., M. G’Sell, A. Rinaldo, R. J. Tibshirani, and L. Wasserman. 2018. “Distribution-free predic-
tive inference for regression”.Journal of the American Statistical Association, V olume 113, N. 523:
1094–1111.
Lewis, P., E. Perez, A. Piktus, F. Petroni, V . Karpukhin, N. Goyal, H. Küttler, M. Lewis, W.-t.
Yih, T. Rocktäschel,et al.2020. “Retrieval-augmented generation for knowledge-intensive nlp tasks”.
Advances in neural information processing systems, V olume 33: 9459–9474.
Li, X., J. Lin,et al.2023. “General Text Embeddings (GTE): A New Family of Text Representation
Models”.arXiv preprint arXiv:2311.09191.
OpenAI. 2025.Introducing GPT-5. https://openai.com/index/introducing-gpt-5/.
16 ISTITUTO NAZIONALE DI STATISTICA

4rd WORKSHOP ON METHODOLOGIES FOR OFFICIAL STATISTICS | PROCEEDINGS
Figure 4.7 - Average coverage for the APS procedure (left axis) by ATECO division, ordered by normalised count
(right axis). LDA probabilities as conformity scores.
Raffel, C., N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena, Y . Zhou, W. Li, and P. J. Liu.
2020. “Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer”.Journal
of Machine Learning Research, V olume 21, N. 140: 1–67.
Reimers, N. and I. Gurevych. 2019. “Sentence-BERT: Sentence Embeddings using Siamese BERT-
Networks”.Proceedings of the 2019 Conference on Empirical Methods in Natural Language Process-
ing: 3982–3992.
Romano, Y ., M. Sesia, and E. Candes. 2020. “Classification with valid and adaptive coverage”.
Advances in neural information processing systems, V olume 33: 3581–3591.
Team, D.-A. 2024. “DeepSeek-R1: Incentivizing Reasoning Capability in Large Language Mod-
els”.arXiv preprint arXiv:2407.XXXX.
Touvron, H., T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, T. Lacroix, B. Rozière, N. Goyal,
E. Hambro, F. Azhar,et al.2023. “LLaMA: Open and Efficient Foundation Language Models”.arXiv
preprint arXiv:2302.13971.
UNECE. 2025. “Generic Statistical Business Process Model (GSBPM) version 5.2”.Report. May
2025. United Nations Economic Commission for Europe.URL: https://unece.github.io/GSBPM-5.2/
(visited on 11/13/2025).
UNECE HLG-MOS. 2025. “Generative AI in Official Statistics”.Report. HLG-MOS. United Na-
tions Economic Commission for Europe.
UNECE HLG-MOS. Dec. 2023. “Large Language Models for Official Statistics”.Report. Geneva:
United Nations Economic Commission for Europe.URL: https://unece.org/statistics/hlg-mos.
United Nations. 2014.Fundamental Principles of Official Statistics. Resolution adopted by the
General Assembly on 29 January 2014 (A/RES/68/261).URL: https://unstats.un.org/unsd/dnss/gp/
fundprinciples.aspx.
ISTITUTO NAZIONALE DI STATISTICA 17

SESSION 2 | AI/ML FOR OFFICIAL STATISTICS
Figure 4.8 - Average coverage for the Conformal Risk Control procedure (left axis) by ATECO division, ordered by
normalised count (right axis). LDA probabilities as conformity scores.
Vaswani, A., N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polo-
sukhin. 2017. “Attention is all you need”. InAdvances in Neural Information Processing Systems:
5998–6008.
V ovk, V ., A. Gammerman, and G. Shafer. 2005.Algorithmic learning in a random world. Springer.
18 ISTITUTO NAZIONALE DI STATISTICA
