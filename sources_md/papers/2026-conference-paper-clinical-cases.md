# Using AI techniques to support cause of death coding for Official Statistics

Source filename: `2026-conference-paper-clinical-cases.pdf`
Document type: conference paper
Source path: `raw/papers/2026-conference-paper-clinical-cases.pdf`

Note: This markdown file is a clean text extraction from the original PDF. Page breaks are preserved to support later checking against the source.

## Page 1

JADT 2026: 18th International Conference on Statistical Analysis of Textual Data 
Using AI techniques to support cause of death coding for 
Official Statistics 
Angela Pappagallo1, Francesco Pugliese1, Chiara Orsi1, Tania Bracci1, 
Francesco Grippo1, Simone Navarra1, 
1Italian Institute of Statistics (Istat) – angela.pappagallo@istat.it 
1Italian Institute of Statistics (Istat) – francesco.pugliese@istat.it 
1Italian Institute of Statistics (Istat) – chiara.orsi@istat.it 
1Italian Institute of Statistics (Istat) – tania.bracci@istat.it 
1Italian Institute of Statistics (Istat) – francesco.grippo@istat.it 
1Italian Institute of Statistics (Istat) – simone.navarra@istat.it 
 
 
 
Abstract 1 (in English) 
 The Italian National Institute of Statistics (Istat) annually produce s cause-specific mortality statistics based on 
death certificates, completed by certifying physicians for each death occurring in Italy. Medical expressions 
reported on each certificate are coded using the World Health Organization’s International Classification of 
Diseases (ICD -10), and the underlying cause of death is selected for official statistics and international 
comparisons, in accordance with the provisions of ICD-10, . Coding process and selection of the underlying cause 
are performed using the Iris software. A first module of Iris assigns the corresponding ICD-10 code to each medical 
expression reported on the certificate, performing text recognition based on a dictionary of med ical terms. An 
additional module selects the underlying cause. Each year, approximately 670,000 death certificates are processed. 
About 80% are fully coded automatically by Iris, while approximately 135,000 require manual coding. Most cases 
not fully coded by Iris are due to failures in medical text recognition (the first module). This inspired the idea o f 
leveraging Artificial Intelligence (AI) techniques to improve the recognition and coding of medical terminology 
on death certificates, supported also by the successful experience of AI application to cause-of-death (CoD) data 
production in France . The ob jective of the present study was to identify AI models suitable for short and noisy 
medical text. The models were designed to support the dictionary-based step, and their performance was evaluated 
in terms of coding accuracy and automatic coverage. 
A curated selection of supervised machine learning models was implemented to perform the coding task, with 
consideration for state-of-the-art deep learning models (e.g. BiLSTM, BERT) and "open-weight" Large Language 
Models (LLMs), including LLaMA 1B. The experime ntal results indicate that AI approaches offer a promising 
pathway towards more efficient and reliable CoD, although there is room for improvement, particularly for terms 
and expressions absent from the training set. 
 
Keywords: causes of death, natural language processing, deep learning, artificial intelligence

## Page 2

2 A. PAPPAGALLO, F. PUGLIESE ET AL. 
 
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data 
Abstract 2 (in French, Italian or Spanish) 
 L’Istituto Nazionale di Statistica (Istat) produce annualmente statistiche di mortalità per causa basate sui certificati 
