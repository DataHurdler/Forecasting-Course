# Proofreading Report: `Slides/Lecture12_Capstone.tex`

**Date:** 2026-03-01
**Reviewer:** Claude Code (proofreading agent)
**File:** `Slides/Lecture12_Capstone.tex`
**Bibliography:** `Bibliography_base.bib`
**Reference lecture:** `Slides/Lecture11_Features.tex`

---

## Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 2     |
| MAJOR    | 4     |
| MINOR    | 6     |
| **Total**| **12**|

---

### Issue 1: Factual error — combination does NOT beat XGBoost on MAE
- **Location:** Line 219, frame "All 11 Methods on RSXFS"
- **Current:** Muted footnote states the equal-weight combination "beats XGBoost on MAE"
- **Proposed:** `"Equal-weight combination (2,080) nearly matches LSTM on RMSE and beats XGBoost on RMSE --- at a fraction of the deployment complexity."`
- **Explanation:** The leaderboard table shows combination MAE = 1,530 and XGBoost MAE = 1,510. The combination is *worse* than XGBoost on MAE (1,530 > 1,510). The claim directly contradicts the table on the same slide.
- **Category:** ACADEMIC QUALITY
- **Severity:** CRITICAL

---

### Issue 2: Combination formula inconsistent with stated three-way combination
- **Location:** Lines 263–265, frame "Recommended Deployment Pipeline for RSXFS"
- **Current:** `$\hat{y}_t = \tfrac{1}{2}(\hat{y}_t^{\text{SARIMA}} + \hat{y}_t^{\text{XGB}})$`
- **Proposed:** Either (a) change to the three-model formula `$\hat{y}_t = \tfrac{1}{3}(\hat{y}_t^{\text{SARIMA}} + \hat{y}_t^{\text{XGB}} + \hat{y}_t^{\text{LSTM}})$`, or (b) clarify that the pipeline recommends the two-model combination with its own RMSE
- **Explanation:** The Forecast Combination slide states the equal-weight combination is SARIMA + XGBoost + LSTM (three models), yielding RMSE = 2,080. The pipeline formula combines only two models with weight 1/2. These are two different combinations producing different results. Students citing RMSE = 2,080 from the formula will be incorrect.
- **Category:** ACADEMIC QUALITY / MATH
- **Severity:** CRITICAL

---

### Issue 3: "30-unit RMSE gain from LSTM" should be 160 units
- **Location:** Lines 275–276, frame "Recommended Deployment Pipeline for RSXFS"
- **Current:** `"the 30-unit RMSE gain from LSTM does not justify the added deployment complexity"`
- **Proposed:** `"the 160-unit RMSE gain from LSTM (2,080 vs.\ 1,920) does not justify the added deployment complexity"`
- **Explanation:** LSTM RMSE = 1,920; combination RMSE = 2,080. Difference = 160 units, not 30. The 30-unit figure is combination (2,080) − XGBoost (2,050).
- **Category:** ACADEMIC QUALITY / TYPO
- **Severity:** MAJOR

---

### Issue 4: `\hat{y}` used instead of `\yhat` macro
- **Location:** Lines 264–265, frame "Recommended Deployment Pipeline for RSXFS"
- **Current:** `$\hat{y}_t = \tfrac{1}{2}(\hat{y}_t^{\text{SARIMA}} + \hat{y}_t^{\text{XGB}})$`
- **Proposed:** `$\yhat_t = \tfrac{1}{2}(\yhat_t^{\text{SARIMA}} + \yhat_t^{\text{XGB}})$`
- **Explanation:** `header.tex` defines `\yhat` as `\hat{y}`. All other lectures use `\yhat`. Direct use of `\hat{y}` is inconsistent with the established macro convention.
- **Category:** CONSISTENCY
- **Severity:** MAJOR

---

### Issue 5: British English spelling "Synthesising"
- **Location:** Line 9, subtitle
- **Current:** `\subtitle{Synthesising the Forecasting Toolkit}`
- **Proposed:** `\subtitle{Synthesizing the Forecasting Toolkit}`
- **Explanation:** All other lectures use American English spelling throughout. "Synthesising" is the British English form. The subtitle should match the established convention.
- **Category:** CONSISTENCY / TYPO
- **Severity:** MAJOR

---

### Issue 6: Undefined symbol `$m$` used without introduction
- **Location:** Line 297, frame "The Business Problem: Residential Natural Gas Demand"
- **Current:** `"virtually no AR structure beyond $m = 12$"`
- **Proposed:** `"virtually no AR structure beyond lag 12 (the seasonal period, $m = 12$)"`
- **Explanation:** The symbol $m$ for the seasonal period is not defined in this lecture or in `header.tex`. In a capstone context, students may not immediately recall the notation; a brief gloss is required.
- **Category:** ACADEMIC QUALITY
- **Severity:** MAJOR

---

### Issue 7: "adversarial" is informal / technically overloaded
- **Location:** Line 311, frame "The Business Problem: Residential Natural Gas Demand"
- **Current:** `"The test period is adversarial --- an honest stress test for all methods."`
- **Proposed:** `"The test period is demanding --- an honest stress test for all methods."`
- **Explanation:** "Adversarial" has a specific technical meaning in ML (adversarial examples). Using it loosely to mean "difficult" may mislead ML-aware students.
- **Category:** ACADEMIC QUALITY
- **Severity:** MINOR

---

