# From textual agreements to structured data: using Large Language Models to enhance Official Statistics on anti-violence networks

Source filename: `2026-conference-paper-gender-violence.pdf`
Document type: conference paper
Source path: `raw/papers/2026-conference-paper-gender-violence.pdf`

Note: This markdown file is a clean text extraction from the original PDF. Page breaks are preserved to support later checking against the source.

## Page 1

From textual agreements to structured data:
using Large Language Models to enhance Official Statistics
on anti-violence networks
Elena Catanese1,Mauro Bruno 2, Maria Giuseppina Muratore3, Paolo Pizzo4,
Claudia Villante5
1Istituto Nazionale di Statistica−elena.catanese@istat.it
2Istituto Nazionale di Statistica−mauro.bruno@istat.it
3Istituto Nazionale di Statistica−muratore@istat.it
4Istituto Nazionale di Statistica−paolo.pizzo@istat.it
5Istituto Nazionale di Statistica−claudia.villante@istat.it
Abstract
This paper compares survey-based and Large Language Model (LLM)-based representations of territorial anti-
violence networks, with the aim of assessing their complementarity in official statistics (OS). Using data from
the 2024–2025 Istat survey on networks combating violence against women, we compare structured questionnaire
responses with information extracted from formal agreements.
We develop a LLM-based information extraction pipeline to identify institutional actors, classify them according
to predefined categories, and assign roles based on information explicitly stated in the documents. The results
show that survey data tend to underestimate the number and diversity of actors involved in territorial networks,
particularly in the presence of complex multi-actor agreements. At the same time, the extraction pipeline provides
a more comprehensive representation while assigning key roles, such as promoters and governance actors, only
when these are explicitly stated in the documents.
Overall, the findings demonstrate that LLM-based text analysis can effectively complement traditional data collec-
tion by identifying omissions, reducing inconsistencies, and enhancing the completeness of statistical information.
Keywords:Large Language Models; Survey Data Integration; Semantic Search; Violence Against Women
1. Introduction and research question
This paper arises from the intersection of two complementary methodological perspectives ap-
plied to the same object of study: territorial networks combating gender-based violence in Italy,
with a specific focus on the subjects that promote these networks and the actors who participate
in them.
The governance mandate introduced by Law 119/2013 has progressively translated, at both
national and territorial levels, into a structured system of formal agreements regulating anti-
violence networks (Istat, 2025). These networks are established through formal acts—such
as protocols, agreements, memoranda, and conventions—through which different institutions
define shared plans of action.
In 2025, Istat collected information on these formal acts through a structured survey admin-
istered to Regions and Autonomous Provinces, in partnership with the Department for Equal
Opportunity (EOD) of Italian Presidency of the Council of Ministers. The questionnaire gathers
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data

## Page 2

