# JOS Paper Outline – ATECO Semantic Coding

## 1. Introduction
- Problem: automatic coding in official statistics
- Limitations of rule-based systems (e.g., CIRCE)
- Opportunity: embedding-based semantic retrieval
- Gap: lack of rigorous evaluation frameworks for NSIs
- Contribution of the paper

## 2. Background and Related Work
### 2.1 Automatic coding in official statistics
- CIRCE, PRODCOM, existing approaches

### 2.2 Embedding-based semantic retrieval
- Sentence transformers
- Retrieval vs classification

### 2.3 Challenges in real-world coding
- Short queries
- Ambiguity
- Uneven subgroup performance

## 3. Problem Formulation
### 3.1 Task definition
- Text → ATECO code shortlist

### 3.2 Coding as a ranking problem
- Top-k retrieval instead of classification

### 3.3 Operational requirements in NSIs
- Shortlist usability
- Offline deployment
- Interpretability and validation

## 4. Methods
### 4.1 Representation of statistical classifications
- Naive
- Disentangled
- Centroid-based
- Strengths and limitations

### 4.2 Evaluation framework
- match@k metrics (definition)
- Rationale for k
- Model selection criteria

## 5. Data
### 5.1 Real-world dataset (CIRCE)
- Characteristics (short queries, distribution)

### 5.2 Synthetic dataset
- Purpose (augmentation)
- Limitations (no typos, abbreviations)

## 6. Experimental Design
- Models
- Combinations (models × methods × datasets)
- Decision rules

## 7. Results
### 7.1 Overall performance

### 7.2 Encoding strategies comparison

### 7.3 Robustness analysis
- Division-wise performance
- Similarity thresholds

## 8. Discussion
### 8.1 Implications for official statistics

### 8.2 Trade-offs
- Accuracy vs deployability

### 8.3 Limitations
- Short queries
- Synthetic data

## 9. Conclusion
- Key findings
- Methodological contribution
- Future work
