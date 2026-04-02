# Pedagogical Review: Lecture06_Evaluation.tex
**Date:** 2026-02-28
**Reviewer:** pedagogy-reviewer agent

---

## Summary

- **Patterns followed:** 8/13
- **Patterns violated:** 3/13
- **Patterns partially applied:** 2/13
- **Deck-level assessment:** This is the strongest-structured lecture in the series so far. The narrative arc is coherent, every section has a `\sectionslide` except the final concluding section, motivation precedes formalism throughout, and visuals (TikZ walk-forward diagram, horizon-profile chart, loss-differential bar chart) consistently appear before formal procedures. The two most significant structural problems are: (1) the DM test section compresses the formal statistic, HAC motivation, and interpretive example into two slides that would benefit from the two-slide decomposition strategy, with the formula appearing with minimal warm-up; and (2) keybox proliferation — 10 keyboxes across approximately 19 content slides (53%), exceeding the 50% ceiling. The concluding section lacks its `\sectionslide` transition, producing an inconsistent rhythm relative to all five preceding sections. These are medium-severity fixes. The deck is ready for commit after addressing the final sectionslide omission and reducing keybox density.

---

## Pattern-by-Pattern Assessment

### Pattern 1: Motivation Before Formalism
- **Status:** Followed
- **Evidence:** The deck opens with two motivating slides ("The Single-Split Trap," lines 39-67, and "Our Model Zoo," lines 70-92) before any metric formula appears. The single-split trap slide explicitly names three failure modes first (lines 44-49), then states requirements. The DM section uses the `\sectionslide` subtitle at line 419 ("Visual inspection says Model A looks better. The DM test asks: is the gap statistically real?") as an informal question before the formula. The Forecast Combination section opens with a portfolio analogy (lines 538-548) before any weight formula. Every section in the deck follows the "Why?" before "What?" structure.
- **Recommendation:** No action required.
- **Severity:** N/A

---

### Pattern 2: Incremental Notation
- **Status:** Partially Applied
- **Evidence:** The error-metrics slide (lines 102-137) introduces $e_{T+h}$, $y_{T+h}$, $\hat{y}_{T+h|T}$, $n$, $\bar{q}$, and all four metric operators on a single slide. That is six new symbols simultaneously, crossing the five-symbol threshold. The subscript $h$ in $\RMSE_h$ first appears in the metric definition without a prior explicit statement that these are horizon-specific quantities. The notation is then correctly extended to the two-subscript form $e_{t,h}$ on the walk-forward step-by-step slide (line 365), and a cross-reference note at lines 380-381 explicitly bridges the two notations — that cross-reference is excellent practice. The DM section introduces $d_t$, $g(\cdot)$, $\bar{d}$, $\widehat{\operatorname{se}}(\bar{d})$, and the HAC concept simultaneously within the definitionbox (lines 424-437): five new symbols/concepts in one box. The simpler "loss differential" concept is not built up from a numerical example before the full statistic appears.
- **Recommendation:** (1) On the metrics slide (line 103), precede the four formulas with a one-sentence statement: "Throughout, $h$ denotes forecast horizon and $n$ the number of forecast origins." This costs two lines and resolves the $n$ ambiguity. (2) For the DM definitionbox (lines 424-437), consider splitting: a first pass defines $d_t = g(e_{1t}) - g(e_{2t})$ and shows a numeric example (e.g., $d_1 = 3.2^2 - 2.8^2 = 1.60$), then the second pass states the full statistic. This aligns with Pattern 7 below.
- **Severity:** Medium

---

### Pattern 3: Worked Example After Every Definition
- **Status:** Followed
- **Evidence:** The `definitionbox{Four Metrics}` (lines 106-120) is followed immediately on the same slide by an inline decision guide (right column, lines 122-133) and then within one slide by the RMSE vs. MAE worked business scenario with the retail inventory `examplebox` (lines 167-174). The DM test `definitionbox` (lines 424-437) is followed on the very next slide (lines 453-491) by a concrete SARIMA vs. ETS interpretation with a TikZ bar chart of $d_t$ values and a worked decision rule. No two consecutive definition slides appear without an example or illustration between them.
- **Recommendation:** No action required.
- **Severity:** N/A

---

