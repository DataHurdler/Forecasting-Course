# QA Critic Report — Round 1: Lecture02_Regression
**Date:** 2026-03-06
**Files compared:**
- Beamer (gold standard): `Slides/Lecture02_Regression.tex`
- Quarto: `Quarto/Lecture02_Regression.qmd`
- HTML: Not yet rendered (no Lecture02 HTML found in `docs/`)

**Method:** Source-to-source comparison (TEX vs QMD), slide-by-slide.

---

## Hard Gate Status

| Gate | Status | Notes |
|------|--------|-------|
| No content overflow | CONDITIONAL | Several complex math slides need render verification |
| Plot/chart quality | N/A | No data plots in Lecture 02 |
| Content parity — all slides present | PASS | All slides accounted for |
| Visual regression (Quarto >= Beamer) | CONDITIONAL | Minor omissions noted below |
| Slide centering | PASS (assumed) | No render available to verify |
| Notation fidelity — all math verbatim or equivalent | MINOR FAIL | Three notation issues found |

---

## Slide-by-Slide Audit

### Slide: Title / Outline
- **Beamer:** `\tableofcontents` generates numbered TOC from `\section` commands
- **Quarto:** Manual numbered list hardcoded
- **Verdict:** PASS — content identical; manual list is acceptable for RevealJS
- **Note:** No section-transition slides visible in QMD (see Issue 1 below)

---

### Slide: What Benchmark Models Cannot Do
- **Beamer:** `\muted{\footnotesize\itshape Examples: ...}` — small muted italic below warning box
- **Quarto:** `[*Examples: ...*]{.neutral .smaller}` — correct mapping
- **Verdict:** PASS

---

### Slide: What Regression-Based Forecasting Adds
- **Beamer:** `\key{Leading indicators}` etc. — blue bold inline for key terms in left column
- **Quarto:** `[**Leading indicators:**]{.hi}` — correct `.hi` class mapping
- **Verdict:** PASS

---

### Slide: General Setup (Regression Model for Forecasting)
- **Beamer:** `\varepsilon_t \sim WN(0, \sigma^2)` in definition box
- **Quarto:** `$\varepsilon_t \sim WN(0, \sigma^2)$` — PASS, verbatim
- **Notation reminder footnote:** Both present, correctly mapped to `.neutral .smaller`
- **Verdict:** PASS

---

### Slide: OLS Estimation
- **Beamer:** `\E[\varepsilon_t \mid \mathbf{X}] = 0` using custom `\E` macro
- **Quarto:** `$\mathbb{E}[\varepsilon_t \mid \mathbf{X}] = 0$` — PASS, equivalent expansion
- **Beamer:** `\parencite[][Ch.~8]{Hamilton1994}` — note: the proofreading report found this was previously Ch.~10 but was corrected to Ch.~8 in the `.tex` file
- **Quarto:** `[@Hamilton1994, Ch. 8]` — PASS, matches corrected Beamer
- **Verdict:** PASS

---

### Slide: What Can $\mathbf{x}_{T+h}$ Contain?
- **Beamer:** `\textbf{\pos{Type 1: Deterministic}}` — green-colored bold heading
- **Quarto:** `[**Type 1: Deterministic**]{.positive}` — correct `.positive` mapping
- **Beamer:** `\textbf{\negc{Type 3: External regressors}}` — red-colored bold heading
- **Quarto:** `[**Type 3: External regressors**]{.negative}` — correct `.negative` mapping
- **Verdict:** PASS

---

### Slide: The Regression Forecast
- **Beamer:** `\muted{\footnotesize\itshape In Lab 02...}`
- **Quarto:** `[*In Lab 02...*]{.neutral .smaller}` — correct
- **Verdict:** PASS

---

### Slide: Model 1: Linear Trend
- **Beamer:** `\muted{\footnotesize\itshape US retail sales...}` — small muted italic
- **Quarto:** `[*US retail sales...*]{.neutral .smaller}` — correct
- **Verdict:** PASS

