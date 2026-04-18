# Big Data and Machine Learning at Istat

- Source file: `raw/chapters/2025-book-chapter-big-data-machine-learning.pdf`
- Document type: `chapter`

## Extracted Text

Big Data and Machine Learning at Istat
M. Bruno, A. Righi, G. Grippo, M. Di Zio, A. Pappagallo, L. Valentino, F. De
Fausti, G. Lancioni, F. Sisti, G. Massacci, F. Ortame, E. Catanese, M. De Cubellis,
E. Cerasti, F. Pugliese, D. Summa
Abstract Over the past decade, Istat has recognized the potential of Big Data and
Machine Learning (ML) in modernizing statistical production. This chapter outlines
Istat’s journey from early experimentation to new statistical production pipelines
based on Trusted Smart Statistics (TSS) principles.
We discuss integrating Big Data sources — such as satellite imagery, web data, and
sensor-based information — into official statistics and the challenges this paradigm
shift poses. The chapter describes several research projects, including maritime traf-
fic analysis using Automatic Identification System (AIS) data, urban green area
estimation through remote sensing, and web intelligence for business statistics. Spe-
cial attention is given to the methodological issues surrounding ML applications
in official statistics, particularly in relation to estimation, imputation, and quality
assessment.
We examine the evolving role of data science skills within Istat, the institutional
investments in human capital, and involvement in international research projects that
have supported innovation. By integrating ML and Big Data into statistical processes,
Istat aims to enhance data quality, improve timeliness, and provide more granular
insights while ensuring compliance with statistical principles and data governance
frameworks. The chapter concludes with considerations on future challenges and
opportunities for official statistics in the datafied society.
Name of First Author
Name, Address of Institute, e-mail: name@email.address
Name of Second Author
Name, Address of Institute e-mail: name@email.address
1

2 Bruno M., Ortame F., et al.
1 Introduction
The National Italian Institute of Statistics (Istat) has faced significant challenges
over the past decade in response to the changes brought by digital transformation,
the increasing amount of data available, and evolving European and international
landscapes. This paragraph outlines Istat’s journey, from initial experimentation
to establishing a dedicated production process for smart statistics. The resulting
products are derived from Big Data sources and use innovative methodologies. We
will describe the organizational solutions put in place, analyze their impact, and
outline the additional requirements necessary to support this transformation.
1.1 Background
When the EU Scheveningen Memorandum1 first formalized the need to look at Big
Data2 sources for official statistics in 2013, Istat gradually became aware of the new
opportunities and challenges offered by Big Data and began its active participation in
the European context with the new data sources (ESSNet Big Data I and II projects).
The increased use of Big Data requires a new approach to statistical production
processes that aligns with the agenda of Istat’s modernization project. This project
has been implemented since 2014 and involves the use of innovative sources, in
addition to traditional statistical information, to obtain more significant insights.
Research and innovation are the pillars of Istat’s Big Data and modernization
strategy3. The research was organized and strategic, with both thematic and method-
ological components recognized as growth elements for the Institute. Methodological
research activities are characterized by a constant drive to innovate methods and tools
to improve process efficiency and data production procedures, increase the quality of
the statistics produced, reduce the costs of statistical processes, and disseminate new
statistical data. Investments in thematic research have represented a tool for enriching
knowledge of the phenomena and, through analyses to deepen the understanding of
social and economic phenomena, have expanded the Institute’s information supply.
Integrating traditional and new sources, focusing on digital technologies and new
computational models, requires a paradigm shift in methodology from traditional
sample survey-based estimates to a model applicable to a multi-source environment.
To support this evolution, the Institute relied on experts gathered in two Big Data
Committees, the first set in 2013 and the second in 2016, which have played a key role
in assisting Istat in developing a roadmap for using Big Data in official statistics and
monitoring investments. Additionally, they have facilitated the sharing of knowledge
1 European Statistical System - ESS, Directors General of the National Statistical Institutes -
DGINS. 2013. Scheveningen Memorandum. Big Data and Official Statistics. Scheveningen – The
Hague, The Netherlands, 25th – 27th September 2013: DGINS Conference.
2 Set of data from different sources that is so large and complex that it requires new technologies,
such as artificial intelligence, to be processed
3 https://www.istat.it/it/files/2010/12/Programma modernizzazione Istat2016.pdf

Big Data and ML at Istat 3
and experiences, promoted and supported new partnerships, and enhanced the role
of research within the Institute.
Another organizational innovation conducive to developing research and inno-
vation in the realm of Big Data involved establishing a new research infrastructure
within the Institute. This infrastructure has been monitored by a governance body
(the Research Committee) since 2017 to ensure the quality and coordination of ac-
tivities. The Research Committee comprises two bodies with predominant roles in
guidance and scientific support: the Scientific Committee for Thematic Research
– the Advisory Committee for Statistical Methodologies (Advisory Board) – and
Thematic Laboratories and the Innovation Laboratory4.
During this period, Istat, a European pioneer in harnessing big data to produce
official statistics, initiated a strategic evaluation to implement the recommendations
provided. The objective is to move from the exploratory phase to a more systematic
and developed use of Big Data. The initial success of experimental statistics and the
outcomes of the ESSnet Big Data projects spurred Eurostat to take decisive action.
The opportunity arose in 2018 with the signing of the ”Bucharest Memorandum
on Official Statistics in a Datafied Society (Trusted Smart Statistics)” by heads of
statistical offices. Trusted Smart Statistics (TSS), mentioned for the first time in this
Memorandum, represent statistical products generated from smart systems crafted
with tools and methodologies adhering to the Code of Practice and Quality Assurance
Framework of official statistics, ensuring verifiability and transparency. National
statistical institutes uphold their validity and accuracy while fully respecting the
privacy of individuals and other stakeholders. The Bucharest Memorandum outlines
the strategic direction that national statistical institutes should take regarding the use
of Big Data sources and the production of smart statistics. It emphasizes the need
to implement mature use cases and develop experimental statistics 5 on emerging
phenomena. These statistics utilize new data sources and methods to respond more
effectively and promptly to users’ needs. Since these statistics have not yet reached
full maturity in terms of harmonization, coverage, or methodology, they are classified
as experimental. This highlights the need for increased awareness that leveraging
Big Data sources requires adjustments to statistical business architecture, processes,
production models, IT infrastructure, methodological and quality frameworks, and
corresponding governance structures.
The Blue Sky Thinking Network of the UNECE High-Level Group for the Mod-
ernisation of Official Statistics (HLGMOS) introduced a proposition in 2018 to en-
dorse adopting new techniques for TSS production. The paper suggests that exploring
opportunities offered by machine learning is essential for processing secondary data
sources (such as administrative sources, big data, and the Internet of Things), which
could also provide added value for primary data. Due to the significant responsibil-
ity of upholding the credibility of statistics based on the Fundamental Principles of
Official Statistics using Machine Learning (ML) in the National Statistical Offices
requires a more careful approach than in other business environment.
4 https://www.istat.it/en/about-istat/activities/research/organisation/
5 https://www.istat.it/en/announcement-and-analisys/experimental-statistics/

4 Bruno M., Ortame F., et al.
1.2 Towards a production system for Trusted Smart Statistics
Since 2018, Istat has embarked on a journey towards TSS, marking a significant mile-
stone as related projects were incorporated into the Istat strategic planning for the
first time. As part of this initiative, investments in human capital and recruiting new
data scientists were strategically programmed. Istat has fostered an extensive collab-
oration network with various statistical institutes, universities, and private partners.
During this phase, a preliminary set of projects has reached completion, spanning
exploration, prototype development, and dissemination activities. The outcomes of
these experiments have been successfully integrated into the production processes,
marking a pivotal step forward in advancing TSS at Istat.
Istat has established an integrated production system with its conventional data
acquisition and production infrastructure to facilitate smart statistics production.
This system incorporates the Integrated System of Registers, current surveys, and
externally manageable processing procedures using agreed methodologies, algo-
rithms, and reliable software. Implementing such a system involves a multi-tiered
data processing workflow organization and adopting standard manufacturing pro-
cess management models, such as the Generic Statistical Business Process Model
(GSBPM). This represents an ongoing, step-by-step process, currently under devel-
opment, which requires continuous efforts to refine and expand the system. Istat’s
effort to innovate methods has prompted the adoption of innovative organizational
solutions for developing TSS despite the lack of specific legal regulations at European
and national levels. To facilitate the integration of the TSS production system without
compromising existing production quality, an internal Director Steering Committee
supervises strategic analysis of the TSS system. Supported by a Scientific Technical
Secretariat, each organizational unit (communication, legal, data collection, IT, hu-
man resources) within the Institute actively contributes its expertise to develop the
new production system collectively. The Steering Committee identifies the demand
for statistical information, prioritizes implementing TSS projects, and supervises
experiments and investments.
The Center for the Production of TSS has been established to assist the Steering
Committee in the TSS Strategic Analysis process, strategic planning, and activ-
ity monitoring. The Center supports TSS experimentation, industrialization, and
production and is a cornerstone for the new TSS production system, promoting
sustainability and certified quality. The Center’s role is to provide an organiza-
tional structure for operational activities conducted across various organizational
structures. The Center is instrumental in refining experimental products, facilitating
communication, and ensuring compliance with regulations. Additionally, it plays a
crucial role in fostering collaborative partnerships with national and international
research institutions, conducting internal training initiatives, and spearheading en-
deavors.
The Center strengthened the Institute’s investments to integrate big data into pro-
duction processes. In fact, since February 2018, Istat started systematically integrat-
ing scanner data into Consumer Price Indexes, incorporating these data into the pro-
visional estimate of the Consumer Price Index. Furthermore, using OpenStreetMap

Big Data and ML at Istat 5
information has enhanced the investigation of road accidents. Additionally, progress
has been made in developing a Social Mood on Economy Index using data from
social media platforms. Special attention has also been given to the dissemination
of the results. Istat has developed dedicated sections on the institutional website
focusing on smart and experimental statistics related to non-traditional sources and
methodologies.
Adopting new data processing methods led to a renewal of the skills of the
staff producing statistics within the Institute. To extract value from big data, it was
necessary to strengthen the interdisciplinary nature of the techniques, in a way that
was greater than what had been necessary to apply the techniques used so far.
Therefore, ML and data science skills were recognized as a strategic priority. ML
presents significant potential for statistical organizations, improving efficiency by
automating processes or assisting human analysts. The Institute has systematically
integrated Machine Learning techniques into Istat’s production.
The Institute has made a notable organizational effort as exploiting Big Data
sources necessitates investments in finances, time, and, most importantly, competen-
cies. The ongoing transformation highlights the importance of acquiring new skills
and resources to enable staff to handle the novel statistical treatment of extensive
databases. Drawing from the experience of the Center for the Production of TSS and
from achieved results, Istat has recognized the need to allocate adequate resources
to these projects and acknowledges the current deficiencies within the Institute.
The agency is focusing on two areas of improvement in human resources: firstly,
developing the skills of current employees, and secondly, hiring new talents with
expertise in data science. The TSS Center has been working closely with the Human
Resources Department to gather information about the company’s current capabili-
ties in data science. This initiative aims to identify existing skills that can be utilized
in new projects and initiatives. The agency has also actively promoted training
programs to enhance employee skills.
Training initiatives have been actively promoted to enhance and redirect existing
resources towards innovative projects. Several internal courses focusing on Python
software usage and web scraping techniques have been conducted, alongside en-
couraging researchers’ participation in the European Statistical Training Programme
ESTP courses covering data science topics. The training activity plan includes ses-
sions addressing innovation and research topics, explicitly focusing on TSS to deepen
understanding of new data sources’ characteristics, potential, limitations, and the req-
uisite processes for TSS production. Training sessions on Machine Learning and the
Python language are also scheduled.
Efforts have been made to broaden researchers’ participation in ESSnet projects,
recognizing the significant benefits of exchanging views and experiences in statistical
production, especially concerning Big Data processes, analysis, and visualization
methods. Pilot projects developed during ESSnet Big Data I and II, ESSnet Smart
Survey initiatives, or in collaboration with universities in the Innovation Laboratory6,
have facilitated the testing of various approaches, thanks to the concerted efforts of
6 https://www.istat.it/listituto/attivita/ricerca/organizzazione/laboratorio-innovazione/

6 Bruno M., Ortame F., et al.
our researchers and fruitful collaborations with colleagues. The ”learning by doing”
approach has proven particularly effective in building capacity for utilizing Big
Data in official statistics. However, data scientists in official statistics need to blend
thematic domain expertise with profound knowledge of statistical/IT methodologies
and tools. This evolution from a T-shaped model to a Pi-shaped model, shown in
Fig. 1, with two distinct areas of expertise, is crucial. The Pi-shaped collaboration
model described in the literature (Ceri, 2018), which inspired Istat to invest in
new resources and improve internal skills, explicitly relies on collaboration between
individuals with different specialized expertise.
Fig. 1 Classic and modern
knowledge models
In recent years, Istat has begun recruiting data scientists 7 and involved them in
TSS projects. Additional data scientists have recently been hired to meet the growing
demand for these resources when developing new projects.
2 Istat’s experience on methodological issues of ML applied to
official statistics.
Istat has started studying the introduction of machine learning techniques in the statis-
tical production processes with the idea of reducing the need for human involvement
by automatically learning from and adapting to data, and because machine learning
may represent intricate, non-linear relationships between variables that could be
challenging to express and to discover with more conventional parametric models.
In addition, the context is favorable. Studies on machine learning are also increasing
with interest in non-traditional data sources, for instance, the use of remote sensing
data (Mugnoli et al., 2024), signals data such as the ones sent by automatic identi-
fication systems of the vessels, natural language processing as X (formerly Twitter)
data (Catanese et al., 2022).
A vast amount of literature on machine learning methods is available; neverthe-
less, their application in the NSI statistical production processes deserves further
studies and reflections because of the peculiarities characterizing official statistics.
7 People with a strong statistical profile who also have IT skills that enable them to operate on
infrastructures and with specific software for processing complex data sets.

Big Data and ML at Istat 7
An essential characteristic of machine learning (ML) methods is that they are mainly
developed for prediction purposes. In contrast, most of the NSIs’ production is con-
cerned with statistics that estimate finite population parameters such as, for instance,
the inflation rate, the total number of people in the country, and poverty indicators.
These are totals, means and percentiles, and more in general quantities related to a
set of statistical units, thus the interest is not on the single unit. The prediction of
values and estimation of aggregated parameters are undoubtedly related. However,
they still present some differences that should be considered when using machine
learning methods and in the uncertainty quantification of the parameter estimates.
An interesting discussion on prediction and estimation can be found in Efron (2020).
A more focused example of such a problem is in Larbi (2023), which studies ML
for the treatment of unit non-response in surveys. They observe that “the most pre-
dictive non-response model may not necessarily yield to the best estimator in terms
of mean square error”. NSIs generally refer to an estimator’s accuracy instead of a
prediction’s accuracy to evaluate the quality of official statistics.
Given the inherent prediction nature of ML, a natural field of application in NSIs
is the treatment of partial non-response through imputation, which is characterized
by a prediction of the missing values. We observe that, in this case, prediction is not
generally the goal of imputation. Indeed, imputation is generally used to estimate
some quantity of interest, such as population totals, obtained using observed and
predicted data. This is an important characteristic that should be considered when
choosing the ML method and how to use it for prediction. In this case, the procedure’s
evaluation should be driven by focusing, for instance, on the mean squared error of
estimates instead of the mean squared error of predictions. There are several studies
in this field; some early papers in the official statistics area can be found at the end
of the 1990s (Nordbotten, 1996; De Waal, 2001; Di Zio et al., 2004), and some
recent papers are Dagdoug et al. (2023), and De Fausti et al. (2022); Di Zio et al.
(2022). Some machine learning methods are tested in those papers with simulated
and real data. However, imputing missing values is essentially a tool for obtaining
a complete dataset that can be used to make inferences on population parameters
more easily. For this reason, making predictions through random imputation can
help preserve variability and avoid biased estimates of the probability distribution
and parameters such as quantiles (Mashreghi et al., 2014). Methods for random
imputation are provided for both quantitative and categorical variables. In the first
case, they are obtained by adding a residual term estimated from data (Dagdoug
et al., 2023); in the second setting, random imputation can be obtained by sampling
at random from the weighted prediction classes (De Fausti et al., 2022).
Another important element is that NSI data is generally gathered through sample
surveys. A problem that must be dealt with is the use of sampling weights and, more
in general, how to take into account the sampling design. For the sake of truth, this
issue must be addressed when models are used, whether they are ML models or not.
When the sampling design is not ignorable, the probability of observing a statistical
unit is related to the target variable we are interested in; it is essential to include infor-
mation on the sampling design in the model to avoid biased inferences. This can be
done by introducing the variables that determine the sampling design in the model;

