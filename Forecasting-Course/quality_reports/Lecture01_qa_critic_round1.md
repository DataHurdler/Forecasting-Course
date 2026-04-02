# QA Critic Report: Lecture01_Intro — Quarto vs. Beamer
**Date:** 2026-03-06
**Round:** 1
**Critic:** Adversarial QA agent
**Files compared:**
- Beamer (gold standard): `Slides/Lecture01_Intro.tex`
- Quarto: `Quarto/Lecture01_Intro.qmd`

---

## Hard Gate Status

| Gate | Status | Notes |
|------|--------|-------|
| No content overflow | PASS | No dense TikZ in Quarto; HTML diagram used |
| Plot/chart quality | N/A | No data visualizations in this lecture |
| Content parity | PASS | All 24 content slides present and accounted for |
| Visual regression (Quarto >= Beamer) | PARTIAL | See Issue 1 — metric equations lose alignment |
| Slide centering | PASS | Standard RevealJS layout |
| Notation fidelity | PASS | All math verbatim or equivalent |

**Overall verdict: NOT APPROVED — 1 Major issue must be fixed before approval.**

---

## Slide-by-Slide Comparison

| Slide | Beamer | Quarto | Status |
|-------|--------|--------|--------|
| Title page | `\titlepage` | YAML frontmatter → auto-rendered | PASS |
| Lecture Outline | `\tableofcontents` | Manual numbered list | PASS |
| Section: Why Forecasting Matters | `\sectionslide{...}` | `# ...` + subtitle body | PASS (structural equiv.) |
| Forecasting Is Everywhere | Two-column layout | Two-column layout | PASS |
| The Cost of Getting It Wrong | examplebox + warningbox | `.examplebox` + `.warningbox` | PASS |
| What Makes Forecasting Hard? | `\key{}` for terms | `[...]{.hi}` for terms | PASS |
| Section: The Forecasting Framework | `\sectionslide` | `# ...` | PASS |
| The Formal Setup | definitionbox + columns | `.definitionbox` + columns | PASS |
| What Should We Actually Forecast? | examplebox | `.examplebox` | PASS |
| The Optimal Point Forecast | keybox + warningbox | `.keybox` + `.warningbox` | PASS |
| Forecast Error | definitionbox + warningbox | `.definitionbox` + `.warningbox` | PASS |
| Types of Forecasts | Three-column layout | Three-column layout + keybox | PASS |
| Section: Time Series Patterns | `\sectionslide` | `# ...` | PASS |
| Components of a Time Series | Columns + examplebox | Columns + `.examplebox` | PASS |
| Seasonality: A Closer Look | booktabs table + warningbox | Markdown table + `.warningbox` | PASS |
| Stationarity: A First Look | definitionbox + columns | `.definitionbox` + columns | PASS |
| Section: Benchmark Models | `\sectionslide` | `# ...` | PASS |
| The Benchmark Principle | keybox + examplebox | `.keybox` + `.examplebox` | PASS |
| Benchmark 1: Naïve | definitionbox + columns | `.definitionbox` + columns | PASS |
| Benchmark 2: Seasonal Naïve | definitionbox + columns | `.definitionbox` + columns | PASS |
| Benchmark 3: Historical Mean | definitionbox + columns | `.definitionbox` + columns | PASS |
| Benchmark 4: RW with Drift | definitionbox + keybox | `.definitionbox` + `.keybox` | PASS |
| Section: Forecast Evaluation | `\sectionslide` | `# ...` | PASS |
| Point Forecast Accuracy Metrics | align* (aligned equations) | Three separate $$ blocks | **FAIL — Issue 1** |
| The Evaluation Principle | keybox + warningbox | `.keybox` + `.warningbox` | PASS |
| Visualizing the Train/Test Split | TikZ diagram | HTML div diagram | PASS (acceptable equiv.) |
| A Better Scale-Free Metric: MASE | `\textcite` + keybox | `@Hyndman2006` + `.keybox` | PASS |
| Section: Course Roadmap | `\sectionslide` | `# ...` | PASS |
| BSAD 8310 in Two Parts | Two-column enum lists | Two-column enum lists | PASS |
| Tools and Expectations | Two-column lists | Two-column lists | PASS |
| Key Takeaways | keybox with enumerate | `.keybox` + `.smaller` | PASS |
| References | `\printbibliography` | `{#refs}` div | PASS |

---

## Issues

### Issue 1 [MAJOR]: Metric equations lose vertical alignment on "Point Forecast Accuracy Metrics" slide

**Beamer (gold standard):**
```latex
\begin{align*}
  \MSE  &= \frac{1}{H}\sum_{h=1}^{H} e_{T+h}^2 \\[1pt]
  \RMSE &= \sqrt{\MSE} \\[1pt]
  \MAE  &= \frac{1}{H}\sum_{h=1}^{H} |e_{T+h}|
\end{align*}
```
The `&=` alignment anchor creates a clean vertical column of equals signs. Students can immediately see MSE, RMSE, and MAE as a family of related metrics, aligned at the operator.

**Quarto (current):**
```markdown
$$\operatorname{MSE} = \frac{1}{H}\sum_{h=1}^{H} e_{T+h}^2$$
$$\operatorname{RMSE} = \sqrt{\operatorname{MSE}}$$
$$\operatorname{MAE} = \frac{1}{H}\sum_{h=1}^{H} |e_{T+h}|$$
```
Three separate centered display equations — each centered independently. The equals signs do not align. This is visually inferior to the Beamer version.

**Fix:** Replace the three separate `$$` blocks with a single aligned equation block using `\begin{aligned}...\end{aligned}` inside one `$$` pair. MathJax (used by Quarto/RevealJS) supports `aligned`.

**Severity:** MAJOR — visual regression against the Beamer benchmark.

---

### Issue 2 [MINOR]: Train/Test HTML diagram — "Forecast origin" label position

**Beamer:** The "Forecast origin" label appears **above** the dashed vertical line at `t=T`.
**Quarto HTML:** The label reads "Forecast origin" but is positioned `top:4px; left:55%` which may clip or overlap on some viewport sizes. The label is inside the outer div but positioned relative to the dashed line — adequate but fragile.

**Fix:** Not critical. The diagram communicates correctly. Document as known minor fragility.

**Severity:** MINOR — no fix required this round.

---

### Issue 3 [MINOR]: Citation style in "The Benchmark Principle" slide

**Beamer:** `\parencite{Makridakis2020}` — renders as "(Makridakis et al., 2020)"
**Quarto:** `[@Makridakis2020]` — renders as "(Makridakis et al., 2020)" with Chicago author-date CSL

These are equivalent. PASS with note.

**Severity:** MINOR — no action needed.

---

## Summary

| # | Slide | Issue | Severity | Fix Required? |
|---|-------|-------|----------|---------------|
| 1 | Point Forecast Accuracy Metrics | align* → separate $$, lose vertical alignment | MAJOR | YES |
| 2 | Visualizing Train/Test Split | HTML diagram label positioning fragile | MINOR | NO |
| 3 | The Benchmark Principle | Citation style (already equivalent) | MINOR | NO |

**Round 1 verdict: NOT APPROVED. Fix Issue 1, then re-audit.**