di morte, compilati da medici certificatori per ciascun decesso avvenuto in Italia. Le espressioni mediche riportate 
su ciascun certificato sono codificate utilizzando la Classificazione Internazionale delle Malattie (ICD -10) 
dell’Organizzazione Mondiale della Sanità, e la causa iniziale di morte , utilizzata per le statistiche ufficiali e i 
confronti internazionali, viene selezionata seguendo le istruzioni dell’ICD-10. Il processo di codifica e la selezione 
della causa iniziale sono effettuati utilizzando il software Iris. Un pri mo modulo di Iris assegna a ciascuna 
espressione medica riportata sul certificato il corrispondente codice ICD -10, effettuando il riconoscimento del 
testo sulla base di un dizionario di termini medici. Un ulteriore modulo consente di selezionare la causa i niziale. 
Ogni anno vengono processati circa 670.000 certificati di morte. Di questi, circa l’80% è completamente codificato 
in modo automatico da Iris, mentre circa 135.000 richiedono una codifica manuale. La maggior parte dei casi non 
completamente codificati da Iris è dovuta a fallimenti nel riconoscimento del testo medico (primo modulo). Ciò 
ha ispirato l’idea di sfruttare tecniche di Intelligenza Artificiale (IA) per migliorare il riconoscimento e la codifica 
della terminologia medica nei certificati di morte. Questa idea è supportata anche dall’esperienza positiva 
dell’applicazione dell’IA alla produzione dei dati di mortalità per causa in Francia. L’obiettivo del presente studio 
è stato identificare modelli di IA adatti a testi medici brevi e rumorosi. I modelli sono stati progettati per supportare 
la fase basata su dizionario e le loro prestazioni sono state valutate in termini di accuratezza di codifica e copertura 
automatica. Un’accurata selezione di modelli supervisionati di apprendimento automatico è stata implementata 
per svolgere il compito di codifica sopra descritto. 
Parole chiave: cause di morte, natural language processing, deep learning, intelligenza artificiale. 
1. Introduction 
 