8 Bruno M., Ortame F., et al.
for example, if stratified random sampling is performed, the stratification variables
should be included as covariates in the ML model. Another critical case frequently
adopted in the NSI’s survey is cluster sampling. This implies dependence on ob-
servations within one cluster, leading to violations of the identically distributed and
independent assumptions. If we do not consider this element in the ML applications,
biased or inefficient estimates can be derived (Kilian et al., 2023).
When it is impossible to take the sampling design into account directly, sampling
weights should be used. In statistical models, they may be introduced as auxiliary
variables (covariates) or by building weighted estimators. Di Zio et al. (2022) discuss
using sampling weights when applying multi-layer perceptron models (MLP) to real
survey data. They carried out a study that compared the results of the MLP procedure
with those of the official one. Sampling weights are used in two ways: 1) weights
are used to expand the sample that is then treated as the entire population; 2) the
loss function used in the training phase of MLP is weighted with sampling weights.
In this way, the MLP incurs different misclassification costs for different training
examples.
All these questions are nicely discussed in Little (2012, 2022) concerning Bayesian
modeling. However, many ideas can be directly interpreted in the ML framework.
A fundamental step of the statistical production process in an NSI is the quality
evaluation of the statistical outputs. Statistics are inevitably affected by uncertainty
due to sampling and non-sampling errors. Institutes should provide a measure to
quantify the uncertainty of numbers disseminated for the correct interpretation and
use by the stakeholders and to maintain confidence in the institute. In the traditional
production of statistics, the quality framework is well established. It refers explicitly
to measuring the accuracy of estimates such as, for instance, means or totals of the
population, measures as mean squared error taking into account (usually) sampling
and non-sampling errors.
As noted, machine learning methods are more developed with the aim of predic-
tion, and thus, available accuracy measures reflect this scope; in fact, they are focused
on prediction accuracy. Further studies are needed to move quality evaluations to-
ward inference (Larbi, 2023). Some answers might directly come from resampling
techniques, e.g., bootstrapping, but further investigation needs to be done to see their
applicability in official statistics contexts. They may be computationally prohibitive
or need special accommodations in the case of the presence of finite populations,
see Chen and Haziza (2019) for a thorough discussion about the latter problem.
Also, cross-validation, which is aimed to assess how well a trained model will
generalize to an independent dataset, should be revised to take into account the non-
exchangeability of the units, which is generally introduced when a complex sampling
design is used (Wieczorek et al., 2022). Another technique used in uncertainty quan-
tification in machine learning is conformal prediction (Vovk et al., 2005). It is used
to provide a way to quantify the uncertainty of individual predictions made by a
model. Unlike traditional machine learning models that typically output a single pre-
diction, conformal prediction gives a prediction set that guarantees a certain level of
confidence or significance. Again, further studies should be conducted on conformal

Big Data and ML at Istat 9
prediction to deal with the uncertainty evaluation of a population parameter and with
complex sampling design (Wieczorek, 2023; Hornung et al., 2023).
3 Research Projects
In recent years, Istat has invested significant efforts in research projects to integrate
new data sources and advanced methodologies, such as machine learning and big
data analytics, into producing official statistics. These projects align with a broader
strategic vision to modernize statistical processes, improve data quality, and enhance
the efficiency and timeliness of statistical outputs. Below, we present some of the
key research projects carried out by Istat in this domain.
• Automatic Identification System (AIS) for Maritime Transport
This project integrates AIS data with existing administrative sources to improve
maritime traffic statistics. The goal is to enhance the accuracy and timeliness
of key indicators, such as vessel arrivals in Italian ports, by reconstructing ship
voyages using geospatial and machine-learning techniques.
• Satellite Images for Urban Green Areas Measurement
This project uses high-resolution satellite imagery to quantify urban green spaces
through vegetation indices like NDVI. The methodology combines remote sens-
ing data with clustering and classification techniques to support environmental
monitoring and urban planning.
• Web Intelligence for Enterprise Data Analysis
Istat has developed automated methods to extract information from enterprise
websites using web scraping and machine learning. Applications include iden-
tifying official URLs, detecting e-commerce activities, and analyzing online job
postings to enrich business statistics.
• Analysis of Trade Data with Network Analysis Techniques
The TERRA project uses network analysis techniques to study external trade
flows and detect key economic patterns. This project identifies central actors
in trade networks by analyzing external trade data (Eurostat COMEXT open-
data), assesses market dependencies, and provides insights into macroeconomic
dynamics. The approach enables the development of experimental indicators that
enhance understanding global supply chains and trade shocks.
• Sentiment Analysis for Economic and Social Insights
This project applies sentiment analysis techniques to various textual data sources,
such as social media, to extract public opinion trends on economic and so-
cial issues. Natural language processing and machine learning models classify
sentiment polarity and detect emerging themes, providing valuable insights for
policymakers and researchers.

10 Bruno M., Ortame F., et al.
3.1 Automatic Identification System (AIS)
Istat’s TRAMAR (MARitime TRAnsport) survey 8 provides statistics on the ship
transport of goods and passengers carried out for commercial purposes in Italian
ports. The survey has a census character and refers to ships with a gross tonnage
of at least 100 tons moving for commercial reasons. The statistical production of
TRAMAR comes through integrating survey data with an administrative source,
namely PMIS (Port Management Information System). PMIS is the digital registry
of the Italian General Command of Harbormaster’s offices.
Integrating data from various sources is necessary to ensure high-quality statistical
outputs. However, relying on a single source does not guarantee complete coverage
of the analyzed phenomenon. For example, the PMIS system only includes the most
important ports for commercial and passenger traffic (i.e., a list of 38 ports), while
the TRAMAR survey covers all ports of interest. Furthermore, due to the extreme
complexity and volubility of ship movements, there is no a priori list of the events
(the landings and embarkations) or the units (the ships) being surveyed.
The project aims to provide an alternative source for improving the quality of
maritime traffic statistics. The Automatic Identification System (AIS)9 is a tracking
system used on ships for safety and management purposes. It provides the GPS
location of all vessels sailing the world’s seas regularly and frequently. Storing this
data in a Big Data archive can theoretically allow the reconstruction of a ship’s
voyage history.
Including the AIS source in the TRAMAR production process can improve the
quality and the timeliness of important statistical outputs, for example, the table
of Vessels arriving in the main ports by type and size of vessels for Eurostat 10.
This table contains the number of arrivals by ports and is often referred to as F2
table. Still, it does not include data on goods quantity or passenger numbers, which
are only collected through the TRAMAR questionnaire. The PMIS source, released
monthly through machine-to-machine communication, is available earlier than the
TRAMAR survey. However, the F2 table cannot be generated solely from the PMIS
data as it does not cover all ports. The AIS source, which is potentially available in
near real-time, could be integrated with the PMIS data to produce an F2 table that is
timely and comprehensive.
The use of AIS data to support official statistics has already been investigated
in several works and projects. In de Wit et al. (2020), the Port Visits Geo-Solution
prototype monitors the ships’ movement inside the Piraeus Central Port, defined by
a polygon, to compute the number of arrivals and departures. In the United Nations
Global Platform (UNGP) Handbook11, several case studies on the use of AIS are
described, such as the experimental statistics of the daily number of vessels visiting
8 https://www.istat.it/informazioni-sulla-rilevazione/trasporto-marittimo/
9 https://www.imo.org/en/OurWork/Safety/Pages/AIS.aspx
10 https://ec.europa.eu/eurostat/web/transport/information-data/maritime-transport
11 https://unstats.un.org/wiki/display/AIS/Case+studies

Big Data and ML at Istat 11
Danish ports using AIS data published from Statistics Denmark12. In the Port Visits
Using Real-Time Shipping Data statistic13 from the Irish Central Statistics Office
(CSO), two methodologies for generating port visits are compared. The first uses
polygons to identify ships inside a port area, as in de Wit et al. (2020). The study
of these researches has been the basis of this work even though none of these aims
at our same goal, that is, the reconstruction of the entire voyages of ships from the
departure port to the arrival port.
3.1.1 Methodology
This section describes the methodology adopted to process AIS data. This process
aims to obtain the entire list of voyages of vessels arriving in or departing from
Italian ports. The vessels of interest are all passenger or commercial vessels, which
we will refer to as vessels with a gross tonnage of more than 100 tons.
Data source
The AIS data used in this study were supplied by the Task Team on AIS Data of
the UN Committee of Experts on Big Data and Data Science for Official Statistics
(UN-CEBD)14. This data is accessible through the UN Global Platform (UNGP)15,
a global repository of live and historical AIS data. The UN-AIS dataset contains
regular observations of all kinds of ships, with a gross tonnage greater than 300
tons, from December 1, 2018. On average, the interval between two observations
of the same ship is 10 minutes. The available attributes in each AIS observation
(Fig. 2) include three categories of information: static (MMSI code, IMO code, ship
name, and type), dynamic (ship’s position coordinates, navigational status, speed,
and course), and voyage-related (destination and draft).
Fig. 2 AIS observation attributes.
The UN-AIS dataset also provides vessel position through the H3 (Hexagonal hierar-
chical geospatial indexing system)16 index at multiple resolutions. H3 is a geospatial
12 https://www.statistikbanken.dk/aisdag
13 https://www.cso.ie/en/statistics/transport/portvisitsusingreal-timeshippingdata
14 https://unstats.un.org/bigdata/task-teams/ais/index.cshtml
15 https://unstats.un.org/bigdata/un-global-platform.cshtml
16 https://h3geo.org/

12 Bruno M., Ortame F., et al.
indexing system developed by Uber Technologies that approximates the GPS coor-
dinates using a hexagonal tessellation of the earth’s surface (Fig. 3). The H3 index
identifies the hexagon containing ship coordinates, with hexagon size depending on
the adopted resolution.
Fig. 3 On the left, the hexagonal tessellation of the earth’s surface by H3 – Uber. On the right, the
H3 index of the hexagon containing a GPS coordinate, i.e. (latitude, longitude)
In addition to the AIS dataset, we used a dataset of world ports taken from Merrien
(2021), containing each port’s geographical coordinates (latitude, longitude).
Data processing pipeline
To achieve the objectives of this work, we need to identify and quantify ships visiting
Italian ports. The desired output is a dataset of ships voyages, as shown in Fig. 4.
The three entities defining a voyage are the ship, the departure (port and data), and
Fig. 4 Dataset produced: the list of vessel trips
the arrival (port and data). In the following, we will refer to all generic vessel visits
in a port as port calls.
Fig. 5 shows the pipeline used to process AIS data. The workflow comprises three
primary logical steps, as illustrated in Fig. 5, along with their corresponding inputs
and outputs. The first step is the vessel selection, which requires access to the AIS
database, the list of Italian ports (including port area), and Lloyd’s ship register 17,
which provides information such as each vessel’s type and gross tonnage. The list
of vessels returned in the output is used to select AIS data for processing in the
subsequent steps. As mentioned, we are only interested in voyages where at least
17 https://www.lr.org/

Big Data and ML at Istat 13
Fig. 5 Pipeline for processing AIS data
one of the ports of departure and arrival must be in Italy. To ensure a comprehensive
analysis, we must consider the port of departure if the ship arrives in Italy, even if it is
foreign. Similarly, we must consider the port of arrival if the ship departs from Italy,
even if it is foreign. Therefore, we cannot limit our analysis to AIS records located
only in Italian waters. However, if the ship does not visit an Italian port during the
specified period, it can be excluded from our analysis. Thus, according to AIS data,
the output list of vessels visiting Italian ports will include all ships, except fishing
and yacht types, that have visited an Italian port and are present in the ship register
with a gross tonnage of more than 100 tons.
The second step is the voyages calculation. An algorithm, described in the fol-
lowing paragraph, computes all trips made by vessels during the specified period.
This process requires the AIS database and lists of Italian and non-Italian ports.
In the third and final step, the ports imputation and missing data in the voyages list
(the unknown ports) are imputed using the ’Port imputation algorithm’. The nature
of how this data is generated will be clarified in the paragraph’ Voyages calculation
algorithm’.
The processing pipeline produces two final outputs: the voyages list, which follows
the format presented in Fig. 4, and the statistics for the F2 table, which displays the
number of voyages grouped by arrival port.
Voyages calculation method
A departure and arrival are two consecutive port calls of the same vessel. For
example, the voyage shown in Fig. 6 is defined by the departure port (ITBRI) at time
T1 and the arrival port (ITRAN) at time T5. Note that the other AIS observations
between T2, T3, and T4 are not required to define the trip. A port call in AIS data is
a record where the speed is 0, and the position falls inside a port area. As previously
stated, we are only interested in ships that have visited an Italian port at least once

14 Bruno M., Ortame F., et al.
and have a gross tonnage exceeding 100 tonnes. Thus, we only need to select these
records to process a ship. Finally, we obtain all the ships’ voyages by ordering the
port calls in time.
The first problem to be addressed is the identification of port areas. For this
purpose, we built each port’s area as a set of hexagons of resolution eight, identified
by H3 indexes (see Fig. 3). First, for each port, we selected the hexagon containing
its geographical coordinates and the first ring of hexagons surrounding the main
hexagon, and we added them to the set representing its area. As a second step, we
collected AIS data for six months in a reference year (e.g., 2022). We filtered the data
by specific ship types, namely cargo, tanker, and passenger, which were stationary
in the port areas (i.e., in the main hexagons containing the geographical coordinates
of the ports). Finally, we added the H3 hexagons of resolution eight containing the
stationary ship positions to the port area (Fig. 7). Visualizing a visit to a port is made
easier by defining each port area as a set of hexagons.
Fig. 6 Example of the voyage
between the ports ITBRI
(Bari) and ITRAN (Ravenna)
in the AIS dataset
Fig. 7 H3 hexagons identifying a port area.

Big Data and ML at Istat 15
Furthermore, two other critical issues, namely incorrect records and missing data,
affect the AIS data. A record is erroneous if one or more variables assume a wrong
value, creating a false port call within the vessel’s timeline. For example, in Fig. 8
(on the left), the AIS observation 𝑇3 is erroneous as, even if the vessel appears with
speed 0, it generates a false port call inITRAN. In this case, we find two trips for the
vessel, ITGOA-ITRAN and ITRAN-ITNAP, instead of ITGOA-ITNAP. Missing data
refers to a period with no AIS observations for a vessel. In Fig. 8 (on the right), the
observations are regular until time 𝑇2. After no data for several hours, the vessel
reappears in the position in the figure at time 𝑇4. If, between 𝑇2 and 𝑇4, the vessel
enters ITOLB, we lose both the two voyages ITGOA-ITOLB and ITOLB-ITGOA.
To face these problems, it is necessary to use also the AIS observations of vessel
Fig. 8 Example of incorrect record (on the left) and lack of data (on the right)
movements that we initially thought were not useful (records 𝑇2, 𝑇3, and 𝑇4 in the
example of Fig. 8). Each record is compared with its predecessor in the timeline by
measuring the difference in the time value (Δ𝑇), the difference in the distance of the
coordinate values (Δ𝑃), and the resulting speed:
𝑟𝑒𝑠𝑢𝑙𝑡𝑖𝑛𝑔 𝑠 𝑝𝑒𝑒𝑑 = Δ𝑃
Δ𝑇
(1)
Finally, the algorithm will calculate the correct trips: ITGOA-ITOLB and ITOLB-
ITGOA. To perform this step, we chose the following thresholds:
Δ𝑇 > 60min, Δ𝑃 > 0, 𝑟𝑒𝑠𝑢𝑙𝑡𝑖𝑛𝑔 𝑠 𝑝𝑒𝑒𝑑 < 15km/h. (2)
Port imputation method: heuristics and deep learning
The voyage dataset generated by the voyages calculation algorithm may contain some
records where the departure or arrival ports are not specified. This occurs in the case

