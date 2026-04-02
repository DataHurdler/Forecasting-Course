# Proofreading Report: `Slides/Lecture11_Features.tex`

**Date:** 2026-03-01
**Reviewer:** Claude Code (proofreading agent)
**File:** `Slides/Lecture11_Features.tex`
**Bibliography:** `Bibliography_base.bib`

---

## Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 0 |
| MAJOR    | 5 |
| MINOR    | 6 |
| **Total**| **11** |

---

### Issue 1: Missing `\sectionslide` for final section
- **Location:** Line 1044, `\section{Takeaways and References}`
- **Current:** `\section{Takeaways and References}` immediately followed by `\begin{frame}{Lecture 11 Key Takeaways}` with no `\sectionslide` between them
- **Proposed:** Insert `\sectionslide{Takeaways and References}{What we learned and where to go next}` between the `\section{}` and the `\begin{frame}`, consistent with Lectures 09 and 10
- **Category:** STRUCTURE
- **Severity:** MAJOR

---

### Issue 2: Overflow risk — Key Takeaways frame
- **Location:** Lines 1048–1082, frame `Lecture 11 Key Takeaways`
- **Current:** A single `keybox` enclosing a 6-item `enumerate` with multi-line entries and `\parencite` citations, followed by a `\smallskip` and three more lines of "Preview of Lecture 12" text — all inside one frame at `\footnotesize`
- **Proposed:** Either split into two frames (takeaways on one, preview on another) or move the Lecture 12 preview outside the keybox; alternatively apply `\setlength{\itemsep}{1pt}` to the enumerate to reduce vertical spacing
- **Category:** OVERFLOW
- **Severity:** MAJOR

---

### Issue 3: Overflow risk — Motivation frame dense content
- **Location:** Lines 27–57, frame `Motivation: The Feature Gap`
- **Current:** A `keybox` (4 lines) + `\medskip` + header + 5-item `itemize` (each item 2 lines) + `\medskip` + 3-line goal statement — no font-size reduction applied
- **Proposed:** Apply `\small` to the itemize list, or reduce `\medskip` to `\smallskip`
- **Category:** OVERFLOW
- **Severity:** MINOR

---

### Issue 4: Rolling mean formula — subscript range written in reverse order
- **Location:** Line 293
- **Current:** `$\bar{y}_{t-1:t-w}$`
- **Proposed:** `$\bar{y}_{t-w:t-1}$`
- **Explanation:** Conventional range subscript notation runs from the lower (older) index to the upper (more recent). Writing `t-1:t-w` implies a range running downward, which is backwards.
- **Category:** MATH
- **Severity:** MAJOR

---

### Issue 5: Rolling std formula — reversed subscript range and undefined symbol
- **Location:** Line 295
- **Current:** `$s_{t-1:t-w}$`
- **Proposed:** `$s_{t-w:t-1}$` (parallel correction to Issue 4); or write out as `$\operatorname{std}(y_{t-w},\ldots,y_{t-1})$`
- **Explanation:** Same reversed-range issue as Issue 4. The symbol `s` for sample std is also not defined in `header.tex` (unlike `\Var`, `\RMSE` etc.).
- **Category:** MATH
- **Severity:** MAJOR

---

### Issue 6: Inconsistency in "time-series" hyphenation
- **Location:** Lines 63, 68 vs. line 1053
- **Current:** Lines 63 and 68: `time-series` (hyphenated modifier); line 1053: `time series` (open noun)
- **Proposed:** Both usages are grammatically correct as written (hyphenated as adjective, open as noun). No change required but worth confirming as intentional.
- **Category:** CONSISTENCY
- **Severity:** MINOR

---

### Issue 7: Inconsistent notation for EWM symbol
- **Location:** Lines 308–321
- **Current:** Formula uses `$\mathrm{EWM}_t$`; the comment "recent values receive ≈3× the weight of values 4 months back" is a reasonable approximation but "4 months back" could be clearer.
- **Proposed:** Clarify "4 months back" as "4 periods earlier" to avoid calendar confusion. No formula change needed.
- **Category:** CONSISTENCY
- **Severity:** MINOR

---