---

### Slide: Model 2: Seasonal Dummy Variables
- **Beamer:** Definition box wraps both the define-sentence and the formula with `{\small ...}` sizing
- **Quarto:** Uses `.smaller` div inside `.definitionbox` — functionally equivalent
- **Beamer:** Two-column layout with interpretation bullets using `{\small\begin{itemize}...}` for font reduction
- **Quarto:** Uses `.smaller` div wrapping bullet list — correct
- **Verdict:** PASS

---

### Slide: Model 3: Trend + Seasonality
- **Beamer:** Forecast line: `$\hat{y}_{T+h|T} = \hat{\beta}_0 + \hat{\beta}_1(T+h) + \hat{\gamma}_{s(T+h)}$ \hfill\muted{(always known)}`
- **Quarto:** `**Forecast:** $\hat{y}_{T+h|T} = \hat{\beta}_0 + \hat{\beta}_1(T+h) + \hat{\gamma}_{s(T+h)}$ &nbsp;&nbsp; *(always known)*` — PASS, `\hfill` replaced with `&nbsp;&nbsp;` spacing
- **Verdict:** PASS

---

### Slide: Extensions: Non-Linear Trend

**ISSUE 1 (MAJOR — Notation): Log-linear forecast formula missing Beamer comment annotation**

- **Beamer:** `\hfill\muted{\small (bias correction)}` appears inline after the forecast formula on same line
- **Quarto:** `&nbsp;&nbsp; *(bias correction)*` — uses italic emphasis, not `.neutral` class
- **Severity:** MINOR — content preserved, styling slightly inconsistent (should be `.neutral` not plain italic)
- **Verdict:** MINOR ISSUE — see Issue 1

---

### Slide: From Point Forecast to Prediction Interval

**ISSUE 2 (MAJOR — Notation): AR(1) `iid` distribution annotation in Beamer not fully preserved**

Wait — checking this slide: the PI formula in Beamer uses nested `\underbrace` with subscript labels. In MathJax (RevealJS), `\underbrace` with `\substack` can render differently.

- **Beamer formula:**
  ```
  \hat{\sigma}_e \sqrt{\underbrace{1}_{\substack{\text{irreducible}\\\text{error}}}
  + \underbrace{\mathbf{x}_{T+h}^{\prime}(\mathbf{X}^{\prime}\mathbf{X})^{-1}\mathbf{x}_{T+h}}_{\text{estimation uncertainty}}}
  ```
- **Quarto formula:** Identical LaTeX source used in `$$...$$` block
- **Concern:** `\substack` inside `\underbrace` subscript is valid in MathJax but may render at reduced size. The Beamer version also has `\substack` with two lines for "irreducible error" — the Quarto version preserves this verbatim.
- **Verdict:** PASS on notation fidelity; CONDITIONAL on visual render (needs browser verification)

---

### Slide: When Prediction Intervals Are Valid
- **Beamer:** `$\varepsilon_t \stackrel{iid}{\sim} \mathcal{N}(0,\sigma^2)$`
- **Quarto:** `$\varepsilon_t \stackrel{iid}{\sim} \mathcal{N}(0,\sigma^2)$` — verbatim match
- **Beamer:** `$\Cov(\varepsilon_t, \varepsilon_s) = 0$` — uses custom `\Cov` macro
- **Quarto:** `$\text{Cov}(\varepsilon_t, \varepsilon_s) = 0$` — PASS, explicit `\text{Cov}` is correct expansion
- **Verdict:** PASS

---

### Slide: The AR(1) Model

**ISSUE 2 (MINOR — Notation): Inline annotation removed from AR(1) definition box**

- **Beamer:** Inside the `definitionbox`:
  ```
  \varepsilon_t \overset{iid}{\sim} WN(0,\sigma^2)
  \;\muted{\small\text{(normality not required for OLS)}}
  ```
  The annotation `(normality not required for OLS)` appears inline inside the formula environment as muted small text.
