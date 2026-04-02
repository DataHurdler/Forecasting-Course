# Baseline Quality Scores — All 12 Beamer Lectures
**Date:** 2026-03-02
**Tool:** `scripts/quality_score.py` (static analysis) + `.log` file inspection

---

## Summary Table

| Lecture | Static Score | Real Overfull hbox | Real Overfull vbox | Effective Grade |
|---------|-------------|-------------------|-------------------|-----------------|
| L01: Intro | 90/100¹ | 0 | 7 (1–5pt each) | ⚠️ PASS with issues |
| L02: Regression | 30/100¹ | 0 | 0 | ✅ EXCELLENCE |
| L03: ETS | 100/100 | 0 | 0 | ✅ EXCELLENCE |
| L04: ARIMA | 100/100 | 0 | 0 | ✅ EXCELLENCE |
| L05: Multivariate | 100/100 | 0 | 0 | ✅ EXCELLENCE |
| L06: Evaluation | 100/100 | 0 | 0 | ✅ EXCELLENCE |
| L07: ML Intro | 100/100 | 0 | 0 | ✅ EXCELLENCE |
| L08: Regularization | 100/100 | 0 | 0 | ✅ EXCELLENCE |
| L09: Trees | 100/100 | 0 | 0 | ✅ EXCELLENCE |
| L10: Neural Nets | 90/100¹ | 0 | 0 | ✅ EXCELLENCE |
| L11: Features | 100/100 | 0 | 0 | ✅ EXCELLENCE |
| L12: Capstone | 100/100 | 0 | 0 | ✅ EXCELLENCE |

¹ Static-analysis false positive: flagged long `\muted{\footnotesize\itshape ...}` paragraph lines
  that LaTeX wraps naturally. Compilation log confirms 0 hbox overflows.

---

## L01 Vbox Overflows — Detail

L01 is the only lecture with real compilation warnings:

| Log Line | Amount | Frame |
|----------|--------|-------|
| 74 | 4.13pt | Intro slide (two-column + keybox) |
| 210 | 4.83pt | Loss functions (warningbox + muted footnote) |
| 234 | 2.72pt | Forecast error (warningbox) |
| 315 | 4.33pt | Decomposition slide |
| 440 | 1.19pt | Naïve benchmark (defbox + columns) |
| 475 | 5.24pt | Seasonal naïve benchmark |
| 508 | 4.28pt | Historical mean benchmark |

**Root cause:** Benchmark slides (L440, L475, L508) share a pattern:
definitionbox + formula + columns (pros/cons + `\vspace{0.2cm}` + Python snippet).
The structure is ~5pt too tall. Reducing `\vspace{0.2cm}` → `\vspace{0.1cm}` (or removing it)
before the Python snippets in each benchmark frame would resolve these.

**Severity:** Minor. Overflows are 1–5pt (Beamer clips silently; no visible content is cut off).
Content is not lost, but technically below the "0 warnings" standard.

---

## Static Analysis Limitation

`quality_score.py` checks source lines >120 chars inside frames as a proxy for hbox risk.
This produces false positives for long `\muted{...}` and inline-text lines that LaTeX wraps naturally.
The script does **not** inspect `.log` files for actual vbox overflows.

**Recommendation:** Supplement with `grep -c "Overfull" Slides/*.log` after each compile.

---

## Overall Assessment

- **11 of 12 lectures:** Excellence (no real compilation warnings)
- **1 lecture (L01):** 7 minor vbox overflows (1–5pt) in introductory frames
- **All 12:** 0 undefined citations, 0 hbox overflows

**Decision:** Fix L01 vbox overflows before Quarto translation, or carry forward as a known
issue (they are cosmetically invisible at typical presentation zoom levels).
