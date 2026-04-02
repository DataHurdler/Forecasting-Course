# Pedagogical Review: Lecture10_NeuralNets.tex
**Date:** 2026-02-28
**Reviewer:** pedagogy-reviewer agent

---

## Summary

- **Patterns followed:** 10/13
- **Patterns violated:** 2/13
- **Patterns partially applied:** 1/13
- **Deck-level assessment:** One of the stronger lectures in the series. Narrative arc from feedforward → RNN → LSTM → attention is coherent and well-paced. Motivation precedes every major concept, TikZ diagrams appear before or alongside notation, and the RSXFS thread anchors all abstractions. Three weaknesses: (1) no `\sectionslide{}{}` at any of seven section boundaries; (2) three slides exceed the two-box maximum (most critically, the LSTM Gates slide has four boxes); (3) two Socratic questions meet the lower bound but a third would strengthen the lecture. These are medium-severity issues.

---

## Pattern-by-Pattern Assessment

### Pattern 1: Motivation Before Formalism — **Followed**
Deck opens with concrete prior result (XGBoost RMSE 2,250) and a specific limitation (no temporal memory) before any formal notation. Every section overview previews purpose before notation.

### Pattern 2: Incremental Notation — **Followed**
Notation introduced carefully in layers. FFN starts with familiar $\hat{y} = \mathbf{w}^\top \mathbf{x} + b$ (Lecture 02), adds only $\sigma(\cdot)$. RNN introduces 3 new symbols on one slide. LSTM gate equations introduce six simultaneously but with structural template and plain-English labels. $\lambda_{\max}$ disambiguation footnote proactively prevents confusion with regularization $\lambda$.

**Recommendation (Low):** On LSTM gates slide, add one sentence recalling that $\mathbf{h}_{t-1}$ and $\mathbf{x}_t$ were already defined in the RNN section.

### Pattern 3: Worked Example After Every Definition — **Followed**
No two consecutive definition-only slides. Activation function → "Why ReLU?" examplebox on same slide. RNN update rule → "Analyst Analogy" examplebox on same slide. LSTM gates → three per-gate exampleboxes on same slide.

### Pattern 4: Progressive Complexity — **Followed**
Exemplary: FFN (no memory) → vanilla RNN (sequential, flawed) → LSTM (gated, robust) → attention (direct access) → application.

### Pattern 5: Fragment Reveals — **Followed (correctly absent)**
No overlay commands. Correct per project rule.

### Pattern 6: Standout Slides at Conceptual Pivots — **Violated (Medium)**
Seven section boundaries; none uses `\sectionslide{}{}`. Each opens with a "Section Overview" keybox frame visually identical to content slides. Most jarring: the RNN-to-LSTM transition ends with "The fix: LSTM introduces gating mechanisms" then immediately enters another keybox.

**Recommendation:** Insert `\sectionslide{}{}` at minimum at three largest conceptual pivots: RNN→LSTM (between lines ~407–413), LSTM→Attention (between lines ~651–655), and Attention→Keras (between lines ~789–793). Ideally all seven.

### Pattern 7: Two-Slide Strategy for Dense Theorems — **Partially Applied (Medium)**
Good structural split: gate equations on Slide 11, cell diagram on Slide 12. However: (1) Slide 11 has no forward pointer ("Cell data flow on next slide"); (2) the six equations share a structural template but the common structure is not made explicit with color coding or `\underbrace{}`.

**Recommendation:** Add forward pointer at bottom of LSTM gates slide left column. Define concatenation bracket notation: "where $[\mathbf{h}_{t-1}, \mathbf{x}_t]$ denotes horizontal concatenation."

### Pattern 8: Semantic Color Usage — **Followed**
Blue = input, green = hidden, red = output — consistent across FFN and RNN TikZ diagrams. Attention bar chart uses blue/green semantically for seasonal vs. momentum lag. Box type colors are semantically correct.

### Pattern 9: Box Hierarchy — **Followed**
All box types semantically correct throughout. definitionbox = formal definitions, examplebox = business analogies, warningbox = pitfalls, keybox = key results.

### Pattern 10: Box Fatigue — **Violated (Medium)**
Three slides exceed the two-box maximum:
- "LSTM Gates: Forget, Input, Output" (lines 423–476): 1 definitionbox + 3 exampleboxes = **4 boxes**
- "Why Vanilla RNNs Fail" (lines 362–407): 1 definitionbox + 1 warningbox + 1 keybox = **3 boxes**
- "When Does LSTM Help?" (lines 888–930): 1 warningbox + 1 examplebox + 1 keybox = **3 boxes**

Deck-level: ~14 keyboxes across 24 content slides ≈ 58% of slides.

**Recommendation:** LSTM Gates — demote 3 exampleboxes to plain bold-italic prose. "Why Vanilla RNNs Fail" — demote transitional keybox to italic bridge text or move to LSTM overview. "When Does LSTM Help?" — merge keybox into examplebox or demote keybox.

### Pattern 11: Socratic Embedding — **Partially Applied (Low)**
Two Socratic questions: line 646 (dropout vs LASSO) and line 784 (positional encoding). Meets the lower bound of 2; target is 2–3.

**Recommendation:** Add one question at the RNN unrolled diagram slide: "The same weight matrices $\mathbf{W}_h$ and $\mathbf{W}_x$ apply at every time step. What does shared-parameter constraint imply about how the model treats January vs July?"

### Pattern 12: Visual-First for Complex Concepts — **Followed**
Attention bar chart (visualization) precedes formal scaled dot-product definition. FFN diagram is simultaneous with equation. One minor gap: LSTM gate equations precede cell diagram — opposite order from attention. Swapping Slides 11/12 would align with visual-first convention but is low priority.

### Pattern 13: Two-Column Comparisons — **Followed**
Linear regression → single neuron comparison, LSTM vs XGBoost, and full leaderboard all use two-column layouts appropriately.

---

## Critical Recommendations (Top 5)

| # | Priority | Fix |
|---|----------|-----|
| 1 | MEDIUM | Insert `\sectionslide{}{}` at RNN→LSTM, LSTM→Attention, and Attention→Keras pivots (minimum); ideally all seven boundaries |
| 2 | MEDIUM | Fix LSTM Gates slide: demote 3 exampleboxes to plain bold-italic prose; add forward pointer "(Cell data flow on next slide.)" and define bracket concatenation notation |
| 3 | MEDIUM | Fix "Why Vanilla RNNs Fail": demote transitional keybox to italic text |
| 4 | MEDIUM | Fix "When Does LSTM Help?": demote keybox or merge with examplebox |
| 5 | LOW | Add third Socratic question at RNN Unrolled slide; add data standardization comment to Keras code listing |

---

## Student Concerns

1. `$[\mathbf{h}_{t-1}, \mathbf{x}_t]$` — concatenation notation not defined; may be read as 2-element array
2. Gates are vectors but not bold — inconsistency with bold/non-bold convention
3. How does $f_t \in (0,1)$ avoid vanishing gradients? The $+$ operation preserving gradients is not explained
4. Keras code has no standardization step — raw RSXFS values will cause slow convergence
5. `gap=1` in `TimeSeriesSplit` not called out in surrounding prose

---

## Appendix: Quantitative Summary

| Metric | Count | Target | Status |
|--------|-------|--------|--------|
| `\sectionslide` calls | 0 | 7 | **Violated** |
| Slides with >2 boxes | 3 | 0 | **Violated** |
| Socratic questions | 2 | 2–3 | Low (meets minimum) |
| TikZ/visual slides | 4 | — | Good |
| Content slides | ~24 | — | — |
