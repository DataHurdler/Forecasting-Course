# Proofreading Report: Lecture02_Regression.tex
**File:** `Slides/Lecture02_Regression.tex`
**Date:** 2026-02-28
**Reviewer:** Proofreading agent

---

## Executive Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 1 |
| MAJOR    | 6 |
| MINOR    | 7 |
| **Total** | **14** |

The deck is largely clean on grammar and spelling. The single CRITICAL issue is a wrong chapter citation for Hamilton (1994). The most significant MAJOR issues are: (1) an undefined abbreviation (Durbin-Watson / DW) used in a formula before it has been introduced, (2) a missing distribution name in the AR(1) definition, (3) an incomplete stationarity condition discussion, and (4) two slides at high overflow risk. Seven MINOR issues cover stylistic grammar, notation-convention shifts, and missing citation for a standard result.

---

### Issue 1: Wrong chapter number in Hamilton (1994) citation
- **Location:** Line 136, slide "OLS Estimation"
- **Current:** `\parencite[][Ch.~10]{Hamilton1994}`
- **Proposed:** `\parencite[][Ch.~8]{Hamilton1994}`
- **Severity:** CRITICAL

**Explanation:** Chapter 10 of Hamilton (1994) covers Vector Autoregressions. The Gauss-Markov theorem and BLUE result are in Chapter 8. Pointing students to Chapter 10 for OLS/BLUE will send them to the wrong material.

---

### Issue 2: Durbin-Watson statistic referenced without definition
- **Location:** Line 557-558, slide "Pitfall 1: Spurious Regression"
- **Current:** `\textbf{Diagnostic heuristic:} $R^2 > DW$ statistic suggests spurious regression`
- **Proposed:** `\textbf{Diagnostic heuristic:} $R^2 > DW$ statistic (where $DW$ is the Durbin-Watson autocorrelation statistic) suggests spurious regression`
- **Severity:** MAJOR

**Explanation:** "DW" has not been defined in Lecture 01 or Lecture 02. The DW statistic is formally introduced only in Lecture 6. As written, the heuristic is uninterpretable to a first-time reader.

---

### Issue 3: Missing distribution identifier in AR(1) definition
- **Location:** Line 414, slide "The AR(1) Model"
- **Current:** `\varepsilon_t \stackrel{iid}{\sim}(0,\sigma^2)`
- **Proposed:** `\varepsilon_t \overset{iid}{\sim} WN(0,\sigma^2)` (consistent with line 111) or `\varepsilon_t \overset{iid}{\sim} \mathcal{N}(0,\sigma^2)` (consistent with line 371)
- **Severity:** MAJOR

**Explanation:** The notation is incomplete — the tilde must be followed by a distribution name. Every other place in the deck uses either `WN(0,\sigma^2)` or `\mathcal{N}(0,\sigma^2)`. The AR(1) definition is the only place where neither appears.

---

### Issue 4: Stationarity condition — explosive root case omitted
- **Location:** Lines 419-420, slide "The AR(1) Model"
- **Current:** `\textbf{Stationarity condition:} $|\phi_1| < 1$. If $\phi_1 = 1$, the model is a \emph{random walk} (non-stationary, covered in Lecture 4).`
- **Proposed:** `\textbf{Stationarity condition:} $|\phi_1| < 1$. If $\phi_1 = 1$, the model is a \emph{random walk}; if $|\phi_1| > 1$, it is \emph{explosive} — both are non-stationary (Lecture 4).`
- **Severity:** MAJOR

**Explanation:** The first sentence correctly states stationarity requires $|\phi_1| < 1$, which excludes both unit roots and explosive roots. The second sentence only mentions $\phi_1 = 1$, leaving the impression that only that case is problematic.

---

### Issue 5: Overflow risk — "From Point Forecast to Prediction Interval" slide
- **Location:** Lines 341-361
- **Current:** Single slide with nested `\underbrace` formula plus secondary formula for $\hat{\sigma}_e^2$ plus bullet points
- **Proposed:** Split into two slides (also recommended by pedagogy report, Pattern 7)
- **Severity:** MAJOR

**Explanation:** Nested `\underbrace` construction with subscript labels plus secondary formula plus bullets creates high overfull vbox risk in Beamer's 16:9 layout at 11pt.

---

### Issue 6: Overflow risk — "When Prediction Intervals Are Valid" slide
- **Location:** Lines 363-397
- **Current:** Two-column `enumerate` + `warningbox` (5 lines) + full-width `keybox` (2 sentences) + spacing commands
- **Proposed:** Move keybox content to a follow-on slide or reduce to one key sentence
- **Severity:** MAJOR

**Explanation:** Three substantial visual blocks on one 16:9 slide at 11pt is at high overflow risk.

---