2 E. CATANESE, M. BRUNO, M. G. MURATORE, P. PIZZO, C. VILLANTE
self-reported information from regional respondents on the composition, objectives, and formal
characteristics of the networks operating in their territory. Each questionnaire is associated with
a corresponding formal agreement, acquired by Istat as a scanned PDF document.
Initial textual analysis was performed to geolocate the institutions involved in these networks.
The present study extends this approach by aiming to identify and classify institutions in terms
of their roles, functions, and attributes. In particular, the analysis distinguishes betweenpro-
moting subjects—those who initiate the network and assume formal responsibility, shaping its
governance structure—andinvolved actors—those who participate operationally without nec-
essarily having promoted the agreement. Comparing how these two categories are represented
across different data sources allows us to assess the ability of survey instruments to capture a
distinction that is both analytically and policy-relevant.
This work explores whether it is possible to automatically extract named institutions, their ty-
pologies, and their roles from unstructured textual documents using artificial intelligence tech-
niques. It compares traditional survey data with an innovative text analysis approach based on
LLMs, consistent with recent initiatives in OS (UNECE High-Level Group for the Modernisa-
tion of Official Statistics, 2023; United Nations Economic Commission for Europe, 2022).
Focusing onpromoting subjectsandinvolved actorsis particularly relevant, as these categories
directly reflect the capacity of the multi-level governance system to understand its own struc-
ture—namely, who is effectively part of the network, with what role, and with what level of
responsibility. In this perspective, textual analysis can provide significant added value by com-
plementing survey data, especially in contexts where monitoring the implementation of formal
agreements is crucial.
The study is guided by the following research questions:
1. Can LLM-based methods reliably extract actors and their roles from formal agreements?
2. How do the extracted data compare with survey-based information?
3. To what extent can this approach improve data quality and reduce respondent burden?
The remainder of the paper is structured as follows. Section 2. presents the background, Sec-
tion 3. describes the data, Section 4. outlines the methodology, Section 5. discusses the results,
and Section 6. concludes with implications and future developments.
2. Background: territorial networks as a tool for anti-violence governance
Strengthening assistance and support for women and their children is a priority objective of the
Extraordinary Plan against sexual and gender-based violence and of Law no. 119 of 15 October
2013, which implements the principles of the Istanbul Convention. 1 Among the objectives set
out in the law is the definition of a structured governance system across all levels of govern-
1 Chapter II of the Istanbul Convention highlights the relevance of integrated policies and data collection in com-
bating violence against women, recommending multi-level governance models in which “all relevant actors,
including public authorities, human rights institutions and civil society organisations”, contribute to integrated
and coordinated policies. Council of Europe. (2011). Council of Europe Convention on preventing and com-
bating violence against women and domestic violence, CETS No. 210. https://rm.coe.int/168008482e In Italy, it
was ratified by Law No. 77 of 27 June 2013, which authorised ratification and gave full effect to the Convention
in the Italian legal order.
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data

## Page 3

LARGELANGUAGEMODELS TO ENHANCEOFFICIALSTATISTICS ON ANTI-VIOLENCE NETWORKS3
ment, building on experiences and good practices already developed within local and territorial
networks.2
In response to this regulatory framework, Italy has progressively developed an articulated sys-
tem of formal agreements—including memoranda of understanding, conventions and frame-
work agreements—that establish and regulate territorial anti-violence networks. The survey
conducted by Istat in 2024–2025, in collaboration with the Department for Equal Opportunities
(DPO), the Regions and the Autonomous Provinces, produced for the first time a systematic
mapping of this system, identifying 251 territorial networks across 18 responding regions. This
represents an unprecedented information asset, enabling observation of the morphology of the
Italian anti-violence governance system in its aggregate dimension.
Yet mapping formal acts alone risks providing only a partial picture of this system. A memoran-
dum of understanding is a legal act that establishes commitments, defines subjects and allocates
responsibilities; however, signing a protocol does not necessarily guarantee either the effec-
tive participation of all listed subjects or the operational vitality of the network that originates
from it. The gap between formal governance and substantive governance is widely discussed
in the literature on anti-violence networks and represents one of the most critical issues in eval-
uating gender-based violence policies (Cimagalli, 2015; Deiana and Pellegrino, 2019; Kantola
and Squires, 2012). Addressing this gap requires analytical tools that go beyond the collection
of self-reported data and engage directly with the content of the formal acts produced by the
networks.
3. Data Sources
The analysis relies on two main data sources.
The first data source is a structured questionnaire completed by representatives of the Regions
and Autonomous Provinces as part of the Istat 2025 survey on territorial anti-violence networks.
Not all regions participated in the survey; overall, 251 responses were collected. The question-
naire, implemented using a CAWI (Computer-Assisted Web Interviewing) approach, collects a
wide range of information on the characteristics of the networks.
In this study, the analysis focuses specifically on the identification of institutions involved in the
networks, their roles, and their typologies. For each network, respondents were asked to iden-
tify the subjects that promoted the formal agreement (i.e., those initiating the network), using a
predefined list of 30 categories adopted for the Istat Antiviolence Centers Survey. Respondents
were also asked to report the total number of actors involved and, where possible, to list them
explicitly. Additional questions concerned the identification of actors, their classification ac-
cording to the same categories, and the subjects responsible for coordination, monitoring, and
management activities.
The second data source consists of the formal documents attached to the questionnaire—protocols,
agreements, memoranda, and conventions—which are typically provided as scanned images of
signed acts. These documents exhibit a high degree of heterogeneity in terms of structure and
editorial standards, as no common template is adopted. In some cases, the document explicitly
lists the parties involved (e.g., through expressions such as “this protocol is between the follow-
ing subjects”), while in others the roles of the actors are not clearly specified, making it difficult
to distinguish between promoting and participating entities.
2 Article 5 of Decree-Law no. 93 of 14 August 2013, converted, with amendments, into Law no. 119 of 15 October
2013.
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data