16 Bruno M., Ortame F., et al.
of a lost port call due to AIS missing data or ambiguous value of the destination
field. In this case, the missing value must be imputed. To do this, we use the last three
months’ voyages. To determine the port of arrival, we use the most frequent arrival
port in the vessel’s history, given the port of departure. Similarly, to determine the
port of departure, we use the most frequent departure port, given the port of arrival.
We limit this rule to ’scheduled’ routes to prevent making uncertain imputations.
This is only the first step. We are working on sequence classification models
to classify arrival ports from AIS trajectories. Preliminary results for this analysis
are presented in Pappagallo et al. (2024). We are now working on assessing the
performance of deep learning models on real-world unlabeled ship trajectories,
often characterized by noise and/or missing data points. At this moment, the best-
performing model is an LSTM network, with an accuracy of 0.82 and a macro
F1-score of 0.56 on the real-world test set18 over 93 prediction classes. The key idea
is to train the network using the dataset of complete voyages (i.e., voyages without
missing AIS data) and use it to predict unspecified arrival ports. The model uses
a dataset consisting of vessel routes (latitude, longitude, speed over ground, course
over ground) as input, and arrival ports as output.
This is a typical case of a supervised learning approach. The model is trained
using labeled voyages where both departure and arrival ports are known and applied
to predict cases where the arrival port is unknown. Fig. 9 gives an example of how
Fig. 9 Example of records used by the ’Port Classifier’ neural network. On the left, the labeled
voyages are used to train the model. On the right, the voyage with the missing arrival port to predict.
The model must use the incomplete route to distinguish the correct arrival port ITOLB
the model has to work, showing on the left the voyages used for training. The vessels
18 The test set mimics the characteristic of unlabeled problematic routes, i.e., incomplete trajectories
and missing observations near ports.

Big Data and ML at Istat 17
departing from the port of ITGOA (Genova) might arrive at ITCVV (Civitavecchia),
sailing on the blue route, or arrive at ITOLB (Olbia), sailing on the yellow route. On
the right is a voyage with a missing port of arrival. In this case, the model should
recognize the pattern and predict ITOLB as the correct port of arrival.
3.1.2 Results
In previous sections, we presented and discussed the first results of the AIS data
processing pipeline. In particular, we compared the number of arrivals produced by
the proposed procedure with the official statistics for Eurostat (F2 Table). As a first
experiment, we calculated the voyages for the fourth quarter of 2021. We could use
the 2021 F2 table as a benchmark. The resulting dataset contained 86,545 voyages.
18,088 of them had a missing port (in 9,042, the arrival port was missing; in 9,046,
the port of departure was missing), 3,274 of their records were imputed with the
current imputation algorithm, and 14,814 remained unknown. The total number of
arrivals in Italian ports calculated from AIS during the period was 57,659 instead of
the 85,075 arrivals reported in the F2 Table. In practice, the procedure detected only
68% of the arrivals, and the remaining 32% were lost, but this varied among ports.
First of all, a few observations:
1. F2 table includes all vessels with a gross tonnage of more than 100 tonnes, but
only vessels with a gross tonnage of more than 300 tonnes are required to have
an AIS tracking system onboard. Therefore, some vessels in F2 may not be in the
AIS dataset.
2. For this first run, we did not have accurate historical records of AIS voyages, and
we used only the historical records of PMIS, which does not include all Italian
ports. Also, imputation is not always possible for routes monitored by PMIS.
3. In case of missing data for an extended period, several port calls may be lost,
but the algorithm will have only one prediction. This problem is particularly
noticeable for shorter routes.
The Italian F2 Table consists of 56 ports. We compared the statistics for each port
and obtained very different results. We calculated two types of indicators from AIS
voyages: the number of arrivals at ports where the port of departure is known (column
AIS from) and the number of all arrivals at ports (column AIS to) including cases
where the port of departure is unknown.
Tables 1 – 4 provide a detailed comparison of ports divided into five classes:
1. Ports where the number of arrivals in F2 falls within the range of ’ AIS from’ and
’ AIS to’. This includes 14 major ports, such as Ancona, Bari, and Gioia Tauro.
2. Ports with over-coverage. This list contains only four ports. Milazzo and Eolie
Islands ports have greater over-coverage and define a route not monitored by
PMIS, where under-coverage of F2 is possible.
3. Ports with small under-coverage. List of 8 ports with under coverage limited to
10%. This includes several big ports like Civitavecchia, Livorno, Napoli, Palermo,
and Trieste.

18 Bruno M., Ortame F., et al.
4. Ports with medium under-coverage: list of 17 ports with varying degrees of
coverage. Some ports are in short routes like Elba and Piombino, Messina and
Reggio Calabria, and Procida. Unfortunately, two important ports, Genova (-25%)
and Ravenna (-37%), are also in this class.
5. Ports with large under-coverage: this group contains only small ports or ports
located in short routes.
Future work planned for this project includes implementing port imputation by
machine learning methods. The first experiments achieved accuracies exceeding
80%. A more sensitive algorithm will also be developed to process only short tracks.
These changes are expected to significantly reduce the current under-coverage of
trips, making AIS a reliable source for generating improved statistics on maritime
traffic.
Table 1 Result of the comparison between the F2 Table and the statistics regarding voyages
produced from AIS data. Ports where F2 is in the range.
UNLO code Port name AIS from AIS to F2
ITAOI Ancona 401 562 426
ITAUG Augusta 239 525 523
ITBRI Bari 434 503 494
ITCHI Chioggia 57 105 81
ITFAL Falconara Marittima 42 63 43
ITGIT Gioia Tauro 335 520 509
ITMDC Marina di Carrara 120 137 133
ITMNF Monfalcone 86 122 108
ITOTN Ortona 43 85 70
ITPFX Porto Foxi (Sarroch) 137 297 205
ITPNG Porto Nogaro 46 77 76
ITRRO Sorrento 972 1094 1032
ITSIR Siracusa 69 140 109
ITVCE Venezia 434 757 630
3.2 Satellite images to quantify urban green areas
Measuring urban green cover is crucial for analyzing and developing various indi-
cators related to different aspects of city life (Jabbar et al., 2022). For instance, the
’quality of life’ often refers directly to citizens’ ability to access public and private
green spaces (such as parks, gardens, historic estates, and sports facilities). Further-
more, environmental quality depends on the presence and health of vegetation cover
in each area.
The proposed statistical analysis could be a fundamental tool for further explo-
ration of the dynamics governing large cities. Numerous studies have utilized remote
sensing for vegetation analysis, focusing on how chlorophyll absorbs light radiation

Big Data and ML at Istat 19
Table 2 Result of the comparison between the F2 Table and the statistics regarding voyages
produced from AIS data. Ports with overcoverageor small undercoverage.
UNLO code Port name AIS from AIS to F2 Difference
IT004 Eolie Islands 1147 1292 679 68,9%
ITMLZ Milazzo 1155 1297 827 39,7%
ITPRJ Capri 2154 2182 2072 4,0%
ITSPE La Spezia 245 290 217 12,9%
IT001 Ischia Island 3334 3408 3686 -7,5%
ITCVV Civitavecchia 505 550 588 -6,5%
ITLIV Livorno 1210 1319 1428 -7,6%
ITNAP Napoli 6434 6563 7215 -9,0%
ITPMO Palermo 857 911 1000 -8,9%
ITPZL Pozzallo 183 219 241 -9,1%
ITSVN Savona 327 391 430 -9,1%
ITTRS Trieste 422 478 535 -10,7%
Table 3 Result of the comparison between the F2 Table and the statistics regarding voyages
produced from AIS data. Ports with medium undercoverge.
UNLO code Port name AIS from AIS to F2 Difference
IT002 Elba Island 1763 1767 2489 -29,0%
ITBDS Brindisi 226 273 321 -15,0%
ITCAG Cagliari 372 404 488 -17,2%
ITCTA Catania 276 294 368 -20,1%
ITGAE Gaeta 36 60 96 -37,5%
ITGAI Golfo Aranci 79 81 95 -14,7%
ITGOA Genova 911 995 1332 -25,3%
ITMSN Messina 9264 9296 13449 -30,9%
ITOLB Olbia 387 387 479 -19,2%
ITPIO Piombino 1768 1932 2231 -13,4%
ITPRO Procida 3032 3035 4338 -30,0%
ITRAN Ravenna 212 538 853 -36,9%
ITREG Reggio Calabria 9025 9035 13263 -31,9%
ITSAL Salerno 440 504 588 -14,3%
ITTAR Taranto 110 205 265 -22,6%
at different wavelengths. The literature presents various indicators for vegetation
classification (Xue and Su, 2017; Pristeri et al., 2021). Following several experi-
ments, we opted to use the NDVI (Normalized Difference Vegetation Index), which
relies on the behavior of chlorophyll a and b. Its standard formula is:
𝑁 𝐷𝑉 𝐼 = (𝑁 𝐼 𝑅− 𝑅𝐸 𝐷)
(𝑁 𝐼 𝑅+ 𝑅𝐸 𝐷) (3)
where 𝑅𝐸 𝐷 is the red wavelength used for absorption, and𝑁 𝐼 𝑅is the Near Infra-Red
for reflection.
We employ high-resolution remote sensing images (AGEA Orthophotos with
20 and 50 cm pixel resolution), which span the entire Italian territory over three

20 Bruno M., Ortame F., et al.
Table 4 Result of the comparison between the F2 Table and the statistics regarding voyages
produced from AIS data. Ports with large undercoverge.
UNLO code Port name AIS from AIS to F2 Difference
IT003 Egadi Islands 952 954 3391 -71,9%
IT88P Off-shore platforms 0 2 167 -98,8%
ITCLF Carloforte 1139 1188 2638 -55,0%
ITCLS Calasetta 650 652 1353 -51,8%
ITFCO Fiumicino 0 0 15 -100,0%
ITGEA Gela 4 4 45 -91,1%
ITIDG Isola del Giglio 1 17 509 -96,7%
ITMDA La Maddalena 14 41 3402 -98,8%
ITPAU Palau 19 38 3607 -98,9%
ITPNZ Ponza 137 154 495 -68,9%
ITPSS Porto Santo Stefano 2 4 512 -99,2%
ITPTO Porto Torres 175 184 324 -43,2%
ITPVE Portoscuso (Porto Vesme) 528 554 1329 -58,3%
ITQOS Oristano 18 52 96 -45,8%
ITTPS Trapani 1023 1122 3180 -64,7%
years. Starting in 2012, these images have been provided to ISTAT in four spectral
bands. From this data, we produce continuous NDVI images (in float format) that
require reclassification to identify pixels corresponding to vegetation specifically.
This process involves a detailed analysis of the NDVI image histogram to determine
a threshold value above which pixels are likely to represent ’green’ areas. Fig. 10
and Fig. 11 demonstrate the clustering of vegetation index pixels within the image
histogram.
Fig. 10 True colors image
of a portion of an urban area
of Rome (Castel Giubileo,
Villa Spada, Serpentara, Colle
Salario)

Big Data and ML at Istat 21
Fig. 11 Part of the histogram of the image shown in Fig. 10, related to the ‘green pixels’
3.2.1 Methodology
Typically, we expect four NDVI classes corresponding to distinct landscape features:
water, built-up areas, bare soil, and vegetated areas, with a standard threshold value
of approximately 0.2 (Aryal et al., 2022) used to discern green vegetation. The NDVI
threshold of 0.2 cannot always be used as a reference for any orthophoto since the his-
tograms show considerable shifts in the vegetation cluster even on orthophotos taken
of the same area in different years. Although there are strong theoretical arguments
for expecting these four distinct regions in the NDVI distribution, these are rarely
observed in actual data. Sometimes, one of the classes overshadows the one next to
it, and in some extreme cases, we observe distributions that exhibit only two max-
ima or even just one. Consequently, we explore various techniques to determine the
threshold automatically. The overall methodological approach is structured into three
primary stages, as shown in Fig. 12: data input and pre-processing, morphological
analysis of the histogram, and evaluation of the outcomes.
At first, a pre-processing data step is performed:
• Ortho-images, in ecw format, are converted into GeoTiff format;
• images are cropped as per the shape file to select the urban areas correctly;
• NDVI is evaluated; note that the input images are multi-band, while the output is
single-band;
• multiple images are combined to form a mosaic: a single image of the full city.
Then, three groups of methods are studied. One is based on Kernel density
estimation (KDE), the second is based on clustering algorithms, and the third is
referred to as a refined version of green detection.
A common feature of NDVI histograms is that they are usually quite noisy
(fluctuating), with frequencies often obscuring the meaningful maxima and minima;
this makes it difficult to discern clear patterns. We address this using the first method:
Kernel Density Estimation (KDE), which estimates the distribution value for each
point as the one-weighted sum of the contributions of a centered Gaussian kernel.
KDE acts as a smoothing mechanism for our data. The smoothed curve represents

22 Bruno M., Ortame F., et al.
Fig. 12 Data processing pipeline
the frequency distribution function of our data, as seen in Fig. 13; it is crucial
in our analysis since it makes it possible to estimate local maxima and minima.
The local maxima, highlighted by KDE, serve a dual purpose: they indicate the
likely number of clusters and provide the starting positions for the centroids in
subsequent clustering algorithms. Both parameters are crucial for correctly applying
the subsequent clustering algorithms.
This approach lets us identify a first-order estimate of the green areas: the threshold
is the minimum rightmost in the distribution. This estimate requires no additional
parameter, i.e., the number of expected clusters.
Fig. 13 Kernel Density Esti-
mation KDE (orange curve)
vs. histogram. Maxima (green
dots) and minima (red dots)
are shown.
In the second approach, we used the K-Means and K-Medians clustering algo-
rithms. The number of clusters is obtained by the number of local maxima identified
by KDE; these values are also set as the algorithms’ initial centroids. The urban
green threshold is then given by the lower limit of the rightmost cluster, i.e., the
cluster related to the centroid with the highest NDVI value, see Fig. 14. We also
explored the K-medians clustering approach. K-means is efficient for segmenting

Big Data and ML at Istat 23
one-dimensional data but can be sensitive to outliers. K-medians effectively address
this issue.
Fig. 14 Clusters centroids
(black lines) and clusters
lower limits (red lines) found
by K-Means.
Incorporating K-medians into our methodology allowed us to validate and enhance
the clustering results obtained from K-means. This complementary approach added
a layer of robustness to our analysis, improving the overall accuracy and reliability
of our conclusions about vegetation distribution in urban environments.
The third approach refines the thresholds evaluated via the clustering methods.
We focus mainly on two challenging aspects commonly encountered in this field.
First, we encountered the challenge of varying green nuances across different im-
ages. One significant factor contributing to this variation is seasonal effects, which
can alter the type of green detected in each image. For instance, the lush vegetation
in spring presents a different shade of green compared to those of a later period
(Eastman et al., 2013). We adopt the approach of Donchyts et al. (2016). This was
initially applied in water-index detection and offers valuable insights for our context.
We customized the methodology for vegetation analysis.
The method consists of the following complete pipeline:
• The KDE threshold is set as a preliminary threshold for green pixels in the
image. Pixels below the KDE threshold are masked, while those above are kept
unchanged. This masking enables the following steps to focus on green areas.
• Canny Edge Detection algorithm is applied on the masked image. It segments the
input image based on the variation of the NDVI values. This generates segments
along the KDE threshold since there is a steep variation between green and non-
green areas, and in all green regions above the KDE threshold, faint-green pixels
can be separated by strong-green pixels.
• A buffering technique is applied around the detected edges. This step narrows
the focus to the immediate areas surrounding the vegetation, providing a more
targeted region for analysis. A buffered image is used as a mask on the original
image to resample pixels in the regions of high index variation. This reduces noise
from the irrelevant areas.
• Otsu clustering is applied to the resampled histogram to determine an optimal
threshold for binary separation. It works on single-tone images (such as the NDVI

24 Bruno M., Ortame F., et al.
Table 5 Results of the different approaches for determining the urban green threshold. Ortho-
images for Ravenna and satellite (Advanced pipeline S2)
Approach Threshold Green pixels Green area (Ha)
KDE 0.06 182,322,979 729,29
K-Means 0.11 165,830,738 663,32
K-Medians 0.08 174,698,659 698,79
Advanced pipeline 0.17 139,599,919 558,40
images) and splits the values into two classes with a threshold. It efficiently
distinguishes non-green from green areas.
3.2.2 Results
We applied the methods to Ravenna, a municipality in Northern Italy. Table 5 shows
the estimated threshold, the number of green pixels, and the green area in terms of
hectares and percentage of covered territory. There is a general agreement on the
first three approaches: KDE, K-Means, and K-Medians. KDE and K-Medians are
closer, while K-Means is slightly different due to the algorithm’s less robustness to
the outliers.
The advanced pipeline remarks a different trend. In this case, there is a strong
segmentation inside the green area, meaning a great variety of vegetal structures with
highly varying NDVI, and the Otsu clustering determines a shift in the threshold to
discard areas of less intense green vegetation. See Fig. 15.
Fig. 15 Ortho-image of Ravenna (left), identification of Green Areas shown in Black for K-Medians
(center), and Advanced pipeline (right)
The research findings suggest that orthophotos are highly effective in extracting
and quantifying green spaces within urban areas. Additionally, machine learning
techniques present a promising approach to overcoming challenges, such as ac-
curately determining threshold levels in an automated and objective manner. The
positive and promising results indicate that future efforts will be focused on refining
methodologies, expanding the study area, enhancing the precision of urban green

