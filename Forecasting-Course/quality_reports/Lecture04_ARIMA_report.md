# Proofreading Report: Lecture04_ARIMA.tex
**File:** `Slides/Lecture04_ARIMA.tex`
**Reviewed against:** `Preambles/header.tex`, `Bibliography_base.bib`
**Date:** 2026-03-01
**Reviewer:** Proofreading agent

---

## Summary

| Category | Critical | Major | Minor | Total |
|----------|----------|-------|-------|-------|
| STRUCTURE | 1 | 0 | 0 | 1 |
| GRAMMAR | 0 | 1 | 1 | 2 |
| TYPO | 0 | 0 | 1 | 1 |
| OVERFLOW | 0 | 1 | 1 | 2 |
| CONSISTENCY | 0 | 1 | 2 | 3 |
| ACADEMIC | 0 | 1 | 2 | 3 |
| MATH | 0 | 0 | 1 | 1 |
| **TOTAL** | **1** | **4** | **8** | **13** |

---

### Issue 1: Missing `\sectionslide` for Section 6 — CRITICAL
- **Location:** Line 526–530, section "Key Takeaways and Roadmap"
- **Current:** `\section{Key Takeaways and Roadmap}` followed immediately by `\begin{frame}{Key Takeaways}` with no intervening `\sectionslide`
- **Proposed:**
  ```latex
  \sectionslide{Key Takeaways and Roadmap}{%
    Stationarity, unit roots, ACF/PACF, ARIMA, and SARIMA in one framework.}
  ```
- **Category:** STRUCTURE
- **Severity:** CRITICAL

All five other sections (lines 32/35, 104/107, 220/223, 329/333, 458/461) correctly follow the `\section`→`\sectionslide` pattern. Section 6 is the sole exception.

---

### Issue 2: Incomplete null hypothesis statement
- **Location:** Line 432, Box-Jenkins slide
- **Current:** `Ljung-Box $H_0$: white noise`
- **Proposed:** `Ljung-Box $H_0$: residuals are white noise`
- **Category:** GRAMMAR
- **Severity:** MAJOR

The null hypothesis statement is missing subject and verb. All other $H_0$ statements in the file include a grammatically complete predicate.

---

### Issue 3: `\parencite` in frame title — inconsistent with established pattern
- **Location:** Line 405
- **Current:** `\begin{frame}{Box-Jenkins Methodology \parencite{BoxJenkins2015}}`
- **Proposed:** `\begin{frame}{Box-Jenkins Methodology \textcite{BoxJenkins2015}}`
- **Category:** CONSISTENCY
- **Severity:** MAJOR

`\parencite` renders as "(Box et al., 2015)" giving "Box-Jenkins Methodology (Box et al., 2015)" in the title bar. `\textcite` renders as "Box et al. (2015)" which reads as a natural attribution. The file already uses `\textcite` correctly for in-text attribution at line 148. Other lectures follow the same pattern.

---

### Issue 4: SARIMA slide likely to overflow
- **Location:** Lines 466–470
- **Current:** Five lines of dense prose including two inline polynomial definitions (`$\phi_p(B)$`, `$\theta_q(B)$`) before a `definitionbox` containing the full 7-term SARIMA equation plus a two-column layout with an examplebox.
- **Proposed:** Reduce the preamble to one introductory sentence; move the polynomial definitions inside the `definitionbox`:
  ```latex
  Monthly retail data exhibit autocorrelation at lags $m, 2m, 3m, \ldots$
  beyond standard ARIMA. SARIMA extends the model with seasonal polynomials:
  ```
- **Category:** OVERFLOW
- **Severity:** MAJOR

---

### Issue 5: Informal first-person register
- **Location:** Line 554
- **Current:** `We now have four model families in our toolkit:`
- **Proposed:** `Four model families are now available in the forecasting toolkit:`
- **Category:** GRAMMAR
- **Severity:** MINOR

The lecture consistently uses third-person or impersonal constructions. "We/our" is informal and inconsistent.

---

### Issue 6: Potential overfull hbox in KPSS slide opening line
- **Location:** Line 193
- **Current:** `The ADF and KPSS (Kwiatkowski--Phillips--Schmidt--Shin) tests address \emph{opposite} null hypotheses:`
- **Proposed:** Move the full name to a muted parenthetical in the body:
  ```latex
  \begin{frame}{Complementary Test: KPSS}
    The ADF and KPSS tests address \emph{opposite} null hypotheses.
    \muted{\footnotesize (KPSS: Kwiatkowski--Phillips--Schmidt--Shin)}
  ```