## Page 4

4 E. CATANESE, M. BRUNO, M. G. MURATORE, P. PIZZO, C. VILLANTE
Textual analysis of these documents offers a richer level of details compared to survey data.
In particular, it enables the identification and geolocation of entities, as well as the extrac-
tion of additional attributes, such as the addresses of anti-violence centres or other institu-
tions—information that is not collected through the questionnaire.
It must be noted that characterising these entities—i.e., understanding their role (promoting,
involved, or supervising) and typology (CA V or RUNTS third-sector organisations)—may be
challenging. In some cases, texts also refer to potential actors that are not listed by respondents.
For example, statements such as “in the case of minors, the victim should go to the court”
introduce entities that are not always reported in the questionnaire, but may nonetheless be
considered part of the network.
4. Methodology
4.1. Survey carried out involving Italian Regions
The survey instrument was developed through a participatory process involving the Regions
themselves, which preceded the administration of the questionnaire. The primary objective of
this process was to establish a shared nomenclature articulated around two dimensions: the clas-
sification of network promoters — that is, the institutional and non-institutional actors assuming
a driving and coordinating role in the establishment of territorial networks — and the classifica-
tion of the actors involved in network activation, encompassing public institutions, third-sector
organizations and specialist bodies.
The co-construction of a shared nomenclature made it possible to overcome the terminologi-
cal and classificatory differences present across the various regional experiences, ensuring the
comparability of the data collected and their interpretability within a systemic framework at the
national level.
4.2. Survey-control data editing
Even though the questionnaire was developed through an extensive collaborative process in-
volving stakeholders and institutional actors engaged in violence against women interventions,
limitations inherent to self-reported survey data remain. Respondents may interpret classifica-
tion categories differently, omit information, or introduce inconsistencies between related items
— limitations that are particularly salient in a domain as complex and institutionally varied as
anti-violence network governance.
To address these quality concerns, a second-stage validation procedure was implemented using
a Large Language Model (LLM)-based pipeline. The formal agreements submitted by respon-
dents as scanned PDF documents within the CAWI system were processed through an extrac-
tion pipeline built on OpenAI models. Using semantic search and entity extraction — guided
by prompts derived directly from the questionnaire’s classification modalities — the pipeline
identified actors, subjects and their roles as described in the original texts, and cross-referenced
these against the corresponding survey responses. Where discrepancies were detected between
the textual content of the formal agreements and the self-reported answers, these were flagged
for review, enabling the research team to resolve inconsistencies and complement item non-
responses with information extracted directly from the source documents.
This approach serves a dual purpose: it functions simultaneously as a quality assessment tool
for the survey data and as a validation framework for the LLM-based extraction methodology
itself, demonstrating the potential of AI-assisted text mining to enhance data quality in official
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data

## Page 5

