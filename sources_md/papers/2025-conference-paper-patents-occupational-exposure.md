# Occupational Exposure to AI: A Patent-Based Approach Using

- Source file: `raw/papers/2025-conference-paper-patents-occupational-exposure.pdf`
- Document type: `paper`

## Extracted Text

Occupational Exposure to AI: A Patent-Based Approach Using
Large Language Models
Massimo Armenise 1, Mauro Bruno 1, Luigi De Iaco 1, Marianna Mantuano 1, Giulio
Massacci1
1Italian National Institute of Statistics (ISTAT), Italy
How to cite: Armenise, M.; Bruno, M.; De Iaco, L.; Mantuano, M.; Massacci, G. 2025. Occupational
Exposure to AI: A Patent -Based Approach Using Large Language Models . In: 7th International
Conference on Advanced Research Methods and Analytics (CARMA 2025). Rome, 2 -4 July 2025.
https://doi.org/10.4995/CARMA2025.2025.20535
Abstract
Artificial Intelligence (AI) is reshaping labor markets, affecting occupations through
automation and new skill requirements. Following Webb (2020) , this study quantifies
occupational exposure to AI using a patent -based approach combined with large
language models (LLMs) and International Standard Classification of Occupations
(ISCO-08) data. By leveraging semantic similarity analysis, we systematically map AI-
related pate nts to specific job categories. Our findings indicate that ICT -related
professions — Software Developers, Database Professionals, and ICT Service Managers
— exhibit the highest AI exposure. However, AI’s impact is expanding beyond technical
roles, increasingly affecting managerial, creative, and process automation occupations.
Temporal analysis reveals an expansion of AI adoption, initially concentrated in
technical sectors (2000s), later extending to business automation (2010s) , and more
recently influencing creative industries (2020s). These results highlight the need for
adaptive workforce policies, including reskilling programs and AI governance
frameworks, to balance AI-driven productivity gains with labor market stability.
Keywords: Artificial Intelligence; Patent Analysis; Large Language Models; Labor
Market; Statistical Indicators; Time Series.
7th Int. Conf. on Advanced Research Methods and Analytics
2-4 July 2025, Rome, Italy
DOI: https://doi.org/10.4995/CARMA2025.2025.20535
CARMA 2025
This work is licensed under a Creative Commons License CC BY-NC-SA 4.0
Editorial Universitat Polit`ecnica de Val`encia
159

Occupational Exposure to AI: A Patent-Based Approach Using Large Language Models

1. Introduction
The rapid advancements in Artificial Intelligence (AI) are reshaping industries, job roles, and
skill requirements. AI-driven automation, machine learning, and large language models (LLMs)
are increasingly embedded in professional tasks, raising concerns a bout job displacement, skill
polarization, and wage inequality (Cazzaniga et al., 2024; OECD, 2021). The OECD (2021)
notes that AI adoption disproportionately affects routine -based occupations while fostering
growth in knowledge-intensive sectors. Similarly, Cazzaniga et al. (2024) highlight AI’s role in
amplifying labor market inequalities, benefiting high -income workers while middle -skill
workers face substitution risks. Recent research (Comunale & Manera, 2024) suggests AI’s
impact extends beyond routine tasks to high-skill, cognitive-intensive jobs.
Efforts to quantify occupational exposure to AI have grown, with Webb (2020) introducing a
patent-based approach to measure AI’s labor market impact. This methodology, using patent
data as a proxy for innovation, has been extended in studies like Dalla Zua nna et al. (2024),
which find AI exposure concentrated in high -income, service -sector jobs. Cazzaniga et al.
(2024) further show that advanced economies, with more cognitive -intensive occupations, are
more exposed to AI and positioned to benefit. This paper employs a patent-based framework to
quantify occupational AI exposure, mapping patents to job categories using the International
Standard Classification of Occupations (ISCO -08). This study introduces an innovative
approach that uses LLMs to improve semantic similarity analysis between patent abstracts and
job descriptions, utilizing embedding -based techniques . The paper is structured as follows:
Section 2 presents data sources, including Google Patents and ISCO-08 classifications. Section
3 details the methodology, covering patent retrieval, occupational classification, and similarity
analysis. Section 4 discusses results, ranking AI -exposed occupations and analyzing trends.
Section 5 concludes with policy recommendations to mitigate AI-driven labor disruptions.
2. Data
This section presents the data sources used in the study, detailing their origin, structure, and
relevance to assessing occupational exposure to AI based on patent literature. The primary data
sources are Google Patents and the ISCO-08. Google Patents provides a rich textual repository
of global innovations. ISCO-08 serves as a comprehensive taxonomy of occupations, enabling
alignment between patent content and job profiles.
2.1. Google Patents
Google Patents is a comprehensive digital platform offering open access to millions of patent
documents from patent offices worldwide. It includes both granted patents and published
applications from key jurisdictions such as the United States Patent and Trademark Office
(USPTO), the European Patent Office (EPO), and the World Intellectual Property Organization
160

