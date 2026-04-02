# Proofreading Report: Lecture09_Trees.tex

**File:** `Slides/Lecture09_Trees.tex`
**Reviewer:** Proofreading Agent
**Date:** 2026-02-28

---

## Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 2 |
| MAJOR    | 6 |
| MINOR    | 4 |
| **Total**| **12** |

---

### Issue 1: `\parencite` inside `definitionbox` title — fragile placement
- **Location:** Line 229, frame "Bagging: Bootstrap Aggregating"
- **Current:** `\begin{definitionbox}{Bagging \parencite{Breiman1996}}`
- **Proposed:** `\begin{definitionbox}{Bagging}` with `\muted{\footnotesize\parencite{Breiman1996}}` at end of box body
- **Severity:** CRITICAL

`\parencite` in tcolorbox title argument is fragile (biblatex/hyperref interaction). Same pattern flagged as Issues 12 and 14 in the L07 proofreading report. Citation key `Breiman1996` itself is correct.

---

### Issue 2: `\mathrm{Var}` instead of `\Var` macro
- **Location:** Line 238, frame "Bagging: Bootstrap Aggregating"
- **Current:** `\mathrm{Var}(\bar{f}) = \rho\sigma^2 + \frac{1-\rho}{B}\sigma^2`
- **Proposed:** `\Var(\bar{f}) = \rho\sigma^2 + \frac{1-\rho}{B}\sigma^2`
- **Severity:** CRITICAL

`header.tex` defines `\Var` as `\operatorname{Var}`. `\mathrm{Var}` bypasses correct operator spacing and breaks cross-lecture notation consistency. Flagged as Issue 6 (MAJOR) in L07; elevated to CRITICAL here as it's a recurring pattern.

---

### Issue 3: "piecewise constants" — wrong inflection
- **Location:** Line 39, frame "Motivation: Beyond Linear Models"
- **Current:** `predictions are piecewise constants over feature regions`
- **Proposed:** `predictions are piecewise constant over feature regions`
- **Severity:** MAJOR

"Piecewise constant" is an adjective; the plural noun form "constants" is incorrect.

---

### Issue 4: "Hastie et al." — plain text citation, no `\parencite`
- **Location:** Line 274, frame "Random Forests: Decorrelating the Trees"
- **Current:** `$\lfloor p/3 \rfloor$ recommended for regression (Hastie et al.)`
- **Proposed:** `$\lfloor p/3 \rfloor$ recommended for regression \parencite[§15.3]{Hastie2009}`
- **Severity:** MAJOR

Plain text "Hastie et al." produces no hyperlink or bibliography entry. `Hastie2009` is already in `Bibliography_base.bib`. Recommendation appears in ESL §15.3.

---

### Issue 5: Contraction "don't" — informal language
- **Location:** Line 655, frame "Tree-Based Forecasting: Design Choices"
- **Current:** `(unused features just don't appear in splits)`
- **Proposed:** `(unused features do not appear in splits)`
- **Severity:** MAJOR

Contractions are inappropriate in academic lecture slides. Same issue type as L07 Issue 16.

---

### Issue 6: Inline fraction formula — should be display math
- **Location:** Line 231, inside bagging `definitionbox`
- **Current:** `$\hat{y}_{\mathrm{bag}} = \frac{1}{B}\sum_{b=1}^{B} \hat{f}^{(b)}(\mathbf{x})$` (inline math)
- **Proposed:** Display math `\[ \hat{y}_{\mathrm{bag}} = \frac{1}{B}\sum_{b=1}^{B} \hat{f}^{(b)}(\mathbf{x}) \]`
- **Severity:** MAJOR

Inline `\frac{}{}` compresses the fraction; `\sum` limits appear inline rather than above/below. The variance equation two lines below (line 238) already uses display math — the bagging definition should match.

---

### Issue 7: Thousands separator inconsistency — plain comma vs. thin space
- **Location:** Line 30 (keybox) vs. lines 692--696 (Forecast Comparison table)
- **Current (line 30):** `RMSE $\approx$ 2,540 on RSXFS` (plain ASCII comma)
- **Current (table):** `2\,540`, `2\,380`, etc. (LaTeX thin space)
- **Proposed (line 30):** `RMSE $\approx$ $2{,}540$ on RSXFS`
- **Severity:** MAJOR

