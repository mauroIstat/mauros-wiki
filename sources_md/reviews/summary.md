# Review Summary – JOS Paper (ATECO Semantic Coding)

## Core Issue

The paper is perceived as a **technical report rather than a scientific article**.

The main weakness is not the experimental work, but the **lack of conceptual framing, methodological clarity, and connection to the literature**.

---

## Major Concerns (Referee 1 + AE)

### 1. Lack of scientific framing
- Encoding approaches (naive, disentangled, centroid) are introduced without justification
- No connection to existing literature
- No discussion of strengths/limitations before results

👉 Required action:
- Introduce a **Background & Related Work** section
- Justify each methodological choice

---

### 2. Unclear problem definition
- The task is not formally defined
- The intended use case (e.g., shortlist of codes) appears too late
- Claims about replacing rule-based systems are not grounded

👉 Required action:
- Introduce a **Problem Formulation** section
- Define the task as a **ranking problem (top-k retrieval)**
- Explicitly state **operational requirements in NSIs**

---

### 3. Inadequate evaluation framework
- Metrics (match@k, thresholds, etc.) are introduced in Results
- No prior definition of evaluation criteria
- No decision rule for selecting best model/method

👉 Required action:
- Move all evaluation definitions to **Methods**
- Clearly define:
  - match@k metrics
  - rationale for k
  - model selection criteria

---

### 4. Weak presentation of results
- Some figures are overcrowded or unclear (e.g., division-wise analysis)
- Threshold analysis lacks interpretation and connection to practice

👉 Required action:
- Simplify visualizations
- Focus on key comparisons
- Link results to **practical deployment decisions**

---

### 5. Synthetic dataset unclear
- Purpose of synthetic queries is not well explained
- Synthetic data is underused in the analysis
- Generated queries lack realistic features (typos, abbreviations)

👉 Required action:
- Clearly state synthetic data purpose (e.g., augmentation)
- Discuss limitations explicitly
- Explain its role in the centroid-based approach

---

### 6. Missing discussion of real-world challenges
- Short queries (majority of data) are not discussed enough
- Uneven performance across divisions is not contextualized

👉 Required action:
- Highlight **short query problem**
- Discuss robustness and subgroup performance
- Connect to existing literature

---

## Minor Concerns (Referee 2)

- Improve organization (separate Data vs Methods)
- Clarify model selection choices
- Improve figure readability (especially thresholds plot)
- Add references where missing (e.g., CIRCE documentation)

---

## Strategic Direction for Revision

The revision should:

1. Shift from:
   - "we tested several models and approaches"

   to:
   - "we propose and evaluate a framework for semantic coding in official statistics"

2. Clearly separate:
   - Background
   - Problem formulation
   - Methods (including evaluation)
   - Results

3. Align the paper with:
   - academic standards
   - methodological transparency
   - practical requirements of NSIs

---

## Key Message to Preserve

The core contribution remains valid:

- Embedding-based semantic retrieval is a viable alternative to rule-based coding systems
- Medium-sized models provide a strong trade-off between performance and deployability
- Centroid-based representations are effective for classification tasks in official statistics

---

## Revision Goal

Transform the manuscript into a **structured academic argument** where:

- the problem is clearly defined
- the methodology is justified
- the evaluation is rigorous
- the results are interpretable
- the implications for official statistics are explicit