Occupational Exposure to AI: A Patent-Based Approach Using Large Language Models

(WIPO), among others. It provides metadata on patent publications, including title, abstract,
publication number, filing and publication dates, and patent office. Additional tables include
assignees (names and locations), inventors, CPC codes for technology classification, citations
for prior art references, and family members, which link related patents across jurisdictions.
Patent document structures vary by country, and there is no universal format. However, some
sections are common across most patents.
Table 1. Descriptions of the patent sections.
Section Description
Title The name of the invention
Abstract A brief summary of the invention
Background Context and prior art related to the invention
Summary An overview of the invention and its advantages
Detailed Description A comprehensive explanation of the invention
Claims The legal scope and protection defined for the invention
Drawings/Figures Visual representations of the invention

For this study, the abstract section was selected as the primary text input for the LLMs. Abstracts
offer a standardized and condensed synthesis of each patent's purpose and technical scope,
facilitating efficient comparison with occupational descriptions. Moreover, using abstracts helps
mitigate noise from extremely detailed or inconsistent textual structures in other patent sections.
2.2. International Standard Classification of Occupations (ISCO-08)
The International Standard Classification of Occupations (ISCO-08) is a hierarchical framework
developed by the International Labour Organization (ILO) to classify and group jobs based on
their tasks and duties. It is a global reference for statistical and analytical purposes, facilitating
international comparisons and harmonizing occupational data. Regarding the hierarchy, ISCO-
08 is a system with four levels of aggregation: Major (10 categories), Sub-major (43 categories),
Minor (130 categories), and Unit (436 categories).
The dataset used contains the following information:
Table 2. Descriptions ISCO classification.
Section Description
Level Level of the hierarchy (1 to 4)
Code 4-digit code which uniquely identifies the occupation class
Title Title of the occupation
Definition Definition, which describes the activity in more detail
Tasks include Description of the activities included in the occupation class
Included occupations Examples of jobs included
Excluded occupations Examples of jobs not included to avoid class overlapping
Notes Other related information to help the occupation definition
161

Occupational Exposure to AI: A Patent-Based Approach Using Large Language Models

This study primarily uses the Minor group (Level 3) classification, as it strikes a balance
between granularity and interpretability. While higher-level categories (e.g., Major groups) may
be too broad to capture AI-related impacts, Unit groups (Level 4) can be overly specific, leading
to sparse data issues.
3. Methodology
This section outlines the methodological framework adopted to extract occupational information
from patent texts using LLMs. The process consists of three main phases: ( 3.1) patent data
collection, ( 3.2) preparation of occupational descriptions from ISCO -08, and ( 3.3) semantic
matching of patents to occupations via text embeddings. Each phase is described in detail below.
3.1. Patent Data Collection
Patent data were collected using Google Patents to analyz e the extent to which different
occupations are exposed to AI -related innovations. To this end, the following filters were
applied during the retrieval process.
● Keywords: "artificial intelligence", "neural network", "llm", "large language model",
"deep learning", "machine learning", "natural language processing"
● Country: European and American countries
● Time range: 2000-01-01 to 2024-10-30
● Status: grant, only granted patents
● Language: English, possibly translated with Google Translate provider
This query yielded 103,554 distinct patents . A data scraping process was initiated to extract
textual information on which to base the AI exposure analysis. Only the abstract section was
retained.
3.2. Structuring Occupational Descriptions
The ISCO-08 was employed to align patent texts with job profiles . Its taxonomy offers a
hierarchical structure of occupations consisting of four aggregation levels: Major, Sub -major,
Minor, and Unit groups. As explained before, we operated at the Minor group level (Level 3),
which includes 130 occupational categories. Each class was enriched by concatenating three
textual components : the title of the Minor group , t he definition provided at Level 3 and
definition of the corresponding Level 4 (Unit group) occupations, where available. This strategy
provided a rich and semantically dense representation of each occupational category, suitable
for downstream embedding tasks.

