# Semantic Integration of Textual Data in

- Source file: `raw/workshop/2026-slides-ai-webscraping.pdf`
- Document type: `workshop`

## Extracted Text

Semantic Integration of Textual Data in
Official Statistics:
Challenges and opportunities
Mauro Bruno
OECD, April 17, 2026

Non-traditional data sources
ModernML/AI methodsenable the integration of non-traditional data sources
in the statistical production process.
•Questionnaire text fields: semantic search methodscan support the
assignment of classification codes to user queries (e.g., NACE, ATECO).
•Enterprise websites:web scraping combined withAI-based retrieval
approachesenables the extraction of information on enterprises’ products
and services, and supports their classification (e.g., PRODCOM).
•Patent data: embedding-based methodscan be used, for example, to
estimate occupations’ exposure to AI.

Automated analysis of Enterprise Websites
Starting in 2013, Istat began exploring the potential of web scraping techniques
within both national and European context.
•E-commerce detection:establish whether an enterprise sells goods or
services online.
•Online job vacancies detection:establish whether an enterprise advertises
job openings on its website.
Statistical objective:use AI/ML methods to derive statistical indicators on
firms’ digitalisation.

Collecting data from web sources
Web scraping involves identifying and extracting relevant information from
enterprise websites. Key challenges include:
•identifying the correct website
•navigating complex and heterogeneous page structures
•extracting relevant content from noisy data
Web data is rich, but difficult to systematically collect and standardize.

Web scraping pipeline
Website identification is a critical step,
as it directly affects the quality of all downstream analyses.

Website Identification: Model Performance
Model Accuracy Recall F1 AUC
Logistic Regression 0.862 0.785 0.778 0.841
Gradient Boosting 0.867 0.813 0.790 0.852
Neural Network0.868 0.827 0.794 0.857
Theneural network modelachieves the best performance across all
metrics and is selected as the final model.

From web data to statistical codes
Web scraping providesraw, unstructured data.
The next step is transforming this information into statistical variables
through automated coding.

Semantic matching for automated coding
Product descriptions are compared with
predefined statistical categories, usingnumerical
vectors, calledembeddings.
Using embeddings:
•both descriptions and categories are
represented in the same semantic space
•similarity can be measured usingdistance
metrics(e.g. cosine similarity)
This allows automated coding systems to match
meaningsrather than individualwords

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
•New opportunities for data integrationAI enables statistical institutions
to integrate large volumes of unstructured textual data into official statistics.
•Statistical reliability remains essentialAI outputs must be supported by
validation, uncertainty quantification, and quality assessment.
•New skills for statistical institutionsAI is transforming statistical
production pipelines, requiring new methods, tools, and stronger AI literacy
across statistical institutions.
The challenge is not only to use AI, but to use it responsibly in Official Statistics.

Q&A
Thank you for listening!
Mauro Bruno
mbruno@istat.it
