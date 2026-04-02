# Pedagogical Review: Lecture11_Features.tex
**Date:** 2026-02-28
**Reviewer:** pedagogy-reviewer agent

---

## Summary

- **Patterns followed:** 8/13
- **Patterns violated:** 3/13
- **Patterns partially applied:** 2/13
- **Deck-level assessment:** A technically strong and well-structured deck with genuine pedagogical care. The visual-first discipline, Socratic questions, and leakage theme are consistently executed. Three issues require attention before deployment: (1) the `\sectionslide{}{}` standout macro is never called — all six section transitions use a plain "Section Overview" `keybox` frame instead; (2) keybox overuse at the deck level (10 keyboxes across 25 slides) dilutes emphasis on genuinely critical results; (3) the EWM smoothing parameter $\alpha$ is not distinguished from the Elastic Net mixing $\alpha$ used in Lecture 08.

---

## Pattern-by-Pattern Assessment

### Pattern 1: Motivation Before Formalism — **Followed**
Every section begins with a "Section Overview" frame posing design questions before introducing formulas. The opening motivation (line 27) is quantitative and concrete: LSTM RMSE 1,920 vs. 2,250 (XGBoost), attributed explicitly to better inputs.

### Pattern 2: Incremental Notation — **Partially Applied**
Most notation introduced gradually. Two issues:
- **EWM α collision (MAJOR):** Line 309 introduces $\alpha$ as EWM decay weight. Lecture 08 explicitly disambiguated its $\alpha$ (L1/L2 mixing) from ETS $\alpha$ (L03). Lecture 11 adds a third use with NO disambiguation note.
- **RMSE subscripts (Low):** $\text{RMSE}_0$ and $\text{RMSE}_j$ on Permutation Importance slide not labeled as "baseline RMSE" and "RMSE after shuffling feature $j$."

**Recommendation (MAJOR):** On the Rolling Statistics and EWM slide (line 282), add muted footnote: "\textit{(Here $\alpha$ is the EWM decay weight — distinct from ETS smoothing $\alpha$ in Lecture 03 and Elastic Net mixing $\alpha$ in Lecture 08.)}"

### Pattern 3: Worked Example After Every Definition — **Followed**
Every definition receives a concrete example within two slides. No two consecutive definition slides without an example between them.

### Pattern 4: Progressive Complexity — **Followed**
Section order is well-calibrated: Lag → Rolling → Calendar → Interaction → Feature Selection → Pipeline → Application. Simple to composite to meta-level arc.

### Pattern 5: Fragment Reveals for Problem → Solution — **Violated (Medium)**
The "Feature Selection via LASSO and Permutation Importance" slide (line 673) presents two full algorithms simultaneously. This is the densest slide in the deck.

**Recommendation (MEDIUM):** Split into:
- Slide A: "Feature Selection via LASSO" (full width)
- Slide B: "Feature Selection via Permutation Importance" (full width, with TikZ importance chart from line 341)

### Pattern 6: Standout Slides at Conceptual Pivots — **Violated (Medium)**
The `\sectionslide{}{}` macro (defined in `header.tex` lines 230-241) is never called. All six section transitions use a plain "Section Overview" `keybox` frame. Students cannot visually detect major topic changes during live lecture.

**Recommendation (MEDIUM):** Insert `\sectionslide{}{}` calls immediately before lines 63, 253, 413, 536, 648, and 781. Retain "Section Overview" content frames as the first slide of each section. This adds 6 slides (total: ~31 slides).

### Pattern 7: Two-Slide Strategy for Dense Theorems — **Partially Applied**
The YoY/MoM section correctly splits content across columns on a single slide. The LASSO objective function would benefit from `\underbrace{}` term decomposition (loss term vs. penalty term) connecting to L08 geometry.

**Recommendation (Low):** On LASSO formula (lines 679-682), apply `\underbrace{}` with subscript labels distinguishing prediction error from feature selection penalty.

### Pattern 8: Semantic Color Usage — **Followed**
ACF/PACF chart: unolightblue (ACF/neutral), unoblue (key lag 1 PACF), unolightgreen (seasonal lag 12 PACF), gray!30 (non-significant). Permutation importance: unoblue (top-4), gray!40 (bottom-4). Pipeline: unolightblue (data stages), unolightgreen (transforms), unolightred (model stage). Minor note: unolightred for model stage could suggest "warning"; consider unoblue instead.