162

Occupational Exposure to AI: A Patent-Based Approach Using Large Language Models

3.3. Embedding Models and Similarity Matching
We used embedding-based models to compute semantic similarity between patent abstracts and
occupational descriptions, leveraging transformer architectures. The core model, BGE-M3
(Chen et al., 2024), is a multilingual embedding model optimized for dense retrieval and multi-
vector tasks. Built on XLM -RoBERTa (Conneau et al., 2019), it benefits from self -knowledge
distillation and optimized batching. Its ability to process up to 8,1 92 tokens makes it ideal for
compact abstracts and detailed occupation descrip tions. While other models (e.g., BERT
(Devlin et al., 2019) , XLM- RoBERTa) were tested, BGE -M3 showed superior performance
and was chosen for final analysis.
3.3.1 Patent-to-Occupation Mapping via Embedding Similarity Threshold
The final step assigns patents to occupations based on semantic similarity between patent
abstracts and ISCO -08 descriptions. Using the BGE -M3 embedding model, both texts are
converted into vectors, and pairwise dot product scores (0 to 1) semantic similarity scores are
calculated. To determine whether a given patent can be reliably associated with an occupation,
a similarity threshold must be defined: a minimum value above which the sema ntic match is
considered valid. A sample dataset was analyz ed to set t he threshold and the results were
manually reviewed. A similarity score of 0.55 was observed to provide a reasonable trade -off:
below this value, associations were often too vague or generic, while above this cut-off, matches
tended to be more meaningful and specific . Table 3 shows the distribution of patents by
similarity score and the average number of occupational classes per patent.
Table 3. (Partial) distribution of patents with the resulting pairwise patent-occupation similarity.
Similarity # of patents (= cutoff) # of patents (>= cutoff) avg # of classes per patent
0.49 330,369 1,137,945 11
0.50 248,813 807,576 8
0.51 175,254 558,763 5
0.52 131,014 383,509 4
0.53 86,151 252,495 2
0.54 61,054 166,344 2
0.55 38,999 105,290 1
0.56 26,104 66,291 1
0.56 + 40,187 40,187 0

Patent–occupation associations with a similarity score below 0.55 were discarded, ensuring only
clear work-related links remained. The valid associations formed the final dataset for analysis.
Each entry includes three key variables: patent publication year , occupation code and title
(from ISCO-08 Minor group classification), and the number of associated patents per year.
This structure creates a time series dataset, tracking AI -related innovations across occupations
and identifying trends in exposure.
163

Occupational Exposure to AI: A Patent-Based Approach Using Large Language Models

4. Results
The results are organized into two parts. First, we rank occupations most exposed to AI based
on the total number of patents associated with each ISCO category. This offers a static,
cumulative view of occupational relevance across the dataset. Second, we conduct a temporal
analysis, examining how patent activity related to AI evolves for the top -ranked occupational
groups. This dynamic perspective helps to identify trends and shifts in the impact of AI across
the labor market.
4.1. Ranking of Occupations Most Exposed to AI
Table 4 ranks Software and Applications Developers and Analysts first, with 8,675 patents,
highlighting softwar e engineering’s key role in AI. Next are Database and Network
Professionals (6,317) and Keyboard Operators (6,034), differing by ~5% but trailing the top
category by 37 –40%. Client Information Workers (5,045) and ICT Service Managers
(4,829) follow closely (~4% gap), though both fall ~20% below the third rank. Other notable
AI-exposed groups include Process Control Technicians, ICT Operations and User Support
Technicians, and even Creative and Performing Artists, reflecting generative AI’s impact on
the arts.
Table 4. Top 10 ranking of the most ISCO professions exposed to AI topics according to the
number of patents associated.
ISCO Title # of Patents % diff from upper pos.
SW and Applications Devs and Analysts 8,675 -
Database and Network Professionals 6,317 37%
Keyboard Operators 6,034 5%
Client Information Workers 5,045 20%
ICT Service Managers 4,829 4%
Process Control Technicians 3,580 35%
ICT Oper. and User Support Technicians 3,351 7%
Creative and Performing Artists 3,297 2%
Telecomm. and Broadcasting Technicians 3,210 3%
Engineering Professionals 3,109 3%
Total 47,447 -