Big Data and ML at Istat 25
space quantification, and categorizing these spaces into established land cover types.
The success of a project like this depends on methodological and thematic exper-
tise, and the authors of this paper are specialists in both fields who conducted this
research.
3.3 Web Intelligence: automated analyses of enterprises’ websites (WI)
Among the vast category of Big Data, the Internet can be considered a data source
that may be used in substitution (with the aim of reducing respondent burden) or
in combination with data collected using traditional statistical survey instruments to
increase the accuracy of estimates.
One of the approaches for Big Data-based data collection on the Internet is Web
scraping, which is a process that permits the extraction of information from websites.
There are two different kinds of Web scraping: specific Web scraping and generic
Web scraping.
Specific Web scraping refers to the case when both the structure and content of
websites to be scraped are almost perfectly known in advance. Generic Web scrap-
ing, instead, assumes that no a priori knowledge on the content is available; in this
case, the whole website has to be scraped and subsequently processed in order to
infer information of interest.
Starting in 2013, Istat began exploring the potential of web scraping techniques
within both national (M. Scannapieco, 2017; Barcaroli et al., 2015a,b, 2016) and
European (G. Stateva, 2018; H. K¨ uhnemann, 2022) contexts, integrated during the
estimation phase with text and data mining algorithms, with the goal of replacing tra-
ditional data collection methods to reduce respondent burden, enhancing estimation
processes, or combining these approaches within an integrated framework. Some
notable use cases that have been covered are:
• Use case 1: Solve the “URL retrieval problem” of identifying the official enterprise
website starting from the enterprise’s name and administrative information.
• Use case 2: Establish whether an enterprise does e-commerce.
• Use case 3: Establish if an enterprise exposes job vacancies on its website.
This experience represented a truly extensive application of generic web scrap-
ing, characterized by: (i) the need to scrape data from several thousand websites,
highlighting its massive scale, and (ii) the lack of prior knowledge or reproducibility
of the websites’ structures, reflecting their inherent heterogeneity and the generic
nature of the approach.

26 Bruno M., Ortame F., et al.
3.3.1 Use case 1 – URL retrieval
Since the main input of a Web scraper is an initial list of URLs to scrape, it is
necessary to have them available before starting the scraping phase of the job.
Unfortunately, this was not the case for most enterprises belonging to the datasets
of interest. Hence, in this use case, the task was to obtain the official URL of their
websites, if available. An automated procedure has been implemented to obtain an
enterprise website (if it exists) starting from a search of the enterprise name in a
search engine. The procedure involves several steps with a mix of techniques, ranging
from scraping and crawling techniques to machine learning ones. The results show
the feasibility of addressing this problem with an automated solution that gets good
results both in terms of quality and efficiency.
More in detail as for Istat, it was used as a case study in the ”Survey on ICT
usage and e-Commerce in Enterprises” (shortly ICT survey), whose population of
interest is composed of enterprises with at least 10 employees and operating in
different branches of industry and services (the population size is around 200,000).
By the ICT survey estimates, it is known that about 70% of these enterprises own a
website for different purposes. Unfortunately, only a subset of the enterprises’ URLs
is available (derived from the ICT survey answers integrated with administrative
data).
Therefore, the objective is to determine the official website for the remaining
enterprises. In this regard, the basic idea is to search a search engine for the name
of each enterprise, collect and submit the search results to web scraping, and apply
ML algorithms to the scraped web content in order to make the prediction. The first
choice to make is to identify the search engine to rely on.
Search engine selection
When you think about search engines, Google is probably the first thing that comes
to mind because it dominates the market by a long margin. But there are also several
alternatives that it is possible to consider, especially if you are more interested in
privacy-related features. However, in this specific use case, the most important feature
is the ability to identify the URL of a searched enterprise’s website (by providing
the enterprise name).
To establish which search engine has the best “enterprise URL finding” per-
formance, NSIs have tested the four search engines (Google, Bing, Yahoo, Duck-
DuckGo) already used in previous projects. A random sample of 99 Italian enterprises
with the corresponding URLs has been downloaded from the publicly available web-
site https://www.downloadaziende.it, and the name of each enterprise was used as a
search parameter in each search engine.
Table 6 illustrates the number of correct domains identified at each link position
in the search engine results page (SERP) by each search engine. Based on this test
(acknowledging that its robustness could be improved by including a larger sample of

Big Data and ML at Istat 27
Table 6 Number of correct domains caught by link position.
Google Bing Yahoo DuckDuckGo
no domain match 25 35 36 42
domain matched by link 1 61 55 50 41
domain matched by link 2 6 5 6 7
domain matched by link 3 2 0 2 2
domain matched by link 4 1 1 0 3
domain matched by link 5 0 1 2 2
domain matched by link 6 0 1 0 0
domain matched by link 7 1 1 1 0
domain matched by link 8 1 0 1 0
domain matched by link 9 2 0 1 1
domain matched by link 10 0 0 0 1
tot cases 99 99 99 99
tot matched domains 74 64 63 57
% of matched domains 74.75 64.65 63.64 57.58
enterprises) Google emerged as the most effective option and was therefore chosen
as the search engine for the use case.
It is possible to query Google in 2 alternative ways: (i) by using their API or
(ii) by scraping the SERP. In order to establish the best way to adopt in terms of
“enterprise URL finding” performance, the enterprise sample was also searched by
using the Google API, and the results were compared to the results obtained by using
the SERP scraping strategy. The output contained in table 7 shows that the SERP
strategy leads to better results and was therefore adopted.
Table 7 Comparison between SERP and API strategies.
GoogleSERP Google API
no domain match 25 33
domain matched by link 1 61 52
domain matched by link 2 6 7
domain matched by link 3 2 4
domain matched by link 4 1 2
domain matched by link 5 0 0
domain matched by link 6 0 0
domain matched by link 7 1 1
domain matched by link 8 1 0
domain matched by link 9 2 0
domain matched by link 10 0 0
tot cases 99 99
tot matched domains 74 66
% of matched domains 74.75 66.67

28 Bruno M., Ortame F., et al.
Technological solution
The technological solution implemented for use case 1 is shown in Fig. 16. The
starting input is a file containing each considered enterprise’s ID code and name;
each software program uses the output of the preceding program as input in a pipeline
fashion. The developed software pipeline is mainly made by the following custom
software programs:
• GURLSearcher19 is a custom Python application that takes as input a list of
enterprises names and identification codes and, for each of them, performs a
query on the Google search engine. The output is a text file containing the first
10 URLs the search engine returns for each enterprise. This program was used
in order to collect a list of web links for a given enterprise name. The underlying
assumption is that, if an enterprise has an official website, this should be found
within the first 10 results provided by Google.
• RootJuice220 is a custom Python application based on the Scrapy project 21 that
takes as input a list of URLs and, on the basis of some configurable parameters,
retrieves the textual content of that website plus the textual content of binary files
contained in websites and loads it into a platform named Solr (see next).
• Apache Solr 22 is a NoSQL database. It parses, indexes, stores, and allows for
searching of scraped content. Providing distributed search and index replication,
Solr is highly scalable and, for this reason, suitable to be used in Big Data context.
• UrlScorer23 is a custom Java program that reads one by one all the documents
related to a specific enterprise contained in a specified Solr collection and calcu-
lates for each one the value of binary indicators, for instance: the URL contains
the enterprise denomination (Yes/No); the scraped website contains geographical
information coincident with enterprise information already available in the Reg-
ister (Yes/No); the scraped website contains the same fiscal code in the Register
(Yes/No); the scraped website contains the same telephone number in the Register
(Yes/No); etc.
• UrlMatchTableGenerator224 is a custom Python application that is responsible to
create the training dataset for the machine learning algorithms used in the analysis
phase of the work.
• Custom Python scripts are used in the analysis phase, which turns to be the last
phase of the process.
19 https://github.com/SummaIstat/GUrlSearcher
20 https://github.com/SummaIstat/RootJuice2
21 https://scrapy.org
22 http://lucene.apache.org/solr/
23 https://github.com/SummaIstat/UrlScorer
24 https://github.com/SummaIstat/UrlMatchTableGenerator2

Big Data and ML at Istat 29
Fig. 16 URLs retrieval software pipeline
Analysis
Once the programs mentioned above retrieved a list of possible URLs associated
with each enterprise name, a machine-learning task was set up. Survey data and
administrative data were integrated as ground truth to predict the correct association
of a URL from the list with an enterprise’s name.
The available dataset was split into three parts: Training (70% of observations),
Validation (20% of observations), and Test (10% of observations). Several super-
vised machine learning algorithms were trained on the training set and the related
performances have been evaluated and compared on the validation set by using the
metrics normally adopted in classification tasks (see Table 8). Based on the calcu-
Table 8 UrlRetrieval performance metrics for different models
Model Accuracy Precision Recall F1 Score AUC
Decision Tree 0.864292 0.773571 0.791667 0.782514 0.844171
Logistic Regr. 0.862038 0.771552 0.785088 0.778261 0.840719
Gradient Boosting 0.866546 0.767956 0.812865 0.789773 0.851674
SVM 0.866997 0.767538 0.815789 0.790928 0.852810
Neural Network 0.867899 0.764189 0.826754 0.794242 0.856500
Random Forest 0.864743 0.759109 0.822368 0.789474 0.853003
Naive Bayes 0.859558 0.756720 0.802632 0.779000 0.843786
K Neighbors 0.813345 0.728426 0.629386 0.675294 0.762379

30 Bruno M., Ortame F., et al.
lated metrics, the Neural Network model was chosen as the champion model because
it simultaneously presents the best accuracy, the best recall, the best f1 score, and
the best AUC. After this initial model comparison, the Neural Network model was
tuned in order to maximize its predictive capabilities, and the best cut-off value for
the ROC curve was computed. As the last step, the tuned model was applied to the
test set. In Table 9, there are the obtained metrics on the three datasets for the tuned
model, while Fig. 17 represents the ROC curves. The Neural network-tuned model
was then used to make predictions.
Performing some manual checks on a small random sample of misclassified cases
in which the target variable was 0 (the URL is not correct) and the predicted value
was 1 (the URL is correct), it emerged that in many cases, the model correctly
identifies the real website although this is different from what should be confirmed
as the company provided it.
This can happen for several reasons, including: (i) the company provided an
incorrect web address (typos); (ii) the company provided a web address that is no
longer valid (replaced by the one found by the SW); (iii) the company has several valid
domains (e.g. “rossi.it” and “rossi.com”) and provided just one of the two while the
software pipeline found the other; (iv) redirect phenomena (e.g. the provided domain
“rossi.it” redirects to “rossi.com” found by the SW).
On the other hand, most of the cases in which the target is 1 and the prediction
is 0 can be explained by the fact that the enterprise incorrectly provided an official
website: (i) a URL that points to a web directory website such as yellow pages; (ii)
the URL of a third-party website that sells the products of the reference enterprise;
(iii) the URL of the mother company in case of franchising enterprises; (iv) a social
network webpage.
In all of these cases, the procedure correctly states 0 (not the official website), but
they are formally considered errors because the value of the prediction (even if it is
actually correct) differs from the value of the target variable supposed to be true.
Table 9 Neural Network tuned model performance.
Dataset Accuracy Precision Recall Specificity F1 Score AUC
Training 0.8743 0.7801 0.8432 0.8888 0.8104 0.8660
Validation 0.8684 0.7652 0.8268 0.8869 0.7948 0.8568
Test 0.8698 0.7671 0.8388 0.8839 0.8014 0.8614
3.3.2 Use cases 2 and 3 – E-commerce and Online job advertisements (OJA)
The objective is to determine whether each enterprise’s website has e-commerce
features (use case 2) and job advertisements (use case 3). Once the complete or
nearly complete list of URLs is available (combining the a priori known URLs
and those obtained through use case 1), it is used as input for the scraper software

Big Data and ML at Istat 31
Fig. 17 ROC curve for the Neural Network tuned model.
program. The scraped content is indexed and loaded into Solr, which will be available
for any use case that relies on it to produce outputs. For use cases 2 and 3, the next
step is executing the program responsible for creating the TDM (Term document
matrix), which represents the analysis’s starting point.
Technological solution
The technological solution implemented for use cases 2 and 3 is shown in Figure
18. The starting input is the URL list; as in use case 1, each software program uses
the output of the preceding program as input in a pipeline fashion. The developed
software pipeline is mainly made by the following custom software programs:
• RootJuice2 (see Use case 1)
• Apache Solr (see Use case 1)
• FirmsDocTermMatrixGenerator25 is a custom Java program that reads all the
documents contained in a specified Solr collection, extracts and stems all the
words from them and generates a matrix having one word for each column and
one entity (enterprise in this case) for each row; the integer values contained in
the cells represent the number of occurrences of each word in each enterprise
website.
• Custom Python scripts are used in the analysis phase.
25 https://github.com/SummaIstat/FirmsDocTermMatrixGenerator

32 Bruno M., Ortame F., et al.
Fig. 18 Web Scraping pipeline
Analyses
Even though use case 2 (establish whether an enterprise does e-commerce or not)
and use case 3 (establish whether an enterprise exposes job vacancies on its website)
have quite different objectives the adopted strategy to determine the target value is
the same. In both cases, the starting labeled datasets were unbalanced (see Table
10 and Table 13), hence as a first step, it was necessary to balance them by using
the random oversampling strategy. The resulting dataset was split into three parts:
Training (70% of observations), Validation (20% of observations), and Test (10% of
observations).
In order to obtain the best possible predictive performance, three different strate-
gies have been applied to the dataset. First, it was used almost as it was; the values
contained in the term-document matrix produced by the FirmsDocTermMatrixGen-
erator software (numbers representing word occurrences) have been converted to
boolean values (presence/absence). The algorithms trained and evaluated on this
dataset have been reported in Table 11 and Table 14 with the “NOSEL” suffix.
Afterwards the dataset was reduced by selecting the words with the highest
predictive power for each of the two classes by means of a chi-square test. The
algorithms trained and evaluated on this dataset have been reported in Table 11 and
Table 14 without any additional suffix.
Finally, the TF-IDF strategy was tested and justified by the fact that occurrence
count is a good starting point but contains an issue: longer documents will have higher
average count values than shorter documents; to avoid these potential discrepancies,

Big Data and ML at Istat 33
it suffices to divide the number of occurrences of each word in a document by the
total number of words in the document: these new features are called tf for Term
Frequencies. Another refinement on top of tf is to downscale weights for words that
occur in many documents in the corpus and are, therefore, less informative than those
that occur only in a smaller portion of the corpus. This downscaling is called tf-idf
for “Term Frequency times Inverse Document Frequency”. The algorithms trained
and evaluated on this dataset have been reported in Table 11 and Table 14 with the
“TFIDF” suffix.
For both use cases, on the basis of the metrics and the roc curves (see Figure
19 and Figure 20), the champion model was chosen. In both cases, the choice was
pretty straightforward because the Random Forest algorithm applied to the “tf-idf
dataset” obtained the best performance in all the metrics.
As in use case 1, the champion models have been tuned in order to maximize their
predictive capabilities and the best cut-off value for the ROC curve was computed.
The tuned models were then applied to the test set (see Table 12 and Table 15) and
used to make predictions.
For both use cases some manual checks on a small random sample of misclassified
cases have been performed.
In particular, for the use case 2 (e-commerce), the focus was on the cases in which
the target variable was 0 (no e-commerce), and the predicted value was 1. It emerged
that in many cases, the model correctly identifies the “real truth,” although this is
different from what should be true as the company declared it. This can happen for
several reasons, including: (i) the company provided an incorrect answer by mistake;
(ii) the company provided an answer that was changed during the time; (iii) the
company voluntarily provided the wrong answer in order to avoid the subsequent
series of related questions since the e-commerce question is a filter question in the
questionnaire.
For use case 3 (online job advertisements), it emerged that when the target variable
was 0 (no OJAs), and the predicted value was 1, the incorrect prediction is often
caused by the presence of a “work with us” section of the website that does not
contain job advertisements for specific positions but only invites to send resumes
claiming that they are always looking for candidates. On the contrary, when the
target variable was one, and the predicted value was 0, in many cases, the model
correctly identifies the “real truth,” although this is different from what should be
true as the company declared it. This can happen for several reasons, including: (i)
the company provided an incorrect answer by mistake; (ii) the company provided
an answer that was changed during the time; (iii) the company provided the wrong
answer because it did not understand correctly the question asking for the presence
of job advertisements limited to their website (hence not including third-party job
posting websites).

