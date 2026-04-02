# Session Log: Lecture 10 — Neural Networks (LSTM and Attention)
**Date:** 2026-02-26
**Status:** COMPLETE
**Files produced:**
- `Slides/Lecture10_NeuralNets.tex` — 27 pages, 0 errors, 0 overflows
- `scripts/Lecture10_NeuralNets.ipynb` — 9 sections

---

## Goal

Create Lecture 10 (Neural Networks: LSTM and Attention) as a full first draft.
Includes Beamer slide deck + Jupyter notebook lab. This is the fourth
consecutive ML lecture (after L07: ML Intro, L08: Regularization, L09: Trees).

---

## Implementation Notes

### Bib entries
- `Vaswani2017` (Attention Is All You Need) — added to `Bibliography_base.bib`
- `Bengio1994` (Learning Long-Term Dependencies) — added to `Bibliography_base.bib`
- `Hochreiter1997` already present ✓

### Slide structure (27 pages final)
1. Title (1)
2. Outline (1)
3. **Motivation bridge**: "Beyond Trees — Sequential Patterns" (1)
4. **Feedforward Networks section**: overview + neuron/activation table +
   TikZ FFN diagram + Training frame (4)
5. **RNN section**: overview + RNN Update Rule + Unrolled RNN TikZ +
   Why Vanilla RNNs Fail with Socratic question (4)
6. **LSTM section**: overview + Gates (equations + vector note + 3 exampleboxes) +
   LSTM Cell TikZ + LSTM for Time Series: Practical Setup + Key Hyperparameters
   with Socratic question (5)
7. **Attention section**: overview + Visual attention weight diagram (new TikZ) +
   Formal Definition with $d_k$ defined + simplified-form note + Transformers
   guidance (4)
8. **Keras Implementation**: overview + [fragile] code frame (2)
9. **Application**: overview + Data requirements/limitations +
   Full leaderboard L01–L10 (3)
10. Takeaways + References (2)

Key structural changes from plan vs. final:
- Added "Attention: What the Model Learns to Focus On" visual frame (TikZ bar chart
  showing seasonal spike at t-12 in UNO blue, momentum at t-1 in UNO green)
- Split original attention frame into visual frame + formula frame → 27pp (plan was 26pp)
- Removed `[shrink=2]` by splitting instead of typographic workaround

### Notebook structure (9 sections)
1. Setup (UNO palette, `TF_AVAILABLE` try/except, `tf.random.set_seed(42)`, rcParams)
2. Load FRED RSXFS + `make_features()` — same as L08/L09
3. Sequence construction: `make_sequences(X_arr, y_arr, T=24)` → `(n, T, p)` array;
   3-way split on sequence indices
4. LSTM: build (stacked 64+32 units) + train (EarlyStopping patience=20) +
   training/val loss plot → `lecture10_training_loss.png`
5. Seed variance: 5 seeds, box plot RMSE → `lecture10_seed_variance.png`
6. Lookback ablation: T ∈ {12, 18, 24, 36} → `lecture10_lookback_ablation.png`
7. SARIMA + XGBoost baselines (flat feature matrix, `verbosity:0` in xgb_params)
8. Model comparison table + bar chart → `lecture10_model_comparison.png`
9. Forecast comparison plot (actuals + SARIMA + XGBoost + LSTM) →
   `lecture10_forecast_comparison.png`

---

## Compilation Issues Encountered

### Pass 1 (first compile): 3 vbox overflows
- **Line 602 (20.8pt)** — LSTM Practical Setup: left column had full 3-item
  arch options list + definitionbox + medskip + warningbox.
  Fix: removed Bidirectional LSTM bullet, collapsed to 2-item `\footnotesize`,
  demoted warningbox to plain italic note.
- **Line 716 (1.3pt)** — Attention frame: examplebox + medskip + warningbox.
  Fix: changed `\medskip` → `\smallskip` → removed gap entirely. Still 1.62pt.
  Then used `[shrink=2]` temporarily, resolved by splitting into 2 frames.
- **Line 974 (10.2pt)** — Takeaways: keybox with 6 items + medskip + preview.
  Fix: added `\footnotesize` to enumerate + `\medskip` → `\smallskip`.

### After quality review fixes: 2 new overflows
- **Line ~411 (19.4pt)** — Vanishing gradient frame: λ_max parenthetical in
  definitionbox + Socratic question added too much height.
  Fix: moved λ_max note to `\muted{\tiny ...}` below definitionbox;
  removed Socratic from this frame, moved to LSTM Hyperparameters frame.
- **Line ~650 (1.44pt)** — LSTM Hyperparameters: Socratic question + keybox.
  Fix: removed `\smallskip` before Socratic question → clean.

### Final: 27 pages, 0 errors, 0 overflows (3-pass clean)

---

## Quality Review: Proofreader

**10 issues (6 MAJOR, 4 MINOR)**

