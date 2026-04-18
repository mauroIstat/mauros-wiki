# Semantic Confidence in Embedding-Based

- Source file: `raw/papers/2026-conference-paper-patents-semantic-confidence.pdf`
- Document type: `paper`

## Extracted Text

Semantic Confidence in Embedding-Based
Mapping of Patents to Economic Sectors
Giulio Massacci and Mauro Bruno
AbstractConnecting technological innovations to economic sectors is a key chal-
lenge when studying how emerging technologies spread. Patent documents provide
detailed descriptions of new inventions, but their technological classifications do
not directly map to economic activity categories. This paper presents a method-
ological analysis of embedding-based semantic retrieval for linking patent descrip-
tions to economic sectors. Using a dataset of AI-related patents and NACE sector
descriptions, we examine the statistical structure of similarity rankings produced
by a multilingual embedding model and introduce a simple semantic confidence
measure based on the margin between the top-ranked candidates. Results show that
similarity rankings exhibit a consistent structure and that higher confidence values
are associated with substantially higher classification accuracy. These findings pro-
vide methodological insights into the behaviour of embedding-based classification
systems and highlight the potential of simple confidence measures to support more
reliable mapping between technological descriptions and economic taxonomies.
Key words:Text embeddings, Semantic similarity, Patent data, Economic classifi-
cation, Large language models
1 Introduction
The rapid spread of artificial intelligence (AI) technologies is transforming produc-
tion processes, labor demands, and the structure of economic activities. Understand-
ing how technological innovation impacts different economic sectors is therefore an
important research question in economics and official statistics. Patent data serve
as a key source of information for examining technological change, as they offer
detailed textual descriptions of new inventions. However, linking patents to eco-
nomic sectors remains difficult because patent classifications reflect technological
fields rather than the economic activities in which technologies are applied. Recent
research has introduced several methods to evaluate how economic sectors and oc-
Italian National Institute of Statistics (Istat).
1

2 Giulio Massacci and Mauro Bruno
cupations are exposed to emerging technologies. For instance, Webb [2020] assesses
AI exposure by comparing semantic similarities between patent texts and occupa-
tional descriptions.
Despite their growing adoption in empirical research, the statistical behaviour of
embedding-based semantic retrieval systems in classification settings remains rela-
tively underexplored (Reimers and Gurevych [2019], Karpukhin et al. [2020]). This
paper provides a methodological analysis of embedding-based semantic retrieval for
mapping patent descriptions to economic sector classifications. Rather than focusing
solely on predictive performance, we investigate the statistical properties of similar-
ity rankings and introduce a simple confidence indicator based on the separation
between the top-ranked sectors.
2 Data
The empirical analysis is based on patent abstracts and sector descriptions used in
the semantic retrieval framework.
2.1 Patent dataset
Patent data were obtained from Google Patents, a comprehensive open-access plat-
form that aggregates patent documents from major patent offices worldwide. In this
study, the patent abstract served as the primary textual input, as it offers a brief
overview of the invention and its technological scope. Patents were selected using a
set of keywords related to artificial intelligence technologies. Additional filters were
applied to limit the dataset to patents filed between 2000 and 2024, written in En-
glish. After data extraction and filtering, the final dataset includes 103,554 unique
patents.
2.2 Economic sector classification
Economic activities are represented using the NACE Rev. 2.1 classification(Eurostat
[2023]). NACE provides a hierarchical taxonomy of economic activities organized
into sections, divisions, groups, and classes. For the purposes of this study, we oper-
ate at the most detailed level of the classification (four-digit classes), which provides
a sufficiently granular representation of economic activities while maintaining inter-
pretability for sector-level analysis.
2.3 LLM-labelled proxy dataset
To evaluate the behaviour of the semantic retrieval system, we constructed a proxy-
labeled dataset using a Large Language Model (LLM). For a subset of patents (10%
sample), the model was prompted to assign the most relevant NACE class based
on the patent title and abstract. The model was instructed to identify the primary
economic activity most likely associated with the development, production, or com-
mercialization of the patented invention. The resulting LLM-labeled dataset is used
as a proxy for human annotation in the evaluation stage, enabling a consistent com-
parison between embedding-based sector assignments and model-generated sector
labels. While not intended as a ground truth, this proxy provides a coherent and
scalable reference for analyzing the statistical behaviour of similarity-based rank-
ings rather than absolute classification accuracy.