Cause-of-death statistics represent one o f the most important sources of information for 
monitoring the health status of the population and guiding public health policies. At the core of 
their production lies the classification of causes of death, a step that is critical for ensuring both 
the quality and the comparability of statistics across time and across countries. 
In Italy, the National Institute of Statistics (Istat) is responsible for collecting, processing, and 
publishing cause-specific mortality statistics on an annual basis. The information is derived 
from the Istat paper-based form, also referred to as death certificate, which follows the standard 
recommended by the World Health Organization (WHO). The death certificate includes several 
lines on which a certifying physician reports the sequence of conditions leading to death, as 
well as any other contributing conditions . For each line, the physician should also report the 
time elapsed from the onset of the conditions described and the death. Each paper form is then 
digitized and the causes of death reported undergo the complex steps of coding according to 
the provisions of the International Classification of Diseases, ICD-10 (WHO, 2019). The coding 
includes three main phases. In the first, an ICD-10 code is attributed to each reported cause; in 
the second, codes assigned in the first phase can be modified on the basis of other information 
reported on the certificate (multiple causes) ; in the third, the underlying cause of death — 
defined as the condition that initiated the chain of events leading directly to death — is selected 
in accordance to rules described in the ICD-10. Both multiple and underlying cause are released 
as official cause-of-death statistics. 
The coding process and the selection of the underlying cause are carried out using Iris, a 
software tool adopted in many European and non -European countries for both automated and 
manual coding of causes of death (www.iris-institute.org). A first module of Iris assigns the 
corresponding ICD-10 code to each medical expression reported on the certificate. To this end, 
Iris performs text recognition based on a dictionary of medical terms developed by Istat experts. 
Regular expressions built into Iris are also used to standardize the text reported on the 
certificate, thereby improving matchi ng performance. The second module is a rule -based 
system that applies ICD-10 rules to determine multiple causes and the underlying cause (Istat,

## Page 3

USING AI TECHNIQUES TO SUPPORT CAUSE OF DEATH CODING FOR OFFICIAL STATISTICS 3 
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data 
2023). Each year, Istat records approximately 670,000 death certificates. Of these, about 80% 
are fully automatically coded by Iris. The remain ing certificates, around 135,000 per year, 
require manual coding, involving a substantial investment of highly trained personnel. 
Most automatic coding failures are due to the inability of Iris to recognize medical terminology 
(the first module), caused by incompleteness of the dictionary, incorrect reporting by certifying 
physicians, or inadequate recording of the certificates. 
2. Related Works 
Impressive results have been achieved by deep learning models in the field of text classification 
(Bruno M. et al., 2024 ). Specifically, in the health -care domain, the application of AI for the 
automatic coding of clinical texts , according to standardized classification syst ems, such as 
ICD-10, has been widely studied in medical informatics. As noted in a systematic review (Kaur 
et al. 2021), the methods have evolved progressively from traditional machine learning based 
on sparse text representations to deep learning and transformer -based architectures, which are 
designed to handle semantic complexity and large label spaces more effectively. Early work on 
clinical text classification and ICD coding primarily relied on methods such as Support Vector 
Machines, Naïve Bayes , and Random Forest, which are based on bag-of-words or TF -IDF 
techniques. In this context, Random Forest is often used as a robust and interpre table baseline 
due to its effectiveness in high-dimensional feature spaces. However, these models rely heavily 
on high-level lexical features, which limits their ability to capture semantic similarity, 
contextual meaning, and variation in medical terminology. Kaur et al. highlight that, across the 
literature surveyed up to 2020, traditional machine learning methods generally perform worse 
than more recent context-based models such as artificial neural networks. A first substantial 
improvement was achieved using deep learning models such as convolutional and attention -
based neural networks (Mullenbach, J. et al., 2018). These models replaced sparse features with 
dense representations learned directly from text. While these architectures improved the 
modelling of local patterns in clinical narratives and generally outperformed traditional 
baselines, their gains were still limited by the challenges of processing long documents, rare 
labels and broader contextual dependencies. 
More recently, transformer-based models, especially BERT (Devlin et al., 2019), have become 
the leading approach for automated ICD coding. BERT-XML (Zhang et al., 2020) is a notable 
example, adapting BERT to extreme multi-label classification and outperforming earlier neural 
baselines on large-scale ICD coding tasks. Pascual et al. (2021) further confirmed the potential 
of BERT -based systems, while also highlighting that constraints on input length remain a 
significant limitation for long clinical notes. Overall, the literature clearly shows a progression 
from traditional methods to deep neural models, and finally to BERT-based approaches. These 
approaches generally achieve the strongest results, often with micro-F1 scores above 0.6 in 
large-scale settings. However, direct comparisons remain difficult because of differences in 
datasets, label sets, and evaluation protocols. This evolution is particularly relevant for cause-
of-death coding , where models must process short and heterogeneous descriptions while 
complying with official coding rules. In this context, BERT-based approaches a ppear better 
suited than Random Forest and other traditional classifiers for capturing the semantic content 
and improving ICD-10 assignment . Nevertheless, explainability, rare-label performance and 
integration into real production workflows remain challenges, especially in institutional 
contexts such as official statistics. 
There is also evidence that AI can support cause-of-death coding with ICD -10 even in 
production settings. Névéol et al. (2018) reported the results of a shared task in which fourteen

## Page 4

4 A. PAPPAGALLO, F. PUGLIESE ET AL. 
 
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data 
research teams developed systems for the automatic ICD -10 coding of death certificates in 
French, Hungarian and Italian , achieving F-measures above 0.83 across all three languages. 
Zambetta et al. (2024) described the French experience of integrating AI in cause-of-death data 
production combining three methods: traditional rule -based automated coding with Iris, 
transformer-based ICD-10 coding t rained on previously coded data, and targeted manual 
coding. Their results suggest that these approaches are complementary, although manual review 
remains necessary for some ICD categories . In summary, most automatic coding failures are 
concentrated in the text recognition phase, wh ereas the subsequent rule -based coding phases 
achieve consistently high performance. Evidence from other national contexts therefore 
suggests that AI methods are most effective when integrated with traditional coding systems 
and supported by targeted manual supervision. 
Motivated by recent advances in automated coding, this work extends the methodological 
landscape of ICD -10 cause -of-death coding . It systematically compares approaches ranging 
from conventional machine learning to BERT-based models and Large Language Models 
(LLMs) on Italian medical records. The analysis provides new evidence on their potential to 
improve medical text recognition within the Iris-based workflow, reduce manual intervention, 
and preserve the comparability of official mortality statistics. 
 
