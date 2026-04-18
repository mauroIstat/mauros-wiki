# Beyond String Matching: Embeddings and

- Source file: `raw/workshop/2025-slides-automatic-coding.pdf`
- Document type: `workshop`

## Extracted Text

Beyond String Matching: Embeddings and
Artificial Intelligence for Statistical
Integration
ITACOMS 2025
Bologna, Italy, 1-4 July 2025
Mauro Bruno, Marco Di Zio, Francesco Ortame (Istat)
July 3, 2025

Artificial Intelligence for Statistical Matching
1 Artificial Intelligence in Official Statistics
▶ Artificial Intelligence in Official Statistics
▶ ATECO Classification
▶ Automated Coding Based on Deterministic Methods
▶ Automated Coding Based on Artificial Intelligence
▶ Conclusion

Non-Traditional Data Sources
1 Artificial Intelligence in Official Statistics
Modern AI methods allow for harnessing non-traditional data sources
• Administrative data: administrative data sources containing complex texts
(e.g., company balance sheets, patents). Semantic search techniques allow
to assign classification codes (NACE, ISCO) to each data source.
• Company websites: web scraping combined with Retrieval Augmented
Generation (RAG) workflows allow the estimate of enterprises’ products.
• Social media data: tweets are filtered, classified using sentiment analysis,
and validated through word embeddings and topic modeling techniques
to analyze themes like hate speech.

Semantic Search for Retrieving Statistical Data
1 Artificial Intelligence in Official Statistics
Traditional search engines require users to know the exact keywords used in
table titles or metadata. This limits accessibility, especially for non-experts
unfamiliar with statistical jargon.
Semantic search engines
Semantic search allows users to write natural queries like:
• “companies performing e-commerce”
• “drinking habits of italian population”
The engine interprets the semantic meaning of users’ queries, improving:
• relevance of results
• user experience
• accessibility to a wider audience

Semantic Search for Retrieving Statistical Data
1 Artificial Intelligence in Official Statistics
Figure: Screenshot of the AI Assistant integrated in the IstatData portal.

Artificial Intelligence for Statistical Matching
2 ATECO Classification
▶ Artificial Intelligence in Official Statistics
▶ ATECO Classification
▶ Automated Coding Based on Deterministic Methods
▶ Automated Coding Based on Artificial Intelligence
▶ Conclusion

The Italian version of the NACE classification
2 ATECO Classification
The ATECO classification, used in many statistical domains (e.g., business
registers, enterprise surveys) has the following characteristics:
Hierarchical, with multiple levels: sections, divisions, groups, classes, and
subcategories.
Semantic-rich, with each code described through:
• Central notes: applying to a group and its descendants.
• Exclusion notes: clarifying boundaries by specifying what is not included.
• Inclusion notes: providing examples and clarifications.
This complexity makes automatic classification a challenging task.

Structure and Complexity of ATECO Notes
2 ATECO Classification

Artificial Intelligence for Statistical Matching
3 Automated Coding Based on Deterministic Methods
▶ Artificial Intelligence in Official Statistics
▶ ATECO Classification
▶ Automated Coding Based on Deterministic Methods
▶ Automated Coding Based on Artificial Intelligence
▶ Conclusion

A Generalized Automated Coding System
3 Automated Coding Based on Deterministic Methods
Wenzowski, a researcher from Statistics
Canada, introduced in 1988 a generalized
method for automated text classification.
ACTR performs deterministic coding of
free-text descriptions by matching them with
classification items using:
• Dictionary
• Parsing strategy
• Matching strategy

Comprehensive Istat R Coding Environment
3 Automated Coding Based on Deterministic Methods
CIRCE, developed by Istat and based on ACTR, is a tool for coding free-text
descriptions into official statistical classifications (e.g., NACE, ISCO).

Dictionary Generation
3 Automated Coding Based on Deterministic Methods

Notes on Dictionary Generation
3 Automated Coding Based on Deterministic Methods
• Expert validation is essential:
The dictionary index is generated through preprocessing, but each extracted
token (unigram, bigram, trigram ) must be reviewed and validated by
domain experts to ensure it captures relevant meaning .
• Index structure:
For each subcategory in the ATECO classification, the dictionary may contain
a list of weighted keys representing its semantic signature:
Example: 01.11.00 → growing&cereals (1.0), growing&crops (0.25),
growing&seeds (0.5)
• Maintenance cost:
Adding or updating classifications requires full regeneration of the
dictionary and a complete review by domain experts.

