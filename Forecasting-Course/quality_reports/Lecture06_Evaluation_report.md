# Proofreading Report: Lecture06_Evaluation.tex
**File:** `Slides/Lecture06_Evaluation.tex`
**Lecture:** BSAD 8310 Lecture 06 — Forecast Evaluation
**Reviewer:** Proofreading Agent
**Date:** 2026-02-28

---

## Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 2 |
| MAJOR    | 5 |
| MINOR    | 8 |
| **Total**| **15** |

---

### Issue 1: Math error — combination variance formula mixes ρ and σ₁₂
- **Location:** Line 541, frame "Why Combine Forecasts?"
- **Current:** `= \tfrac{1}{4}\bigl(\sigma_1^2 + 2\rho\sigma_{12} + \sigma_2^2\bigr)`
- **Proposed:** `= \tfrac{1}{4}\bigl(\sigma_1^2 + 2\rho\sigma_1\sigma_2 + \sigma_2^2\bigr)`
- **Severity:** CRITICAL

The middle term `2ρσ₁₂` conflates ρ (dimensionless correlation) with σ₁₂ (covariance). The product ρ·σ₁₂ = ρ²σ₁σ₂, not ρσ₁σ₂. The correct correlation-form expansion of Var(½e₁+½e₂) is ¼(σ₁²+2ρσ₁σ₂+σ₂²).

---

### Issue 2: Logic error — MAPE asymmetry description is factually reversed
- **Location:** Lines 189–191, frame "MAPE Pitfalls and When to Use MASE"
- **Current:** `a 100\% overforecast produces MAPE = 100\%; a 100\% underforecast is impossible when $y>0$ (bounded at 100\% from below but not above)`
- **Proposed:** `when $y>0$, under-forecasts contribute at most 100\% to MAPE (bounded: when $\hat{y}=0$, $|e/y|=1$); over-forecasts are unbounded above --- MAPE $\to\infty$ as $\hat{y}\to\infty$`
- **Severity:** CRITICAL

Under-forecasts (ŷ→0) are bounded **above** at 100%. Over-forecasts are unbounded above. The current text states the opposite — "bounded at 100% from below but not above" — inverting the direction of the bound. Students will learn the wrong direction of MAPE's asymmetry bias.

---

### Issue 3: Undefined notation — `e^+` and `e^-` used without definition
- **Location:** Lines 172–173, frame "RMSE vs. MAE: Align with Business Costs"
- **Current:** `use asymmetric loss $L(e) = c_1 e^+ + c_2 e^-$.`
- **Proposed:** `use asymmetric loss $L(e) = c_1 e^{+} + c_2 e^{-}$ where $e^{+} = \max(e,0)$ and $e^{-} = \max(-e,0)$.`
- **Severity:** MAJOR

Positive-part/negative-part notation is non-standard and undefined in L01–L06. Students cannot interpret the formula without a definition.

---

### Issue 4: Hardcoded "Section~2" cross-reference opaque to students
- **Location:** Line 379, frame "Walk-Forward Validation: Step-by-Step"
- **Current:** `$e_{t,h}$ generalizes $e_{T+h}$ from Section~2 to multiple`
- **Proposed:** `$e_{t,h}$ generalizes $e_{T+h}$ from the Error Metrics section to multiple`
- **Severity:** MAJOR

Beamer does not display section numbers to students on slides. "Section 2" is opaque; "Error Metrics section" is self-evident.

---

### Issue 5: Overstated empirical claim — "consistently outperform"
- **Location:** Lines 546–548, frame "Why Combine Forecasts?"
- **Current:** `\textcite{BatesGranger1969} showed that weighted combinations \emph{consistently} outperform the best individual model in out-of-sample tests.`
- **Proposed:** `\textcite{BatesGranger1969} showed that weighted combinations \emph{generally} outperform the best individual model in empirical comparisons.`
- **Severity:** MAJOR

Bates & Granger (1969) demonstrated the result empirically with a limited set of series under specific conditions. "Consistently" implies a universal theorem. "Generally" or "typically" is the standard formulation in the survey literature.

---

### Issue 6: Missing accent — `naive` on line 127
- **Location:** Line 127, inside keybox, frame "Forecast Accuracy Metrics"
- **Current:** `MASE $<1$: beats naive\\`
- **Proposed:** `MASE $<1$: beats na\"{i}ve\\`
- **Severity:** MAJOR

Every other occurrence of "naïve" in the file (lines 197, 198, 233, 255, 396, 397) uses the accented form. Line 127 is the sole exception.

---

### Issue 7: No `\MASE` macro despite `\RMSE` and `\MAE` existing in header
- **Location:** Lines 108, 110, 115, 197, 198 (use `\operatorname{MASE}`)
- **Proposed:** Add `\newcommand{\MASE}{\operatorname{MASE}}` to `Preambles/header.tex` and replace all `\operatorname{MASE}` usages with `\MASE`
- **Severity:** MAJOR

Header defines `\RMSE` and `\MAE` as operator shortcuts but not `\MASE`. The verbose `\operatorname{MASE}` is repeated throughout. Adding the macro maintains the established pattern.

---

