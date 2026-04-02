# Proofreading Report: Lecture07_MLIntro.tex
**File:** `Slides/Lecture07_MLIntro.tex`
**Lecture:** BSAD 8310 Lecture 07 — Machine Learning Introduction
**Reviewer:** Proofreading Agent
**Date:** 2026-02-28

---

## Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 4 |
| MAJOR    | 7 |
| MINOR    | 6 |
| **Total**| **17** |

---

### Issue 1: Undefined citation key `Zou2005`
- **Location:** Line 568, frame "Ridge, LASSO, and Elastic Net"
- **Current:** `\textbf{EN \parencite{Zou2005}:}`
- **Proposed:** `\textbf{EN \parencite{ZouHastie2005}:}`
- **Severity:** CRITICAL

The bibliography key for the Zou and Hastie (2005) Elastic Net paper is `ZouHastie2005` (see `Bibliography_base.bib`), not `Zou2005`. The current key is undefined and will produce a "[?]" citation.

---

### Issue 2: Frame title "Three Gaps ML Fills" but the table lists four gaps
- **Location:** Lines 67--93, frame "Three Gaps ML Fills"
- **Current:** Title `{Three Gaps ML Fills}` with table containing four rows: Non-linearity, Many predictors, Interactions, Non-Gaussian.
- **Proposed:** Change to `{Four Gaps ML Fills}` (or remove one row, or relabel as "Key Gaps ML Fills")
- **Severity:** CRITICAL

The frame title explicitly states "Three Gaps" but the table body lists four distinct gaps. Students counting from the title will be confused.

---

### Issue 3: M4 Competition sMAPE values inaccurate — Theta shown tied with ES-RNN
- **Location:** Lines 107--111, frame "Evidence: The M4 Competition"
- **Current:**
  ```
  Hybrid ES-RNN (ML + ETS)  & 1  & 11.37 \\
  Theta (classical)         & 2  & 11.37 \\
  FFORMA (ML ensemble)      & 3  & 11.57 \\
  ```
- **Proposed:**
  ```
  Hybrid ES-RNN (ML + ETS)  & 1  & 11.374 \\
  Theta (classical)         & 2  & 11.551 \\
  FFORMA (ML ensemble)      & 3  & 11.720 \\
  ```
- **Severity:** CRITICAL

Makridakis, Spiliotis, and Assimakopoulos (2020, Table 1, overall sMAPE): ES-RNN = 11.374, Theta = 11.551, FFORMA = 11.720. All three values in the slide are incorrect. The tie between ranks 1 and 2 is a notable factual error — Theta did not tie with the winning hybrid method.

---

### Issue 4: `James2021` bibliography entry mixes Python subtitle with 2021 R edition year
- **Location:** `Bibliography_base.bib`, entry `James2021`
- **Current:** `title = {An Introduction to Statistical Learning with Applications in {Python}}, edition = {2nd}, year = {2021}`
- **Proposed:** `title = {An Introduction to Statistical Learning with Applications in {Python}}, edition = {1st}, year = {2023}` (for the Python edition)
- **Severity:** CRITICAL

ISL with Applications in R (ISLR2) was published as 2nd edition in 2021. ISL with Applications in Python (ISLP) was published as 1st edition in 2023. The bib entry combines the 2021 year/2nd edition (identifying the R version) with the Python subtitle — this combination matches no real publication. Since the course uses Python, the intended reference is ISLP (2023, 1st ed.).

---

### Issue 5: `p > T` uses VAR lag-order notation for number of predictors — clashes with L05
- **Location:** Line 76, frame "Three/Four Gaps ML Fills", "Many predictors" row
- **Current:** `Many predictors & VAR fails ($p>T$) & Regularization \\`
- **Proposed:** `Many predictors & OLS collapses ($k \gg T$) & Regularization \\`
- **Severity:** MAJOR

In Lecture 5, $p$ denotes the VAR lag order. Using $p > T$ here implies the lag order exceeds sample size — a different pathology from having too many predictor variables. The correct statement is that parameter count ($k$) exceeds observations ($T$).

---

### Issue 6: `\operatorname{Var}` instead of `\Var` macro in keybox (line 794)
- **Location:** Line 794, Key Takeaways keybox
- **Current:** `$\MSE = \operatorname{Bias}^2 + \operatorname{Var} + \sigma^2$`
- **Proposed:** `$\MSE = \operatorname{Bias}^2 + \Var + \sigma^2$`
- **Severity:** MAJOR

`header.tex` defines `\Var` as `\operatorname{Var}`. The definitionbox on lines 141--145 correctly uses `\Var[\hat{f}(x_0)]`. The keybox summary reverts to the verbose form, inconsistently typesetting the same formula.

---

### Issue 7: Claim that $\sigma^2$ can be reduced by "better data" is incorrect
- **Location:** Lines 154--156, frame "MSE Decomposition"
- **Current:** `\item \textbf{$\sigma^2$}: irreducible --- better models cannot reduce this, only better data can`
- **Proposed:** `\item \textbf{$\sigma^2$}: irreducible --- determined solely by the data-generating process; neither better models nor additional observations can eliminate it`
- **Severity:** MAJOR

$\sigma^2 = \Var[\varepsilon]$ is the variance of the DGP noise. It cannot be reduced by collecting more observations. "Only better data can" implies that gathering more data reduces $\sigma^2$, which is false and contradicts the meaning of "irreducible."

---

### Issue 8: `\hat{\beta}` instead of `\bhat` macro (line 561)
- **Location:** Line 561, frame "Ridge, LASSO, and Elastic Net"
- **Current:** `\hat{\beta} = \arg\min_\beta`
- **Proposed:** `\bhat = \arg\min_\beta`
- **Severity:** MAJOR