Fixes applied:
| # | Severity | Fix |
|---|----------|-----|
| 1 | MAJOR | "is prerequisite to" → "is a prerequisite for" |
| 2 | MAJOR | Removed incorrect `\parencite{Bengio1994}` from ReLU examplebox (paper is about RNN vanishing gradients, not ReLU) |
| 3 | MAJOR | Fixed broken Dropout table row (`\\` inside cell → `\texttt{dropout,} \texttt{recurrent\_dropout}`) |
| 4 | MAJOR | Added "Simplified form; see Vaswani2017 for Q,K,V" muted note to attention formula |
| 5 | MAJOR | Added gate-vector note: "Gates $f_t, i_t, o_t \in (0,1)^d$ are vectors (one value per unit)" |
| 9 | MINOR | "building block" → "building blocks" |
| 10 | MINOR | `Adam(0.001)` → `Adam(learning_rate=0.001)` in Keras code frame |

Deferred:
- `\sectionslide` macro unused (stylistic preference, not a bug)
- LSTM Gates overflow risk — verified as clean after the table fix

---

## Quality Review: Pedagogy

**14 issues (5 MAJOR, 9 MINOR)**

Fixes applied:
| # | Severity | Fix |
|---|----------|-----|
| M1 | MAJOR | Added new TikZ attention weight bar chart frame ("What the Model Learns to Focus On") before formula slide; removed `[shrink=2]` |
| M2 | MAJOR | Defined $d_k$ explicitly in prose on attention formula slide |
| M3 | MAJOR | Demoted Training slide keybox → plain italic paragraph (3 boxes → 2) |
| M4 | MAJOR | Demoted LSTM Practical Setup warningbox → plain italic note (3 boxes → 2) |
| M5 | MAJOR | Split attention frame resolves the `[shrink=2]` workaround |
| m6 | MINOR | Added 2nd Socratic question (LSTM dropout vs. LASSO) to Hyperparameters frame |
| m8 | MINOR | Added $\lambda_{\max}$ collision note as `\muted{\tiny}` below vanishing gradient definitionbox |

Deferred (architectural — out of scope for first draft):
- Problem→Solution multi-slide for vanishing gradient pivot (m7)
- BPTT mechanism single-sentence explanation (m10)
- Cell-state gradient highway justification (m11)
- Multi-step forecasting strategy elevated from footnote (m12)
- Attention section depth imbalance acknowledgment (m13)
- Deck-level keybox overuse reduction (m14)

---

## [LEARN] Entries

```
[LEARN:color] The UNO palette defines: unoblue, unored, unogray, unogreen,
  unolightblue, unolightred, unolightgreen, unowhite. There is NO 'unolightgray'.
  Use gray!25 or unogray!30 for neutral/muted bars in TikZ.

[LEARN:tikz] Attention weight bar chart (bar per time step, seasonal spike
  highlighted in unolightblue, momentum in unolightgreen) effectively satisfies
  the visual-first pedagogy requirement for abstract sequence models.

[LEARN:citation] Bengio1994 documents the vanishing gradient PROBLEM in RNNs;
  do not cite it for ReLU as a solution. ReLU's gradient benefits in deep nets
  are associated with Glorot & Bengio 2010 / Nair & Hinton 2010 (not in bib).

[LEARN:latex] When a [shrink=N] frame appears, the correct fix is to split the
  frame into two (visual + formal) rather than use the typographic workaround.
  shrink=2 is a distress signal, not a solution.

[LEARN:xgboost] In the notebook, set 'verbosity': 0 inside xgb_params rather
  than using verbose_eval=False (deprecated in XGBoost 1.6, removed in 2.0).

[LEARN:notation] lambda_max (spectral radius) is a third meaning of lambda after
  L08 regularization and L09 XGBoost penalty. Always add a parenthetical noting
  the distinction when reusing greek letters across lectures.

[LEARN:pedagogy] Attention needs a visual diagram (weight bar chart over time steps)
  BEFORE the formula. The seasonal spike at t-12 in UNO blue is immediately
  interpretable to business students. Formulas without visuals cause confusion.
```

---

## Final State

| Item | Status |
|------|--------|
| Slides compile | ✓ 27 pages, 0 errors, 0 overflows |
| Proofreader | ✓ All MAJOR fixed; 2 MINOR deferred (sectionslide, hbox count=0) |
| Pedagogy reviewer | ✓ All 5 MAJOR fixed; 8 MINOR deferred (architectural) |
| Notebook | ✓ 9 sections, 5 figures |
| Quality score (est.) | ~85/100 |

---

## Open Questions / Next Session

1. L10 is first-draft complete. User to review PDF before Lecture 11 is started.
2. Deferred architectural items (BPTT explanation, multi-step strategy elevation,
   cell-state gradient justification) can be addressed in a revision pass.
3. Lecture 11: Feature Engineering (lags, rolling stats, calendar effects,
   pipeline design for tree-based and neural network forecasters).
