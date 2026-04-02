# Proofreading Report: Lecture01_Intro.tex
**File:** `Slides/Lecture01_Intro.tex`
**Date:** 2026-03-01
**Reviewer:** Proofreading agent

---

## Executive Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 2 |
| MAJOR    | 5 |
| MINOR    | 7 |
| **Total** | **14** |

The deck is well-structured with consistent section/sectionslide pairing and no box fatigue. The two CRITICAL issues are a mathematically inaccurate claim relating the random walk with drift to Holt's exponential smoothing, and a missing verb that leaves a bullet item as a fragment. The five MAJOR issues cover missing articles, an internally inconsistent forecast-sequence notation across two slides, and a high-overflow-risk footnote. Seven MINOR issues address informal language, non-standard terminology, an imprecise benchmark label, a missing parallel structure, and a possible department-name mismatch in the metadata.

---

### Issue 1: Mathematically inaccurate claim about Holt's method
- **Location:** Lines 527–528, slide "Benchmark 4: Random Walk with Drift"
- **Current:** `Special case of Holt's linear exponential smoothing (Lecture 3) with $\alpha = 1$, $\beta = 1$`
- **Proposed:** `Limiting case: as $\alpha \to 1$ and $\beta \to 1$, Holt's method approaches the random walk with drift (Lecture 3).`
- **Category:** MATH
- **Severity:** CRITICAL

Setting $\alpha = 1$ and $\beta = 1$ exactly in Holt's linear method does not algebraically reduce to the random walk with drift in general. With $\alpha = 1$ the level equation becomes $\ell_t = y_t$ (correct), but with $\beta = 1$ the trend update becomes $b_t = \ell_t - \ell_{t-1} = y_t - y_{t-1}$, so the h-step forecast is $y_t + h(y_t - y_{t-1})$, not $y_t + h\hat{c}$ with $\hat{c}$ estimated over the full history. The claim as written is incorrect and will confuse students in Lecture 3.

---

### Issue 2: Missing verb — bullet item is a sentence fragment
- **Location:** Lines 80–81, slide "The Cost of Getting It Wrong"
- **Current:** `\item \textbf{UK NHS (2020):} Initial COVID hospitalization forecasts off by 4$\times$ ---`
- **Proposed:** `\item \textbf{UK NHS (2020):} Initial COVID hospitalization forecasts were off by 4$\times$ ---`
- **Category:** GRAMMAR
- **Severity:** CRITICAL

---

### Issue 3: Missing articles — "ML half of course"
- **Location:** Line 109, slide "What Makes Forecasting Hard?"
- **Current:** `(especially in ML half of course).`
- **Proposed:** `(especially in the ML half of the course).`
- **Category:** GRAMMAR
- **Severity:** MAJOR

---

### Issue 4: Missing article — "mean and variance may change"
- **Location:** Line 116, slide "What Makes Forecasting Hard?"
- **Current:** `Non-stationarity: mean and variance may change over time.`
- **Proposed:** `Non-stationarity: the mean and variance may change over time.`
- **Category:** GRAMMAR
- **Severity:** MAJOR

---

### Issue 5: Inconsistent forecast-sequence notation between slides
- **Location:** Line 555, slide "Point Forecast Accuracy Metrics"; contrast with line 635, slide "Visualizing the Train/Test Split"
- **Current (line 555):** `and forecasts $\{\hat{y}_{T+1|T}, \ldots, \hat{y}_{T+H|T+H-1}\}$`
- **Proposed:** Change to a fixed-origin sequence consistent with the train/test diagram: `and forecasts $\{\hat{y}_{T+1|T}, \ldots, \hat{y}_{T+H|T}\}$` — or, if rolling origin is intended, add `\muted{\small Rolling-origin, 1-step-ahead.}` and update the diagram accordingly.
- **Category:** CONSISTENCY
- **Severity:** MAJOR

Line 555 uses rolling-origin notation $\hat{y}_{T+H|T+H-1}$ (each forecast uses a progressively larger information set, implying 1-step-ahead rolling evaluation). The diagram on line 635 uses $\hat{y}_{T+H|T}$ (fixed forecast origin at $T$). These represent fundamentally different evaluation schemes and will confuse students.

---

### Issue 6: Overflow risk — dense footnote on already-full slide
- **Location:** Line 581, slide "Point Forecast Accuracy Metrics"
- **Current:** `\muted{\footnotesize \textbf{Metric choice:} RMSE/MAE for same-series; MAPE across series; MASE vs.\ seasonal na\"{i}ve. Prefer RMSE for costly outliers; MAE for robust comparison.}`
- **Proposed:** Remove this line and relocate its content to the MASE slide (line 642 onward) or a dedicated "Choosing a Metric" slide. The slide already has an intro paragraph, two columns with display equations, inline muted text under each column, and a `warningbox`.
- **Category:** OVERFLOW
- **Severity:** MAJOR

---

### Issue 7: Capitalization artifact — fragment after colon
- **Location:** Lines 82–83, slide "The Cost of Getting It Wrong"
- **Current:** `\item \textbf{Toys R Us (2017):} Systematically over-ordered inventory based on outdated demand forecasts --- contributed to bankruptcy.`
- **Proposed:** `\item \textbf{Toys R Us (2017):} systematically over-ordered inventory based on outdated demand forecasts, contributing to bankruptcy.`
- **Category:** GRAMMAR
- **Severity:** MAJOR