34 Bruno M., Ortame F., et al.
Table 10 Proportion of websites with and without E-commerce facilities
Yes No
e-commerce (declared) 19.24% 80.76%
Table 11 E-commerce performance metrics for different models
Model Accuracy Precision Recall F1-score AUC
Random Forest TFIDF 0.947964 0.956869 0.941331 0.949036 0.948165
Random Forest NOSEL 0.946886 0.954835 0.941331 0.948035 0.947054
Random Forest 0.926395 0.947974 0.906757 0.926908 0.926990
Neural Network 0.909679 0.920856 0.902043 0.911352 0.909910
Neural Network NOSEL 0.908061 0.888119 0.939759 0.913209 0.907102
Logistic NOSEL 0.869507 0.837198 0.926663 0.879662 0.867776
SVM 0.822324 0.890625 0.746464 0.812197 0.824621
K Neighbors 0.818280 0.817808 0.832373 0.825026 0.817853
K Neighbors NOSEL 0.813966 0.804902 0.842850 0.823439 0.813091
Gradient Boosting TFIDF 0.771637 0.835651 0.692509 0.757376 0.774032
Gradient Boosting 0.721758 0.784925 0.632792 0.700696 0.724452
Logistic 0.701806 0.759871 0.614982 0.679792 0.704435
Decision Tree NOSEL 0.678889 0.724656 0.606600 0.660393 0.681078
Decision Tree 0.678889 0.752107 0.561027 0.642664 0.682458
Naive Bayes 0.669992 0.732835 0.564694 0.637870 0.673180
Naive Bayes TFIDF 0.661364 0.718395 0.562598 0.631022 0.664355
Naive Bayes NOSEL 0.661364 0.718395 0.562598 0.631022 0.664355
Table 12 Tuned Random Forest model performance on E-commerce use case
Dataset Accuracy Precision Recall Specificity F1 Score AUC
Training 0.978425 0.990587 0.965630 0.990990 0.977950 0.978310
Validation 0.951469 0.975261 0.929282 0.975000 0.951717 0.952141
Test set 0.948248 0.975000 0.920601 0.976165 0.947020 0.948383
Table 13 Proportion of websites with and without OJA
Yes No
Online job advertisement (declared) 28.17% 71.83%
3.4 Input privacy
As stated in previous sections of this chapter, the NSIs actively participated in
research projects to harness the potential of new data sources for producing offi-
cial statistics. They began their research journey many years ago and have recently
focused on transferring the knowledge acquired from research projects into the sta-
tistical production processes. NSIs have embarked on a path affecting technological,
methodological, organizational, and legislative aspects (Ricciato et al., 2019). They

Big Data and ML at Istat 35
Fig. 19 E-commerce ROC curves comparison
Table 14 OJA performance metrics for different models
Model Accuracy Precision Recall F1-score AUC
Random Forest TFIDF 0.880570 0.872289 0.888344 0.880243 0.880661
Random Forest NOSEL 0.868445 0.853846 0.885276 0.869277 0.868642
Random Forest 0.863292 0.848198 0.880982 0.864279 0.863499
Neural Network 0.858442 0.854789 0.859509 0.857143 0.858454
Neural Network NOSEL 0.840557 0.797735 0.907362 0.849024 0.841338
Logistic NOSEL 0.832980 0.809879 0.865031 0.836547 0.833354
SVM 0.807517 0.824104 0.776074 0.799368 0.807150
Gradient Boosting TFIDF 0.793271 0.804236 0.768712 0.786073 0.792984
K Neighbors 0.777508 0.806430 0.723313 0.762613 0.776875
K Neighbors NOSEL 0.766293 0.804826 0.695706 0.746298 0.765468
Gradient Boosting 0.766293 0.787291 0.722086 0.753280 0.765776
Logistic 0.751440 0.782033 0.688957 0.732551 0.750710
Decision Tree 0.731737 0.781557 0.634356 0.700305 0.730599
Decision Tree NOSEL 0.722037 0.800337 0.582822 0.674476 0.720410
Naive Bayes 0.665353 0.719167 0.529448 0.609894 0.663765
Naive Bayes NOSEL 0.654441 0.704849 0.517178 0.596603 0.652837
Naive Bayes TFIDF 0.654138 0.704261 0.517178 0.596392 0.652537
aim to enable a new official statistics production system that can integrate tradi-

36 Bruno M., Ortame F., et al.
Fig. 20 OJA ROC curves comparison
Dataset Accuracy Precision Recall Specificity F1 Score AUC
Training 0.979728 0.999462 0.960234 0.999477 0.979456 0.979855
Validation 0.895423 0.918567 0.865031 0.925105 0.890995 0.895068
Test 0.900000 0.925730 0.864932 0.933571 0.894298 0.899251
Table 15 Tuned Random Forest model performance on OJA use case
tional data sources with new ones, adhering to the principles of official statistics and
maintaining the quality levels of statistical products that NSIs have always upheld.
In the traditional paradigm of statistical production, NSIs addressed privacy
concerns during the dissemination phase of statistical results. However, integrating
new Big Data sources, when acquired from public or private entities external to
the NSIs, requires implementing privacy-preserving techniques in the input phase.
Thus, significant privacy preservation considerations are introduced during the data
collection and processing phases.
Private entities external to NSIs often collect and hold data autonomously. In-
stitutions have also initiated several collaborations aimed at sharing data for the
mutual goal of producing joint statistics. In both scenarios, whether accessing exter-
nal data held by private entities or engaging in data-sharing collaborations among
multiple entities, the sensitivity of the processed data often necessitates ensuring
their confidentiality. To address the challenges of privacy protection and data confi-

Big Data and ML at Istat 37
dentiality, researchers started to investigate new techniques, known asInput Privacy
techniques, that have recently emerged from the intersection of multiple disciplines
such as cryptography, computer science, and distributed processing. At the heart of
these techniques is the basic concept of transforming data to fulfill confidentiality
requirements. The data transformation must ensure at least two conditions: (i) the
transformed data cannot be restored to the original data; (ii) the transformed data
must allow the calculation of the correct output. How the processing phase trans-
forms the original data distinguishes one technique from another. In the following
paragraphs, we will illustrate some of the main input privacy techniques. The advent
of big data and the availability of huge amounts of open data have also required
increased privacy protection on the traditional output front. Traditional output pri-
vacy techniques, such as statistical disclosure controls, need enhancement to address
the growing risk of privacy breaches. In this context, a new term has emerged: pri-
vacy enhancing technologies (PET), which encompasses techniques for preserving
privacy on both the input and output sides (as sketched in Fig. 21).
Fig. 21 Privacy Enhancing Technologies: Input Privacy techniques (left), Output Privacy tech-
niques (right)
Federated Learning
Recent advancements in Input Privacy include distributed training methods such
as Federated Learning (Stock et al., 2023). This technique allows training Machine
Learning models on datasets held by multiple entities (clients) without sharing
them, enhancing data confidentiality. Clients share a neural network model while a
central authority oversees the training process and guides the model training without
accessing sensitive data directly. At the end of each training round, the central
authority applies a strategy to aggregate the model parameters received from clients.
Federated learning protocol can be combined with Homomorphic Encryption to
increase the security level. In official statistics, Federated Learning can be applied
in experimental statistics and developing trusted smart statistics, such as those that
need to exploit smartphone data input.

38 Bruno M., Ortame F., et al.
Secure Multi-Party Computation
Secure Multi-Party Computation (SMPC) is a cryptographic technique that enables
a group of parties to compute the functions on their private data collaboratively
(UN, 2023). It is a technique falling in the field of input privacy, and it is mainly
thought to prevent collisions among a subset of involved parties aimed at controlling
results. SMPC protocols are suited to balance privacy and utility needs but display
disadvantages, like the high communication cost between parties. To minimize risks
and simplify communication, data can be stored in various private domains, and an
SMPC technique is used to perform a calculation using them all for the benefit of
all parties involved. Overall, SMPC provides superior privacy protection compared
to data obfuscation methods. It only reveals the final result, enhancing data privacy
and security in collaborative computations. SMPC finds applications in secure data
sharing, privacy-preserving analytics, and confidential computation.
Private Set Intersection (PSI) (De Cristofaro and Tsudik, 2010) is a particular case
of SMPC and an important cryptographic tool. PSI has received much attention from
the crypto community since it represents a building block for many more complex
functionalities. PSI is applied in cases where two parties (public or private) are
interested in linking their respective datasets while disclosing information relative
only to the data included in the dataset intersection to the other party. In the PSI
framework, we assume a scenario where both parties are honest but curious, meaning
that they respect the protocol but still try to learn information about the other party’s
dataset.
There are several possible implementations of PSI (Kamara et al., 2014), namely:
• three-party solution: a reliable third party is introduced in the process, and it is
responsible for carrying out the linkage between the datasets of the two parties;
• two-party solution for supposed dishonest parties: more complex than the previous
one;
• solution with data transfer: it is similar to the three-party solution with the dif-
ference that the third party sends some microdata to one of the two parties. This
solution requires perfect linkage.
Various scenarios have been defined to support the linkage of sensitive information
in a manner that preserves privacy. They differ in the performed join, the shared
information, and the type of analysis to perform. The PSI is applicable in numerous
instances within official statistics, as in the case of the integration of external data
sources with those gathered directly by NSIs.
Homomorfic encryption
Homomorphic encryption (HE) is a specific type of cryptography that allows calcu-
lations to be performed directly on encrypted data without the need to perform the
decryption step. The HE concept was first introduced in 1978, and it remained largely
theoretical until 2009, when Craig Gentry presented the first Fully Homomorphic

Big Data and ML at Istat 39
Encryption scheme. Gentry’s work, based on lattice cryptography, revolutionized
the field and triggered a surge in research aimed at optimizing HE for practical
applications.
HE scheme operates through the following phases:
• Encryption phase: data is encrypted using complex algorithms, often involving
vectors and matrices, especially in lattice-based systems.
• Computation phase: encrypted data undergoes arithmetic operations, e.g., addi-
tion and multiplication.
• Decryption phase: the calculated encrypted result is converted back into the
original value. This phase must effectively counteract the noise introduced during
the computation phase to ensure accurate decryption.
The applications of HE vary from cloud computing to statistical analysis, where
private data are computed without exposing individual information. Homomorphic
encryption also promotes secure data sharing and collaborative practices, allowing
collaborative processing of the data where the privacy of a single-party dataset
is preserved. Homomorphic encryption represents a revolutionary innovation in
cryptographic technology, offering a pathway for secure and privacy-respecting
data processing. Although current implementations face significant computational
complexity, efficiency, and scalability challenges, the field is rapidly evolving, and
ongoing research is progressing toward more practical, high-performance, and robust
systems.
Differential privacy
Differential privacy aims to ensure that the output of a system or algorithm cannot
be used to infer information about single individuals. This is assured if the response
to a query or the release of a computational result is substantially the same in both
cases when a particular individual is included in the dataset. There are various tech-
niques for implementing differential privacy, and one of the most common involves
introducing statistically controlled noise into the dataset or in the algorithm output.
The noise insertion makes it challenging to infer whether a particular individual is
included in the dataset, and the difficulty varies according to the amount of noise. The
adversary’s inability to determine the presence of a record in the database is mea-
sured in terms of similarity between the probability distributions on outputs when the
record is present or missing in the database. This similarity measure is numerically
parameterized, with smaller values of these parameters representing stronger privacy
protection. Although these values have an exact statistical interpretation, there is no
general, application-independent recipe to set appropriate values. This represents
one of the current limitations to the usability of this technique. Differential privacy
works well when a single query is sent to a database, or the output of a computation
is evaluated. Still, it can break down when the issuer repeatedly asks several queries
to the database. The privacy protection effect due to the noise diminishes as the
number of observed samples increases. Hence, the noise level required to adhere

40 Bruno M., Ortame F., et al.
to a differential privacy level of security is higher in the case of multiple queries.
A technical component in the protocol, called ”privacy accountant”, keeps track of
previously sent queries and calculates the information gained from the combination
of query results. However, increasing the amount of the inserted noise also results in
the reduction of output data usability. Noise degrades the quality and utility of the
output data. In cases where a large amount of noise is needed for privacy require-
ments, the possibility of extracting useful information from the data is jeopardized.
Therefore, the Differential Privacy technique relies on the fundamental trade-off be-
tween privacy preservation and output utility. When the data output is too distorted,
it can become difficult or impossible for researchers, analysts, or machine learning
algorithms to extract meaningful insights or make accurate predictions based on that
data (Drechsler and Bailie, 2024).
Differential privacy was formally introduced in Dwork (2006). Since then, it has
been the subject of extensive research, along with developing several protocols for its
implementation. These include high-level mechanisms like SQL engines intercepting
SQL queries and adding appropriate noise to return differential privacy-compliant
output (Johnson et al., 2018). Other protocols focus on training machine learning
models in a differential privacy mode (Ruan et al., 2023).
Synthetic data
Generating synthetic datasets for statistical purposes allows the production of datasets
containing different information than real data but with the same statistical character-
istics. The utility of using synthetic rather than real data is to protect against privacy
attacks. The advantage of synthetic data is that, depending on the user’s purpose, it
offers a trade-off between the analytical value of the dataset and the risk of disclo-
sure. Every NSI seeks to use and share data securely. Synthetic data are increasingly
considered an alternative to the privacy-preserving exchange of sensitive data. There
are various levels of synthetic data, each with a different trade-off between analytical
value and disclosure risk. Depending on this trade-off and the intended use of the
dataset, synthetic data can be used for the following applications (UNECE et al.,
2023):
• To release synthetic microdata to the public: traditional output disclosure mea-
sures used by NSOs can limit users’ access to high-quality microdata. NSOs are
exploring generating synthetic data as a new output disclosure option.
• To test analysis: some NSOs provide limited access to microdata to trusted entities,
either through remote access or at physical Research Data Centers. However, se-
curity checks, audits, and approvals can slow down research and analysis projects.
Synthetic data could enable researchers to develop and test their models, algo-
rithms, or analyses and conduct preliminary data analyses as they wait to access
the original real data.
• Education: high-quality data is needed for students, academics, and users to learn
new concepts and methods; by providing data for education purposes, an NSO may

Big Data and ML at Istat 41
preserve only the distributions related to the studied dimensions and synthetically
generate the others.
• Testing technologies: dummy data are often used when testing new software. The
file layout and error rates represent real data, but there is no analytical value.
However, as machine learning becomes prevalent, the testing will require more
analytically realistic data. In these cases, synthetic data with some inferential
validity can be beneficial
There are many methods for generating synthetic data, such as sequential mod-
eling, statistical obfuscation, and innovative deep learning methods, such as general
adversarial networks.
3.4.1 Results
From a technical perspective, privacy enhancing technologies are in a mature devel-
opment phase and are ready for use within NSIs. However, their application in the
official statistics has not yet been realized due to a series of challenging issues that
remain unsolved. Among those issues are legal concerns: every process using sen-
sitive information must comply with the GDPR. Also, outside the European Union,
there are other privacy regulations and legislation, and a standard is lacking. From
an organizational perspective, the application of PETs has impacts both in terms of
the costs required for their implementation and in terms of integration of PETs into
current production processes. Furthermore, the adoption of PET requires researchers
and analysts to change their working procedures. A crucial aspect regarding the trust
model to adopt is the centralized versus distributed trust model and trust models
with or without the presence of a neutral third party. It’s essential to assess each
use case individually to determine the most appropriate trust model. Finally, another
critical issue concerns choosing between custom and general-purpose solutions. To
address the above-mentioned open issue, the UN Statistical Division currently pro-
motes experimental projects on PETs involving several National Statistical Institutes,
Istat included. The main case studies developed are collected in the UN case study
repository26.
3.5 Analyzing trade data with network analysis techniques: the
experimental statistics TERRA
Istat found a valuable resource in the COMEXT data source provided by Euro-
stat, which contains information on international trade in goods. COMEXT cov-
ers the value and quantity of goods traded between EU Member States (intra-EU
trade) and between EU Member States and non-EU countries (extra-EU trade).
Trade data is disseminated monthly and at the most detailed level of the following
26 https://unstats.un.org/wiki/display/UGTTOPPT/Case+study+repository