3. Methodology 
In this section, we describe the used datasets, the data preparation process, and the models used 
to perform the classification of medical texts according to the ICD-10. 
3.1 Dataset 
For model development, datasets were prepared composed by the whole lines of the death 
certificates. Each line can contain a single or several medical expression s separated by 
semicolons. A single expression may correspond to one or more ICD -10 codes. In more 
complex cases, conjunctions, prepositions, or other separating phrases within a single 
expression lead to multiple diagnostic entities, each requiring a separate code. The time elapsed 
between the onset of the conditions and death, reported alongside the death certificates lines, 
has not been taken into consideration in this work.From the full set of lines referring to deaths 
occurring in 2022 and 2023 (total available lines: 4,327,927), completely coded either 
automatically by Iris or manually by expert coders, 300,000 were randomly extracted. Each line 
included the medical text and the corresponding ICD -10 code (or codes) . Furthermore, 
additional 950 death certificate lines , partially or completely unrecognized by Iris, have been 
extracted. The coding of these lines has been validated by expert coders, and the resulting 
dataset has been used as gold standard. This set includes only lines not fully coded by Iris, as 
the study specifically aims to apply AI methods to the text that Iris fails to recognize , and is 
used to evaluate the models’ ability to generalize to previously unseen data. 
3.2 Models 
To the aim of classifying Italian medical texts according to the ICD-10, a heterogeneous set of 
models was evaluated to compare approaches with different levels of representational 
complexity. The experimental setup started including Random Forest as a traditional machine-

## Page 5

USING AI TECHNIQUES TO SUPPORT CAUSE OF DEATH CODING FOR OFFICIAL STATISTICS 5 
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data 
learning baseline. Subsequently, we adopted a BiLSTM ( Schuster and Paliwal, 1997) 
implemented in PyTorch (Mikolov et al., 2013) with Word2Vec embeddings (Paszke et al., 
2019). Furthermore, we made use of several transformer -based architectures. In particular, 
XLM-RoBERTa Base and XLM-RoBERTa Large were identified as multilingual encoder-only 
models (Conneau et al., 2020); while BioBIT and MedBIT -r3-plus (Buonocore et al., 2023; 
Crema et al., 2023) were included to assess the contribution of their Italian biomedical internal 
knowledge. Finally, Llama 3.2 1B (Me ta, 2024) was considered to explore the potential of a 
compact large language model in order to perform the ICD -10 classification. Overall, this set 
of models enabled a comparison of conventional ensemble learning, recurrent neural networks, 
multilingual transformers, Italian biomedical transformers and lightweight LLMs within a 
unified classification framework. 
Before the training, we tuned the experimented models by setting their hyperparameters. With 
regard to Random Forest, we set two estimators. A s fa r as the deep learning models are 
concerned, hyperameters, such as the learning rate, the number of epochs and the batch size, 
were selected as summarized in Table 1. 
 
Table 1 – Deep Learning models and LLM model hyperparameters 
Model Type 
 
Number of 
epochs 
Learning 
rate 
Batch size 
XLM-Roberta - Large 70 2*10-5 512 
Llama Base 1B 70 2*10-5 128 
XLM-Roberta - Base 70 2*10-5 512 
Bert Bio ITA 70 2*10-5 512 
MedBIT-r3-Plus 70 2*10-5 512 
Pytorch - BiLSTM - W2V 70 10-3 256 
 
In some cases, we performed re -training of the language model prior to training the actual 
classification model. The purpose of this procedure was to enrich the existing embedding space 
with new medical terms present in the dataset and in the gold standard . This was done only 
when we made use of Word2Vec for Deep Learning models based on BiLSTM classifiers and 
XLM-RoBERTa (Base and Large). Regarding the BiLSTM with Word2Vec embedding, we 
choose an embedding vector of size 300, an embedding window of size 8, skip-gram (Mikolov 
et al., 2013) as embedding algorithm and 30 epochs for the training of the embedding. For the 
BERT embedding retraining. For XLM -RoBERTa the embedding retraining hyperparameters 
that we chose are: 1 epoch, learning rate of 5*10-5 and a batch size of 32. 
The quality of the classification performed by all the models was measured harnessing the 
weighted F1 -score (Christen P. et al., 2023). This performance metric was cho sen as the 
primary evaluation metric since the ICD -10 classification is significantly imbalanced. Indeed, 
if compared to accuracy, F1 -score is more resilient to situation s with a strong unbalance of 
classes in the dataset. Compared to macro F1 -score, the weighted F1-score reflects the real -
world distribution of labels rather than treating extremely rare and frequent codes in the same