After the bold label and colon, "Systematically" is capitalized as if starting a new sentence, but it has no subject, making it a dangling fragment. Line 81 (UK NHS) correctly uses lowercase after its colon label.

---

### Issue 8: Informal language — "memorized the past"
- **Location:** Line 588, slide "The Evaluation Principle: Always Out-of-Sample"
- **Current:** `In-sample fit measures how well you memorized the past,`
- **Proposed:** `In-sample fit measures how well the model reproduces past observations,`
- **Category:** ACADEMIC QUALITY
- **Severity:** MINOR

"Memorized" is informal and colloquial. The second-person "you" is also inconsistent with the third-person voice used elsewhere.

---

### Issue 9: Inconsistent benchmark label in MASE slide
- **Location:** Line 650, slide "A Better Scale-Free Metric: MASE"
- **Current:** `\item $\text{MASE} > 1$: model is \emph{worse} than the na\"{i}ve benchmark`
- **Proposed:** `\item $\text{MASE} > 1$: model is \emph{worse} than the \emph{seasonal} na\"{i}ve benchmark`
- **Category:** CONSISTENCY
- **Severity:** MINOR

The denominator of MASE is defined two lines above as the in-sample MAE of the "seasonal na\"ive forecast." Dropping "seasonal" on line 650 is inconsistent and potentially misleading.

---

### Issue 10: Non-standard terminology — "expanding variance"
- **Location:** Line 372, slide "Stationarity: A First Look"
- **Current:** `\textbf{Rule of thumb:} Visible trend or expanding variance`
- **Proposed:** `\textbf{Rule of thumb:} Visible trend or growing variance (heteroscedasticity)`
- **Category:** ACADEMIC QUALITY
- **Severity:** MINOR

"Expanding variance" is not a standard technical term. Standard terms are "non-constant variance," "heteroscedasticity," or "variance growing with the level."

---

### Issue 11: Missing conjunction in parallel structure
- **Location:** Lines 84–85, slide "The Cost of Getting It Wrong"
- **Current:** `caused shelves to be overstocked on some items, empty on others`
- **Proposed:** `caused shelves to be overstocked on some items and empty on others`
- **Category:** GRAMMAR
- **Severity:** MINOR

---

### Issue 12: Author metadata may not match course department
- **Location:** Line 14
- **Current:** `\author{Department of Economics}`
- **Proposed:** Verify against official course catalog; update if course sits in a different unit (e.g., `Department of Economics and Finance` or `College of Business Administration`).
- **Category:** ACADEMIC QUALITY
- **Severity:** MINOR

The course is BSAD 8310 — a Business Administration designation — but the author field reads "Department of Economics."

---

### Issue 13: Forward reference to Lecture 6 for density forecasting
- **Location:** Line 277, slide "Types of Forecasts"
- **Current:** `Density forecasting is introduced in Lecture 6.`
- **Proposed:** Verify against `Lecture06_Evaluation.tex`; the `CLAUDE.md` course table describes Lecture 6 as covering RMSE/MAE/MAPE, DM test, and combinations — no density forecasting is listed.
- **Category:** CONSISTENCY
- **Severity:** MINOR

---

### Issue 14: Rhetorical teaser is borderline informal
- **Location:** Line 550, sectionslide for "Forecast Evaluation"
- **Current:** `Forecasting without evaluation is not science --- it is storytelling.`
- **Proposed:** No change required — acceptable as a motivational section opener. Flagged for instructor awareness only.
- **Category:** ACADEMIC QUALITY
- **Severity:** MINOR

---

## Structure Checks

| Check | Result |
|-------|--------|
| Every `\section{}` followed by `\sectionslide{}{}` | PASS |
| No slide has more than 2 colored boxes | PASS |
| No `\pause` or overlay commands | PASS |
| `\textcite` used for author-prominent citations | PASS |
| `\parencite` used for parenthetical citations | PASS |

---

## Summary Table

| # | Location | Issue | Category | Severity |
|---|----------|-------|----------|----------|
| 1 | Lines 527–528 | Holt's method claim mathematically wrong | MATH | CRITICAL |
| 2 | Lines 80–81 | "forecasts off by 4×" — missing verb | GRAMMAR | CRITICAL |
| 3 | Line 109 | Missing articles "the" twice | GRAMMAR | MAJOR |
| 4 | Line 116 | Missing article before "mean and variance" | GRAMMAR | MAJOR |
| 5 | Lines 555, 635 | Rolling vs. fixed-origin notation inconsistency | CONSISTENCY | MAJOR |
| 6 | Line 581 | Dense footnote on overloaded slide — overflow risk | OVERFLOW | MAJOR |
| 7 | Lines 82–83 | "Systematically" — capital letter creates fragment | GRAMMAR | MAJOR |
| 8 | Line 588 | "memorized the past" informal | ACADEMIC | MINOR |
| 9 | Line 650 | "naïve" should be "seasonal naïve" | CONSISTENCY | MINOR |
| 10 | Line 372 | "expanding variance" non-standard | ACADEMIC | MINOR |
| 11 | Lines 84–85 | Missing "and" in parallel structure | GRAMMAR | MINOR |
| 12 | Line 14 | Department name may not match course | ACADEMIC | MINOR |
| 13 | Line 277 | Lecture 6 reference for density forecasting unverified | CONSISTENCY | MINOR |
| 14 | Line 550 | Rhetorical teaser borderline informal | ACADEMIC | MINOR |
