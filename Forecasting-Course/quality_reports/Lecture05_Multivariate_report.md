# Proofreading Report: Lecture05_Multivariate.tex
**File:** `Slides/Lecture05_Multivariate.tex`
**Reviewed against:** `Preambles/header.tex`, `Bibliography_base.bib`
**Date:** 2026-03-01
**Reviewer:** Proofreading agent

---

## Executive Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 0 |
| MAJOR    | 10 |
| MINOR    | 6 |
| **Total** | **16** |

The lecture is well-structured and mathematically sound. All four `\section{}` commands are followed by `\sectionslide{}{}` except the final one. Citation keys all resolve correctly except `EngleGranger1987` (missing from bib). The primary issues are: one missing `\sectionslide`; citations placed in frame/box title arguments (fragile hyperref interaction); `iid` not romanized in math mode; en-dash inconsistency in two compound names; a verb tense error; a missing primary citation for the Engle–Granger test; and a likely overflow on the Key Takeaways slide.

---

### Issue 1: Missing `\sectionslide` after final `\section`
- **Location:** Line 462, section "Key Takeaways and Roadmap"
- **Current:** `\section{Key Takeaways and Roadmap}` followed immediately by `\begin{frame}{Key Takeaways}`
- **Proposed:** Insert between them:
  ```latex
  \sectionslide{Key Takeaways and Roadmap}{%
    VAR, ARIMAX, cointegration, and ECM in one multivariate framework.}
  ```
- **Category:** STRUCTURE
- **Severity:** MAJOR

All four preceding sections (lines 32/35, 90/93, 243/246, 358/361) correctly follow the `\section`→`\sectionslide` pattern. Section 5 is the sole exception.

---

### Issue 2: `\parencite` in frame title argument
- **Location:** Line 151
- **Current:** `\begin{frame}{Granger Causality \parencite{Granger1969}}`
- **Proposed:** `\begin{frame}{Granger Causality}` — move citation to frame body, e.g., `\textcite{Granger1969} formalizes...` or as a `\muted{\footnotesize\parencite{Granger1969}}` in the body.
- **Category:** CONSISTENCY
- **Severity:** MAJOR

`\parencite` in a Beamer frame title triggers biblatex in the PDF bookmark context, producing hyperref warnings ("Token not allowed in a PDF string") and potentially corrupted bookmarks. All other lectures move citations to slide bodies.

---

### Issue 3: `\parencite` in `\definitionbox` title argument
- **Location:** Line 106
- **Current:** `\begin{definitionbox}{VAR($p$) Model \parencite{Sims1980}}`
- **Proposed:** `\begin{definitionbox}{VAR($p$) Model}` — add `\muted{\footnotesize\parencite{Sims1980}}` at end of box body.
- **Category:** CONSISTENCY
- **Severity:** MAJOR

Same fragility as Issue 2 — the `tcolorbox` title argument does not robustly handle biblatex commands. This is the established pattern for other lectures in the series.

---

### Issue 4: `iid` not romanized in math mode
- **Location:** Line 112
- **Current:** `\boldsymbol{\varepsilon}_t \overset{iid}{\sim}`
- **Proposed:** `\boldsymbol{\varepsilon}_t \overset{\mathrm{iid}}{\sim}`
- **Category:** MATH / CONSISTENCY
- **Severity:** MAJOR

In math mode `iid` renders as three italic variables $i$, $i$, $d$ — incorrect typesetting. Multi-letter abbreviations require `\mathrm{}`. Also noted in L03 (same pattern).

---

### Issue 5: Hyphen instead of en-dash in "Dickey-Fuller" (line 412)
- **Location:** Line 412
- **Current:** `Augmented Dickey-Fuller (ADF) on $\hat{e}_t$:`
- **Proposed:** `Augmented Dickey--Fuller (ADF) on $\hat{e}_t$:`
- **Category:** TYPO
- **Severity:** MAJOR