## Page 6

6 A. PAPPAGALLO, F. PUGLIESE ET AL. 
 
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data 
way. For these reasons, it was considered the most appropriate metric for assessing performance 
in a production-oriented setting. 
3.3 Data Preparation 
In this work, we designed a rather complex and structured preprocessing pipeline aimed at 
transforming raw textual descriptions of causes of death into a standardized format suitable for 
serving as both training and test sets for the models we compared during the model selection 
phase. As a first step, data integrity checks were performed to identify and remove incomplete 
or inconsistent records. In particular, a missing values management procedure was 
implemented by removing entries containing missing values from both the textual field and the 
associated label (ICD-10 codes). These entries were then excluded from subsequent processing 
stages, where models frequently encounter failure when dealing with missing values, especially 
in the labels. 
A preliminary Exploratory Data Analysis was also conducted, revealing that 3.99% of labels in 
the dataset contained more codes than the number of textual diagnostic entities separated by 
“;”, which is conventionally used as the separator for both codes and texts. Optionally, “/” is 
also used as a label separator, but this is less common. Additionally, in 0.80% of cases, there 
were more diagnostic entities than codes. The remaining 95.21% of the data exhibits a one-to-
one correspondence between the number of medical texts and the number of codes in the labels. 
These calculations were performed on a sample of 300,000 reco rds of the dataset of 4 million 
lines, as previ ously anticipated in section 3.1 . However, since this sample was obtained via 
simple random sampling, we believe these percentages are likely representative of the entire 
dataset. 
After data cleaning and preliminary analysis, all multiple-text entries of the form “text1;text2” 
and “code1;code2” were split, where possible, into multiple atomic rows, resulting in entries 
such as “text1” with “code1” and “text2” with “code2” on a subsequent row. These cases, where 
the number of texts equals the number of codes, were estimated at 34,274 out of 300k records. 
This procedure led to an initial reduction in the number of distinct classes from 54,200 to 
26,446, since instead of treating combined codes like “code1;code2” as distinct classes, they 
were treated as atomic classes “code1” and “code2”, which may repeat. On the other hand, the 
number of text entries increased from 300,000 to 343,973. The same splitting procedure was 
applied to the gold standard dataset, increasing it from 950 to 1,154 entries. The only cases in 
which the texts were not split were those where the number of codes exceeded the number of 
medical text segments in the entry. This occurred under two conditions: either because the text 
explicitly reported fewer diagnostic entities, possibly due to an error or omission, or because 
multiple diagnostic entities were linked within the same text segment by conjunctions such as 
“with” or “in”. We did not implement semantic splitting procedures for conjunction -based 
cases, an idea we reserve for future work. Conversely, cases with more pathologies than codes 
were discarded, although rare, due to ambiguity in code assignment. Furthermore, all medical 
texts whose class appeared only once in the entire dataset were removed. This decision was 
made because we performed stratified train-test splitting to preserve the same data distribution. 
A class with only one occurrence would prevent this and create severe imbalance, which would 
be detrimental to model training. This cut -off procedure reduced the number of cl asses in the 
training set from 16,714 to 9,732. Subsequently, a target cleaning procedure removed suffixes 
such as “years”, “months”, or “days” in expressions like “code1 (n years)” or “code1 (n 
months)”, normalizing them to “code1”. This resulted in a fur ther reduction in the number of 
classes from 9,732 to 2,934 in the 300k dataset, and to 716 classes in the gold standard. The