- **Quarto:** The definition box contains only:
  ```
  $$y_t \;=\; \phi_0 + \phi_1 y_{t-1} + \varepsilon_t, \qquad \varepsilon_t \overset{iid}{\sim} WN(0,\sigma^2)$$
  ```
  The inline annotation `(normality not required for OLS)` is **missing entirely**.
- **Severity:** MAJOR — this is a pedagogically important clarification that students need. It distinguishes WN from Gaussian assumptions for OLS estimation.

---

### Slide: The AR($p$) Model and Lag Selection
- **Beamer:** AIC/BIC equations in `align*` environment
- **Quarto:** Two separate `$$` display blocks for AIC and BIC
- **Concern:** Two separate display blocks rather than aligned pair — minor visual difference vs. Beamer `align*`
- **Beamer:** `\parencite[][Ch.~5]{BoxJenkins2015}` — after BIC recommendation
- **Quarto:** `[@BoxJenkins2015, Ch. 5]` — PASS
- **Severity:** MINOR — separate `$$` blocks do not align equals signs the way `align*` does in Beamer

**ISSUE 3 (MINOR — Visual): AIC/BIC formulas not aligned in Quarto**
- **Beamer:** `align*` aligns `=` signs across AIC and BIC
- **Quarto:** Two separate `$$` blocks — equations are vertically separate, not aligned
- The L01 QA fix established precedent: use `\begin{aligned}...\end{aligned}` inside a single `$$` block
- **Severity:** MINOR

---

### Slide: Multi-Step AR Forecasts: The Recursive Method
- **Beamer:** Three-equation `align*` block in the example box
- **Quarto:** Three separate `$$` blocks in the examplebox
- **Same issue as AR(p) slide** — the three recursive equations are not aligned across `=` signs
- **Severity:** MINOR (same pattern as Issue 3 above — consistent precedent from L01 fix applies here too)

---

### Slide: Diagnosing an AR Model
- **Beamer:** `$\pm 1.96/\sqrt{T}$` in the residual ACF check bullet
- **Quarto:** `$\pm 1.96/\sqrt{T}$` — verbatim match
- **Verdict:** PASS

---

### Slide: Pitfall 1: Spurious Regression
- **Beamer:** `\textcite{GrangerNewbold1974} show that...` — author-text citation
- **Quarto:** `@GrangerNewbold1974 show that...` — PASS, correct author-text citation form
- **Beamer:** `$R^2 > DW$ statistic (where $DW$ is the Durbin-Watson autocorrelation statistic, Lecture 6)` — the proofreading report flagged the missing definition and it was added to the `.tex`
- **Quarto:** `$R^2 > DW$ statistic (where $DW$ is the Durbin-Watson autocorrelation statistic, Lecture 6)` — PASS, matches corrected Beamer
- **Verdict:** PASS

---

### Slide: Pitfall 2: Overfitting
- **Beamer:** `\muted{\small \textbf{Rule of thumb:} Keep $k \ll T$. A common bound: $k \leq T/10$.}` — this is a muted small paragraph below the bullet list
- **Quarto:** `[**Rule of thumb:** Keep $k \ll T$. A common bound: $k \leq T/10$.]{.neutral .smaller}` — correct mapping
- **Verdict:** PASS

---

### Slide: Pitfall 3: The Regressor Availability Problem
- **Beamer:** `\item[\pos{$\checkmark$}]` — green checkmark list item prefix
- **Quarto:** `- $y_T, y_{T-1}, \ldots$ (lagged $y$)` — checkmarks dropped entirely
- **Beamer:** `\item[\negc{$\times$}]` — red X list item prefix
- **Quarto:** no X prefix
- **Severity:** MINOR — the colored checkmarks/X markers are visual emphasis that aids comprehension; their absence is a parity gap vs. Beamer