### Pattern 9: Box Hierarchy — **Followed**
All four box types used for correct semantic purposes throughout.

### Pattern 10: Box Fatigue — **Violated (Medium — deck level only)**
Per-slide: no slide exceeds 2 colored boxes. **Deck level:** 10 keyboxes across 25 slides. Six of these are section overview frames (lines 64, 254, 414, 537, 649, 782). Keybox loses signal value when used as section header.

**Recommendation (MEDIUM):** Demote the six "Section Overview" keyboxes to plain bold paragraph text or simple `\textbf{}` heading. Reserve keyboxes for: (1) opening motivation (line 29), (2) shift-before-rolling rule, (3) feature-engineering-beats-model-selection finding (line 1008).

### Pattern 11: Socratic Embedding — **Followed**
Three genuine Socratic questions well-targeted and appropriately placed:
1. Line 185: "ACF at lag 12 is strong, but PACF at lag 12 is also strong. Why include `lag_12` even in an ARIMA model that handles seasonality through differencing?"
2. Line 484: "A SARIMA model with $s=12$ handles seasonality through seasonal differencing. Why might month dummies improve a Random Forest but add no value to SARIMA?"
3. Line 600: "YoY removes the seasonal level but still contains trend. What additional transformation would make $\text{YoY}_t$ a stationary series?"

### Pattern 12: Visual-First for Complex Concepts — **Followed**
All three TikZ diagrams appear before or alongside the formal notation they illustrate. ACF/PACF chart visual precedes the $\pm 1.96/\sqrt{n}$ rule. Permutation importance preview appears before the formal algorithm. Pipeline flow diagram appears in the left column with steps in the right.

### Pattern 13: Two-Column Definition Comparisons — **Followed**
Three concept pairs correctly presented side-by-side: shift(k) vs. lookahead bug (line 194); lag_12 vs. month_12 (line 469); YoY vs. MoM (line 559). The LASSO vs. permutation importance slide (line 673) would benefit from explicit column labels and a unifying takeaway sentence.

---

## Deck-Level Analysis

### Narrative Arc
Coherent closed arc: Motivation (line 27) promises extended features + selection + leaderboard update. Application section (line 944) delivers exactly that. One minor gap: Feature Selection and Pipeline Design sections are presented independently but are conceptually inseparable — add one bridging sentence at the Pipeline Section Overview.

### Pacing
Feature Selection section is the most underpaced: three distinct methods (LASSO, permutation importance, RFECV) in two content slides, one of which is split two-column with full code. Consider separating the RFECV definition from its implementation.

### Notation Consistency
$\alpha$ collision (EWM/ETS/Elastic Net) is the only significant issue. $\lambda$ (regularization) and $\boldsymbol{\beta}$/$\mathbf{x}_t$ are consistent with prior lectures. Rolling mean notation $\bar{y}_{t-1:t-w}$ (line 293) uses colon-range syntax not previously established.

### Student Concerns
1. YoY as feature vs. transformation: clarify it is computed at feature-creation time, not as a model pre-processing step
2. RFECV curve not shown on slide — cross-reference to notebook
3. Pre-pipeline feature engineering subtlety: `make_features_extended()` is safe pre-pipeline because all ops use `shift(k)`; but students extending the function with non-lagged transforms need to know these must go inside the pipeline

---

## Critical Recommendations (Top 5)

1. **Disambiguate $\alpha$ on Rolling Statistics and EWM slide (line 282) — MAJOR:** Add muted footnote distinguishing EWM $\alpha$ from ETS $\alpha$ (L03) and Elastic Net $\alpha$ (L08).
2. **Insert `\sectionslide{}{}` macro calls at all six section boundaries — MEDIUM:** Before lines 63, 253, 413, 536, 648, 781. Retain Section Overview content frames as first slide of each section.
3. **Demote six Section Overview keyboxes to plain text headings — MEDIUM:** Reserve keyboxes for three highest-priority results only.
4. **Split LASSO + Permutation Importance slide into two slides (line 673) — MEDIUM:** This is the densest slide in the deck; two full algorithms on one frame.
5. **Add pre-pipeline feature engineering subtlety note — LOW:** Clarify when feature engineering must go inside the pipeline vs. when it is safe to compute beforehand.