Semantic Confidence in Embedding-Based Mapping of Patents to Economic Sectors 3
3 Methodology
3.1 Embedding-based semantic retrieval
Letp i denote the textual description of patenti, represented by its abstract, and let
s j denote the textual description of sectorjtaken from the NACE Rev. 2.1 classifi-
cation at the four-digit level. Both patent and sector descriptions are mapped into a
shared semantic space using a multilingual embedding model. Let
e(p i),e(s j)∈R d (1)
denote the embedding vectors associated with patentp i and sector descriptions j,
respectively, wheredis the embedding dimension.
Semantic similarity between patents and sector descriptions is measured using
cosine similarity between their embedding vectors. For each patentp i, similarity
scores are computed with respect to all sector descriptions, producing a ranked list
of candidate sectors:
s(1),s (2), . . . ,s(K) (2)
wheres (1) denotes the sector with the highest similarity score andKis the total
number of sectors considered.
3.2 Semantic confidence
While the top-ranked sector provides a natural prediction for the patent–sector map-
ping, the reliability of this assignment may depend on the separation between the
first and subsequent candidates. To quantify this aspect, we define a semantic confi-
dence measure based on the margin between the two highest similarity scores:
C(p i) =sim(p i,s (1))−sim(p i,s (2))(3)
wheres (1) ands (2) denote the first and second ranked sector candidates, respectively.
Intuitively, larger values ofC(p i)indicate stronger semantic separation between the
top-ranked sector and its closest alternative, suggesting a more reliable classifica-
tion.
3.3 Evaluation against proxy labels
To evaluate the behaviour of the semantic retrieval system, we compare the retrieved
sector rankings with a proxy dataset labelled using a large language model.
For each patentp i, lety i denote the set of proxy labels assigned by the LLM, in-
cluding the primary code and any optional secondary codes. Since this set typically
contains one primary sector and only a small number of secondary sectors, the eval-
uation corresponds to matching the retrieved top-ranked sector against a restricted
set of plausible labels. Formally, given a patentp i:
s(1) ∈y i ⇒correct prediction (4)
We evaluate retrieval performance using standard information retrieval metrics,
including Top-1 accuracy and Hit@k(Manning et al. [2008]), and analyse how pre-
diction accuracy varies as a function of the semantic confidenceC(p i).

4 Giulio Massacci and Mauro Bruno
Fig. 1Median cosine similarity between patent embeddings and NACE sector descriptions as a
function of the ranking position. The shaded area represents the interquartile range (p25–p75). The
dashed horizontal line indicates the global baseline similarity across all patent–sector pairs.
4 Results
4.1 Structure of semantic similarity rankings
We first analyse the statistical structure of similarity rankings produced by the
embedding-based retrieval system (Chen et al. [2024]). For each patent, cosine sim-
ilarity scores are computed between the patent embedding and each NACE sector
description, yielding a ranked list of candidate sectors.
Figure 1 shows the median cosine similarity as a function of the ranking posi-
tion across patents, together with the interquartile range. The results reveal a clear
monotonic decay pattern: similarity values decrease smoothly as the rank increases.
The highest-ranked sector typically exhibits a substantially higher similarity score
than subsequent candidates, indicating that the semantic retrieval model captures
meaningful relationships between patent descriptions and sectoral activities.
The relatively narrow and stable interquartile range across ranking positions sug-
gests that this pattern is consistent across patents, with limited dispersion in similar-
ity scores at each rank.
The dashed horizontal line indicates the overall baseline similarity observed
across all patent–sector pairs. The top-ranked sectors consistently appear above this
baseline, while lower-ranked candidates gradually move closer to it. This pattern
suggests that the embedding space provides a structured representation in which
semantically relevant sector descriptions are systematically ranked above unrelated
ones.
4.2 Distribution of semantic confidence
We then analyze the distribution of the semantic confidence measure introduced in
Section 3. Figure 2 shows the empirical cumulative distribution of the confidence
score across patents.
The distribution is strongly concentrated at low values: the median confidence is
0.009 and the mean is 0.013, indicating that for most patents the margin between