42 Bruno M., Ortame F., et al.
product nomenclatures: the Combined Nomenclature (CN)27, the Standard Interna-
tional Trade Classification (SITC)28, the Broad Economic Categories classification
(BEC)29, the Classification of Products by Activity (CPA)30, and the Standard Goods
Classification for Transport Statistics/Revised (NSTR)31. In addition, trade flows are
classified by mode of transport, providing helpful information for transportation
policy, monitoring international transport routes, and evaluating the impact of trade
on the environment.
As international trade represents a major part of the world economy, statistics
on trade in goods are an instrument of primary importance for numerous users,
including public and private sector decision-makers. For example, statistics regarding
international trade in goods are valuable to:
• inform on recent and long-term developments in trade and economy;
• help EU businesses conduct market research and define their commercial strategy;
• enable EU authorities to prepare multilateral and bilateral negotiations under the
common commercial policy;
• provides an essential source of information for other statistical domains, such as
Balance of Payment statistics or national accounts.
International trade provides a rich data source for users to explore different as-
pects of global commerce. However, navigating and understanding the data can be
challenging with so much information available. An innovative visualization tool that
displays trade data in a suitable graphical form can illustrate the evolution of trade
flows and show the trade volume and the composition of the basket of traded goods.
TERRA (imporT ExpoRt netwoRk Analysis) is a data visualization tool designed
at Istat. TERRA is an Experimental Statistics 32, publicly available from November
2023. TERRA offers researchers and policymakers the opportunity to explore the
dynamics of trade flows, with the possibility of focusing on specific products and
transport modes, tracing the critical phases of recent years. It also makes it possible
to simulate flow disruptions or closures of specific logistics hubs or transport routes,
allowing the outline of possible scenarios of modification or relocation of global
27 Official Journal of the European Union, Commission implementing regulation
(EU) 2024/2522, Council Regulation (EEC) No 2658/87 https://eur-lex.europa.eu/legal-
content/EN/TXT/PDF/?uri=OJ:L 202402522
28 Standard International Trade Classification: revision 4 (ISBN: 9211614937)
https://ec.europa.eu/eurostat/statistics-explained/index.php?
29 United Nations Statistics Division, Classification by Broad Economic Categories, Defined in
terms of SITC, Rev.3, ST/ESA/STAT/SER.M/53/Rev.3, E.89.XVII.4
30 Official Journal of the European Union, Commission delegated regulation (EU) 2024/3103,
amending Regulation (EC) No 451/2008 of the European Parliament and of the Council as
regards updating the classification of products by activity (CPA) https://eur-lex.europa.eu/legal-
content/EN/TXT/PDF/?uri=OJ:L 202403103&qid=1736955449829
31 United Nations, Report of the working party on transport statistics on its fifty-ninth ses-
sion, ECE/TRANS/WP.6/155/Add.1 https://unece.org/fileadmin/DAM/trans/doc/2008/wp6/ECE-
TRANS-WP6-155a1e.pdf
32 Detailed information on TERRA is available in Istat Experimental Statistics website:
https://www.istat.it/en/archive/290408

Big Data and ML at Istat 43
chains capable of mitigating the risk of shock transmission (changes in bilateral
relations between countries, logistics, or transport investments, increased foreign
investment, etc.).
European Big Data Hackathon
The European Big Data Hackathon is an international competition (hackathon)
organized by Eurostat as part of the New Techniques and Technologies for Offi-
cial Statistics (NTTS) conference. Teams of experts (data scientists, researchers,
methodologists, domain experts, etc.) from different European statistical institutes
participate in the competition to implement innovative products that integrate tra-
ditional data sources and Big Data sources. As part of the competition, teams must
produce a product that responds to a policy question related to a pressing issue in the
European context (e.g., COVID-19) and a statistical problem (integration of Big Data
sources, use of new data collection tools, increasing the quality of outputs of specific
production processes, etc.). The team representing Istat (Team-Istat) implemented
TERRA’s prototype during the virtual competition from February 26 to March 4,
2021. Team-Istat won first place in the competition.
3.5.1 Data source and data analysis tools
TERRA monthly processes about one billion foreign trade records produced by the
member countries according to harmonized methodologies publicly available on
Eurostat’s COMEXT database. The information base provides official estimates of
trade flows in monetary value and physical quantities at the highest granularity in
temporal resolution (monthly frequency), characteristics of traded products, trading
partner countries, and mode of transport. COMEXT’s bulk download function lets
users download large volumes of data in .dat format, facilitating easy import for
R, SAS, or Python analysis. The datasets include metadata such as classifications,
data availability details, and methodological notes. COMEXT data are organized in
different folders. TERRA is fed from the folders:
• PRODUCTS: containing EU countries’ monthly and annual trade interchange
with each partner country in value (Euro) and quantity (kg and any additional
units) for products classified according to Combined Nomenclature, SITC, CPA.
• TRANSPORT: containing data on monthly trade interchange of EU countries
with non-EU partner countries in value (Euro) and quantity (kg) by means of
transport. Products are detailed according to NSTR classification.
The main functionalities implemented in TERRA allow for the analysis of the
impact of shocks in the means of transportation and the effects of disruptions in cross-
country trade relations for specific products with social network analysis techniques
implemented in Python, offering a set of indicators proper to graph analysis.
The data analysis features offered by TERRA are the following:

44 Bruno M., Ortame F., et al.
• Interactive map: This section provides a map showing for each country the total
population, some macroeconomic indicators, the main imported and exported
products, and major trading partner countries. In addition, a time-lapse feature
is provided to depict the changes in monthly trends in international trade for the
past three years.
• Graph EU – Extra EU: This section displays graphs representing international
trade by product (NSTR classification, see above) and mode of transport from
COMEXT source, along with relevant global and local measures detailing the
structure of trade relations between EU and Extra-EU countries. The panel is in-
teractive and allows for the application of various filters. In addition, an animation
shows the evolution of the international trade graph over time.
• Graph EU – World: This section displays graphs representing international trade
by product (CPA 2.1 classification, see above) from COMEXT source, along
with relevant global and local measures detailing the structure of trade relations
recorded by EU countries to/from each trading partner country.
• Time-series: COMEXT data time series visualization tool. This section allows
for easy and understandable reading despite the underlying data volume. Series
are provided in value and quantity, and download is available in various formats.
• Basket of traded products: This section provides, for each EU Member State,
a monthly time series of trend changes in the composition of the basket of
exported and imported goods, classified according to the divisions of the CPA
2.1 classification.
3.5.2 Methodology
International trade relationships can be represented in interactive graphs and an-
alyzed using network analysis techniques Wasserman and Faust (1994). These
networks represent countries as nodes, and trade flows between them as directed
weighted edges. The weights indicate the value of a product exchanged (Euro) as
a percentage of the total trade volume for a specific time frame. Network metrics
provide quantitative insight into the trade structure and the roles of individual coun-
tries. Density, a global metric, measures how interconnected the network is, ranging
from 0 (no connections) to 1 (fully connected). A dense network reflects more com-
plex trade relationships, while a sparse network indicates fewer interactions. Other
centrality measures quantify node-specific roles:
• Degree centrality: quantifies the number of connections a node has. It is calcu-
lated based on the count of connections (edges) a node possesses, with higher
values indicating a more central position within the network.
• In-degree centrality : the number of import partners, reflecting the country’s
reliance on others. Low in-degree centrality indicates potential vulnerability due
to dependence on a few suppliers, who may have greater bargaining power.
• Out-degree centrality: the number of export partners, indicating trade outreach.
• Closeness centrality: measures how close a country is to others, calculated as
the inverse of the sum of the shortest paths to all nodes.

Big Data and ML at Istat 45
𝐶𝐶 (𝑢) = 𝑛 − 1
Í𝑛−1
𝑣=1 𝑑 (𝑣, 𝑢)
where 𝑑 (𝑣, 𝑢) is the shortest-path distance between𝑣 and 𝑢, and 𝑛−1 is the number
of nodes reachable from 𝑢. High closeness indicates a hub role, minimizing trade
distances De Benedictis et al. (2014).
• Betweenness centrality of a node is the sum of the fraction of all-pairs shortest
paths that pass through.
𝐵𝐶 (𝑢) =
∑︁
𝑠,𝑡 𝜖 𝑉
𝜎(𝑠, 𝑡|𝑢)
𝜎(𝑠, 𝑡)
where 𝑉 is the set of nodes, 𝜎(𝑠, 𝑡) is the number of shortest (𝑠, 𝑡)-paths, and
𝜎(𝑠, 𝑡|𝑢) is the number of paths passing through some node 𝑢 other than (𝑠, 𝑡).
High values indicate control over trade flows, positioning a country as a bridge
or bottleneck in the network.
• Distinctiveness centrality : highlights connections to peripheral nodes over
hubs, emphasizing the importance of countries bridging the core and periph-
ery Fronzetti Colladon and Naldi (2020).
𝐷𝐶 (𝑢) =
𝑛∑︁
𝑗=1, 𝑗≠𝑢
𝑤𝑢 𝑗𝑙𝑜𝑔 10
𝑛 − 1
𝑔 𝛼
𝑗
where 𝑤𝑢 𝑗 is the weight of the link between the node 𝑢 and 𝑗 (0 is there is no
link between those nodes), 𝑔 𝛼
𝑗 is the degree of the node 𝑗 elevated to 𝛼≥1, and is
used to allow a stronger penalization of connections with highly connected nodes.
Unlike traditional measures, distinctiveness centrality penalizes redundant ties to
dominant hubs, favoring strategically critical links to less-connected nodes.
COMEXT data gives a general overview of Europe but does not fully represent
global trade. It relies solely on declarations from European countries and excludes
interactions between non-European (Extra – EU) countries. This limitation can
distort density, closeness, and betweenness, as the network remains incomplete. To
mitigate this, extra-EU countries are grouped into a single node, balancing data
completeness with detail. Future development plans include integrating additional
data sources to address these gaps and build a more comprehensive trade network.
3.5.3 Architecture
TERRA implements a data processing pipeline to ensure data analysis is promptly
available to stakeholders a few hours after Eurostat data is published. The application
retrieves and processes monthly data spanning a 10-year time series. Additionally,
TERRA offers the option to select two types of monthly time series – raw data and
yearly variation.

46 Bruno M., Ortame F., et al.
To download and process a large volume of data, a specific batch program (shown
in the left panel of Fig. 22), implemented in Python, runs automatically each month.
This batch script is scheduled to start on the 24th day of every month. It downloads
files, performs the necessary processing, produces outputs, and ultimately updates
the data stored on the server.
The script runs on a cloud platform to minimize processing time using high-
performance algorithms. It accesses the bulk download section of the Eurostat portal.
The script initiates a parallel process to download 144 files containing monthly
product data, two files for annual product data, 144 files for monthly transport data,
and the associated classification files. Due to the varied and complex nature of the
data analysis algorithms, we opted for a microservices architectural paradigm. This
approach divides the application’s functions into multiple services, allowing for
individual responsibility; each service is implemented and deployed independently
of the others.
Fig. 22 TERRA main architectural layers and components
Fig. 22 sketches the main architectural components of TERRA33. Three different
layers can be identified in the architecture: data storage, data processing, and data
visualization.
1. Data storage layercontains raw data downloaded from the Eurostat portal. Batch
processing stores the aggregated data in this layer, which is further processed by
the microservices in the data processing layer.
2. Data processing layer, or backend, includes the three microservices: the first two
aim to process Python scripts, the third microservice exposes static data, such as
33 The source code of TERRA is open-source and available in the following GitHub repository:
https://github.com/istat-methodology/terra

Big Data and ML at Istat 47
classifications and metadata. The frontend communicates with the microservices
through requests according to the HTTP protocol, exchanging messages in JSON
format.
3. Data visualization layer, or frontend, includes the web component as the user
interface. This application was implemented as a single-page application using
open-source web frameworks. The use of these modern technologies makes the
application responsive. For instance, the layout adapts to the size of the display,
making it possible to access the dashboard from PCs and mobile devices.
3.5.4 Use case
This section examines the trends in electricity supply when countries were primarily
addressing the challenges of the COVID-19 pandemic.
Fig. 23 illustrates the interactive map panel of TERRA, which facilitates the
analysis of monthly percentage variations over the previous year for imported and
exported data, over the last five years, expressed in Euro. It displays a color-coded
heatmap based on the chosen variation index, with values ranging from -60% to
+60%. In April 2020, European nations experienced a significant negative impact,
as shown in the heatmap. This prompts further exploration of the effects on goods
exchanges between countries.
Fig. 23 Interactive map panel of EU exportation: comparison between April 2019 and April 2020
The analysis focuses on the product category ”Electricity, transmission, and dis-
tribution services.” By comparing the trade networks for this product in April 2020
with those from the same period the previous year — while combining Extra-EU
countries and averaging the flow, as illustrated in Fig. 24 — we observe a slight
decline in network density, which decreased from 0.20 to 0.19 (a 5% reduction). De-

48 Bruno M., Ortame F., et al.
spite this notable impact, the network remained relatively stable without significant
disruptions.
However, looking into individual country metrics reveals more nuanced insights.
For instance, Italy’s betweenness centrality fell from 0.21 in April 2019 to 0.12
in April 2020, and its normalized degree metric dropped from 0.11 to 0.06. This
indicates that while trade exchanges continued largely uninterrupted during the
pandemic, dominant countries adjusted their strategies, leading to a loss of centrality
for some nations.
Fig. 24 Graph EU — World: prevalent trade network (60%) on ”Electricity, transmission and
distribution services”. Comparison between April 2019 and April 2020
To complete the analysis including a time series point of view, Fig. 25 shows
Italy’s Electricity import data in Euro and includes these components:
• Green Line (Lag 12 Months Differences) : This line shows the difference be-
tween data points lagged by 12 months.
• Yellow Line (Mean) : A constant horizontal line representing the mean value
of the data series. This provides a reference point for comparison against the
fluctuations in the green line, which is approximately 23.7 million
• Standard deviation: approximately 402 million, suggesting high variability in
the data
• Time–Range: The x-axis spans from November 2014 to September 2024
The data remained relatively stable until March 2020, after which significant
volatility was observed. There was a decline around mid-2020, followed by peaks in
late 2021 and sharp decreases through mid-2022. In 2023, the data shows signs of
recovery and stabilization, although fluctuations persist. This pattern is particularly
noticeable during the COVID-19 pandemic, when electricity prices fell below the
average. Additionally, a more pronounced effect can be seen in the subsequent
years, where prices sharply increased in response to the Russia-Ukraine conflict,
significantly exceeding the average value for the analyzed period, before decreasing
a year after reaching their peak.

Big Data and ML at Istat 49
Fig. 25 Time series related to Italy’s import of Electricity between November 2014 and September
2024
3.5.5 Results
The TERRA platform demonstrates the potential of integrating advanced data vi-
sualization, analytical tools, and modern architectural solutions to disseminate and
interpret complex trade data. Using Eurostat’s COMEXT database, TERRA provides
granularity and timeliness in monitoring international trade flows. Its innovative use
of network analysis techniques offers policymakers and researchers with robust
metrics to assess trade dynamics, identify vulnerabilities, and explore scenarios to
mitigate disruptions in global supply chains. The platform includes interactive maps,
trade network graphs, and time series data. The detailed case study on electricity
trade during the COVID-19 pandemic highlights TERRA’s ability to highlight crit-
ical shifts in trade patterns and economic impacts during crises, confirming its role
as a robust tool for navigating an increasingly interconnected global economy. As
TERRA evolves, the integration of additional data sources and the refinement of
analytical capabilities promise to enhance its relevance and utility further, ensuring
that it can meet future challenges and opportunities in the analysis of international
trade.
3.6 Sentiment Analysis
Sentiment analysis identifies and categorizes opinions expressed as text to deter-
mine opinions toward a specific theme, i.e., positive, negative, and neutral. Indeed,
sentiment analysis is a branch of natural language processing (NLP) that aims to
identify a text’s emotional tone. It allows for extrapolating opinions from any social
media platform and determining users’ feelings regarding specific topics. Sentiment
analysis also allows for assessing public views on particular issues (Steinert, 2018).
Social media are an excellent source of information for sentiment analysis to pro-