### Pattern 4: Progressive Complexity
- **Status:** Followed
- **Evidence:** The ordering is: (1) motivating problem and requirements → (2) error metrics (simplest: RMSE/MAE → relative: MASE → scale-free: MAPE) → (3) horizon profiles → (4) walk-forward validation (procedural complexity) → (5) DM test (inferential complexity) → (6) forecast combination (ensemble complexity) → (7) takeaways + ML preview. Within the metrics section, scale-dependent metrics (RMSE, MAE) precede scale-free (MASE, MAPE), which is the correct order for a student who has only seen RMSE in prior lectures. Within walk-forward, the visual diagram precedes the step-by-step recipe, which precedes the full results table. The DM test correctly waits until after walk-forward errors are established, since the DM statistic is defined in terms of $e_{t,h}$.
- **Recommendation:** No action required.
- **Severity:** N/A

---

### Pattern 5: Fragment Reveals for Problem → Solution
- **Status:** Followed (correctly absent per project rule)
- **Severity:** N/A

---

### Pattern 6: Standout Slides at Conceptual Pivots
- **Status:** Partially Applied
- **Evidence:** Five of the six `\section{}` declarations are paired with a `\sectionslide{}{}` call. The sixth section, "Key Takeaways and Roadmap" (line 639), has no `\sectionslide`. The `\begin{frame}{Key Takeaways}` at line 643 follows the `\section{}` declaration immediately — the same omission flagged in the proofreading report (Issue 11). The final section break produces no visual transition, creating an abrupt shift from "Combination in Practice" to the summary keybox.
- **Recommendation:** Insert `\sectionslide{Key Takeaways and Roadmap}{Five evaluation principles that apply from Lecture 1 through Lecture 12.}` between lines 640 and 642.
- **Severity:** Medium

---

### Pattern 7: Two-Slide Strategy for Dense Theorems
- **Status:** Violated
- **Evidence:** The "DM Statistic and Mechanics" frame (lines 423-450) is the primary violation. This single slide contains: (a) the formal definition of the loss differential $d_t = g(e_{1t}) - g(e_{2t})$, (b) the full DM statistic formula with asymptotic distribution ($DM \xrightarrow{d} \mathcal{N}(0,1)$), (c) the null hypothesis statement, (d) the HAC variance explanation, and (e) a `warningbox` with Newey-West bandwidth specification. That is five distinct conceptual elements on one slide. A student encountering $\widehat{\operatorname{se}}(\bar{d})$ for the first time has no interpretive scaffolding.
- **Recommendation:** Split into two slides. Slide 1 ("DM Test: Loss Differentials"): define $d_t = g(e_{1t}) - g(e_{2t})$ with a numeric example ($d_1 = 3.2^2 - 2.8^2 = 1.60$) and introduce $\bar{d}$, ending with a forward pointer. Slide 2 ("DM Test: The Statistic"): show full formula with `\underbrace` labels for $\bar{d}$ and $\widehat{\operatorname{se}}(\bar{d})$, plus $H_0$ and HAC motivation columns.
- **Severity:** High

---

### Pattern 8: Semantic Color Usage
- **Status:** Followed
- **Severity:** N/A

---

### Pattern 9: Box Hierarchy
- **Status:** Followed
- **Severity:** N/A

---

### Pattern 10: Box Fatigue (Per-Slide and Deck-Level)
- **Status:** Violated
- **Evidence:** Deck-level keybox count = 10 instances (lines 87, 122, 196, 248, 374, 513, 551, 626, 644, 672). The deck has approximately 19 content slides. 10 keyboxes = 53% of slides carry a keybox, just above the 50% ceiling. Total colored box count across all types = 17 across 19 content slides (89%). Specific low-value keyboxes: (1) Line 248 ("Always report accuracy by horizon") — transitional remark, not a key result. (2) Line 374 ("Walk-forward errors...track record") — motivational prose. (3) Line 551 ("If two models have equal accuracy...simple average outperforms") — could be bold italic inline.
- **Recommendation:** Demote 3 keyboxes to plain `\textbf{\textit{...}}` or `\muted{\small\itshape}`: lines 248-251, lines 374-378, lines 551-555. Reduces keybox count from 10 to 7 (37% of content slides).
- **Severity:** Medium

---

### Pattern 11: Socratic Embedding
- **Status:** Followed
- **Evidence:** Three embedded questions present (lines 135-136, 208-209, 522-523). All at slide bottoms as muted italic. Target of 2-3 met exactly.
- **Severity:** N/A

---

### Pattern 12: Visual-First for Complex Concepts
- **Status:** Followed
- **Severity:** N/A

---

### Pattern 13: Two-Column Definition Comparisons
- **Status:** Followed
- **Severity:** N/A