Semantic Confidence in Embedding-Based Mapping of Patents to Economic Sectors 5
Fig. 2Empirical cumulative distribution of the semantic confidence score. The vertical lines indi-
cate the median, mean, and 90th percentile of the distribution.
the top two sector candidates is relatively small. The difference between mean and
median reflects the right-skewed nature of the distribution, with a relatively small
number of high-confidence cases driving the upper tail. This pattern reflects the
inherent ambiguity in mapping technological descriptions to economic activities.
At the same time, the upper tail of the distribution highlights a subset of patents
with more pronounced separation between candidates. In particular, the 90th per-
centile is equal to 0.031, meaning that approximately 10% of patents exhibit a con-
fidence level above this threshold, indicating clearer semantic dominance of the top-
ranked sector.
Overall, these results indicate that while semantic retrieval often operates in a
regime of close competition between candidate sectors, it also produces a structured
distribution of confidence values that can be used to distinguish between more and
less reliable assignments.
4.3 Confidence and prediction reliability
The overall retrieval performance of the embedding-based system against the LLM-
labelled proxy dataset is reported in Table 1. Although Top-1 accuracy remains rel-
atively modest, the progressive increase in Hit@kvalues indicates that the correct
sector is frequently retrieved among the top-ranked candidates. This suggests that
the embedding-based retrieval system captures meaningful semantic relationships
between patents and economic activities, even when the top prediction is uncertain.
We then analyse the relationship between semantic confidence and classification
reliability.
Patents are grouped into quintiles based on their semantic confidence score, from
the lowest confidence group (Q1) to the highest (Q5). Top-1 accuracy increases
steadily across quintiles, from approximately 0.17 in Q1 to 0.38 in Q5, indicating a
strong positive relationship between semantic confidence and prediction accuracy.
Despite the fact that correctness is evaluated against a restricted proxy label set,
the observed gradient suggests that semantic confidence provides a useful signal

6 Giulio Massacci and Mauro Bruno
for identifying more reliable classifications. This supports its potential use in selec-
tive validation or human-in-the-loop workflows, where high-confidence cases can
be treated differently from more ambiguous ones.
Table 1Performance of the embedding-based retrieval against the LLM-labelled proxy dataset.
Metric Value
Top-1 accuracy 0.247
Hit@3 / Hit@5 / Hit@10 0.451 / 0.552 / 0.679
Top-1 accuracy (Q1) 0.17
Top-1 accuracy (Q5) 0.38
5 Conclusion
This paper provides a methodological analysis of embedding-based semantic re-
trieval for mapping patent descriptions to economic sector classifications, showing
that similarity rankings exhibit a consistent structure and that the margin between
the top candidates offers a simple and effective signal of prediction reliability. Em-
pirical results indicate that high-confidence cases achieve substantially higher accu-
racy, while the use of an LLM-based proxy dataset enables scalable evaluation but
should be interpreted as an approximate reference rather than ground truth.
These findings highlight the potential of semantic confidence as a practical tool to
support more reliable and transparent classification workflows in official statistics.
In particular, the proposed measure can be used to identify high-confidence cases
for automated processing and low-confidence cases for further validation, enabling
more efficient and targeted human-in-the-loop strategies.
References
Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, and Zheng Liu. Bge
m3-embedding: Multi-lingual, multi-functionality, multi-granularity text embed-
dings through self-knowledge distillation, 2024.
Eurostat. Nace rev. 2 statistical classification of economic activities, 2023. URL
https://ec.europa.eu/eurostat/web/nace.
Vladimir Karpukhin et al. Dense passage retrieval for open-domain question an-
swering.Proceedings of EMNLP, 2020.
Christopher Manning, Prabhakar Raghavan, and Hinrich Sch ¨utze. Introduction to
information retrieval.Cambridge University Press, 2008.
Nils Reimers and Iryna Gurevych. Sentence-bert: Sentence embeddings using
siamese bert-networks. InProceedings of EMNLP, 2019.
Michael Webb. The impact of artificial intelligence on the labor market.Available
at SSRN 3482150, 2020.