50 Bruno M., Ortame F., et al.
vide perceptions for various scopes, whether commercial or not. In recent years,
the explosive growth of online media, such as social networking sites, has enabled
individuals to express opinions on many potentially interesting subjects for statistical
purposes and public policy evaluation. Moreover, evaluating real-time conversations
and trends on social media allows for a timely representation of people’s opinions,
which cannot be obtained through traditional Official Statistics. However, sentiment
indexes based on social media are not representative of the general population but
only of the active platform users. For instance, Twitter users tend to have a lower
average age than the real population. In addition, the users who discuss the topic
of interest are a subset of the active users on the specific platform and may have
different characteristics. This justifies why National Statistical Offices are interested
in creating synthetic indexes to monitor the debate on topics relevant to public policy
or for specific purposes for which traditional surveys can hardly collect data (such
as cyber violence, prejudices, and homo-transphobia).
Sentiment analysis tasks, also known as opinion mining, consist of labeling peo-
ple’s opinions as different categories, such as positive and negative (or relevant and
out of scope, subjective vs. objective) from a given piece of text (maybe a tweet or
an article). Classifying these documents is an arduous task. In recent years, many
methods, techniques, and enhancements have been proposed to solve the problem of
SA in different tasks at different levels. Sentiment analysis can be measured using
three main approaches:
1. Machine Learning (Pak et al., 2010)
2. Lexicon-based (Taboada et al., 2011).
3. Hybrid (Kolchyna et al., 2015), combining 1 and 2.
These techniques can be split into several distinct methods, as shown in Fig. 26
Fig. 26 Hierarchical structure of sentiment analysis techniques
NLP analyzes language for its meaning; therefore, a ”word” may have multiple
meanings varying according to the context. It is a superior technique compared to
lexicon-based approaches, which are essentially based on keyword processing: They

Big Data and ML at Istat 51
assign positivity or negativity to individual words and calculate the overall per-
centage score for the post. Supervised machine learning techniques, however, rely on
manually labeled data, i.e., manual processing: human interpretation of the sentiment
must be accurate. In the machine learning approach, the supervised learning model
can be easily trained, and the unsupervised model can easily categorize the data. The
lexicon approaches are based on sentiment lexicons, namely a list of lemmas (words
or composite expressions) with pre-computed sentiment scores. The sentence scores
of each sentence can easily be calculated as the mean of the sentiment scores of the
matched words.
It must be stressed that most of these methods are developed for the English
language. There are several quality problems in all approaches. The primary issue in
all techniques is classification accuracy, and many efforts imply correctly classifying
opinion and sarcasm, and it is well known that most of the text is often classified as
neutral. In addition to this problem, most research on sentiment analysis focuses on
text written in English. Indeed, the validation sets labeled in Italian were very few at
the time (roughly less than 10,000). Even if an approach may provide a better accuracy
on that set, when dealing with the specific problems of a daily index collecting
billions of tweets with a specific domain, i.e., economy, it is not evident how this
will affect the accuracy of the dynamics of a daily index of sentiment. Sentiment
classification based on insufficient labeled data is still a challenging problem, and
the amount needed for specific tasks is unclear even when a lexicon-based approach
is validated. Semi-supervised or unsupervised methods need less human labor and
may provide the same accuracy. However, lexicon-based approaches usually have
limited word coverage and thus may fail to recognize emotional words (especially
domain-specific words) and are still unable to deal with complex sentences, for
instance, with mistakes in spellings, acronyms, or neologisms (seeCovid, lockdown)
and have static sentiment.
In addition, but outside the scope of this paragraph, sentiment analysis has various
sub-streams, such as bias analysis and emotion detection.
Fig. 27 Social Mood on Economy Index (SMEI) data processing pipeline

52 Bruno M., Ortame F., et al.
3.6.1 Social Mood on Economy Index (SMEI)
In recent years, the Italian National Institute of Statistics (Istat) has exploited so-
cial media messages to assess the mood of Italians about the country’s economic
situation. In October 2018, this effort led to the release of the Social Mood on
Economy Index (SMEI) (Zardetto, 2018; Catanese et al., 2022), an experimental
high-frequency sentiment index based on Twitter data. Among the first experimental
statistics published by Istat, the Social Mood on Economy Index (SMEI) is a daily
index computed starting from the Italian Twitter’s public stream aimed at repre-
senting the perception of the evolution of economic features 34. Though computed
daily, the index is published since October 2018 each quarter, with the daily time
series provided as an attachment to the publication. The SMEI production pipeline
is shown in Fig. 27.
The sentiment analysis procedure adopts an unsupervised lexicon-based approach
(based on vocabularies whose lemmas are associated with pre-computed sentiment
scores), as applying supervised methods requires large sets of manually labeled texts.
Briefly, the index calculation pipeline consists of four fundamental steps:
1. Data collection: collection of a daily sample of public tweets matching a set of
keywords (the filter) related to the economy
2. Text cleaning: we only analyze the textual content of the tweets (no information
concerning Twitter users is ever stored: the index only uses unlinked anonymized
data). We perform standard Natural Language Processing (NLP) pre-processing
steps: (i) convert text to lowercase, (ii) tokenize the text into words, (iii) apply basic
orthographic repairs, (iv) remove URLs, (v) remove non-alphabetic characters
(e.g., # or @ ); (vi) remove stop words (vii) if needed, stem words to get rid of
inflected forms
3. Score extraction: calculation of tweets’ positive and negative sentiment scores, as
weighted averages of the sentiment scores of each word in the tweet
4. Index computation: computation of the daily index value as an appropriate central
tendency measure of the tweets’ score distribution.
Subject matter experts, borrowing keywords from the Italian Consumer Con-
fidence Survey (CCS) questionnaire, designed the first level filter in 2018 in the
following CCS-filter. It consists of questions deemed most appropriate to assess the
optimism/pessimism of consumers (namely: assessments and expectations on the
Italian general economic situation, on unemployment, assessments on households’
financial situation, opportunity and possibility of savings, current of durable goods
purchases, assessments on the family budget). A typical social media pipeline con-
sists of choosing a set of keywords and then filtering all the texts that contain at
least one of these keywords. There is solid evidence that a significant portion of all
the messages being exchanged on whatever social media platforms lack any rele-
vant information (Morstatter et al., 2013). Ideally, filters should be able to capture
relevant messages and- eliminate off-topic messages from the beginning. For this
34 Detailed information on SMEI is available from Istat’s website, at the following link
https://www.istat.it/wp-content/uploads/2024/05/Methodological Note.pdf

Big Data and ML at Istat 53
purpose, the filter choice should be split into a top-down and bottom-up approach.
First, experts choose a list of words according to the intended statistics. Then, the
list should be validated by some data-driven analysis that ensures the relevance of
the sampled texts. It is a well-known problem that words may have multiple mean-
ings, but they also can be used in different contexts, and a priori, it is impossible to
establish which ones. This data-driven analysis can be performed through machine
learning methods for semantic analysis, such as word embedding or topic modeling,
a frequently used text-mining tool for discovering hidden semantic structures in a
text body. In 2021, a quality enhancement concerned the filter design, i.e., the rele-
vance: i) analyze the filter via data-driven techniques to enhance tweets’ relevance,
i.e., grasp appropriate information for economic statistical purposes. ii) address the
”multiple meaning problem”, i.e., a word in the filter may have different meanings
in different contexts. To accomplish both tasks, an analysis through word embedding
techniques was performed. This, in particular, led to redesigning the filter (Catanese
et al., 2022) and further investigation of the coherence with other economic series
as shown in (Catanese et al., 2024a)
In particular, the change of sampled tweets, induced by the changes in the filter,
enhanced the economic interpretability of observed peaks.
As supervised methods require large sets of manually labeled texts, sentiment
scores are obtained in an unsupervised setting using an Italian sentiment lexicon, a
vocabulary whose lemmas are associated with pre-computed sentiment scores. The
texts of all tweets are compared with the lexicon. Based on the scores of the matched
words, for each tweet, the positive (𝑝) and negative (𝑛) sentiment scores are obtained
averages (more details can be found in the methodological note35). The calculation
of the daily index (𝐼) uses polar coordinates transformation and is a weighted average
of the polarity in terms of intensity, as shown in eq. 4
𝐼 =
Í
𝑡 𝑖𝑡 𝜔𝑡Í
𝑡 𝑖𝑡
∗ 100 (4)
where polarity 𝜔 = 1 − 4𝜋/𝜃 so that 𝜔 ∈ [− 1, 1] and 𝜃 = arctan (𝑛/𝑝), intensity
𝑖 =
√︁
𝑝2 + 𝑛2, so that 𝑖 ∈ [− 1, 1].
There are two quantitative lexicons in Italian (Basile and Nissim, 2013; Castel-
lucci et al., 2015) for the corpus-based method on tweets. In 2021, the lexicon of
SMEI has been revised mainly to increase the coherence with other economic time
series. In (Daas et al., 2012; Van den Brakel et al., 2017), several quality issues are
posed that are relevant in evaluating SMEI’s quality, like the selectivity concerning
the intended target population and the bias estimation problem. A method for vali-
dating and interpreting SMEI is correlating the series with official statistics derived
from monthly surveys, e.g., the Consumer Confidence Survey. However, there is no
guarantee that the correlation is based on true causality and that the correlation will
occur in the future. Indeed, the probability sampling for finite population inference
is stronger than reliance on co-integration. Series obtained from social media are
35 SMEI’s methodological note is available at the following link https://www.istat.it/wp-
content/uploads/2024/05/Methodological Note.pdf

54 Bruno M., Ortame F., et al.
selected by maximizing the correlation with the series from the sample survey and
do not necessarily measure the same concept as the survey. The 2021 validation of
the DPL vocabulary and redesign of the filter was carried out by comparing the
trend of SMEI with official economic statistics indicators (such as IPI and Consumer
Confidence Index). The new SMEI improved all analyzed correlations, increasing
consistency with other short-term business statistics.
As described, the SMEI index has been revised by changing the filter and replacing
the lexicon. The former change ensured a better filter relevance, while the second
change improved the coherence of the index with other NSI economical time series.
For all these reasons, the entire time series of SMEI has been reviewed and published
since the last quarter of 2021 with the new methodology. A note to explain to the
user the significant changes has also been published on the site. In the present study,
we highlighted the enhancements of the SMEI achieved by redesigning the filter and
changing the vocabulary.
With rare exceptions, the Big Data generation mechanism does not fall under the
control of the statistician, and it is not known. Therefore, ensuring the accuracy and
reliability of the statistical outputs derived from these sources is still a matter of
research. For these outputs to be configured as Trusted Smart Statistics, they must
be evaluated and validated ex-post according to rigorous and shared methodologies.
These methodologies do not fall within the traditional quality assurance framework
of the European National Statistical Institutes and are often the subject of current
research in the academic field. Integrating Big Data into the production processes
of the National Statistical Institutes presents complex challenges in reviewing and
adapting business processes and assuring and evaluating the quality of products.
Supervised machine learning techniques have the main advantage of evaluating
accuracy on the test set. However, they cannot compute the ”bias” or ”concept drift.”
This can be overcome by dynamically retraining them.
3.6.2 Istat supervised machine learning approaches for text classification
Since 2018, Istat has relied on lexicon-based sentiment analysis to calculate the
Social Mood on Economy Index (SMEI), mainly due to the lack of labeled Italian
datasets dealing specifically with the economy. In general, there are no significant
amounts of Italian-labeled datasets. However, while relatively straightforward and
efficient to implement, lexicon-based sentiment analysis presents shortcomings due
to the grammar of a sentence. Indeed, each word in a sentence is assigned a positive,
negative, and neutral score, and these scores are static and independent of context.
The sentiment of a given text is then obtained summing all the scores. This implies
that ”negations”, ”adverbs” or adjectives may alter the sense of a sentence and this
approximation may induce biases. Some experimentation is carried out to include
the use of valence shifters as shown in (Catanese et al., 2024b)
Due to both advancements in natural language processing techniques (Vaswani,
2017) and available labeled datasets (Basile et al., 2014; Mencarini et al., 2019;
Bianchi et al., 2021), Istat has explored the possibility of computing the SMEI

Big Data and ML at Istat 55
using supervised machine learning techniques, following two main approaches: (1)
Training Recurrent Neural Networks (RNNs) from scratch, and (2) fine-tuning pre-
trained encoder-only transformer-based models for sequence classification.
Recurrent Neural Networks (RNNs)
A popular way to deal with sequences of textual data is to use recurrent neural
networks, i.e., neural networks designed to process sequential data by maintaining
a ”memory” of previous steps in the sequence. In particular, Istat experimented
with RNNs like Long Short-Term Memory (LSTM) networks (Hochreiter, 1997)
and bidirectional LSTMs (Schuster and Paliwal, 1997) to compute the SMEI (Bruno
et al., 2024a). The results are promising and show an increased flexibility in the
classification when the labeled utilized dataset contains an explicit reference to
COVID-19. This approach is conceptually equivalent to the classifier’s dynamic
re-training to overcome the concept drift problem. In addition also, pre-trained
an embedding layer on the entire prediction corpus using a FastText algorithm
(Bojanowski et al., 2017), used as the first layer of the classification model, may
provide some knowledge of Covid-related vector space. In general, this made the
model more robust to the classification of sentences comprising words that are not
seen in the training set but are seen in the corpus.
Pre-trained Transformers
After their introduction in (Vaswani, 2017), transformer models have become state-
of-the-art in several natural language processing tasks, including text classification,
such as hate-speech recognition, racism, irony, and offensiveness. Only supervised
methods can be utilized for these tasks.
In particular, pre-trained encoder-only transformers like BERT (Devlin, 2018)
are particularly suited for fine-tuning for text classification tasks, as they are pre-
trained on vast amounts of textual data, and thus have a general knowledge of how
language and context work, and are easily fine-tuned to handle specific tasks, like
those previously mentioned. The issue with models like BERT is that they are pre-
trained on mainly English text and show sub-par performance in other languages.
This was addressed with the introduction ofmultilingual RoBERTa(Conneau, 2019),
pre-trained in over 100 languages. Istat used multilingual RoBERTa on labeled data
from (Basile et al., 2020) to experiment with the classification of hate speech in
Italian tweets (Bruno et al., 2024b), and compared the results to an attention-based
bidirectional LSTM (AT-BiLSTM), showing a significantly better performance of
the former. It is, however, a matter of fact that supervised methods need a significant
amount of labeled texts. For instance, for the task of hate speech detection against
immigrants, Istat’s training data comes from the EV ALITA 2020 HaSpeeDe 2 task,
which consists of roughly 7,000 records. To improve the capability of the classifier,
Istat labeled some of their most viral records. Texts likely to contain hateful tweets,