### Issue 8: `n_h` formula uses `H` instead of `h` on right-hand side
- **Location:** Line 381, frame "Walk-Forward Validation: Step-by-Step"
- **Current:** `Number of origins $n_h = T - T_0 - H + 1$ for $h=H$;`
- **Proposed:** `Number of usable origins at horizon $h$: $n_h = T - T_0 - h + 1$; at the maximum horizon $h=H$: $n_H = T - T_0 - H + 1$.`
- **Severity:** MINOR

Left-hand side uses subscript `h` (general) but right-hand side uses maximum `H`. Students computing origin counts for intermediate horizons (h=1, 3, …) will get wrong results using the current formula.

---

### Issue 9: "Fail to reject" bullet ends abruptly
- **Location:** Lines 483–484, frame "Interpreting the DM Test"
- **Current:** `\item Fail to reject: insufficient evidence --- do not conclude models are equal`
- **Proposed:** `\item Fail to reject $H_0$: insufficient evidence that models differ --- do not interpret as evidence of equality`
- **Severity:** MINOR

The positive framing (cannot conclude they differ) is missing. Adding `$H_0$` label and both directions of inference is pedagogically complete.

---

### Issue 10: Citation embedded in frame title bar
- **Location:** Line 102
- **Current:** `\begin{frame}{Forecast Accuracy Metrics \parencite{Hyndman2006}}`
- **Proposed:** `\begin{frame}{Forecast Accuracy Metrics}` with citation moved inside body as `\muted{\footnotesize\parencite{Hyndman2006}}`
- **Severity:** MINOR

All L01–L05 lectures place citations inside slide body or muted footnote, not in the frametitle bar. The current form is visually cluttered and inconsistent.

---

### Issue 11: Final section lacks `\sectionslide`
- **Location:** Lines 638–641
- **Current:** `\section{Key Takeaways and Roadmap}` followed immediately by `\begin{frame}{Key Takeaways}`
- **Proposed:** Insert `\sectionslide{Key Takeaways and Roadmap}{...}` between lines 638 and 641, or add comment `% intentionally no sectionslide for concluding section`
- **Severity:** MINOR

All five preceding sections have `\sectionslide` openers. Sixth section does not — creating an inconsistent visual rhythm.

---

### Issue 12: No `\label` on sections
- **Location:** Lines 32, 95, 265, 414, 526, 638
- **Proposed:** Add `\label{sec:...}` after each `\section{...}` command
- **Severity:** MINOR

Forces hardcoded numbers in cross-references (see Issue 4). Low-cost defensive practice.

---

### Issue 13: ML "Minimal" assumptions overstated
- **Location:** Line 684, frame "What's Next: Machine Learning for Forecasting"
- **Current:** `Assumptions & Linearity, normality & Minimal \\`
- **Proposed:** `Assumptions & Linearity, normality & Fewer formal, but stationarity helpful \\`
- **Severity:** MINOR

"Minimal" risks the misconception that ML models are assumption-free. Lecture 7 will need to correct this.

---

### Issue 14: `e^+`/`e^-` LaTeX encoding should use braces
- **Location:** Lines 172–173
- **Current:** `$L(e) = c_1 e^+ + c_2 e^-$`
- **Proposed:** `$L(e) = c_1 e^{+} + c_2 e^{-}$`
- **Severity:** MINOR

Without braces, source is ambiguous (superscript vs. function notation). Using `{+}` and `{-}` makes intent explicit.

---

### Issue 15: Walk-forward sectionslide subtitle is a sentence fragment
- **Location:** Line 269, `\sectionslide` for "Walk-Forward Validation"
- **Current:** `A single test set gives one data point. Walk-forward gives a distribution.`
- **Proposed:** `A single test set yields one error estimate. Walk-forward validation yields a distribution of errors across forecast origins.`
- **Severity:** MINOR

"Walk-forward gives" is a sentence fragment (subject should be "Walk-forward validation"). "Gives" is informal; "yields" is standard academic register.

---

## Summary Table

| # | Location | Issue | Severity |
|---|----------|-------|----------|
| 1 | Line 541 | Combination variance: `2ρσ₁₂` → `2ρσ₁σ₂` | CRITICAL |
| 2 | Lines 189-191 | MAPE asymmetry direction inverted | CRITICAL |
| 3 | Lines 172-173 | `e⁺`/`e⁻` undefined | MAJOR |
| 4 | Line 379 | "Section~2" cross-reference opaque | MAJOR |
| 5 | Lines 546-548 | "consistently" overstates BatesGranger1969 | MAJOR |
| 6 | Line 127 | `naive` missing accent | MAJOR |
| 7 | Header | `\MASE` macro missing | MAJOR |
| 8 | Line 381 | `n_h` uses `H` instead of `h` | MINOR |
| 9 | Lines 483-484 | "Fail to reject" bullet incomplete | MINOR |
| 10 | Line 102 | Citation in frame title bar | MINOR |
| 11 | Lines 638-641 | Final section missing `\sectionslide` | MINOR |
| 12 | Lines 32,95,265… | No `\label` on sections | MINOR |
| 13 | Line 684 | ML "Minimal" assumptions oversimplified | MINOR |
| 14 | Lines 172-173 | `e^+` needs braces `{+}` | MINOR |
| 15 | Line 269 | Walk-forward subtitle fragment | MINOR |
