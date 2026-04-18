# Semantic Integration of Textual Data in

- Source file: `raw/workshop/2026-slides-ai-reliability.pdf`
- Document type: `workshop`

## Extracted Text

Semantic Integration of Textual Data in
Official Statistics:
From Deterministic Coding to Language Models
Mauro Bruno
Utrecht University, March 18, 2026

Official statistics rely on structured
classifications
•Official statistics transform real-world phenomena into structured categories.
•Classifications such asNACE,ISCOprovide a shared statistical language.
•These systems are essential forconsistency, comparability, and
integration.
But integrating new and rapidly evolving data sources into these structured systems
is becoming an increasingly important challenge.

Textual data in Official Statistics
Many emerging data sources used in official statistics containunstructured
textual information.
Examples include:
•Administrative data– demographic, economic, fiscal records
•Web data– information about firms’ products and services.
•Public online data– sources such as patents
These sources contain valuable information but arenot directly compatible
with structured statistical classifications.

Traditional automated coding systems
Traditional systems assign classification codes to textual descriptions using
deterministic rules.
Typical components include:
•Dictionariesderived from classification descriptions
•Parsing and normalization rules
•Matching strategiesbased on word overlap
Examples used in official statistics include systems such asACTRandCIRCE.
These systems match words, but they do not capture meaning.

Matching meaning with AI
Modern AI models represent text asnumerical
vectors, calledembeddings.
In this representation:
•texts with similar meanings are located close
to each other
•similarity can be measured usingdistance
metrics(e.g. cosine similarity)
This allows automated coding systems to match
meaningsrather than individualwords

Lexical vs. semantic representations

Assessing Reliability of AI-based coding
Semantic retrieval generates candidate codes.
How can we assess whetherthe prediction can
be considered reliable?
Reliability can be assessed through:
•confidence thresholds
•prediction sets
•uncertainty quantification
Developing these methods requiresnew
statistical and computational skillswithin
statistical institutions.

AI in official statistics: opportunities and
responsibilities
•New data integration opportunities.Modern AI methods enable
statistical institutions to integrate large volumes of textual and unstructured
data into established classification systems.
•Statistical reliability remains essential.AI predictions must be
supported by quality assessment, uncertainty quantification, and robust
statistical validation procedures.
•New skills for statistical institutions.AI is transforming how statistical
research is conducted, requiring new methods, tools, and stronger AI literacy
across statistical institutions.

Q&A
Thank you for listening!
Mauro Bruno
mbruno@istat.it
