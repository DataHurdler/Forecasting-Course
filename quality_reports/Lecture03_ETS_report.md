# Proofreading Report: Lecture03_ETS.tex
**File:** `Slides/Lecture03_ETS.tex`
**Date:** 2026-03-01
**Reviewer:** Proofreading agent

---

## Executive Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 0 |
| MAJOR    | 4 |
| MINOR    | 10 |
| LOW      | 1 |
| **Total** | **15** |

The deck has consistent `\sectionslide` usage for five of its six sections but is missing one for the final "Key Takeaways" section. The most significant issues are: a notation collision between `\hat{\ell}` (used for log-likelihood) and `\ell_t` (used for level state throughout); a factually incorrect cross-reference describing SES as having an "AR(1) error-correction structure" (it is ARIMA(0,1,1)); three British–American spelling inconsistencies; and a likely overflow risk on the Key Takeaways slide.

---

### Issue 1: Missing `\sectionslide` after final `\section`
- **Location:** Line 474, section "Key Takeaways and Roadmap"
- **Current:** `\section{Key Takeaways and Roadmap}` followed immediately by `\begin{frame}{Key Takeaways}` with no intervening `\sectionslide`
- **Proposed:** Insert `\sectionslide{Key Takeaways and Roadmap}{Synthesis and what comes next.}` between the section declaration and the first frame.
- **Category:** STRUCTURE
- **Severity:** MAJOR

---

### Issue 2: Notation collision — `\hat{\ell}` for log-likelihood conflicts with `\ell_t` for level
- **Location:** Line 449, AIC/model-selection slide
- **Current:** `\hat{\ell} = \text{maximized log-likelihood}`
- **Proposed:** `\hat{L} = \text{maximized log-likelihood}` (or `\ell^*`), reserving `\ell` exclusively for the level state used throughout (lines 94, 102, 203, 296, etc.)
- **Category:** MATH / CONSISTENCY
- **Severity:** MAJOR

---

### Issue 3: Incorrect cross-reference — SES is ARIMA(0,1,1), not AR(1)
- **Location:** Line 118, slide "Simple Exponential Smoothing: Error-Correction Form"
- **Current:** `(Recall from Lecture 2: SES shares the AR(1) error-correction structure, but requires no stationarity.)`
- **Proposed:** `(Recall from Lecture 2: SES is equivalent to an ARIMA(0,1,1) model --- the error-correction form mirrors IMA(1,1) updating, but requires no stationarity assumption.)`
- **Category:** ACADEMIC QUALITY / MATH
- **Severity:** MAJOR

SES is mathematically equivalent to ARIMA(0,1,1)/IMA(1,1), not AR(1). The error-correction form `ell_t = ell_{t-1} + alpha * e_t` resembles MA(1) updating on a differenced series. Students will be confused when they reach Lecture 4 on ARIMA.

---

### Issue 4: Overflow risk — Key Takeaways slide
- **Location:** Lines 478–499, slide "Key Takeaways"
- **Current:** A single `keybox` containing `\begin{enumerate}` with 5 items (some multi-line) inside `{\small ...}`, followed by a `\muted` footnote below the box, with no vertical spacing compression.
- **Proposed:** Split into two slides, or reduce to 4 items by merging items 4 and 5, or add `\vspace{-0.2cm}` before the `keybox` and `\setlength\itemsep{1pt}` inside the enumerate.
- **Category:** OVERFLOW
- **Severity:** MAJOR

---

### Issue 5: British spelling — `minimise`
- **Location:** Line 143
- **Current:** `choose $\alpha$ and $\ell_0$ to minimise`
- **Proposed:** `choose $\alpha$ and $\ell_0$ to minimize`
- **Category:** CONSISTENCY
- **Severity:** MINOR

Conflicts with American `minimize` at line 351.

---

### Issue 6: British spelling — `optimisation`
- **Location:** Line 149
- **Current:** `Solved numerically (bounded nonlinear optimisation).`
- **Proposed:** `Solved numerically (bounded nonlinear optimization).`
- **Category:** CONSISTENCY
- **Severity:** MINOR

---

### Issue 7: British spelling — `initialise`
- **Location:** Line 354
- **Current:** `Holt-Winters requires at least $\mathbf{2m}$ observations to initialise.`
- **Proposed:** `Holt-Winters requires at least $\mathbf{2m}$ observations to initialize.`
- **Category:** CONSISTENCY
- **Severity:** MINOR

Conflicts with American `initialization` at lines 97 and 344.

---

### Issue 8: `\pos` (green) inside `keybox` (blue background) — contrast failure
- **Location:** Lines 77–78
- **Current:** `\pos{$\alpha \approx 1$}: almost all weight on the latest value.`
- **Proposed:** Use `\textbf{$\alpha \approx 1$}` inside the keybox, or remove `\pos{...}` wrapper. As defined in `header.tex`, `\pos` applies `unogreen` color — on a `colback=unoblue` background, green-on-blue has poor contrast.
- **Category:** ACADEMIC QUALITY
- **Severity:** MINOR

---

### Issue 9: Missing period at end of sentence
- **Location:** Line 445
- **Current:** `Fit all 15 valid ETS models; select by minimum AIC`
- **Proposed:** `Fit all 15 valid ETS models; select by minimum AIC.`
- **Category:** TYPO
- **Severity:** MINOR

---