Compound proper names (two persons' surnames) take an en-dash (`--`), not a hyphen. Especially inconsistent because line 408 on the same slide correctly uses `Engle--Granger` with an en-dash.

---

### Issue 6: Hyphen instead of en-dash in "Diebold-Mariano" (line 504)
- **Location:** Line 504
- **Current:** `the Diebold-Mariano test \parencite{Diebold1995}`
- **Proposed:** `the Diebold--Mariano test \parencite{Diebold1995}`
- **Category:** TYPO
- **Severity:** MAJOR

Same rule as Issue 5.

---

### Issue 7: Verb tense inconsistency — "assumed" vs. present
- **Location:** Line 252
- **Current:** `Standard OLS forecasting (Lecture 2) assumed independent errors.`
- **Proposed:** `Standard OLS forecasting (Lecture 2) assumes independent errors.`
- **Category:** GRAMMAR
- **Severity:** MAJOR

The surrounding text and the rest of the slide use present tense. OLS still assumes independent errors as a model property; "assumed" implies the assumption was abandoned historically.

---

### Issue 8: Key Takeaways slide likely overflows
- **Location:** Lines 466–487
- **Current:** Single `keybox` with a 5-item enumerate (some items multi-clause, no `\small` applied), followed by a muted note below.
- **Proposed:** Options: (a) wrap enumerate in `{\small ...}`; (b) shorten items 2 and 4; (c) move muted note to a separate "What's Next" slide.
- **Category:** OVERFLOW
- **Severity:** MAJOR

At 11pt base font in a 16:9 frame with 0.5cm margins, five long items inside a colored `keybox` plus a trailing muted line will very likely exceed the usable height (~7.2cm).

---

### Issue 9: Engle–Granger test lacks primary citation
- **Location:** Line 408
- **Current:** `\textbf{Engle--Granger test} \parencite[][Ch.~19]{Hamilton1994}:`
- **Proposed:** Add the primary reference: `\textbf{Engle--Granger test} \parencite{EngleGranger1987}` (and add `EngleGranger1987` to `Bibliography_base.bib`). The Hamilton citation can remain as a secondary textbook reference.
- **Category:** ACADEMIC QUALITY
- **Severity:** MAJOR

The original paper is: Engle, R.F. and Granger, C.W.J. (1987), "Co-integration and Error Correction: Representation, Estimation, and Testing," *Econometrica*, 55(2), 251–276. Citing only Hamilton's textbook treatment implies the test originates there. `EngleGranger1987` does not currently exist in `Bibliography_base.bib`.

---

### Issue 10: En-dash inconsistency within same slide
- **Location:** Lines 408 and 412 (frame "Spurious Regression Revisited")
- **Current:** Line 408: `Engle--Granger` (correct); Line 412: `Dickey-Fuller` (hyphen)
- **Proposed:** Line 412: `Dickey--Fuller`
- **Category:** CONSISTENCY
- **Severity:** MAJOR

Internal inconsistency on the same slide is particularly visible. This overlaps with Issue 5 but is flagged separately for emphasis.

---

### Issue 11: `$^\dagger$` in text mode
- **Location:** Lines 339 and 347
- **Current:** `\textbf{IRF, FEVD$^\dagger$}` and `\muted{\footnotesize\itshape $^\dagger$FEVD = ...}`
- **Proposed:** `\textbf{IRF, FEVD\textsuperscript{\textdagger}}` and `\muted{\footnotesize\itshape \textsuperscript{\textdagger}FEVD = ...}`
- **Category:** TYPO
- **Severity:** MINOR

`$^\dagger$` forces math-mode italic in a text context. `\textsuperscript{\textdagger}` is the idiomatic text-mode form.

---

### Issue 12: Spurious Regression slide — minor overflow risk
- **Location:** Lines 366–421
- **Current:** Two TikZ figures (h=1.6cm each) in left column; right column has a `keybox` with a 3-step procedure using `\\[3pt]` spacing plus a muted paragraph.
- **Proposed:** Reduce `\\[3pt]` to `\\[1pt]` inside the keybox, or reduce the muted note to `\tiny`.
- **Category:** OVERFLOW
- **Severity:** MINOR

---

### Issue 13: Frame title — informal "When to Use Which"
- **Location:** Line 329
- **Current:** `\begin{frame}{VAR vs.\ ARIMAX: When to Use Which}`
- **Proposed:** `\begin{frame}{VAR vs.\ ARIMAX: When to Use Each}` (or "Choosing Between VAR and ARIMAX")
- **Category:** ACADEMIC QUALITY
- **Severity:** MINOR

"When to Use Which" is colloquial. "When to Use Each" or "Choosing Between..." matches the academic register of the rest of the lecture.

---

### Issue 14: `\begin{itemize}\small` — non-idiomatic placement
- **Location:** Lines 80, 130, 157, 266, 290, 316, 443
- **Current:** `\begin{itemize}\small`
- **Proposed:** Consistent pattern (either is acceptable — just pick one): `{\small \begin{itemize}...\end{itemize}}` or keep `\begin{itemize}\small` uniformly.
- **Category:** CONSISTENCY
- **Severity:** MINOR

Both forms work but mixing them (some frames use one, some the other) is inconsistent. The `\begin{itemize}\small` form is functional since `\small` is a declaration; normalize it across the file.

---

### Issue 15: BIC formula — `\kappa` introduced awkwardly
- **Location:** Lines 133–135
- **Current:** `\mathrm{BIC} = -2\hat{\ell} + \kappa\ln T, \quad \kappa = k^2p+k \text{ parameters}`
- **Proposed:** `\mathrm{BIC} = -2\hat{\ell} + \kappa\ln T, \quad \kappa = k^2 p + k \;\text{(free parameters)}`
- **Category:** MATH
- **Severity:** MINOR

The phrase `\kappa = k^2p+k \text{ parameters}` conflates a mathematical equation with a verbal label. Parenthesizing the label is cleaner. Also add spaces around `+` in source for readability.

---

### Issue 16: Source spacing in BIC formula
- **Location:** Line 135
- **Current:** `k^2p+k`
- **Proposed:** `k^2 p + k`
- **Category:** TYPO
- **Severity:** MINOR

LaTeX handles operator spacing in math mode automatically, but source readability benefits from explicit spaces around `+`.

---

## Summary Table

| # | Line | Issue | Category | Severity |
|---|------|-------|----------|----------|
| 1 | 462 | Missing `\sectionslide` for final section | STRUCTURE | MAJOR |
| 2 | 151 | `\parencite` in frame title (hyperref fragility) | CONSISTENCY | MAJOR |
| 3 | 106 | `\parencite` in `\definitionbox` title | CONSISTENCY | MAJOR |
| 4 | 112 | `iid` → `\mathrm{iid}` | MATH | MAJOR |
| 5 | 412 | `Dickey-Fuller` → `Dickey--Fuller` | TYPO | MAJOR |
| 6 | 504 | `Diebold-Mariano` → `Diebold--Mariano` | TYPO | MAJOR |
| 7 | 252 | "assumed" → "assumes" (tense) | GRAMMAR | MAJOR |
| 8 | 466–487 | Key Takeaways likely overflows | OVERFLOW | MAJOR |
| 9 | 408 | Engle–Granger missing primary citation | ACADEMIC | MAJOR |
| 10 | 408, 412 | En-dash inconsistency within same slide | CONSISTENCY | MAJOR |
| 11 | 339, 347 | `$^\dagger$` in text mode | TYPO | MINOR |
| 12 | 366–421 | Spurious Regression slide — minor overflow | OVERFLOW | MINOR |
| 13 | 329 | "When to Use Which" informal | ACADEMIC | MINOR |
| 14 | 80, 130, … | `\begin{itemize}\small` non-idiomatic | CONSISTENCY | MINOR |
| 15 | 133–135 | BIC formula `\kappa` definition awkward | MATH | MINOR |
| 16 | 135 | Source spacing in `k^2p+k` | TYPO | MINOR |

---

## Citation Verification

| Key | Status |
|-----|--------|
| `Sims1980` | FOUND |
| `Granger1969` | FOUND |
| `GrangerNewbold1974` | FOUND |
| `Hamilton1994` | FOUND |
| `Diebold1995` | FOUND |
| `EngleGranger1987` | **NOT IN BIB** — add for Issue 9 |

---

## Structure Audit

| Section | `\section` line | `\sectionslide` | Status |
|---------|----------------|-----------------|--------|
| 1: Beyond Univariate Forecasting | 32 | 35 | OK |
| 2: Vector Autoregression (VAR) | 90 | 93 | OK |
| 3: ARIMAX Models | 243 | 246 | OK |
| 4: Cointegration and Error Correction | 358 | 361 | OK |
| 5: Key Takeaways and Roadmap | 462 | **MISSING** | MAJOR |

## Box Usage Audit

No slide exceeds 2 colored boxes. All box types used appropriately per project conventions.