56 Bruno M., Ortame F., et al.
i.e., those with offensive languages, such asfate schifo (“you suck”), andavete rotto
i c****oni (”you pi**ed us off ”) were retrieved. This approach isolated 242,000
tweets, of which 67,000 were unique. Then, stratified sampling was carried out, an
effective method for handling skewed distributions, using the total number of tweets
as the target variable. The tweets were stratified into five classes based on the number
of retweets, with the final class being a take-all stratum, resulting in 681 sampled
texts, ensuring a coefficient of variation of 5%. These tweets were manually labeled,
resulting in 225 hateful and 456 not hateful. Adding this dataset to the training led
to more plausible results, at least in terms of average values, when the classifier was
applied to the Corpus of X posts.
4 Conclusion
Istat has successfully integrated Big Data processing pipelines into its statistical pro-
duction system, marking a significant step toward modernizing official statistics. The
maturity levels of these pipelines vary: some projects are still in the pilot stage, while
others have progressed to the status of experimental statistics available on Istat’s of-
ficial website. A few projects have fully transitioned into operational production.
At the core of this development is the institute’s commitment to sound innovation,
guaranteeing that new methodologies undergo thorough testing before they become
operational.
Looking ahead, Istat is strategically investing in a fully developed production
system based on non-traditional data sources. These investments will focus on
strengthening cross-cutting capabilities, such as methodological frameworks, IT
infrastructures, and governance models, as well as enhancing subject-matter exper-
tise in specific statistical domains. The ultimate goal is establishing a robust and
scalable system capable of continuously integrating new data sources into statistical
production.
Despite these advancements, several challenges remain. One of the key issues
is the ongoing evaluation of accuracy and uncertainty in Big Data-driven statistics.
Traditional statistical sources continue to play a crucial role, either by directly in-
tegrating with Big Data or serving as benchmarks for validation. While significant
progress has been made in assessing the reliability of results across different projects,
further refinement is still necessary. A potential path forward involves developing a
generalized reference framework for evaluating Big Data-based statistical products.
This framework would provide a standardized approach to ensuring methodological
soundness and consistency across different applications.
In the coming years, Istat will continue to enhance its capabilities, address method-
ological challenges, and refine its production processes. Istat aims to reinforce its
role in the European Statistical System by integrating big data and machine learning
into official statistics. This will ensure that new data-driven insights contribute to
informed policymaking and improve public understanding.

Big Data and ML at Istat 57
References
Stefano Ceri. On the role of statistics in the era of big data: A computer science
perspective. Statistics & Probability Letters, 136:68–72, 2018.
Stefano Mugnoli, Alberto Sabbi, Fabrizio De Fausti, Giuseppe Lancioni, and
Francesco Sisti. Quantification of urban green areas: An innovative remote sens-
ing approach for official statistics.Second Workshop on methodologies for official
statistics, Rome, 2024.
Elena Catanese, Monica Scannapieco, Mauro Bruno, and Luca Valentino. Natural
language processing in official statistics: The social mood on economy index
experience. Statistical Journal of the IAOS, 38(4):1451–1459, 2022.
Bradley Efron. Prediction, estimation, and attribution. International Statistical
Review, 88:S28–S59, 2020.
Haziza Dagdoug Larbi, Tsang. On the use of machine learning methods for the
treatment of unit nonresponse in surveys.Second Workshop on methodologies for
official statistics, Rome, 2023.
Svein Nordbotten. Neural network imputation applied to the norwegian 1990 popu-
lation census data. Journal of Official Statistics, 12:385–402, 1996.
Ton De Waal. Waid 4.1: a computer program for imputation of missing values.
Research in Official Statistics, 4:53–70, 2001.
Marco Di Zio, Mauro Scanu, Lucia Coppola, Orietta Luzi, and Alessandra Ponti.
Bayesian networks for imputation. Journal of the Royal Statistical Society Series
A: Statistics in Society, 167(2):309–322, 2004.
Mehdi Dagdoug, Camelia Goga, and David Haziza. Imputation procedures in surveys
using nonparametric and machine learning methods: an empirical comparison.
Journal of Survey Statistics and Methodology, 11(1):141–188, 2023.
Fabrizio De Fausti, Marco Di Zio, Romina Filippini, Simona Toti, and Diego
Zardetto. Multilayer perceptron models for the estimation of the attained level of
education in the italian permanent census. Statistical Journal of the IAOS, 38(2):
637–646, 2022.
M Di Zio, F De Fausti, R Filippini, S Toti, and D Zardetto. The imputa-
tion of the “attained level of education” in the base register of individuals
through neural networks using sampling weights. UNECE conference of Eu-
ropean Statisticians, Expert Meeting on Statistical Data Editing , 2022. URL
https://unece.org/statistics/events/SDE2022.
Z Mashreghi, D Haziza, and C L ´eger. Pseudo-population bootstrap methods for
imputed survey data, 2014.
Pascal Kilian, Sangbeak Ye, and Augustin Kelava. Mixed effects in machine
learning–a flexible mixedml framework to add random effects to supervised ma-
chine learning regression. Transactions on Machine Learning Research, 2023.
Roderick J Little. Calibrated bayes, an alternative inferential paradigm for official
statistics. Journal of official statistics, 28(3):309–334, 2012.
Roderick J Little. Bayes, buttressed by design-based ideas, is the best overarching
paradigm for sample survey inference.Survey Methodology, 48(2):257–281, 2022.

58 Bruno M., Ortame F., et al.
Sixia Chen and David Haziza. Recent developments in dealing with item non-
response in surveys: A critical review.International Statistical Review, 87:S192–
S218, 2019.
Jerzy Wieczorek, Cole Guerin, and Thomas McMahon. K-fold cross-validation for
complex sample surveys. Stat, 11(1):e454, 2022.
Vladimir Vovk, Alexander Gammerman, and Glenn Shafer.Algorithmic learning in
a random world, volume 29. Springer, 2005.
Jerzy Wieczorek. Design-based conformal prediction. arXiv preprint
arXiv:2303.01422, 2023.
Roman Hornung, Malte Nalenz, Lennart Schneider, Andreas Bender, Ludwig Both-
mann, Bernd Bischl, Thomas Augustin, and Anne-Laure Boulesteix. Evaluating
machine learning models in non-standard settings: An overview and new findings.
arXiv preprint arXiv:2310.15108, 2023.
de Wit et al. Essnet big data ii (2020) work package e ”tracking ships
– deliverable e4: Consolidated report on project results., 2020. URL
”https://indata.istat.it/tramar/index.php”.
Claude Merrien. Worldwide list of seaports, version 2021, 2021. URL
”http://dx.doi.org/10.12770/59ab5f6f-79ea-425d-830e-be5ecdb7bdbe”.
A Pappagallo, F Ortame, G Massacci, F Sisti, and F Pugliese. Deep learning for the
classification of ports in maritime transport statistics via ais data. InInternational
Conference on Learning and Intelligent Optimization , pages 318–332. Springer,
2024.
Muhammad Jabbar, Mariney Mohd Yusoff, and Aziz Shafie. Assessing the role
of urban green spaces for human well-being: A systematic review. GeoJournal,
pages 1–19, 2022.
Jinru Xue and Baofeng Su. Significant remote sensing vegetation indices: A review
of developments and applications. Journal of sensors, 2017(1):1353691, 2017.
Guglielmo Pristeri, Francesca Peroni, Salvatore Eugenio Pappalardo, Daniele
Codato, Antonio Masi, and Massimo De Marchi. Whose urban green? map-
ping and classifying public and private green spaces in padua for spatial planning
policies. ISPRS International Journal of Geo-Information, 10(8):538, 2021.
Jagannath Aryal, Chiranjibi Sitaula, and Sunil Aryal. Ndvi threshold-based urban
green space mapping from sentinel-2a at the local governmental area (lga) level
of victoria, australia. Land, 11(3):351, 2022.
J Ronald Eastman, Florencia Sangermano, Elia A Machado, John Rogan, and Assaf
Anyamba. Global trends in seasonality of normalized difference vegetation index
(ndvi), 1982–2011. Remote Sensing, 5(10):4799–4818, 2013.
Gennadii Donchyts, Jaap Schellekens, Hessel Winsemius, Elmar Eisemann, and
Nick Van de Giesen. A 30 m resolution surface water mask including estimation
of positional and thematic differences using landsat 8, srtm and openstreetmap: a
case study in the murray-darling basin, australia.Remote Sensing, 8(5):386, 2016.
A. Virgillito D. Zardetto M. Scannapieco, D. Summa. ”istat’s reference architecture
for internet as a data source for official statistics”, 2017.
Giulio Barcaroli, Monica Scannapieco, Marco Scarn `o, and Donato Summa. Using
internet as a data source for official statistics: a comparative analysis of web

Big Data and ML at Istat 59
scraping technologies. In Proceedings of Proceedings of the New Techniques and
Technologies for Statistics Conference (NTTS), 2015a.
Guilio Barcaroli, Alessandra Nurra, Sergio Salamone, Monica Scannapieco, Marco
Scarn`o, and Donato Summa. Internet as data source in the istat survey on ict in
enterprises. Austrian Journal of Statistics, 44(2):31–43, 2015b.
Giulio Barcaroli, Monica Scannapieco, and Donato Summa. On the use of internet
as a data source for official statistics: a strategy for identifying enterprises on the
web. Rivista Italiana di Economia Demografia e Statistica, 70(4):25–41, 2016.
D. Windmeijer J. Maslankowski G. Barcaroli M. Scannapieco D. Summa M. Green-
away I. Jansson D. Wu G. Stateva, O. Bosch. ”deliverable 2.4 final report on web
scraping enterprise characteristics”, 2018.
D. Summa J. Gussenbauer A. Ils K. L ¨oytynoja H. K¨ uhnemann, A. van Delden.
”report: Url finding methodology”, 2022.
Fabio Ricciato, Albrecht Wirthmann, Konstantinos Giannakouris, Fernando Reis,
and Michail Skaliotis. Trusted smart statistics: Motivations and principles. Sta-
tistical Journal of the IAOS, 35(4):589–603, 2019.
Joshua Stock, Oliver Hauke, Julius Weißmann, and Hannes Federrath. The appli-
cability of federated learning to official statistics. In International Conference on
Intelligent Data Engineering and Automated Learning , pages 70–81. Springer,
2023.
UN. United nations guide on privacy-enhancing technologies for official statistics,
2023.
Emiliano De Cristofaro and Gene Tsudik. Practical private set intersection protocols
with linear complexity. In International Conference on Financial Cryptography
and Data Security, pages 143–159. Springer, 2010.
Seny Kamara, Payman Mohassel, Mariana Raykova, and Saeed Sadeghian. Scaling
private set intersection to billion-element sets. In Financial Cryptography and
Data Security: 18th International Conference, FC 2014, Christ Church, Barbados,
March 3-7, 2014, Revised Selected Papers 18, pages 195–215. Springer, 2014.
J¨org Drechsler and James Bailie. The complexities of differential privacy for survey
data. Technical report, National Bureau of Economic Research, 2024.
Cynthia Dwork. Differential privacy. In International colloquium on automata,
languages, and programming, pages 1–12. Springer, 2006.
Noah Johnson, Joseph P Near, and Dawn Song. Towards practical differential privacy
for sql queries. Proceedings of the VLDB Endowment, 11(5):526–539, 2018.
Wenqiang Ruan, Mingxin Xu, Wenjing Fang, Li Wang, Lei Wang, and Weili Han.
Private, efficient, and accurate: Protecting models trained by multi-party learning
with differential privacy. In2023 IEEE Symposium on Security and Privacy (SP),
pages 1926–1943. IEEE, 2023.
UNECE et al. Synthetic data for official statistics: a starter guide. (No Title), 2023.
Stanley Wasserman and Katherine Faust. Social Network Analysis: Methods and
Applications. Structural Analysis in the Social Sciences. Cambridge University
Press, 1994.

60 Bruno M., Ortame F., et al.
Luca De Benedictis, Silvia Nenci, Gianluca Santoni, Lucia Tajoli, and Claudio
Vicarelli. Network analysis of world trade using the baci-cepii dataset. Global
Economy Journal, 14(03n04):287–343, 2014.
Andrea Fronzetti Colladon and Maurizio Naldi. Distinctiveness centrality in social
networks. Plos one, 15(5):e0233276, 2020.
ZC Steinert. Twitter as data (elements in quantitative and computational methods
for the social sciences), 2018.
Alexander Pak, Patrick Paroubek, et al. Twitter as a corpus for sentiment analysis
and opinion mining. In LREc, volume 10, pages 1320–1326, 2010.
Maite Taboada, Julian Brooke, Milan Tofiloski, Kimberly Voll, and Manfred Stede.
Lexicon-based methods for sentiment analysis. Computational linguistics, 37(2):
267–307, 2011.
Olga Kolchyna, Tharsis TP Souza, Philip Treleaven, and Tomaso Aste. Twitter senti-
ment analysis: Lexicon method, machine learning method and their combination.
arXiv preprint arXiv:1507.00955, 2015.
D Zardetto. Using twitter data for the social mood on economy index. In Atti della
XIII Conferenza nazionale di statistica, Rome, pages 4–6, 2018.
Fred Morstatter, J¨ urgen Pfeffer, Huan Liu, and Kathleen Carley. Is the sample
good enough? comparing data from twitter’s streaming api with twitter’s firehose.
In Proceedings of the international AAAI conference on web and social media ,
volume 7, pages 400–408, 2013.
Elena Catanese, Mauro Bruno, and Luca Valentino. Quality enhancements in ex-
perimental statistics: The italian social mood on economy index. In Giuseppe
Giordano and Michelangelo Misuraca, editors, New Frontiers in Textual Data
Analysis, pages 93–103, Cham, 2024a. Springer Nature Switzerland. ISBN 978-
3-031-55917-4.
Valerio Basile and Malvina Nissim. Sentiment analysis on italian tweets. InProceed-
ings of the 4th workshop on computational approaches to subjectivity, sentiment
and social media analysis, pages 100–107, 2013.
Giuseppe Castellucci, Danilo Croce, and Roberto Basili. Acquiring a large scale
polarity lexicon through unsupervised distributional methods. In Natural Lan-
guage Processing and Information Systems: 20th International Conference on
Applications of Natural Language to Information Systems, NLDB 2015, Passau,
Germany, June 17-19, 2015, Proceedings 20, pages 73–86. Springer, 2015.
Piet JH Daas, Marko Roos, Mark van de Ven, and Joyce Neroni.Twitter as a potential
data source for statistics. Statistics Netherlands, 2012.
Jan Van den Brakel, Emily S ¨ohler, Piet Daas, and Bart Buelens. Social media as
a data source for official statistics; the dutch consumer confidence index. Survey
Methodology, 43(2):183–210, 2017.
Elena Catanese, Giorgia Sacco, and Luca Valentino. A quantitative assessment of
the impact of valence shifters and emoji in lexicon for italian sentiment analysis.
JADT 2024 Mots compt´es, textes d´echiffr´es, 1:179–188, 2024b.
A Vaswani. Attention is all you need. Advances in Neural Information Processing
Systems, 2017.

Big Data and ML at Istat 61
Pierpaolo Basile, Nicole Novielli, et al. Uniba at evalita 2014-sentipolc task: Pre-
dicting tweet sentiment polarity combining micro-blogging, lexicon and semantic
features. Proceedings of EVALITA, pages 58–63, 2014.
Letizia Mencarini, Delia Iraz´ u Hern´andez-Far´ıas, Mirko Lai, Viviana Patti, Emilio
Sulis, and Daniele Vignoli. Happy parents’ tweets. Demographic Research, 40:
693–724, 2019.
Federico Bianchi, Debora Nozza, Dirk Hovy, et al. Feel-it: Emotion and sentiment
classification for the italian language. InProceedings of the eleventh workshop on
computational approaches to subjectivity, sentiment and social media analysis .
Association for Computational Linguistics, 2021.
S Hochreiter. Long short-term memory. Neural Computation MIT-Press, 1997.
Mike Schuster and Kuldip K Paliwal. Bidirectional recurrent neural networks.IEEE
transactions on Signal Processing, 45(11):2673–2681, 1997.
Mauro Bruno, Elena Catanese, Francesco Ortame, and Francesco Pugliese. Mea-
suring social mood on economy during covid times: A bilstm neural network
approach. In International Conference on Learning and Intelligent Optimization,
pages 305–317. Springer, 2024a.
Piotr Bojanowski, Edouard Grave, Armand Joulin, and Tomas Mikolov. Enrich-
ing word vectors with subword information. Transactions of the association for
computational linguistics, 5:135–146, 2017.
Jacob Devlin. Bert: Pre-training of deep bidirectional transformers for language
understanding. arXiv preprint arXiv:1810.04805, 2018.
A Conneau. Unsupervised cross-lingual representation learning at scale. arXiv
preprint arXiv:1911.02116, 2019.
Valerio Basile, Maria Di Maro, Danilo Croce, Lucia Passaro, et al. Evalita 2020:
Overview of the 7th evaluation campaign of natural language processing and
speech tools for italian. In CEUR WORKSHOP PROCEEDINGS, volume 2765.
CEUR-ws, 2020.
Mauro Bruno, Elena Catanese, and Francesco Ortame. Towards a hate speech
index with attention-based lstms and xlm-roberta. In Proceedings of the Tenth
Italian Conference on Computational Linguistics (CLiC-it 2024) , 2024b. URL
¨https://ceur-ws.org/Vol-3878/13bis main long.pdf”.
