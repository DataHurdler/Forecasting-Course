# Proofreading Report: Lecture10_NeuralNets.tex

**File:** `Slides/Lecture10_NeuralNets.tex`
**Reviewer:** Proofreading Agent
**Date:** 2026-02-28

---

## Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 0 |
| MAJOR    | 7 |
| MINOR    | 5 |
| **Total**| **12** |

---

### Issue 1: Fourth `\alpha` use with no disambiguation note
- **Location:** Frames "Attention: What the Model Learns to Focus On" and "Attention: Formal Definition"
- **Current:** `weight $\alpha_s$`, `\boldsymbol{\alpha}`, `$\alpha_{t-12}$` — no disambiguation note
- **Proposed:** Add after the "Scaled Dot-Product Attention" definitionbox: `\muted{\footnotesize\itshape Note: $\boldsymbol{\alpha}$ here denotes attention weights --- distinct from the ETS smoothing $\alpha$ (Lecture~03), ECM speed-of-adjustment $\alpha$ (Lecture~05), and Elastic Net mixing $\alpha$ (Lecture~08).}`
- **Severity:** MAJOR

The course has three established uses of `\alpha` (ETS smoothing L03, ECM adjustment L05, EN mixing L08). L10 introduces a fourth without a disambiguation note, violating the cross-lecture notation policy.

---

### Issue 2: Three different notations for attention weights across two slides
- **Location:** Line ~701 (bar chart y-axis) vs. definition box (`\boldsymbol{\alpha}`) vs. example box (`$\alpha_{t-12}$`)
- **Current:** `weight $\alpha_s$` (scalar), `\boldsymbol{\alpha}` (bold vector), `$\alpha_{t-12}$` (time-subscripted scalar) — three notations within two consecutive slides
- **Proposed:** Clarify in the definition box: "Weights $\boldsymbol{\alpha} = (\alpha_1,\ldots,\alpha_T)^\top$ sum to 1." Makes scalar/vector relationship explicit and aligns all three uses.
- **Severity:** MAJOR

---

### Issue 3: `\parencite` inside `definitionbox` titles — rendering risk
- **Location:** `\begin{definitionbox}{Vanishing Gradient \parencite{Bengio1994}}` and `\begin{definitionbox}{LSTM Gate Equations \parencite{Hochreiter1997}}`
- **Proposed:** Move citations to the body of each box. Change titles to `{Vanishing Gradient}` and `{LSTM Gate Equations}`, and add `\muted{\footnotesize\parencite{Bengio1994}}` / `\muted{\footnotesize\parencite{Hochreiter1997}}` as first body line.
- **Severity:** MAJOR

`\parencite` in tcolorbox title arguments is fragile (biblatex/hyperref interaction). Course convention (L06--L08) is citations in body only.

---

### Issue 4: Overflow risk — LSTM Gate Equations definitionbox
- **Location:** Frame "LSTM Gates: Forget, Input, Output", left column (0.56\textwidth)
- **Current:** `definitionbox` contains a six-equation `align*` (five gate/state equations + one hidden-state equation) plus prose defining `\sigma` and `\odot`, all in a narrow column.
- **Proposed:** Verify compiled output. If overflowing, split into two equation groups (gates: $f_t, i_t, \tilde{\mathbf{c}}_t, o_t$; state updates: $\mathbf{c}_t, \mathbf{h}_t$) across two frames, or apply `\small` inside the align environment.
- **Severity:** MAJOR

---

### Issue 5: Overflow risk — Hyperparameter table frame
- **Location:** Frame "LSTM Key Hyperparameters"
- **Current:** Four-column table + full-width `keybox` + Socratic note — total content is near frame capacity for 16:9 Beamer.
- **Proposed:** Verify compiled output. If overflowing, shorten "Effect" column entries or move Socratic note to a muted line at the bottom without preceding `\vspace`.
- **Severity:** MAJOR

---

### Issue 6: Overflow risk — Takeaways keybox
- **Location:** Frame "Lecture 10 Key Takeaways"
- **Current:** Single `keybox` with six-item enumerate at `\footnotesize`; items 3--6 are multi-line. Approximately 28--32 lines of content.
- **Proposed:** Verify compiled output. If overflowing, split into two slides ("Takeaways 1/2" and "2/2") or abbreviate items 5--6.
- **Severity:** MAJOR