LARGELANGUAGEMODELS TO ENHANCEOFFICIALSTATISTICS ON ANTI-VIOLENCE NETWORKS5
statistics on gender-based violence.
4.3. LLM-based information extraction pipeline
To complement survey data, an automated text analysis approach was developed to extract
structured information from formal agreements. The method relies on a multi-step informa-
tion extraction pipeline combining semantic search techniques and transformer-based language
models (Devlin, 2019), which have recently shown strong capabilities in processing unstruc-
tured text and supporting information extraction tasks (Brown, 2020).
The goal of the pipeline is to identify relevant institutional actors, classify them according
to predefined categories, and assign roles based on explicit textual evidence. The extraction
process is designed to prioritise precision and interpretability, avoiding implicit inferences and
relying only on information explicitly stated in the documents, in line with recent approaches
emphasising controllability and reliability in LLM-based systems (Bommasani, 2021).
In the first stage, the pipeline identifies (i) the formal signatories of the protocol and (ii) all
institutional and organisational actors mentioned in the text. Signatories are defined as enti-
ties explicitly listed as parties formally subscribing to the agreement, typically appearing in
the opening or closing sections of the document (e.g., lists introduced by expressions such as
“between”, “the parties”, or “signed by”).
All remaining entities are extracted assubjects, including public institutions, service providers,
associations, and other organisations mentioned in any capacity. Each subject is recorded using
a structured schema (name, type, municipality, address, lead role, and notes).
Classification relies on a predefined controlled vocabulary (the 30 categories adopted in the
survey) combined with a hierarchical set of rules to ensure consistency across cases. To max-
imise precision, the extraction process is restricted to clearly identifiable organisations: only
entities explicitly mentioned in the text are retained, no attributes are inferred, and duplicates
are removed. Entities that cannot be reliably interpreted as organisations (e.g., individuals, legal
references, or abstract concepts) are excluded.
The system also addresses heterogeneity in naming conventions by normalising alternative des-
ignations referring to the same entity (e.g., “ASL”, “Azienda Sanitaria Locale”, or specific
names of territorial health authorities).
In the second stage, the subset ofproposing actorsis identified. These are defined as entities
that explicitly initiate or promote the protocol. Selection is restricted to the previously extracted
subjects and relies solely on explicit textual evidence (e.g., expressions such as “promoted by”
or “initiated by”). No inference is applied at this stage: entities are not classified as proposing
actors based on their role as signatories or coordinators unless this function is clearly stated in
the text.
In the third stage,actors involvedin the operational implementation of the protocol are iden-
tified. These include entities participating in service delivery, collaboration networks, or inter-
vention activities. Identification relies on explicit indicators of operational roles (e.g., partici-
pation, collaboration, service provision, case management), and is again restricted to the set of
previously extracted subjects.
This step also supports the disambiguation between different organisational typologies, par-
ticularly between CA V and third-sector organisations listed in the RUNTS. In cases where an
organisation is formally classified as a non-profit entity but is described in the text as respon-
sible for providing support to victims of violence, it is reclassified as an anti-violence centre
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data

## Page 6