**ISSUE 4 (MINOR — Visual): Checkmark/X list prefixes missing from Pitfall 3 slide**
- **Beamer:** Valid items prefixed with green `✓`, invalid items prefixed with red `✗`
- **Quarto:** Plain bullet points with no marker
- **Note:** L01 QA established precedent: `[\pos{$\checkmark$}]` → `[✓]{.positive}` and `[\negc{$\times$}]` → `[✗]{.negative}` as list item prefixes. The same pattern was used in L01.

---

### Slide: Lecture 2: Key Takeaways
- **Beamer:** All 5 numbered points in `keybox` with `\small` sizing
- **Quarto:** All 5 points in `.keybox` with `.smaller` — PASS
- **Content:** Verbatim match across all 5 points
- **Verdict:** PASS

---

### Slide: References
- **Beamer:** `\printbibliography[heading=none]`
- **Quarto:** `::: {#refs}` div — correct Quarto equivalent
- **Verdict:** PASS

---

### Section Transition Slides

**ISSUE 5 (MAJOR — Content Parity): Section transition slides missing**

- **Beamer:** Uses `\sectionslide{Title}{Subtitle}` macro for 6 section transitions:
  1. "From Benchmarks to Regression" / "Naïve models ignore information..."
  2. "The Regression Model for Forecasting" / "OLS is not just for causal inference..."
  3. "Trend and Seasonality as Regressors" / "Deterministic components require no forecasting..."
  4. "Prediction Intervals" / "A point forecast without uncertainty bounds..."
  5. "Autoregressive Models" / "The past values of a series often predict its future..."
  6. "Pitfalls" / "Regression in time series requires extra care..."

- **Quarto:** Uses level-1 headers (`# Section Title`) with a subtitle paragraph below — this is correct RevealJS practice and produces equivalent section-break slides. The subtitle text is present.
- **Verdict:** PASS — the `#` header + subtitle paragraph is the correct RevealJS equivalent of `\sectionslide{}{}`. Not a parity gap.

---

## Issues Summary

| # | Slide | Issue | Severity |
|---|-------|-------|----------|
| 1 | Extensions: Non-Linear Trend | Bias correction annotation uses plain italic instead of `.neutral` class | MINOR |
| 2 | The AR(1) Model | Inline annotation `(normality not required for OLS)` missing from definition box | MAJOR |
| 3 | AR($p$) Model / AR(2) example | AIC/BIC and three recursive equations not aligned (separate `$$` blocks vs `align*`) | MINOR |
| 4 | Pitfall 3: Regressor Availability | Green ✓ / Red ✗ list item prefixes missing | MINOR |

---

## Hard Gate Re-Assessment

| Gate | Status |
|------|--------|
| No content overflow | CONDITIONAL — needs render to verify PI formula with `\substack` |
| Plot/chart quality | N/A |
| Content parity — all slides present | PASS (with Issue 2 noted) |
| Visual regression (Quarto >= Beamer) | CONDITIONAL — Issues 3, 4 are parity gaps |
| Slide centering | UNVERIFIED — no HTML rendered |
| Notation fidelity | MINOR FAIL — Issue 2 (missing annotation) |

---

## Recommendation

**NOT YET APPROVED** — proceed to Phase 2 (fix cycle).

Priority order:
1. **Issue 2 (MAJOR):** Restore `(normality not required for OLS)` annotation in AR(1) definition box
2. **Issue 3 (MINOR):** Align AIC/BIC equations using `\begin{aligned}` pattern (L01 precedent)
3. **Issue 3b (MINOR):** Align AR(2) recursive example equations using `\begin{aligned}` pattern
4. **Issue 4 (MINOR):** Restore `[✓]{.positive}` / `[✗]{.negative}` prefixes on Pitfall 3 lists
5. **Issue 1 (MINOR):** Change `*(bias correction)*` to `[*(bias correction)*]{.neutral}` for correct class

After fixes: re-render and re-audit.
