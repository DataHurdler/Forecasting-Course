# Proofreading Report: Lecture08_Regularization.qmd

**File:** `Quarto/Lecture08_Regularization.qmd`
**Date:** 2026-03-02
**Reviewer:** Proofreader Agent
**Total issues found:** 7

---

## Summary by Category

| Category | Count | Severity |
|:---|---:|:---|
| GRAMMAR | 1 | Minor |
| TYPOS | 0 | — |
| OVERFLOW | 1 | Minor |
| CONSISTENCY | 3 | Minor |
| ACADEMIC QUALITY | 2 | Minor |

**Overall assessment:** The file is clean. No critical issues. All findings are minor. The mathematical notation is accurate and consistent with the Beamer source. SVG diagrams are well-formed.

---

## Detailed Findings

---

### GRAMMAR

**Issue G-01** | Line 510 | Minor

- **Slide:** "TimeSeriesSplit CV for Regularization"
- **Current:** `e.g. $10^{-3}$ to $10^{3}$ (50 points, log-spaced)`
- **Issue:** Missing comma after "e.g." (standard academic convention: "e.g.,")
- **Proposed fix:** `e.g., $10^{-3}$ to $10^{3}$ (50 points, log-spaced)`

---

### OVERFLOW

**Issue O-01** | Line 115 | Minor

- **Slide:** "Penalized Regression: General Form" — footer note
- **Current:** Single long inline span with `.neutral .smaller`: `[$\lambda \geq 0$ controls penalty strength; $\lambda=0$ recovers OLS. $\lambda \to \infty$ shrinks $\hat{\boldsymbol{\beta}} \to \mathbf{0}$. Elastic Net $\alpha$ is the L1/L2 mixing ratio --- distinct from ETS smoothing $\alpha$ (L03) and ECM speed-of-adjustment $\alpha$ (L05). The tuning of $\lambda$ (and $\alpha$ for Elastic Net) is covered in Section 5.]{.neutral .smaller}`
- **Issue:** This is a very long single-line footnote that may wrap awkwardly at 1280×720. At `.smaller` (85% of 30px = ~25.5px), it spans approximately 120+ characters. Consider splitting into two sentences or wrapping in a `::: {.smaller}` block for better control.
- **Proposed fix:** Wrap in a div block:
  ```markdown
  ::: {.neutral .smaller}
  $\lambda \geq 0$ controls penalty strength; $\lambda=0$ recovers OLS; $\lambda \to \infty$ shrinks $\hat{\boldsymbol{\beta}} \to \mathbf{0}$. Elastic Net $\alpha$ is the L1/L2 mixing ratio --- distinct from ETS smoothing $\alpha$ (L03) and ECM speed-of-adjustment $\alpha$ (L05). Tuning of $\lambda$ (and $\alpha$ for Elastic Net) is covered in Section 5.
  :::
  ```

---

### CONSISTENCY

**Issue C-01** | Line 733 | Minor

- **Slide:** "Forecast Comparison: SARIMA vs. Regularized Models" — comparison table
- **Current:** `| Seasonal Naive | 4,210 | 3,120 |`
- **Issue:** The Beamer source uses "Seasonal Naïve" (with diaeresis on the i). Quarto can render the Unicode character ï. For consistency with L06 and L07 where "Naïve" is used, this should carry the accent.
- **Proposed fix:** `| Seasonal Naïve | 4,210 | 3,120 |`

**Issue C-02** | Line 734 | Minor

- **Slide:** Forecast Comparison table
- **Current:** `| SARIMA(1,1,1)(1,1,1)₁₂ | 2,840 | 2,100 |`
- **Issue:** The subscript "₁₂" is Unicode subscript digits, which renders fine. However, the standard pattern used in L04 and L06 QMD files should be checked for consistency. This is acceptable if other Quarto files use the same approach — confirm it matches convention.
- **Note:** No change required unless convention differs. Flagged for awareness.

**Issue C-03** | Line 627 | Minor

- **Slide:** Slide title: "sklearn Pipeline for Leakage-Free CV"
- **Current:** `## sklearn Pipeline for Leakage-Free CV`
- **Issue:** `sklearn` starts a heading with lowercase. Quarto renders heading text verbatim, so this will appear as `sklearn` in the slide title. The Beamer source uses `\texttt{sklearn}` inline in a larger sentence (not as a standalone heading word). Consider capitalizing the heading to "Sklearn Pipeline for Leakage-Free CV" or "Pipeline for Leakage-Free CV (sklearn)" for title-case consistency with other slide headings.
- **Proposed fix:** `## Pipeline for Leakage-Free CV (sklearn)`
- **Note:** Low priority — lowercase package names in headings is a common convention.

---

### ACADEMIC QUALITY

**Issue A-01** | Line 64 | Minor

- **Slide:** "OLS Instability with Many Predictors" — examplebox
- **Current:** `With 12 lags + 3 rolling windows + 12 month dummies = 27 predictors on $n \approx 300$ monthly obs. Small by ML standards, but already enough for OLS instability with correlated lag features.`
- **Issue:** "obs." ends with a period that could be read as a full stop, but a sentence continues after it. In the Beamer source this used `obs.\ ` (LaTeX forced-space after abbreviation period). In Markdown the period-space is handled normally, but the sentence flow reads slightly awkwardly. A minor restructure improves clarity.
- **Proposed fix:** `With 12 lags + 3 rolling windows + 12 month dummies = 27 predictors on $n \approx 300$ monthly observations. Small by ML standards, but already enough for OLS instability with correlated lag features.`

**Issue A-02** | Line 262 | Minor

- **Slide:** "Ridge: Key Properties Summary" — keybox
- **Current:** `**When to use Ridge:** when you believe *all* predictors contribute a little (dense signal), or when predictors are highly correlated groups.`
- **Issue:** "or when predictors are highly correlated groups" — the phrasing "are highly correlated groups" is slightly awkward; predictors are not "groups" but rather "form correlated groups" or "come in highly correlated groups."
- **Proposed fix:** `**When to use Ridge:** when you believe *all* predictors contribute a little (dense signal), or when predictors come in highly correlated groups.`

---

## Issues NOT Found

- No duplicated words detected
- No subject-verb agreement errors
- No tense inconsistency (present tense used consistently throughout)
- No missing article errors (a/an/the)
- No citation format inconsistencies (all use `[@Key]` Pandoc style correctly)
- No mathematical notation errors (all equations verified against Beamer source)
- No `\pause`, `\onslide`, or overlay commands present
- No broken Quarto div fences detected
- All box environments (`.keybox`, `.definitionbox`, `.warningbox`, `.examplebox`) are properly opened and closed
- SVG blocks all use valid `{=html}` raw blocks
- YAML header is valid and consistent with L07 conventions

---

## Recommended Action

Apply fixes for:
- **G-01** (comma after "e.g.") — cosmetic, easy
- **O-01** (long footnote span) — consider wrapping for layout safety
- **C-01** (Naïve accent) — consistency with other lectures
- **A-01** ("obs." abbreviation) — clarity
- **A-02** ("are highly correlated groups") — phrasing

Defer:
- **C-02** (SARIMA subscript notation) — acceptable as-is
- **C-03** (lowercase heading) — low priority