## Page 7

USING AI TECHNIQUES TO SUPPORT CAUSE OF DEATH CODING FOR OFFICIAL STATISTICS 7 
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data 
main dataset was then split into training and test sets using stratification, with an 80% –20% 
ratio. The creation of an internal test set is crucial for evaluating model performance both during 
training (e.g., for regularization purposes) and afterward, particularly for comparing models 
during model selection. After the split, the training set consisted of 272,564 data points and the 
test set of 65,452. 
To re-train the language model for both Word2Vec with BiLSTM and XLM-RoBERTa, it was 
necessary to merge all texts from the datasets into a single large corpus during the preprocessing 
stage. This was due to the fact that both embeddings are generally trained in a fully 
unsupervised manner on textual corpora. To use transformer models (e.g., LLaMA and BERT), 
the preprocessed data were converted into the “Hugging Face Dataset format ”, where each 
instance contains the raw text and its encoded label. Tokenization then transforms text into 
numerical tokens using pre -trained tokenizers, which are effect ive in handling rare or 
compound biomedical terms through subword decomposition. To manage variable -length 
sequences, dynamic padding was applied at the batch level, improving memory efficiency and 
training speed compared to static padding. The tokenized o utput includes input IDs and 
attention masks, enabling the model to distinguish real tokens from padding. Encoded labels 
are also preserved, ensuring compatibility with supervised learning. 
 
 
 
 4. Results 
Table 2 reports, for each model, the F1 score obtained on the training set, the test set (meant as 
the 20% of the whole labelled dataset), and the gold standard, together with the training time. 
As expected, all the models reach a very high F1 sc ore when recoding the training set with 
values ranging from 0,967 for Pytorch - BiLSTM - No pretrained to 0,995 for XLM-Roberta - 
Large- 300k. The F1 score is slightly lower on the labelled test set, but still high with values 
ranging from 0.942 for Random Forest to 0.977 for XLM-Roberta - Large-- - embeddings 
retraining. A sharp drop in F1 values is observed when testing the gold standard: the highest 
score is reached by XLM -Roberta - Large with embeddings retraining with 0.535 which 
plummets to 0.357 in case of Pytorch - BiLSTM - W2V- No pretrained. Concerning the training 
time, faster training is associated with overall low performance: Pytorch and Random Forest 
with a training time of less than 13 minutes (only 4 minutes in case of Random Forest) show 
also the overall lowest perform ance. On the other hand, XLM-Roberta, especially the variety 
with embedding retraining, needing 4 hours of training , reaches the best overall performance 
both on the labelled test set and on the gold standard. 
 
Table 2 – F1 score on different test sets and training time for different models tested. 
Model Type 
F1 SCORE 
Training 
Time 
Training 
set 
Test set Gold 
Standard 
XLM-Roberta – Large - embeddings retraining 0,994 0,977 0,535 4h 
XLM-Roberta - Large- 0,995 0,976 0,519 3h e 49 min

## Page 8

8 A. PAPPAGALLO, F. PUGLIESE ET AL. 
 
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data 
Llama Base 1B 0,985 0,953 0,513 50 h 
XLM-Roberta - Base 0,991 0,973 0,502 1h e 36 min 
Bert Bio ITA 0,990 0,972 0,493 1h e 44 min 
MedBIT-r3-Plus 0,990 0,971 0,487 1h e 42 min 
Random Forest 0,974 0,942 0,418 3.69 min 
Pytorch - BiLSTM - W2V 300 - No pretrained - FULL Corpus 0,970 0,948 0,370 13 min 
Pytorch - BiLSTM - W2V - No pretrained 0,967 0,946 0,357 13 min 
 