6 E. CATANESE, M. BRUNO, M. G. MURATORE, P. PIZZO, C. VILLANTE
based on its functional role. This rule-based reinterpretation ensures consistency between for-
mal classifications and the operational roles described in the protocols.
In the final stage, an enrichment step assigns roles to each extracted subject by matching them
against the lists of signatories, proposing actors, and involved actors. This matching process
combines normalized string comparison, rule-based alias generation (to account for variations
in naming conventions), and optional fuzzy matching with a conservative threshold to minimise
false positives.
Within this framework, a further analytical distinction is introduced betweenactors involved
andgovernance actors. The former includes all entities participating in operational activities,
whereas the latter refers to entities exercising coordination, strategic oversight, or institutional
responsibility (e.g., lead organisations or coordinators when explicitly indicated). These roles
are captured through specific attributes (e.g., “lead entity”) and annotations in the structured
data, rather than inferred automatically.
Across all stages, conservative extraction rules are applied to minimise false positives: entities
are retained only when clearly supported by the text, duplicates are removed, and no assump-
tions or implicit inferences are introduced. The final output consists of structured lists of signa-
tories, subjects, proposing actors, and involved actors for each protocol. All extracted entities
are assigned a role based on explicit textual evidence; in the absence of such evidence, they are
classified as involved actors. This structured representation enables a systematic comparison
between survey-based and text-derived information, supporting the analysis presented in the
next section.
5. Results
This section presents the main findings of the analysis, focusing on areas of convergence and
divergence between survey-based and text-derived representations of territorial networks. The
results provide insights into both the structure of anti-violence governance and the quality of
the information collected through different data sources.
5.1. Results from survey
Figure 1 displays the distribution of network actors by institutional category, distinguishing be-
tween promoting bodies — those who take the initiative in establishing territorial anti-violence
networks — and involved actors, who are subsequently called upon to participate in and con-
tribute to the network once constituted.
The data reveals that Anti-violence Centres and shelters represent the most frequent promoters
(203), confirming their central role as drivers of network governance at the local level, as also
recommended by the Istanbul Convention.
The distribution of actors involved in the protocols reveals a hierarchy of presence that reflects,
but does not perfectly replicate, that of the promoting subjects. The judicial sector is the most
broadly represented actor, with 367 presences out of 1,791 actors overall recorded (20.5% of the
total): Prefectures, Courts, Public Prosecutors’ Offices, and bar associations build around the
networks a legal protection architecture that goes beyond their role as promoters alone. CA V
and Shelters, taken jointly, account for 18.1% of actors, confirming their centrality not only as
subjects that initiate networks but as operational nodes actively involved in the care of victims.
The gap between the position of municipal services among the promoters (28 occurrences)
and their presence as involved actors (237) signals a broadening effect of the network at the
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data

## Page 7

LARGELANGUAGEMODELS TO ENHANCEOFFICIALSTATISTICS ON ANTI-VIOLENCE NETWORKS7
Figure 1: Promoting bodies and actors involved in territorial protocols/agreements by type.
Year 2025 (Absolute values)
implementation stage: many bodies enter the operational ecosystem of the network without
having signed the founding agreement. This finding is methodologically significant: it suggests
that the number of signatory subjects systematically underestimates the plurality of actors that
effectively inhabit territorial networks. More information is provided in Figure 2.
Figure 2: Source: Istat, Survey on Territorial Networks against Violence against Women, 2025
Figure 2 shows the regional distribution of promoting bodies — those who take the initiative in
establishing territorial anti-violence networks — and involved actors, those subsequently called
upon to participate in them. In the large majority of regions involved actors consistently out-
number promoting bodies — a structural feature consistent with the logic of anti-violence net-
work governance, in which coordinating institutions activate a broader constellation of public
agencies, service providers and civil society organizations around a shared governance frame-
work. It has to be mentioned that Umbria, Valle d’Aosta and Sardegna have only one proponent
body.
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data

## Page 8

8 E. CATANESE, M. BRUNO, M. G. MURATORE, P. PIZZO, C. VILLANTE
5.2. Comparison between survey data and LLM-based extraction
Figure 3 shows the distribution of entities by type and role identified through the LLM-based
extraction pipeline.
The results show that the number of protocol signatories identified in the texts (2,689) exceeds
the total number of promoting and involved actors reported in the survey (2,413). This suggests
that survey responses may underestimate the full set of stakeholders formally participating in
territorial agreements.
More broadly, the total number of actors identified in the protocols is substantially higher than
that recorded through the questionnaire. The largest discrepancies concern municipalities and
local public bodies. A plausible explanation is that, when a large number of municipalities are
involved in the same agreement, respondents tend to report aggregated counts rather than listing
each entity individually.
Figure 3: Entities identified in territorial protocols and agreements by type and role through the
LLM-based extraction pipeline. Year 2025. Absolute values.
By contrast, the number of promoting subjects identified through the extraction pipeline (586)
is lower than the survey estimate (808). This result is consistent with the conservative design of
the method, which classifies promoters only when explicit textual evidence is available, thereby
minimising false positives.
The number of governance actors identified (367 across 251 agreements) is consistent with the
expectation that, in most cases, a single lead institution is responsible for coordination. Here,
governance actors refer to entities responsible for coordination, monitoring, or strategic over-
sight when such roles are explicitly stated in the text. For some typologies, such as CA V and the
residual category “other”, the number of governance actors exceeds that of explicitly identified
promoters. This suggests that coordinating institutions may effectively play a promoting role
even when this function is not formally stated in the protocol.
To further investigate these differences, signatories identified in the texts (2,689) were compared
with the total number of actors reported in the survey (2,413) at the regional level (Figure 4).
The extraction-based estimates are slightly lower than survey counts only in Lazio and Veneto,
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data