---

### Issue 7: "it sees an unordered set of hidden states" — imprecise
- **Location:** Frame "Transformers and Practical Guidance", Socratic note
- **Current:** `"self-attention has no built-in sense of order --- it sees an unordered set of hidden states"`
- **Proposed:** `"self-attention treats its inputs as an unordered set of vectors --- it has no built-in notion of sequence position"` (hidden states are an RNN concept; self-attention operates on token embeddings)
- **Severity:** MAJOR

---

### Issue 8: Universal approximation claim lacks citation
- **Location:** Frame "From Linear Regression to a Single Neuron", `definitionbox{Activation Function}`
- **Current:** `"Non-linearity is what gives neural networks their universal approximation property."` — no citation; neither `Cybenko1989` nor `Hornik1991` is in `Bibliography_base.bib`
- **Proposed:** Either add bib entries and cite `\parencite{Cybenko1989}`, or soften to: `"Non-linearity enables neural networks to approximate arbitrary continuous functions (the \emph{universal approximation property})."`
- **Severity:** MAJOR

---

### Issue 9: `\sigma` dual use — generic activation then redefined as sigmoid
- **Location:** MLP section (generic activation function) vs. LSTM Gates frame (explicitly `$\sigma$ = sigmoid`)
- **Current:** `\sigma(\cdot)` introduced as generic nonlinear activation; later `$\sigma$ = sigmoid` is declared explicitly in LSTM gate equations — apparent redefinition.
- **Proposed:** In the LSTM section, add: "(here $\sigma$ denotes sigmoid specifically; cf.\ the generic activation $\sigma$ on slide 3)" or use `\mathrm{sigmoid}(\cdot)` in LSTM equations.
- **Severity:** MAJOR

---

### Issue 10: Socratic note on dropout vs. LASSO is slightly vague
- **Location:** Frame "LSTM Key Hyperparameters", Socratic note
- **Current:** `"What is the key difference between the two forms of regularization?"`
- **Proposed:** `"What is the key conceptual difference between dropout-based regularization and L1 penalty-based regularization (LASSO)?"`
- **Severity:** MINOR

---

### Issue 11: `$\sim$50,000` — spacing of approximation symbol
- **Location:** Frame "When Does LSTM Help?"
- **Current:** `"A two-layer LSTM with 64 units has $\sim$50,000 parameters."`
- **Proposed:** Use `${\approx}\,50{,}000$` or `approximately 50,000` for cleaner typesetting.
- **Severity:** MINOR

---

### Issue 12: No disambiguation note for learning rate `\eta`
- **Location:** Training section (learning rate definition)
- **Current:** `$\eta$` introduced as learning rate with no note about potential clash with other uses in course
- **Proposed:** Add `\muted{\footnotesize Not to be confused with prior uses of $\eta$ in the course.}` if any clash exists. Low priority — verify first.
- **Severity:** MINOR

---

## Summary Table

| # | Severity | Issue |
|---|----------|-------|
| 1 | MAJOR | 4th `\alpha` use (attention weights) — no disambiguation note |
| 2 | MAJOR | Three notations for attention weights across two slides |
| 3 | MAJOR | `\parencite` inside `definitionbox` titles (Bengio1994, Hochreiter1997) |
| 4 | MAJOR | Overflow risk: LSTM Gate Equations definitionbox (6 equations, narrow column) |
| 5 | MAJOR | Overflow risk: Hyperparameter table + keybox + Socratic note |
| 6 | MAJOR | Overflow risk: 6-item Takeaways keybox near frame capacity |
| 7 | MAJOR | "unordered set of hidden states" — imprecise for Transformers |
| 8 | MAJOR | Universal approximation claim uncited; no Cybenko/Hornik bib entry |
| 9 | MAJOR | `\sigma` dual use: generic activation → sigmoid in LSTM section |
| 10 | MINOR | Socratic note on dropout vs. LASSO slightly vague |
| 11 | MINOR | `$\sim$50,000` approximation symbol spacing |
| 12 | MINOR | Learning rate `\eta` — check for cross-lecture clashes |
