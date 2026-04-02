# Proofreading Report: Lecture08_Regularization.tex

**File:** `Slides/Lecture08_Regularization.tex`
**Reviewer:** Proofreading Agent
**Date:** 2026-02-28

---

## Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 0 |
| MAJOR    | 11 |
| MINOR    | 8 |
| **Total**| **19** |

---

### Issue 1: Cross-section reference "Section~6" is incorrect — tuning is Section 5
- **Location:** Line 128, frame "Penalized Regression: General Form"
- **Current:** `"The tuning of $\lambda$ (and $\alpha$ for Elastic Net) is covered in Section~6."`
- **Proposed:** `"The tuning of $\lambda$ (and $\alpha$ for Elastic Net) is covered in Section~5."`
- **Severity:** MAJOR

Section 5 = Tuning λ via Cross-Validation; Section 6 = Application to Forecasting. The reference is wrong by one section.

---

### Issue 2: `\mathrm{Var}` and `\mathrm{MSE}` instead of `\Var` / `\MSE` macros
- **Location:** Lines 75, 82, 92 (frame "The Bias--Variance View" and its keybox)
- **Current:** `\mathrm{Var}(\hat{\bm{\beta}}_{\mathrm{OLS}})`, `\mathrm{Var}(\hat{\bm{\beta}}_{\lambda})`, `$\mathrm{MSE} = \mathrm{Bias}^2 + \mathrm{Var} + \sigma^2$`
- **Proposed:** `\Var(...)`, `\Var(...)`, `$\MSE = \mathrm{Bias}^2 + \Var + \sigma^2$`
- **Severity:** MAJOR

`header.tex` defines `\Var` as `\operatorname{Var}` and `\MSE` as `\operatorname{MSE}`. `\mathrm` bypasses correct operator spacing. Three instances — all must use the macros for consistency with L06, L07, and all other lectures.

---

### Issue 3: `\alpha` disambiguation note appears 4 sections after first use
- **Location:** Line 119 (first use, Section 1 table) vs. line 471 (disambiguation note, Section 4)
- **Current:** `\alpha` as EN mixing parameter first appears in Section 1's comparison table, but the disambiguation note ("not ETS α, not ECM α") only appears in the Section 4 overview.
- **Proposed:** Add disambiguation note immediately after the comparison table in Section 1: `\muted{\footnotesize\itshape Note: $\alpha$ here is the Elastic Net L1/L2 mixing parameter --- distinct from ETS level-smoothing $\alpha$ (L03) and ECM speed-of-adjustment $\alpha$ (L05).}`
- **Severity:** MAJOR

---

### Issue 4: "penalised" — British spelling (frame body, line 102)
- **Location:** Line 102
- **Current:** `All penalised regression methods solve:`
- **Proposed:** `All penalized regression methods solve:`
- **Severity:** MAJOR

Frame title on line 100 correctly reads "Penalized Regression" (American). Body text on line 102 uses British spelling — inconsistent within a single frame.

---

### Issue 5: "minimises" → "minimizes" (line 563)
- **Location:** Line 563
- **Current:** `select $\lambda^*$ that minimises out-of-sample prediction error`
- **Proposed:** `select $\lambda^*$ that minimizes out-of-sample prediction error`
- **Severity:** MAJOR

---

### Issue 6: "regularised" → "regularized" (line 579)
- **Location:** Line 579
- **Current:** `Fit regularised model on each train fold`
- **Proposed:** `Fit regularized model on each train fold`
- **Severity:** MAJOR

---

### Issue 7: "regularisation" → "regularization" (line 764)
- **Location:** Line 764
- **Current:** `What survives LASSO regularisation on RSXFS?`
- **Proposed:** `What survives LASSO regularization on RSXFS?`
- **Severity:** MAJOR

---

### Issue 8: "Regularised" in frame title → "Regularized" (line 801)
- **Location:** Line 801
- **Current:** `\begin{frame}{Forecast Comparison: SARIMA vs.\ Regularised Models}`
- **Proposed:** `\begin{frame}{Forecast Comparison: SARIMA vs.\ Regularized Models}`
- **Severity:** MAJOR

Frame titles appear in the header and table of contents — British spelling is visible in both.

---

### Issue 9: "regularised" → "regularized" (line 826)
- **Location:** Line 826
- **Current:** `All regularised models beat SARIMA on this feature set`
- **Proposed:** `All regularized models beat SARIMA on this feature set`
- **Severity:** MAJOR

---

### Issue 10: "regularisation" → "regularization" (line 831)
- **Location:** Line 831
- **Current:** `(shared regularisation) or when many external regressors exist`
- **Proposed:** `(shared regularization) or when many external regressors exist`
- **Severity:** MAJOR

---