## Page 9

LARGELANGUAGEMODELS TO ENHANCEOFFICIALSTATISTICS ON ANTI-VIOLENCE NETWORKS9
while higher values are observed for Lombardia, Emilia-Romagna, Toscana, Puglia, Abruzzo,
Liguria and Marche. For the remaining regions, the two sources show a high degree of consis-
tency.
Figure 4: Comparison between signatories identified in formal agreements and actors reported
in the survey, by region. Year 2025. Absolute values.
6. Conclusions
This paper examined the extent to which survey-based representations of territorial anti-violence
networks align with those obtained through direct analysis of formal agreements, and what di-
vergences between the two sources reveal about network structure and data quality. The findings
provide both substantive and methodological contributions. From a substantive perspective, the
study offers new evidence on the governance of anti-violence networks in Italy. The 2024–2025
Istat survey represents the first systematic national mapping of these networks, highlighting the
plurality of institutional and non-institutional actors involved in their functioning.
From a methodological perspective, the paper demonstrates the potential of LLMs for OS. The
proposed extraction pipeline shows how complex and heterogeneous textual documents can be
transformed into structured statistical information. The comparison between extracted entities
and survey responses reveals that text-based approaches can effectively complement traditional
data collection by identifying omissions, reducing inconsistencies, and capturing a broader set
of actors.
Comparing the two methodologies the results indicate that LLM-based extraction can effec-
tively complement survey data by identifying omitted actors, improving consistency, and pro-
viding a more complete representation of territorial governance networks. Overall, the integra-
tion of survey data with documentary text analysis helps bridge the gap between formal gov-
ernance and observed governance. While structured questionnaires ensure comparability and
standardisation, text analysis provides additional contextual depth that would otherwise remain
inaccessible.
Future research will focus on protocol-level micro-analysis to better understand discrepancies
between sources, improve classification accuracy, and further refine the extraction process, with
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data

## Page 10

10 E. CATANESE, M. BRUNO, M. G. MURATORE, P. PIZZO, C. VILLANTE
a spefic focus on the network monitoring activities. Additional developments include the geo-
referencing of network actors, the extension of the pipeline to other types of agreements, and
the longitudinal analysis of network evolution over time.
References
Bommasani R. e. a. (2021). On the opportunities and risks of foundation models.arXiv.
Brown T. e. a. (2020). Language models are few-shot learners.NeurIPS.
Cimagalli F., editor (2015).Le reti antiviolenza: Esperienze, metodologie e prospettive. Carocci.
Deiana G. and Pellegrino S. (2019). Le reti territoriali contro la violenza di genere: Struttura, funzioni e
criticità.La Rivista delle Politiche Sociali, (2):87–104.
Devlin J. e. a. (2019). Bert: Pre-training of deep bidirectional transformers.NAACL.
Istat (2025). Prevenire e combattere la violenza contro le donne: le reti territoriali. anno 2025.
Kantola J. and Squires J. (2012). From state feminism to market feminism?International Political
Science Review, 33(4):382–400.
UNECE High-Level Group for the Modernisation of Official Statistics (2023). Large language models
for official statistics.
United Nations Economic Commission for Europe (2022). Machine learning for official statistics.
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data