Focusing on the results of the best -performing model on the gold standard (XLM-RoBERTa 
Large, with embeddings retraining), we compared the codes attributed by the model with those 
assigned by expert coders to each string reported in the rows. Rows can contain more than one 
string separated by a semicolon, yielding a total of 1,154 strings derived from 950 rows. The 
predicted code exactly matches the gold standard in 55.7% of cases (642 strings). Examining 
the probability of code attribution, 19,8% of strings (229) were coded with a probability of 
100%; among these, for 218 the predicted code is the same as the gold standard, meaning that 
the agreement rate is 95.2%. Moreover, 34,2% of strings (395) were coded with a probability 
>=95% and <100%; among these, the agreement rate between the predicted and the gold 
standard codes is 74,7%, compared to only 24.3% when the probabilit y falls below 95%. A 
further factor influencing agreement is the complexity of the strings. For strings requiring more 
than one code , the agreement rate drops to 8.7% , as the model tends to predict only a single 
code in such cases. 
5. Discussion 
The best-performing model for the automatic coding of texts , found on Italian cause-of-death 
certificates, is XLM-RoBERTa large with embedding s retraining. This model yielded an F1 
score of 0.535 and an agreement rate of 55.7% with the gold standard. The model performs 
much better on the test set, which represents 20% of the full dataset, than on the gold standard 
set. This difference is expected because the gold standard contains rows not fully coded by Iris. 
These rows are usually harder to classify, which makes the gold standard a more challenging 
test set. The confidence probability of code attribution can be used to identify cases where AI 
coding is reliable. However, a portion of certificates would still require manual revision, in line 
with studies recommending the integration of such methods with human supervision (Zambetta 
et al. 2024; Névéol et al. 2018). 
Analysis of disagreement cases shows that discrepancies stem mostly on complex medical texts 
requiring several codes. For these texts the model predicts fewer codes than the gold standard, 
with agreement dropping sharply to 8.7%. Results should also be interpreted in light of the 
known error rates in manual coding, particularly for causes such as infectious diseases and 
traffic accidents (Harteloh et al., 2010; Grippo et al., 2015). 
A key limitation is that the model was applied to entire rows, including those partially coded 
by Iris. An alternative approach could be to provide the model with individual diagnostic 
entities rather than certificate lines, this would likely improve performance. However, it is 
necessary to evaluate methods that allow for proper separation of diagnostic entities. As

## Page 9

USING AI TECHNIQUES TO SUPPORT CAUSE OF DEATH CODING FOR OFFICIAL STATISTICS 9 
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data 
previously highlighted, in many cases entities are separated by semicolons, but in others by 
words or expressions that are not always easily identifiable automatically. 
7. Conclusions 
The study's findings are relevant both for the national and the broader international community, 
as integrating such methods with existing automated coding systems like Iris could yield further 
performance gains. Contrary to expectations, decoder -only LLMs such as Llama do not 
outperform encoder-only models such as XLM-RoBERTa, which appear to be particularly well 
suited to automatic coding tasks. Moreover, large -scale decoder -only models, contain ing 
billions of parameters, are computationally expensive to train, as reflected in the results reported 
in Table 2. Future w ork could therefore explore hybrid approaches in which such models are 
used selectively, for example , to support the correction of the most challenging coding cases, 
without requiring full model retraining. 
 