### Issue 10: `\beta^* = 0` violates stated parameter constraint
- **Location:** Line 227
- **Current:** `SES is nested inside Holt: set $\beta^* = 0$ and $b_0 = 0$.`
- **Proposed:** `SES is nested inside Holt: take $\beta^* \to 0$ and $b_0 = 0$ (so $b_t = 0$ for all $t$).`
- **Category:** MATH
- **Severity:** MINOR

Line 206 states the constraint as `0 < \beta^* \leq 1` (strict lower bound). Setting `\beta^* = 0` exactly violates this constraint; the limit `\beta^* \to 0` is more precise.

---

### Issue 11: `iid` should be upright (roman) in math mode
- **Location:** Line 410
- **Current:** `\varepsilon_t \overset{iid}{\sim} \mathcal{N}(0,\sigma^2)`
- **Proposed:** `\varepsilon_t \overset{\mathrm{iid}}{\sim} \mathcal{N}(0,\sigma^2)`
- **Category:** CONSISTENCY
- **Severity:** MINOR

`iid` in math mode renders italic; the correct standard for abbreviations is `\mathrm{iid}`.

---

### Issue 12: Gaussian assumption stated for "every ETS model" but applies only to additive-error models
- **Location:** Lines 407–410
- **Current:** `Every ETS model can be written as a \textbf{state space model}: [...]  \varepsilon_t \overset{iid}{\sim} \mathcal{N}(0,\sigma^2)`
- **Proposed:** Add "(additive-error form shown)" qualifier: `Every ETS model can be written as a \textbf{state space model} (additive-error form shown):`
- **Category:** ACADEMIC QUALITY
- **Severity:** MINOR

For multiplicative-error models (E=M), `varepsilon_t` represents a relative error, not a Gaussian additive error. The muted note later clarifies this, but the opening sentence is still misleading.

---

### Issue 13: Citation format — confirmed correct
- **Location:** Lines 371, 144, 236, 289, 446, 466
- **Current:** Mix of `\textcite{...}` (line 371, author as sentence subject) and `\parencite{...}` (remaining, parenthetical)
- **Proposed:** No change needed — usage is correct per project convention.
- **Category:** CONSISTENCY
- **Severity:** LOW (flagged for confirmation only)

---

### Issue 14: "One parameter" understates SES complexity
- **Location:** Line 485
- **Current:** `\textbf{SES}: one parameter, flat forecast ---`
- **Proposed:** `\textbf{SES}: one smoothing parameter ($\alpha$), flat forecast ---`
- **Category:** ACADEMIC QUALITY
- **Severity:** MINOR

SES has two estimated quantities: smoothing parameter `alpha` and initial level `ell_0`. "One parameter" may confuse students who recall the optimization (line 146) minimized over both.

---

### Issue 15: Seasonal-index notation only valid for `h ≤ m`
- **Location:** Lines 314, 319
- **Current:** `s_{T+h-m}` in Holt-Winters forecast equations
- **Proposed:** Add a muted note: `\muted{\footnotesize\itshape For $h > m$, the seasonal index cycles with period $m$.}`
- **Category:** MATH
- **Severity:** MINOR

`s_{T+h-m}` is the standard shorthand but is only strictly correct for `h <= m`. For multi-step forecasts with `h > m`, students need to understand the index cycles. No clarifying note is present.

---

## Structure Checks

| Check | Result |
|-------|--------|
| Every `\section{}` followed by `\sectionslide{}{}` | **FAIL** — Section 6 "Key Takeaways and Roadmap" missing sectionslide |
| No slide has more than 2 colored boxes | PASS |
| No `\pause` or overlay commands | PASS |
| `\textcite` for author-prominent citations | PASS |
| `\parencite` for parenthetical citations | PASS |
| American spelling consistent | **FAIL** — 3 British spellings (Issues 5–7) |

---

## Summary Table

| # | Line | Issue | Category | Severity |
|---|------|-------|----------|----------|
| 1 | 474 | Missing `\sectionslide` for "Key Takeaways and Roadmap" | STRUCTURE | MAJOR |
| 2 | 449 | `\hat{\ell}` notation collision (level vs. log-likelihood) | MATH | MAJOR |
| 3 | 118 | SES described as AR(1) — should be ARIMA(0,1,1) | ACADEMIC/MATH | MAJOR |
| 4 | 478–499 | Key Takeaways slide likely overflows | OVERFLOW | MAJOR |
| 5 | 143 | `minimise` → `minimize` | CONSISTENCY | MINOR |
| 6 | 149 | `optimisation` → `optimization` | CONSISTENCY | MINOR |
| 7 | 354 | `initialise` → `initialize` | CONSISTENCY | MINOR |
| 8 | 77–78 | `\pos` (green) inside `keybox` (blue) — poor contrast | ACADEMIC | MINOR |
| 9 | 445 | Missing period after "AIC" | TYPO | MINOR |
| 10 | 227 | `\beta^* = 0` violates stated strict constraint | MATH | MINOR |
| 11 | 410 | `iid` → `\mathrm{iid}` | CONSISTENCY | MINOR |
| 12 | 407–410 | Gaussian stated for "every ETS" but applies only to E=A | ACADEMIC | MINOR |
| 13 | 371, 144 | `\textcite`/`\parencite` mix — confirmed correct | CONSISTENCY | LOW |
| 14 | 485 | "one parameter" understates SES | ACADEMIC | MINOR |
| 15 | 314, 319 | `s_{T+h-m}` only valid for `h ≤ m` — no clarifying note | MATH | MINOR |
