# Pedagogical Review: `Slides/Lecture12_Capstone.tex`

**Date:** 2026-03-01
**Reviewer:** Claude Code (pedagogy-reviewer agent)
**File:** `Slides/Lecture12_Capstone.tex`

---

## Summary

| Metric | Result |
|--------|--------|
| Patterns followed | 9/13 |
| Patterns partially applied | 1/13 |
| Patterns violated | 3/13 |
| Internal numerical errors | 1 (MAE claim, line 219) |
| Socratic questions | 0 (target: 2-3) — **violated** |
| TikZ/visual slides | 0 (target: ~3-4) — **below target** |

**Deck assessment:** A well-structured capstone that successfully closes the course narrative. Narrative arc, box semantics, and section-divider record (first perfect `\sectionslide` usage in the series) are the standout strengths. Primary weaknesses: zero Socratic questions across 13 content slides, a factual error in the leaderboard footnote, and an unresolved two-model vs. three-model combination inconsistency.

---

## Slide Inventory

| # | Frame Title | Type |
|---|-------------|------|
| 1 | Title page | Structural |
| 2 | Outline | Structural |
| 3 | `\sectionslide` Course Synthesis | Section divider |
| 4 | L01–L11: A Two-Part Toolkit | Content |
| 5 | The Forecasting Decision Framework | Content |
| 6 | Five Common Failure Modes | Content |
| 7 | `\sectionslide` Combining and Testing Forecasts | Section divider |
| 8 | Forecast Combination: The Robust Baseline | Content |
| 9 | DM Test Across the Leaderboard | Content |
| 10 | `\sectionslide` RSXFS Final Leaderboard | Section divider |
| 11 | All 11 Methods on RSXFS | Content |
| 12 | What the DM Test Tells Us | Content |
| 13 | Recommended Deployment Pipeline for RSXFS | Content |
| 14 | `\sectionslide` Case Study: Utility Demand Forecasting | Section divider |
| 15 | The Business Problem: Residential Natural Gas Demand | Content |
| 16 | Applying the Decision Framework to RESGAS | Content |
| 17 | RESGAS Leaderboard: Framework Prediction vs. Results | Content |
| 18 | What Transferred, What Did Not | Content |
| 19 | `\sectionslide` Communication and Deployment | Section divider |
| 20 | Presenting Forecasts to Stakeholders | Content |
| 21 | Monitoring and Maintenance | Content |
| 22 | `\sectionslide` Takeaways and References | Section divider |
| 23 | BSAD 8310 Key Takeaways | Content |
| 24 | References | Structural |

Total: 24 frames. Content slides: 13. Section dividers: 6 (best in series).

---

## Pattern-by-Pattern Assessment

### Pattern 1: Motivation Before Formalism — **Followed**
The Course Synthesis section opens with a retrospective two-column map before the Decision Framework. The capstone question in the keybox ("which part of the toolkit do you reach for first?") motivates the entire lecture. RESGAS opens with the business problem before any model. Communication opens with a practitioner checklist. No action required.

---

### Pattern 2: Incremental Notation — **Followed (minor concern)**
Notation load per slide is low. The combination formula at line 264 uses $\hat{y}_t$ (no $h$ subscript) while course convention since L01 has been $\hat{y}_{t+h|t}$.

**Recommendation (Low):** Add parenthetical after the combination formula at line 264: "(here at $h=1$ for simplicity)".

---

### Pattern 3: Worked Example After Every Definition — **Followed**
No two consecutive slides present definitions without an interpretive or example frame between them. No action required.

---

### Pattern 4: Progressive Complexity — **Followed**
Correct ordering: synthesis → decision framework → combination/DM testing → RSXFS leaderboard → RESGAS transfer → communication → takeaways. Mirrors the L11 forward pointer promise. No action required.

---

### Pattern 5: Fragment Reveals — **Followed (correctly absent)**
No `\pause`, `\onslide`, `\only`, or `\uncover` commands, consistent with project rule. The "Framework Prediction vs. Results" framing achieves implicit problem-then-solution without overlay commands. No action required.

---