### Issue 8: Grammar — missing article and awkward preposition in `\sectionslide` subtitle
- **Location:** Line 63, `\sectionslide` subtitle
- **Current:** `Converting time-series forecasting to supervised regression`
- **Proposed:** `Converting time-series forecasting into a supervised regression problem`
- **Explanation:** "to" → "into" (standard idiom for conversion); missing indefinite article "a" before "supervised regression problem". Compare line 68–69 which correctly uses "into a standard supervised regression problem".
- **Category:** GRAMMAR
- **Severity:** MINOR

---

### Issue 9: Grammar — sentence fragment in enumerate
- **Location:** Lines 668–669
- **Current:** `Implicit selection via regularization path`
- **Proposed:** `Implicit selection via the regularization path.`
- **Explanation:** Missing article "the" before "regularization path".
- **Category:** GRAMMAR
- **Severity:** MINOR

---

### Issue 10: Academic quality — informal contraction "Today's"
- **Location:** Line 54
- **Current:** `\textbf{Today's goal:} build \texttt{make\_features\_extended()}`
- **Proposed:** `\textbf{Lecture goal:} Build \texttt{make\_features\_extended()}`
- **Explanation:** "Today's" anchors the slide to a delivery moment; academic slides should use timeless language.
- **Category:** ACADEMIC
- **Severity:** MINOR

---

### Issue 11: Ambiguous RMSE inequality in keybox
- **Location:** Lines 1031–1038
- **Current:** `\textbf{LSTM 36f $<$ XGBoost 36f $<$ LSTM 26f}: the feature gap dominates the model gap.`
- **Proposed:** `\textbf{RMSE: LSTM 36f $<$ XGBoost 36f $<$ LSTM 26f}: the feature gap dominates the model gap.`
- **Explanation:** Without the "RMSE:" prefix, the inequality reads as a quality ranking (LSTM worse than XGBoost) rather than an RMSE ordering (lower = better).
- **Category:** ACADEMIC
- **Severity:** MAJOR

---

## Citation Verification

| Key | Line(s) | Entry in .bib | Correct? |
|-----|---------|---------------|----------|
| `Tibshirani1996` | 698 | Tibshirani (1996), LASSO | Yes |
| `Molnar2022` | 711, 1066 | Molnar (2022), Interpretable ML | Yes |
| `Guyon2003` | 755, 1066 | Guyon & Elisseeff (2003), feature selection | Yes |
| `Pedregosa2011` | 822, 1070 | Pedregosa et al. (2011), scikit-learn | Yes |
| `BoxJenkins2015` | 1055 | Box et al. (2015), Time Series Analysis | Yes |

No citation key errors found.

---

## Section / `\sectionslide` Audit

| Section | `\sectionslide` Present? |
|---------|--------------------------|
| `Lag Features` (line 60) | Yes |
| `Rolling Statistics` (line 250) | Yes |
| `Calendar and Structural Features` (line 417) | Yes |
| `Interaction and Ratio Features` (line 540) | Yes |
| `Feature Selection` (line 652) | Yes |
| `Pipeline Design` (line 801) | Yes |
| `Application to Forecasting` (line 964) | Yes |
| `Takeaways and References` (line 1044) | **Missing** — see Issue 1 |

---

## Summary Table

| # | Location | Issue | Severity |
|---|----------|-------|----------|
| 1 | Line 1044 | Missing `\sectionslide` for final section | MAJOR |
| 2 | Lines 1048–1082 | Key Takeaways frame overflow risk | MAJOR |
| 3 | Lines 27–57 | Motivation frame overflow risk | MINOR |
| 4 | Line 293 | Rolling mean subscript range backwards (`t-1:t-w` → `t-w:t-1`) | MAJOR |
| 5 | Line 295 | Rolling std subscript range backwards and symbol undefined | MAJOR |
| 6 | Lines 63/1053 | "time-series" hyphenation consistency | MINOR |
| 7 | Lines 308–321 | EWM "4 months back" unclear | MINOR |
| 8 | Line 63 | Missing article in `\sectionslide` subtitle | MINOR |
| 9 | Lines 668–669 | Missing article in enumerate item | MINOR |
| 10 | Line 54 | Informal "Today's goal" | MINOR |
| 11 | Lines 1031–1038 | RMSE inequality ambiguous without "RMSE:" prefix | MAJOR |

*End of report.*