### Issue 7: Awkward phrasing — "worse out-of-sample forecast"
- **Location:** Line 574
- **Current:** `More predictors $\Rightarrow$ better in-sample fit, but often worse out-of-sample forecast.`
- **Proposed:** `More predictors $\Rightarrow$ better in-sample fit, but often worse out-of-sample forecasting performance.`
- **Severity:** MINOR

---

### Issue 8: \textcite followed by colon — ungrammatical
- **Location:** Lines 543-546
- **Current:** `\textcite{GrangerNewbold1974}: Regressing two \emph{independent} random-walk series...`
- **Proposed:** `\textcite{GrangerNewbold1974} show that regressing two \emph{independent} random-walk series...`
- **Severity:** MINOR

---

### Issue 9: Missing citation for log-normal bias correction
- **Location:** Lines 320-321
- **Current:** `$\hat{y}_{T+h|T} = \exp\!\bigl(\hat{\beta}_0 + \hat{\beta}_1(T+h) + \tfrac{1}{2}\hat{\sigma}^2\bigr)$ \hfill\muted{\small (bias correction)}`
- **Proposed:** Add `\parencite[][Sec.~9.4]{Hyndman2021}` or equivalent
- **Severity:** MINOR

---

### Issue 10: Notation shift from lowercase t to uppercase T not explained
- **Location:** First occurrence at line 195; lecture-wide
- **Current:** Lecture uses `$\hat{y}_{T+h|T}$` throughout without explaining convention change from L01's `$\hat{y}_{t+h|t}$`
- **Proposed:** Add one-line note on first use (line 115 "General Setup" slide)
- **Severity:** MINOR

---

### Issue 11: AIC/BIC parameter count note is formulation-dependent
- **Location:** Lines 459-460
- **Current:** `$p+2$ parameters: $p$ AR coefs + intercept + $\sigma^2$.`
- **Proposed:** Add qualifier noting this follows Gaussian MLE convention; some implementations (statsmodels) do not count $\sigma^2$ in AIC penalty
- **Severity:** MINOR

---

### Issue 12: \section{Lecture 2: Key Takeaways} — non-parallel in TOC
- **Location:** Line 638
- **Current:** `\section{Lecture 2: Key Takeaways}`
- **Proposed:** `\section*{Key Takeaways}` or remove `\section` entirely (consistent with L01 which has no section for takeaways)
- **Severity:** MINOR

---

### Issue 13: \parencite mid-sentence (linked to Issue 1)
- **Location:** Line 136
- **Current:** `is the \key{Best Linear Unbiased Estimator} (BLUE) \parencite[][Ch.~10]{Hamilton1994}.`
- **Proposed:** Correct chapter (Ch.~8); citation placement is otherwise acceptable
- **Severity:** MINOR

---

### Issue 14: BoxJenkins2015 Ch. 5 borderline for BIC recommendation
- **Location:** Line 470
- **Current:** `\textbf{Use BIC} for forecasting in most business applications \parencite[][Ch.~5]{BoxJenkins2015}.`
- **Proposed:** Supplement with `\parencite{Hyndman2021}` which explicitly recommends AICc/BIC for lag selection
- **Severity:** MINOR

**Explanation:** Box-Jenkins (2015) Ch. 5 covers model identification via ACF/PACF. BIC was proposed by Schwarz (1978) and is not the primary recommendation of the Box-Jenkins framework. A more direct citation would better support the "Use BIC" claim.

---

## Summary Table

| # | Location | Issue | Severity |
|---|----------|-------|----------|
| 1 | Line 136 | Hamilton Ch.~10 cited for OLS/BLUE — should be Ch.~8 | CRITICAL |
| 2 | Line 557 | DW statistic used without definition | MAJOR |
| 3 | Line 414 | AR(1): distribution name missing after `\sim` | MAJOR |
| 4 | Lines 419-420 | Stationarity: explosive root case omitted | MAJOR |
| 5 | Lines 341-361 | Overflow risk: PI formula slide | MAJOR |
| 6 | Lines 363-397 | Overflow risk: PI validity slide | MAJOR |
| 7 | Line 574 | "worse out-of-sample forecast" — awkward phrasing | MINOR |
| 8 | Lines 543-546 | `\textcite` followed by colon | MINOR |
| 9 | Lines 320-321 | Log-normal bias correction: no citation | MINOR |
| 10 | Line 195+ | Notation shift t→T not explained | MINOR |
| 11 | Lines 459-460 | AIC/BIC parameter count formulation-dependent | MINOR |
| 12 | Line 638 | `\section{Lecture 2: Key Takeaways}` non-parallel | MINOR |
| 13 | Line 136 | `\parencite` citation style (linked to Issue 1) | MINOR |
| 14 | Line 470 | BoxJenkins2015 Ch. 5 borderline for BIC | MINOR |