References (0.5 pages) 
Bruno, M., Catanese, E., Ortame, F., & Pugliese, F. (2024, June). Measuring social mood on economy 
during covid times: A BiLSTM neural network approach. In International Conference on Learning 
and Intelligent Optimization (pp. 305-317). Cham: Springer Nature Switzerland. 
Zambetta E., Razakamanana N., Robert A., Clanché F., Rivera C., Martin D., Hebbache Z., Flicoteaux 
R. and Coudin E. (2024). Combining deep neural networks, a rule-based expert system and targeted 
manual coding for ICD -10 coding causes of death of Fren ch death certificates from 2018 to 2019. 
International Journal of Medical Informatics, 188, 105462. DOI: 10.1016/j.ijmedinf.2024.105462 
Kaur, R. and Ginige, A. and Obst, O. (2023). AI -based ICD Coding and Classification Approaches 
Using Discharge Summaries: A Systematic Literature Review. In Expert Systems with Applications. 
Elsevier. 
Mullenbach, J., Wiegreffe, S., Duke, J., Sun, J., & Eisenstein, J. (2018, June). Explainable prediction of 
medical codes from clinical text. In Proceedings of the 2018 conference of the north American chapter 
of the association for computational linguistics: human language technologies, volume 1 (long papers) 
(pp. 1101-1111). 
Devlin J., Chang M.W., Lee K., and Toutanova K. 2019. BERT: Pre -training Deep Bidirectional 
Transformers for Language Understanding. In Proceedings of the 2019 Conference of the North 
American Chapter of the Association for Computational Linguistics: Human Language 
Technologies, Volume 1 (Long and Short Papers), pages 4171 –4186, Minneapolis, Minnesota. 
Association for Computational Linguistics. 
Zhang, Z., Liu, J., & Razavian, N. (2020, November). BERT-XML: Large scale automated ICD coding 
using BERT pretraining. In Proceedings of the 3rd Clinical Natural Language Processing Workshop 
(pp. 24-34). 
Pascual, D., Luck, S., & Wattenhofer, R. (2021, June). Towards BERT -based automatic ICD coding: 
Limitations and opportunities. In Proceedings of the 20th workshop on biomedical language 
processing (pp. 54-63). 
World Health Organization. (2019). International classific ation of diseases, 10th revision (ICD -10), 
version 2019. https://icd.who.int/browse10/2019/en

## Page 10

10 A. PAPPAGALLO, F. PUGLIESE ET AL. 
 
JADT 2026: 18th International Conference on Statistical Analysis of Textual Data 
Névéol A., Robert A., Grippo F., Morgand C., Orsi C., Pelikan L., Ramadier L., Rey G. and 
Zweigenbaum P. (2018). CLEF eHealth 2018 Multilingual Information Extraction Task Overview: 
ICD10 Coding of Death Certificates in French, Hungarian and Italian. Conference and Labs of the 
Evaluation Forum (CLEF). 
Istat. (2023). Codifica delle cause di morte con l'ICD -10, versione 2020. Istat, Letture Statistiche – 
Metodi. https://www.istat.it/produzione-editoriale/codifica-delle-cause-di-morte-con-licd-10-
versione-2020/ 
Schuster, M., & Paliwal, K. K. (1997). Bidirectional recurrent neural networks. IEEE Transactions on 
Signal Processing, 45(11), 2673–2681. 
Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in 
vector space. arXiv preprint arXiv:1301.3781 
Paszke, A., Gross, S., Massa, F., et al. (2019). PyTorch: An imperative style, high -performance deep 
learning library. In Advances in Neural Information Processing Systems 32 
Conneau, A., Khandelwal, K., Goyal, N., et al. (2020). Unsupervised cross -lingual representation 
learning at scale. In Proceedings of ACL 2020, 8440–8451. 
Buonocore, T. M., et al. (2023). Localizing in-domain adaptation of transformer-based language models 
for the Italian biomedical domain. Journal of Biomedical Informatics, 142, 104398. 
Crema, C., et al. (2023). Advancing Italian biomedical information extraction with large language 
models: Methodological insights and multicenter practical application. Journal of Biomedical 
Informatics, 145, 104473. 
Meta. (2024). Llama 3.2 model card. 
Christen P., Hand D.J., and Kirielle N. 2023. A Review of the F -Measure: Its History, Properties, 
Criticism, and Alternatives. ACM Comput. Surv. 56, 3, Article 73 (March 2024), 24 pages. 
https://doi.org/10.1145/36063 
Harteloh P., de Bruin K. and Kardaun J. (2010). The reliability of cause -of-death coding in The 
Netherlands. European Journal of Epidemiology, 25, 531–538. DOI: 10.1007/s10654-010-9445-5 
Grippo F., Grande E., Simeoni S., Pennazza S., Cinque S., Bracci T. and Frova L. (2015). Reliability of 
causes-of-death statistics: the Italian experience from the ICD-10 training course. Rivista di Statistica 
Ufficiale, 17(3), 103–119