### Pattern 6: Standout Slides at Conceptual Pivots — **Followed (best in series)**
This is the **first lecture in the 12-lecture series with a perfect `\sectionslide` record**. All six section transitions use `\sectionslide{}{}` with informative subtitles. This resolves the Pattern 6 failure in L09, L10, and L11 and should be the model for retroactive fixes.

---

### Pattern 7: Two-Slide Strategy for Dense Theorems — **Partially Applied**

**Good:** RSXFS section correctly splits leaderboard across three slides (table → DM interpretation → deployment recommendation).

**Gap:** The DM pairwise matrix slide (slide 9) presents a 5×4 significance table with no formula reminder for students who have not reviewed L06 in 6 weeks. No color-coding distinguishes significant from non-significant cells. No forward pointer on slide 11 links to the DM interpretation on slide 12.

**Recommendation (Medium):**
1. Add two-line formula recall at top of slide 9: `\muted{\footnotesize\itshape (Recall from L06: $DM = \bar{d}/\widehat{\text{se}}(\bar{d}) \sim \mathcal{N}(0,1)$; $d_t = e_{1t}^2 - e_{2t}^2$. Harvey-Leybourne-Newbold correction applied; $n=48$.)}`
2. Add forward pointer at bottom of slide 11: `\muted{\footnotesize\itshape Which of these gaps are statistically confirmed? DM test results on the next slide.}`

---

### Pattern 8: Semantic Color Usage — **Followed**
Box types are semantically correct throughout: `keybox` for key results, `warningbox` for failure modes and monitoring warnings, `examplebox` for M4 and RESGAS outcomes, `definitionbox` for the Decision Framework. No action required.

---

### Pattern 9: Box Hierarchy — **Followed**
The single `definitionbox` (Decision Framework) is genuinely definitional. `warningbox` is used for genuine pitfalls. `examplebox` for genuine applied illustrations. No action required.

---

### Pattern 10: Box Fatigue — **Followed (borderline)**
8 keyboxes across 13 content slides = 62% (target ≤ 50%). The deployment pipeline (slide 13) uses a keybox for a five-step numbered procedure — better suited to `definitionbox{Five-Step Production Pipeline}`.

**Recommendation (Low):** Demote the deployment pipeline keybox (slide 13, lines 257–273) to `\begin{definitionbox}{Five-Step Production Pipeline}`.

---

### Pattern 11: Socratic Embedding — **VIOLATED**
**Zero Socratic questions** across 13 content slides. Target: 2–3. This is the only lecture in the series with zero Socratic prompts.

**Recommendation (High):** Add at least two questions:
1. Bottom of slide 5 (Decision Framework): `\muted{\footnotesize\itshape Q5 asks about refit cadence. If an economic shock makes weekly refit feasible for the first time, does that change which model you choose --- or only how you maintain it?}`
2. Bottom of slide 17 (RESGAS leaderboard): `\muted{\footnotesize\itshape SARIMA wins partly because COVID shifted residential usage patterns that ML could not anticipate. Is that an advantage of SARIMA --- or a limitation of the test period?}`

---

### Pattern 12: Visual-First for Complex Concepts — **Followed (minor gap)**
The DM matrix is preceded by the concrete three-number combination result. RESGAS comparison pairs table with interpretation simultaneously. No slide introduces notation before visualization.

**Minor gap:** DM matrix cells are not color-coded — significant and non-significant cells appear in identical black-on-white format.

**Recommendation (Low):** Add `\cellcolor{unolightgreen}` to significant cells and `\cellcolor{unolightred}` to n.s. cells (requires `colortbl` package if not already loaded).

---

### Pattern 13: Two-Column Definition Comparisons — **Followed**
Two-Part Toolkit (slide 4), What Transferred/What Did Not (slide 18), RESGAS leaderboard (slide 17), and Stakeholder Communication (slide 20) all use two-column format where comparison IS the pedagogical point. No action required.

---

## Deck-Level Analysis

### Narrative Arc
Four-act structure: (1) Synthesis → (2) Application I: RSXFS → (3) Application II: RESGAS → (4) Communication. Opens with capstone question (line 58) and closes with six takeaways directly answering it. This is genuine narrative closure.