---

## Deck-Level Analysis

### Narrative Arc
Coherent five-act structure: (1) Evaluation Problem → (2) Error Metrics → (3) Walk-Forward → (4) DM Test → (5) Forecast Combination → (6) Takeaways/Roadmap. The Key Takeaways slide enumerates all five acts in order; the "What's Next" slide correctly reuses "Walk-forward; DM test" in the Evaluation row, demonstrating these tools carry forward.

**Minor gap:** The opening motivation (line 39) names "statistical testing to separate signal from noise" as a requirement but never explicitly closes that loop in the Key Takeaways summary. A single sentence at line 662 ("These four requirements, introduced in slide 2, are now met.") would provide complete narrative closure.

### Pacing
Content slide count by section: Evaluation Problem (2), Error Metrics (4), Walk-Forward (4), DM Test (3), Forecast Combination (3), Takeaways (2) = 18 content slides. No stretch of more than 4 consecutive theory-heavy slides.

**Pacing concern:** The transition from Section 5 (Combination in Practice, line 608) to Key Takeaways is abrupt — no visual break. The missing `\sectionslide` for Section 6 is the primary driver.

### Notation Consistency
Cross-lecture notation is well-managed. The $e_{T+h}$ → $e_{t,h}$ extension is explicitly bridged at lines 380-381.

**Inconsistency:** The RMSE formula in the metrics definitionbox (line 108) uses $e_{T+h}$ without an explicit sum index; the walk-forward RMSE (line 369) uses $\sum_t e_{t,h}^2$ explicitly. A note "(same formula, now averaging over origins $t$)" would close this gap.

**`\MASE` macro:** `header.tex` defines `\RMSE` and `\MAE` but not `\MASE`. Three occurrences of `\operatorname{MASE}` (lines 115, 197, 198) need replacement — cross-report consensus finding (also flagged as MAJOR in proofreading report).

### Student Concerns
1. **$\bar{q}$ in MASE** — footnote is muted/small; add "(see L01 benchmark models)" pointer.
2. **HAC undefined term** — add "(heteroskedasticity- and autocorrelation-consistent: robust to serial correlation)" parenthetical.
3. **DM test in Python** — no in-slide code hint; add note pointing to Lab 6 implementation.
4. **Clark-West correction** — mentioned but not explained; add parenthetical "(the null implies the larger model's extra terms are zero, making the $d_t$ distribution degenerate)."
5. **Combination puzzle theory** — acknowledge explicitly that the equal-weight result is primarily empirical, not a theoretical guarantee.
6. **ML bridge assumes regularization knowledge** — "Overfitting risk: Higher (regularize!)" cell implies L08 concepts before L07; change to "High (mitigated by CV)."

---

## Critical Recommendations (Top 5)

| # | Priority | Fix |
|---|----------|-----|
| 1 | HIGH | Split "DM Statistic and Mechanics" (lines 423-450) into two slides: "DM Test: Loss Differentials" (define $d_t$ + numeric example) + "DM Test: The Statistic" (full formula with `\underbrace` labels) |
| 2 | MEDIUM | Add `\sectionslide{Key Takeaways and Roadmap}{Five evaluation principles...}` before line 642 |
| 3 | MEDIUM | Demote 3 keyboxes (lines 248, 374, 551) to plain bold italic |
| 4 | MEDIUM | Add `\MASE` macro to `Preambles/header.tex`; replace `\operatorname{MASE}` at lines 115, 197, 198 (cross-report consensus with proofreading Issue 7 — already done in prior fix pass) |
| 5 | MEDIUM | Strengthen ML bridge: fix "Minimal" assumptions → "Fewer formal (stationarity helpful)"; add walk-forward-to-CV sentence; add "(Ridge, LASSO — Lecture 8)" pointer |

---

## Appendix: Quantitative Summary

| Metric | Count | Target | Status |
|--------|-------|--------|--------|
| `\sectionslide` calls | 5 | 6 (one per section) | Missing 1 |
| `keybox` instances | 10 | ≤ 9 for 19 content slides | Slightly over |
| `definitionbox` instances | 2 | — | Appropriate |
| `warningbox` instances | 4 | — | Appropriate |
| `examplebox` instances | 1 | — | Low (acceptable) |
| Socratic questions | 3 | 2-3 | Met |
| TikZ/visual slides | 4 | — | Good distribution |
| Content slides | ~19 | — | Compact lecture |
| Total frames (incl. structural) | ~26 | — | — |