### Issue 11: "regularisation" / "penalised" → American English (lines 847, 861)
- **Location:** Lines 847, 861
- **Current (847):** `regularisation — the bias--variance tradeoff at work`
- **Current (861):** `capture nonlinearities that penalised linear models cannot`
- **Proposed (847):** `regularization —...`
- **Proposed (861):** `...that penalized linear models cannot`
- **Severity:** MAJOR

---

### Issue 12: `\parencite` inside `\sectionslide` arguments — fragile (lines 292, 462)
- **Location:** Lines 292 (LASSO section), 462 (Elastic Net section)
- **Current:** `\sectionslide{LASSO Regression (L1)}{... \parencite{Tibshirani1996}.}` and `\sectionslide{Elastic Net}{... \parencite{ZouHastie2005}.}`
- **Proposed:** Remove `\parencite` from `\sectionslide` arguments. Both citations already appear correctly in the corresponding Section Overview frames (lines 297, 468).
- **Severity:** MINOR

`\sectionslide` passes its argument through a macro; citation commands in moving arguments risk fragility with biblatex/hyperref.

---

### Issue 13: Bias-variance keybox lacks `\parencite{Hastie2009}` citation
- **Location:** Lines 90--94, keybox in "The Bias--Variance View" frame
- **Current:** Formula `$\MSE = ...$` with no citation
- **Proposed:** Add `\muted{\footnotesize\parencite{Hastie2009}}` at end of keybox body
- **Severity:** MINOR

L07 cites Hastie2009 for the identical formula. Consistent attribution requires the same citation here.

---

### Issue 14: `mean_squared_error` used in code listing but not imported
- **Location:** Line 740, right-column code listing
- **Current:** `mean_squared_error(y_test, y_pred)` — function called but not imported
- **Proposed:** Add to import block in left column: `from sklearn.metrics import mean_squared_error`
- **Severity:** MINOR

Students copying the code would receive a `NameError`.

---

### Issue 15: Missing article "a" — sectionslide subtitle (line 34)
- **Location:** Line 34, `\sectionslide` for Section 1
- **Current:** `Regularization trades a little bias for large variance reduction.`
- **Proposed:** `Regularization trades a little bias for a large variance reduction.`
- **Severity:** MINOR

The Section Overview frame (line 39) correctly has "a large variance reduction."

---

### Issue 16: sklearn `alpha` comment misleading for Elastic Net users (line 725)
- **Location:** Line 725, code listing
- **Current:** `# sklearn 'alpha' = our lambda (penalty strength)`
- **Proposed:** `# sklearn 'alpha' = our lambda (penalty strength) for Ridge/Lasso.`\
  `# For ElasticNet: sklearn 'alpha'=lambda, 'l1_ratio'=our alpha.`
- **Severity:** MINOR

Accurate for `Ridge()` but dangerously misleading for `ElasticNet()`, which uses `alpha` for penalty strength and `l1_ratio` for the mixing parameter (our `\alpha`).

---

### Issue 17: No `\label` on any `\section` declaration
- **Location:** Lines 29, 132, 288, 458, 556, 694, 838
- **Proposed:** Add labels; this would also make the `Section~5` reference in Issue 1 self-correcting.
- **Severity:** MINOR

---

## Summary Table

| # | Severity | Issue |
|---|----------|-------|
| 1 | MAJOR | "Section~6" wrong — tuning is Section 5 |
| 2 | MAJOR | `\mathrm{Var}` / `\mathrm{MSE}` → `\Var` / `\MSE` macros (3 instances) |
| 3 | MAJOR | `\alpha` disambiguation appears 4 sections after first use |
| 4 | MAJOR | "penalised" → "penalized" (line 102) |
| 5 | MAJOR | "minimises" → "minimizes" (line 563) |
| 6 | MAJOR | "regularised" → "regularized" (line 579) |
| 7 | MAJOR | "regularisation" → "regularization" (line 764) |
| 8 | MAJOR | "Regularised" in frame title → "Regularized" (line 801) |
| 9 | MAJOR | "regularised" → "regularized" (line 826) |
| 10 | MAJOR | "regularisation" → "regularization" (line 831) |
| 11 | MAJOR | "regularisation" / "penalised" → American English (lines 847, 861) |
| 12 | MINOR | `\parencite` inside `\sectionslide` args (lines 292, 462) |
| 13 | MINOR | Bias-variance keybox missing `\parencite{Hastie2009}` |
| 14 | MINOR | `mean_squared_error` not imported in code listing |
| 15 | MINOR | Missing article "a" before "large" (line 34) |
| 16 | MINOR | sklearn `alpha` comment misleading for Elastic Net |
| 17 | MINOR | No `\label` on any `\section` declaration |

**British-spelling count: 9 instances** across lines 102, 563, 579, 764, 801, 826, 831, 847, 861.
**Citation keys verified:** `HoerlKennard1970`, `Tibshirani1996`, `ZouHastie2005` — all correct in `Bibliography_base.bib`.