Matching Phase
3 Automated Coding Based on Deterministic Methods
The input text is compared against all dictionary entries:
The matching phase calculates a similarity score ( S), by comparing the input text
with each dictionary entry. Based on the score, computed as a weighted average on
matching terms , CIRCE determines the most suitable match using the following
rules.
Matching outcomes:
Unique: S1 > Smax and ( S1 − S2) > ∆ S
Multiple: S1 > Smax and ( S1 − S2) < ∆ S
Possible: Smin < S1 ≤ Smax
Failed: S1 ≤ Smin or no S1
The thresholds Smin, Smax,∆ S can be tuned by the user.

Limitations of the Classical Approach
3 Automated Coding Based on Deterministic Methods
• Parsing strategy requires manual maintenance:
Rules for tokenization, normalization, and replacement words must be
updated to cover spelling variants and synonyms.
• No semantic understanding:
Sentences are reduced to standardized tokens sorted alphabetically.
E.g., “vendere prodotti agricoli” → vendere, prodotti, agricoli
• Rigid matching logic:
Exact or near-exact word overlap is needed to trigger a match; rephrasings are
often missed.
• Low scalability:
Adapting to new domains or tasks requires building new
dictionaries and strategies from scratch .

Artificial Intelligence for Statistical Matching
4 Automated Coding Based on Artificial Intelligence
▶ Artificial Intelligence in Official Statistics
▶ ATECO Classification
▶ Automated Coding Based on Deterministic Methods
▶ Automated Coding Based on Artificial Intelligence
▶ Conclusion

A Breakthrough in AI Text Understanding
4 Automated Coding Based on Artificial Intelligence
Attention is All You Need:
• Introduced the Transformer
architecture, revolutionizing NLP.
• Based on a new mechanism:
Self-Attention.
• Enables capturing long-range
dependencies and semantic relations.
• Foundation of modern Large Language
Models (e.g., BERT, GPT).
Transformer enables accurate semantic matching of textual descriptions, marking a
shift from rule-based to meaning-based approaches .

Semantic Search Workflow
4 Automated Coding Based on Artificial Intelligence
To test Artificial Intelligence methods for automated coding, we implemented a
semantic search workflow for coding free-text descriptions into official statistical
classifications (e.g., NACE, ISCO).

Knowledge Base Generation
4 Automated Coding Based on Artificial Intelligence
We explored several approaches. For our prototype, we settled on the most
detailed classification level (5 and 6 digits), where for each code, we create one or
more descriptive elements.
Each text is embedded using an open sentence embedding model ( BAAI/bge-m3).

Matching Phase
4 Automated Coding Based on Artificial Intelligence
Once the user inputs a query, the model embeds it and retrieves the topk matches.
If multiple retrieved vectors refer to the same code, only the most similar is
retained.

Limitations of the AI Approach
4 Automated Coding Based on Artificial Intelligence
• High Computational Costs:
Embedding-based models can be resource-intensive, especially when applied to
large knowledge bases or complex document collections.
• Representation Biases:
Sentence embeddings are influenced by training objectives and may overlook
key distinctions. For example, the sentences ”including rice” and ”excluding
rice” could be mistakenly considered similar, leading to inaccurate retrievals
in coding tasks.
• Domain specificity:
Most models are trained on general-purpose text and may underperform on
domain-specific content. Expert-driven fine-tuning and validation are
essential to ensure reliable results.

Artificial Intelligence for Statistical Matching
5 Conclusion
▶ Artificial Intelligence in Official Statistics
▶ ATECO Classification
▶ Automated Coding Based on Deterministic Methods
▶ Automated Coding Based on Artificial Intelligence
▶ Conclusion

Comparison Between Approaches
5 Conclusion

Future Work and Opportunities
5 Conclusion
• First, we need to validate our approach. This will be done in two ways:
— Comparing our results on the 2022 version of the ATECO classification (the one
used by CIRCE) with the baseline.
— Manually labeling a set of texts produced by enterprises using the 2025 ATECO
version and evaluating our system on it.
• We plan to integrate the human-labeled vocabulary that CIRCE uses to
fine-tune and specialize our models.
• When our system goes into production, we will carry out continuous
learning to dynamically improve its performance based on user feedback and
activity.
• Domain expertise will be utilized for validating and enhancing the system’s
performance, rather than building vocabularies.