This ranking highlights the concentration of AI exposure in ICT -related professions and hints
at AI's growing presence in non-traditional domains such as the arts and broadcasting.
4.2. Trends in Occupational Exposure to AI
Figure 1 shows the yearly distribution of AI -related patents across the 10 most exposed ISCO-
08 occupations, which account for 47,447 patents (45% of the total 105,290).
164

Occupational Exposure to AI: A Patent-Based Approach Using Large Language Models

Figure 1. Time series of the top 10 ISCO professions by number of patents on AI. Percentage data on an annual basis.
The trends reveal several key patterns: Software and Applications Developers and Analysts
lead AI-related patent activity, peaking at over 20% from 2020 –2022 before a slight decline.
Database and Network Professionals show steady growth, ranking second in AI exposure
since 2011. Keyboard Operators see growth (2002–2005, 2015–2016) before a sharp decline,
reflecting AI -driven automation replacing manual data entry. Client Information Workers
double their AI -related patents from 2003 to 2014, then gradually d ecline, suggesting AI
adoption peaked in customer service. ICT Service Managers experience fluctuations, with a
sharp AI -driven surge around 2023. Process Control Technicians steadily increase in AI
exposure, highlighting industrial automation integration. ICT Operations and User Support
Technicians fluctuate, peaking around 2010 due to AI’s role in IT support. Creative and
Performing Artists see rising AI -related patents, nearing 10% in 2012 and increasing again
recently, reflecting AI’s role in generative content creation. Telecommunications and
Broadcasting Technicians remain stable with modest AI involvement, likely due to automation
in media transmission. Engineering Professionals peak in AI patents around 2002 –2003
(>10%) before declining in 2023–2024, indicating early AI research later specialized in specific
fields. These trends illustrate AI’s dominance in software -related professions and its gradual
penetration into less conventional domains such as creative industries and process control. The
rise and decline of AI exposure in some occupations also highlights the dynamic nature of
technological adoption, where initial enthusiasm may be followed by stabilization or even
displacement due to automation.
5. Conclusion and Future Works
This study assessed occupational exposure to AI using LLMs, patent data, and ISCO -08
classifications. By analysing patents, w e identified professions most affected by AI -related
patents and tracked their evolution over time.
165

Occupational Exposure to AI: A Patent-Based Approach Using Large Language Models

Results show that ICT-related roles have the highest AI exposure due to their direct involvement
in AI development and deployment. Managerial and technical roles also show significant
exposure, reflecting AI’s growing role in automation and decision-making.
Future research will integrate labor market indicators like employment trends and wages to
better assess AI’s workforce impact. Additionally, refining similarity measurements and
exploring alternative embedding models will improve assessment accuracy.
References
Cazzaniga, M., Jaumotte, F., Li, L., Melina, G., Panton, A.J., Pizzinelli, C., Rockall, E.J., &
Tavares, M.M. (2024). Gen-AI: Artificial Intelligence and the Future of Work .
https://doi.org/10.5089/9798400262548.006
Chen, J., Xiao, S., Zhang, P., Luo, K., Lian, D. & Liu, Z. (2024). M3 -Embedding: Multi -
Linguality, Multi -Functionality, Multi -Granularity Text Embeddings Through Self -
Knowledge Distillation. https://arxiv.org/pdf/2402.03216
Comunale, M., & Manera, M. (2024). The Economic Impacts and the Regulation of AI .
International Monetary Fund, Working Paper WP/24/065
Conneau, A., Khandelwal, K., Goyal, N., Chaudhary, V., Wenzek, G., Guzmán, F., ... &
Stoyanov, V. (2019). Unsupervised cross -lingual representation learning at scale. arXiv
preprint arXiv:1911.02116
Dalla Zuanna, A., Dottori, D., Gentili, E., & Lattanzio, S. (2024). An Assessment of
Occupational Exposure to Artificial Intelligence in Italy. Banca d’Italia, Occasional Papers
No. 878.
Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019 ). Bert: Pre -training of deep
bidirectional transformers for language understanding. In Proceedings of the 2019
conference of the North American chapter of the association for computational linguistics:
human language technologies, volume 1 (long and short papers) (pp. 4171-4186).
OECD (2021). The Impact of Artificial Intelligence on the Labour Market. Organisation for
Economic Co-operation and Development.
Webb, M. (2020). The Impact of Artificial Intelligence on the Labor Market. Stanford
Univeristy
166