The thin-space convention `\,` is established in the table and in L08. Inline numbers must match.

---

### Issue 8: "XGBoost beats vanilla GBM" — informal and uncited
- **Location:** Line 417, keybox in "XGBoost: Regularized Gradient Boosting"
- **Current:** `Together: XGBoost beats vanilla GBM on most benchmarks.`
- **Proposed:** `Together: XGBoost outperforms vanilla GBM on most benchmarks \parencite{Chen2016}.`
- **Severity:** MAJOR

"Beats" is informal; claim needs citation. `Chen2016` is already cited in this frame (lines 345, 387).

---

### Issue 9: No `\label` on any `\section` declaration
- **Location:** Lines 51, 214, 337, 475, 563, 629, 722
- **Proposed:** Add `\label{sec:cart}`, `\label{sec:rf}`, `\label{sec:boosting}`, `\label{sec:importance}`, `\label{sec:tuning}`, `\label{sec:application}`, `\label{sec:takeaways}`
- **Severity:** MINOR

Same pattern flagged in L07 Issue 15. Hardcoded cross-references break when sections are reordered.

---

### Issue 10: "feature engineers should lead with lag\_12" — informal phrasing
- **Location:** Line 556, examplebox in "Feature Importance: XGBoost Gain and Rankings"
- **Current:** `feature engineers should lead with lag\_12`
- **Proposed:** `lag\_12 should be the primary feature in any RSXFS model`
- **Severity:** MINOR

"Lead with" is idiomatic and informal; the sentence also lacks an explicit grammatical subject.

---

### Issue 11: Long XGBoost gain bullet — overflow risk in half-width column
- **Location:** Line 544
- **Current:** `\item Use \textbf{XGBoost gain} when comparing feature contributions inside a boosted model`
- **Proposed:** Add manual linebreak: `...when comparing\\feature contributions...`
- **Severity:** MINOR

68 characters in `\footnotesize` at `0.50\textwidth` may produce an overfull `\hbox`.

---

### Issue 12: `\mathrm{Imp}` and `\mathrm{RSS}` — should use `\operatorname`
- **Location:** Lines 494--496
- **Current:** `\mathrm{Imp}(j)`, `\Delta \mathrm{RSS}`
- **Proposed:** `\operatorname{Imp}(j)`, `\Delta\operatorname{RSS}`
- **Severity:** MINOR

Course convention uses `\operatorname` for all operator-like symbols (consistent with `\Var`, `\MSE`, `\RMSE` macros in `header.tex`). `\mathrm` produces different spacing in math mode.

---

## Summary Table

| # | Severity | Issue |
|---|----------|-------|
| 1 | CRITICAL | `\parencite` inside `definitionbox` title (line 229) |
| 2 | CRITICAL | `\mathrm{Var}` → `\Var` macro (line 238) |
| 3 | MAJOR | "piecewise constants" → "piecewise constant" (line 39) |
| 4 | MAJOR | "Hastie et al." plain text → `\parencite{Hastie2009}` (line 274) |
| 5 | MAJOR | "don't" → "do not" (line 655) |
| 6 | MAJOR | Inline fraction formula → display math (line 231) |
| 7 | MAJOR | `2,540` plain comma → `$2{,}540$` thin space (line 30) |
| 8 | MAJOR | "beats" informal + uncited → "outperforms \parencite{Chen2016}" (line 417) |
| 9 | MINOR | No `\label` on any `\section` (lines 51, 214, 337, 475, 563, 629, 722) |
| 10 | MINOR | "lead with lag\_12" — informal phrasing (line 556) |
| 11 | MINOR | XGBoost gain bullet overflow risk (line 544) |
| 12 | MINOR | `\mathrm{Imp}`, `\mathrm{RSS}` → `\operatorname` (lines 494--496) |

**Citation keys verified:** `Breiman2001`, `Breiman1996`, `Chen2016` — all correct in `Bibliography_base.bib`. No undefined citation keys detected.