`header.tex` defines `\bhat` as `\hat{\beta}`. Using the raw construct instead of the macro is inconsistent with all other lectures.

---

### Issue 9: Test RMSE ($1{,}620$) substantially below CV RMSE ($1{,}780$) without explanation
- **Location:** Lines 537--544, examplebox "LASSO on RSXFS"
- **Current:** `CV RMSE $= 1{,}780$ (optimal) ... Test RMSE with $\lambda^* = 0.1$: $1{,}620$.`
- **Proposed:** Adjust test RMSE to be close to or slightly above CV RMSE (e.g., $1{,}810$), or add explanation.
- **Severity:** MAJOR

Test RMSE ~9% below CV RMSE contradicts the pedagogical narrative that CV is an honest generalization estimator. Students will rightly question this discrepancy. Refitting on the full train+val set typically yields performance close to (or slightly better than) CV RMSE, not 9% lower without explanation.

---

### Issue 10: "modelling" — British spelling; should be "modeling"
- **Location:** Line 131, `\sectionslide` subtitle
- **Current:** `Every modelling decision shifts error between bias and variance.`
- **Proposed:** `Every modeling decision shifts error between bias and variance.`
- **Severity:** MAJOR

Course is at University of Nebraska at Omaha (US institution). American English convention is "modeling" (single l). All other lectures use "modeling."

---

### Issue 11: "minimising" — British spelling; should be "minimizing"
- **Location:** Line 529, frame "CV in Practice: Hyperparameter Tuning"
- **Current:** `\item Select $\lambda^*$ minimising mean CV RMSE`
- **Proposed:** `\item Select $\lambda^*$ minimizing mean CV RMSE`
- **Severity:** MAJOR

Same as Issue 10. American English required throughout.

---

### Issue 12: `\parencite` inside `definitionbox` title (line 136) — fragile
- **Location:** Line 136
- **Current:** `\begin{definitionbox}{Bias-Variance Decomposition \parencite{Hastie2009}}`
- **Proposed:** Move to body: `\begin{definitionbox}{Bias-Variance Decomposition}` with `\muted{\footnotesize\parencite{Hastie2009}}` inside the box.
- **Severity:** MINOR

Embedding `\parencite` in tcolorbox title arguments can cause hyperref/font-size issues. Course convention (L01--L06) is to place citations in body or as muted footnotes.

---

### Issue 13: "$k$-fold" vs "$k$-Fold" capitalization inconsistency
- **Location:** Lines 406 and 409
- **Current:** Subtitle: `$k$-fold CV` / Frame title: `$k$-Fold CV`
- **Proposed:** Standardize to lowercase `$k$-fold CV` throughout
- **Severity:** MINOR

Two adjacent lines use different capitalization for the same term.

---

### Issue 14: Second `\parencite` inside `definitionbox` title (line 558)
- **Location:** Line 558
- **Current:** `\begin{definitionbox}{Penalized Regression \parencite{Hastie2009}}`
- **Proposed:** Move citation to box body
- **Severity:** MINOR

Same fragility as Issue 12.

---

### Issue 15: No `\label` on section declarations
- **Location:** Lines 32, 127, 282, 401, 548, 652
- **Proposed:** Add `\label{sec:why-ml}`, `\label{sec:bias-variance}`, etc. after each `\section{}`.
- **Severity:** MINOR

Forces hardcoded references if cross-referencing. Same pattern as L06 proofreading Issue 12.

---

### Issue 16: "Now we stress-test" — informal register, tense mismatch
- **Location:** Line 41
- **Current:** `Six lectures built a powerful toolkit. Now we stress-test its assumptions.`
- **Proposed:** `Six lectures have built a powerful toolkit. This lecture examines where its assumptions break down.`
- **Severity:** MINOR

"Now we stress-test" is informal. Tense mismatch (past "built" / present "stress-test"). Academic register required.

---

## Summary Table

| # | Location | Issue | Severity |
|---|----------|-------|----------|
| 1 | Line 568 | Citation key `Zou2005` undefined; should be `ZouHastie2005` | CRITICAL |
| 2 | Lines 67--93 | "Three Gaps" title but four gaps listed | CRITICAL |
| 3 | Lines 107--111 | M4 sMAPE values wrong; Theta shown tied with ES-RNN | CRITICAL |
| 4 | Bib `James2021` | Python subtitle but 2021/2nd matches R edition; Python ed. is 2023/1st | CRITICAL |
| 5 | Line 76 | `p > T` clashes with L05 VAR lag-order notation | MAJOR |
| 6 | Line 794 | `\operatorname{Var}` should be `\Var` macro | MAJOR |
| 7 | Lines 154--156 | $\sigma^2$ "reducible by better data" is incorrect | MAJOR |
| 8 | Line 561 | `\hat{\beta}` should use `\bhat` macro | MAJOR |
| 9 | Lines 537--544 | Test RMSE 9% below CV RMSE without explanation | MAJOR |
| 10 | Line 131 | "modelling" → "modeling" (British → American) | MAJOR |
| 11 | Line 529 | "minimising" → "minimizing" (British → American) | MAJOR |
| 12 | Line 136 | `\parencite` inside `definitionbox` title — fragile | MINOR |
| 13 | Lines 406, 409 | "$k$-fold" vs "$k$-Fold" capitalization inconsistent | MINOR |
| 14 | Line 558 | Second `\parencite` inside `definitionbox` title | MINOR |
| 15 | Lines 32, 127, 282, 401, 548, 652 | No `\label` on `\section` declarations | MINOR |
| 16 | Line 41 | "Now we stress-test" — informal register, tense mismatch | MINOR |