- **Category:** OVERFLOW
- **Severity:** MINOR

The 85-character sentence with an em-dash-separated compound proper name is a candidate for overfull hbox at standard frame margins.

---

### Issue 7: Inconsistent `\small` usage inside colored boxes
- **Location:** Lines 128–132 vs. 142–149
- **Current:** `warningbox` on lines 128–132 has no font-size modifier; the immediately following `definitionbox` wraps content in `{\small ...}`
- **Proposed:** Add `{\small ...}` inside the `warningbox` for visual consistency.
- **Category:** CONSISTENCY
- **Severity:** MINOR

---

### Issue 8: Missing `\small` in Weak Stationarity itemize
- **Location:** Lines 51–55
- **Current:** `\begin{itemize}` with no `\small`
- **Proposed:** `\begin{itemize}\small`
- **Category:** CONSISTENCY
- **Severity:** MINOR

All other `itemize` blocks in the file (lines 208, 273, 386, 507, 533) use `\begin{itemize}\small`.

---

### Issue 9: "signals" should be "suggests" for hypothesis test language
- **Location:** Line 433
- **Current:** `$p$-value $<0.05$ signals residual autocorrelation --- re-identify`
- **Proposed:** `$p$-value $<0.05$ suggests residual autocorrelation --- re-identify`
- **Category:** ACADEMIC
- **Severity:** MINOR

"Signals" implies a firm cutoff rule. "Suggests" is standard hypothesis-test phrasing and consistent with other evidence statements in the file (e.g., line 209: "evidence of unit root").

---

### Issue 10: Missing citation in SARIMA examplebox
- **Location:** Lines 496–499
- **Current:** `SARIMA(1,1,1)(0,1,1)[12] is a common starting point for monthly retail series` — no citation
- **Proposed:** Add `\parencite[][Ch.~9]{Hyndman2021}` to support the claim. The Hyndman2021 reference is already used on line 396.
- **Category:** ACADEMIC
- **Severity:** MINOR

---

### Issue 11: Box-Jenkins body text covers only Steps 1 and 3 of 4
- **Location:** Lines 429–433
- **Current:** Only Steps 1 (Identify) and 3 (Diagnose) are commented on in the body text below the TikZ diagram.
- **Proposed:** Add brief text for Steps 2 and 4, or add an explicit note that they are covered elsewhere:
  ```
  Step 2 (Estimate): maximize conditional or exact likelihood
  Step 4 (Forecast): covered on the following slide
  ```
- **Category:** ACADEMIC
- **Severity:** MINOR

---

### Issue 12: `na\"{i}ve` encoding — XeLaTeX best practice
- **Location:** Lines 130, 556
- **Current:** `na\"{i}ve`
- **Proposed:** With XeLaTeX (UTF-8 source), `naïve` (direct Unicode) is cleaner. Both occurrences are internally consistent. Low priority.
- **Category:** TYPO
- **Severity:** MINOR

---

### Issue 13: "interval width" vs. "half-width" imprecision
- **Location:** Line 448
- **Current:** `prediction interval width scales as $\sigma\sqrt{h}$ for ARIMA(0,1,0).`
- **Proposed:** `prediction interval half-width scales as $\sigma\sqrt{h}$ for ARIMA(0,1,0).`
- **Category:** MATH
- **Severity:** MINOR

Total interval width is $2\sigma\sqrt{h} \cdot z_{\alpha/2}$. The half-width (point forecast to bound) scales as $\sigma\sqrt{h}$.

---

## Structure Audit

| Section | `\section` line | `\sectionslide` | Status |
|---------|----------------|-----------------|--------|
| 1: Stationarity | 32 | 35 | OK |
| 2: Unit Roots and Differencing | 104 | 107 | OK |
| 3: ACF and PACF | 220 | 223 | OK |
| 4: The ARIMA Model | 329 | 333 | OK |
| 5: Seasonal ARIMA | 458 | 461 | OK |
| 6: Key Takeaways and Roadmap | 526 | **MISSING** | **CRITICAL** |

## Citation Verification

| Key | Status |
|-----|--------|
| `DickeyFuller1979` | Correct |
| `Kwiatkowski1992` | Correct |
| `Hyndman2021` | Correct |
| `BoxJenkins2015` | Correct |

No undefined citation keys.

## Box Usage Audit

No slide exceeds 2 colored boxes. No box fatigue issues.