### Issue 8: "auto-AIC" should be "auto-AICc"
- **Location:** Line 203, frame "All 11 Methods on RSXFS"
- **Current:** `ETS (auto-AIC)`
- **Proposed:** `ETS (auto-AICc)`
- **Explanation:** ETS model selection uses AICc (corrected AIC), not plain AIC. This is the terminology from Lecture 03 and the default in standard ETS implementations.
- **Category:** CONSISTENCY / ACADEMIC QUALITY
- **Severity:** MINOR

---

### Issue 9: Overflow risk — DM test table frame
- **Location:** Lines 150–182, frame "DM Test Across the Leaderboard"
- **Current:** 5-column tabular with `p{1.7cm}` columns at `\footnotesize` — no `\resizebox` applied
- **Proposed:** Wrap the `tabular` in `\resizebox{\textwidth}{!}{...}` to guarantee it fits within the slide text width
- **Explanation:** Total table width ≈ 1 (row label) + 4 × 1.7 = 7.8 cm plus column padding may approach or exceed the 16:9 slide text width. `\resizebox` is the safe guard.
- **Category:** OVERFLOW
- **Severity:** MINOR

---

### Issue 10: "Weekly" ambiguous without "refit" in decision framework
- **Location:** Lines 78–79, frame "The Forecasting Decision Framework"
- **Current:** `"Weekly \Rightarrow prefer simpler models; Monthly \Rightarrow ML feasible."`
- **Proposed:** `"Weekly refit \Rightarrow prefer simpler models; Monthly refit \Rightarrow ML feasible."`
- **Explanation:** Without "refit", the arrow reads as if the series frequency (not the refit cadence) determines model choice. The question heading says "Refit cadence?" but the answer drops the word.
- **Category:** GRAMMAR / ACADEMIC QUALITY
- **Severity:** MINOR

---

### Issue 11: Lowercase sentence-start in enumerate item
- **Location:** Lines 105–107, frame "Five Common Failure Modes"
- **Current:** `"a forecast without a prediction interval is not actionable for most business decisions."`
- **Proposed:** `"A forecast without a prediction interval is not actionable for most business decisions."`
- **Explanation:** Sentence begins with lowercase "a". All other enumerate items begin with a capitalized noun phrase.
- **Category:** GRAMMAR
- **Severity:** MINOR

---

### Issue 12: "within 8%" arithmetically incorrect
- **Location:** Lines 135–136, frame "Forecast Combination: The Robust Baseline"
- **Current:** `"RMSE $= 2{,}080$ --- within 8\% of LSTM"`
- **Proposed:** `"RMSE $= 2{,}080$ --- within 9\% of LSTM"` (or more precisely "8.3\% above LSTM")
- **Explanation:** (2,080 − 1,920) / 1,920 = 8.33%. "Within 8%" implies ≤ 8%, which is false. Rounds to 9%.
- **Category:** ACADEMIC QUALITY / TYPO
- **Severity:** MINOR

---

## Citation Verification

| Key | Line(s) | Entry in .bib | Present? |
|-----|---------|---------------|----------|
| `BatesGranger1969` | 121, 513 | Bates & Granger (1969) | Yes |
| `Timmermann2006` | 121, 513 | Timmermann (2006) | Yes |
| `StockWatson2004` | 121 | Stock & Watson (2004) | Yes |
| `Makridakis2020` | 145, 519 | Makridakis et al. (2020) | Yes |
| `Diebold1995` | 152, 516 | Diebold & Mariano (1995) | Yes |
| `Harvey1997` | 152 | Harvey, Leybourne & Newbold (1997) | Yes |

No missing or incorrect citation keys found.

---

## Section / `\sectionslide` Audit

| `\section{}` | Line | `\sectionslide{}` Present? |
|---|---|---|
| `Course Synthesis` | 27 | Yes (line 30) |
| `Combining and Testing Forecasts` | 113 | Yes (line 116) |
| `RSXFS Final Leaderboard` | 185 | Yes (line 188) |
| `Case Study: Utility Demand Forecasting` | 281 | Yes (line 284) |
| `Communication and Deployment` | 421 | Yes (line 424) |
| `Takeaways and References` | 495 | Yes (line 498) |

All six sections have corresponding `\sectionslide` commands. No structural issues found.

---

## Summary Table

| # | Location | Issue | Severity |
|---|----------|-------|----------|
| 1 | Line 219 | Combination does not beat XGBoost on MAE — factual error | CRITICAL |
| 2 | Lines 263–265 | 2-model formula contradicts described 3-model combination | CRITICAL |
| 3 | Lines 275–276 | "30-unit RMSE gain" should be 160 units | MAJOR |
| 4 | Lines 264–265 | `\hat{y}` should use `\yhat` macro | MAJOR |
| 5 | Line 9 | "Synthesising" → "Synthesizing" (British → American) | MAJOR |
| 6 | Line 297 | Symbol $m$ undefined — needs brief gloss | MAJOR |
| 7 | Line 311 | "adversarial" informal/overloaded — use "demanding" | MINOR |
| 8 | Line 203 | "auto-AIC" → "auto-AICc" | MINOR |
| 9 | Lines 150–182 | DM table overflow risk — add `\resizebox` | MINOR |
| 10 | Lines 78–79 | "Weekly" ambiguous without "refit" | MINOR |
| 11 | Lines 105–107 | Lowercase sentence-start in enumerate | MINOR |
| 12 | Lines 135–136 | "within 8%" should be ~9% (8.33%) | MINOR |

*End of report.*