**Gap:** The L11 forward pointer promises "presentation-ready visualizations." Zero TikZ figures appear. The stakeholder summary slide (slide 20) presents interval values as text but no visual.

### Internal Numerical Consistency Error (HIGH PRIORITY)
Lines 219–221: "Equal-weight combination (2,080) beats XGBoost (2,050) on MAE" is directly contradicted by the leaderboard table on the same slide: Combination MAE = 1,530, XGBoost MAE = 1,510. XGBoost wins on both RMSE and MAE. The combination does not beat XGBoost on either metric individually — the correct claim is that it nearly matches both LSTM and XGBoost at lower deployment complexity.

### Two-Model vs. Three-Model Combination Inconsistency
Slide 8 (line 134) describes the equal-weight combination as SARIMA + XGBoost + LSTM (three models, RMSE = 2,080). Slide 13 (lines 263–264) recommends a two-model production pipeline (SARIMA + XGBoost, weight = 1/2). No bridge sentence explains the change. Students will correctly notice this discrepancy.

**Recommended fix:** Add at top of slide 13 before the pipeline keybox: "For production, we use the two-model combination (SARIMA + XGBoost), dropping LSTM to eliminate GPU dependency. The RMSE impact is modest ($\approx$100 units); the deployment simplification is significant."

### Cross-Lecture RMSE Continuity
L10 reports LSTM RMSE = 2,180 (pre-feature engineering); L12 reports 1,920 (post-L11 features). L10 reports XGBoost RMSE = 2,250 (pre-features); L12 reports 2,050 (post-L11 features). The footnote $\dagger$ at line 194 ("ML models use 36-feature set from L11") correctly marks this. Adequate but easy to miss at small font size.

### Learning Objectives vs. L11 Forward Pointer

| Promise | Delivered? |
|---------|------------|
| Model selection | Yes — Decision Framework + RSXFS + RESGAS |
| Uncertainty quantification | Partially — intervals cited but never constructed |
| Presentation-ready visualizations | No — zero TikZ figures |

### Pacing
Content slides by section: Synthesis (3), Combining/Testing (2), RSXFS (3), RESGAS (4), Communication (2), Takeaways (1). Compact and appropriately sized. The Combining and Testing section (2 slides) moves quickly given the DM table's inferential complexity.

---

## Top 5 Critical Recommendations

### 1. Correct the MAE factual error (HIGH)
Lines 219–221: Replace the muted note with:
`\muted{\footnotesize\itshape Equal-weight combination (RMSE 2,080, MAE 1,530) nearly matches XGBoost (RMSE 2,050, MAE 1,510) and LSTM (RMSE 1,920, MAE 1,410) at a fraction of the deployment complexity.}`

### 2. Add two Socratic questions (HIGH)
See Pattern 11 recommendations above (slides 5 and 17).

### 3. Clarify two-model vs. three-model combination (HIGH)
Add a bridge sentence at the top of slide 13 explicitly explaining why LSTM is dropped from the production combination (see above).

### 4. Add DM formula recall + forward pointer (MEDIUM)
See Pattern 7 recommendations above (slides 9 and 11).

### 5. Add prediction interval construction note (MEDIUM)
Three-line expansion on slide 13 explaining the bootstrap method: "(1) collect walk-forward residuals; (2) bootstrap-resample; (3) form empirical quantiles at 10%/5% and 90%/95%." Or a TikZ fan chart to simultaneously fulfill the L11 "presentation-ready visualizations" promise.

---

## Quantitative Summary

| Metric | Count | Target | Status |
|--------|-------|--------|--------|
| `\sectionslide` calls | 6 | 6 | Met — best in series |
| `keybox` instances | 8 | ≤ 7 (50% of 13 slides) | Slightly over |
| Socratic questions | 0 | 2–3 | **Violated** |
| TikZ/visual slides | 0 | ~3–4 | **Below target** |
| Internal numerical errors | 1 | 0 | **Fix required** |
| Content slides | 13 | — | Compact, appropriate |
| Total frames | 24 | — | — |

*End of report.*
