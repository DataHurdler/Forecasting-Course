# Plan: lab recording scripts for Labs 4–12

**Date:** 2026-08-31 · **Status:** IN PROGRESS

Labs 1–3 shipped scripts on 2026-08-27. Eleven labs remain: 4, 5, 6, 7, 8, 9 Part 1,
9 Part 2, 10, 11 Part 1, 11 Part 2, 12.

## Method (per lab)

1. Read `Labs/LectureNN_lab.qmd`.
2. Extract the `{python}` chunks and run them in `.venv` to capture **measured** output —
   the scripts quote real numbers, never numbers copied from the prose.
3. Compare the lab's prose claims against that output. Every script so far has turned up at
   least one claim the output does not support; fix the lab, note the fix in the script.
4. Write `Narration/LectureNN_lab_script.md` in the established shape: how-to-use → corrections
   → in-room language to replace → OPENING → SETUP → STEP n → BEFORE YOU LEAVE → appendix table
   of expected output + "things to know before recording".
5. Re-render the lab and copy the HTML into `docs/labs/` if the `.qmd` changed.

## Verification gates

- Every number in a script traceable to a captured run, not to the lab's prose.
- Lab still renders after any correction.
- `docs/labs/` HTML matches the corrected `.qmd`.

## Log

- **Lab 4** — done. Correction applied: Step 3's "you built a small Random Forest by hand" is
  bagging, not a forest — Lecture 5 defines the difference as exactly the feature subsampling
  this lab omits. Lab 5's opening had the same slip; both fixed and re-rendered.
- **Lab 5** — done. Two corrections. (1) Step 6's grid moved learning rate and tree count at the
  same time, so it slid along the `lr x n` ridge and never showed overfitting; the prose claimed
  the `lr=0.3` row had the lowest training error and worst test error, when measured it had
  neither (train 95, test 238 — the *best* test error in the grid). Grid now holds `lr=0.1` and
  sweeps rounds 100/300/1000/3000: test 244/243/250/253, which turns up and mirrors Step 2's
  forest curve that never does. (2) Step 5 called MDI's `avg_price` score "non-trivial"; it is
  0.017, ninth of ten. Replaced with the true contrast against `is_event` (MDI 0.017 > 0.012;
  permutation 0.0 < 22.3), which is the high-cardinality bias — 173 distinct prices vs 2.
  Scoreboard deliberately keeps `lr=0.1, n=100` (244) rather than the grid's best test number.
- **Lab 6** — done. No corrections needed; every prose claim survived the measurement pass,
  including the multiples-of-7 survivors and the CV-pessimism argument. Script adds two numbers
  the lab does not print: OLS's *training* RMSE at n=120 (145, against a test RMSE of 3.6M), and
  the fold average with and without the starved first fold (323 vs 296, test 286).
- **Lab 7** — done. Numbers were exact: the callout's "about 100 RMSE" single-seed advantage
  measures 102, and the five-seed means differ by 4, as written. One correction: Step 5's broken
  model "lands around 7,400" — measured 7,325 (the 3.4x-worse-than-benchmark claim is unaffected).
  Verified the three carried-in figures: seasonal naive **2,152** recomputes exactly on the same
  1,590 test weeks, and LASSO 744 / XGBoost 781 match Lecture 8, Lecture 13 (both formats), and
  Labs 8 and 9 Part 2.
- **Lab 8** — done. Two corrections. (1) Step 4's window experiment ran **2 seeds** per window and
  concluded a longer window "hurts, monotonically" from gaps of 64 and 27 — the exact error Lab 7
  exists to teach against. Re-ran at 5 seeds: 13w 975+/-48, 26w 984+/-87, 52w 1094+/-35, so 13 and
  26 are indistinguishable and only the 52-week penalty is real. Step 4 now runs 3 seeds per
  window (reusing Step 3's three flatten runs for W=26 — 6 new fits, not 9) and prints the runs:
  980/42, 1032/80, 1103/26. Callout rewritten to reject the middle comparison (52 vs sd 80) and
  claim only the ends (123 RMSE, no overlap: worst 13-week run 1,039 < best 52-week run 1,068).
  (2) Slow-cell warning said "roughly two minutes apiece"; measured, Step 3 is ~4 min and Step 4
  ~3 min.
- **Cross-lab scoreboard audit** (zero-compute pass): the hard-coded figures agree everywhere —
  Lab 8 quotes the FFN at 1,084 (Lab 7's five-seed mean, not its seed-1 draw), Lab 9 Part 2 quotes
  the CNN at 1,032, Lecture 8's deck table carries 1,032 / 1,418 / 1,534 with 8,161 parameters,
  and Lecture 13's course scoreboard carries 744 / 781 / 842 / 899 / 987 / 990 / 1,032 / 2,152.
  **One gap for the owner:** Lecture 13's scoreboard says "every model in this course, on the M5
  weekly panel" but omits the FFN (1,084). Consistent with the deck-measured convention (Lecture 7
  reports no FFN RMSE), so left alone — adding a row would also disturb the "fifth and sixth of
  eight" prose.
- **Lab 8 shipped** — re-rendered and synced to `docs/labs/`; the rendered Step 4 table matches
  the script's appendix exactly (980/42, 1032/80, 1103/26).
- **Open framing question (owner, 2026-08-31).** Owner flagged that "the RNN wins at every
  window" should be stated cautiously *even though the lab's numbers support it*. Agreed, on two
  grounds. (1) **Generality:** the a priori expectation runs the other way — gating exists because
  vanilla RNNs fail on long dependency chains — so this is a dataset-specific result that
  contradicts the default, and a student can easily carry away "RNNs beat LSTMs" as a fact. What
  generalizes is the conditional the deck already states: *an LSTM solves a problem this data does
  not have*. (2) **Evidence:** the deck's "holds at more than one window length, so it is not a
  fluke of one setting" treats three windows as three independent tests. They share one panel, one
  split and one recency structure — one finding measured three ways. That rules out a
  window-specific fluke, not a dataset-specific one, which is the inference actually at issue.
  Plan: bound the claim in Lab 9 Part 1 and both scripts ("on this panel", plus an explicit
  statement of the prior expectation). **Deck change not made — awaiting owner decision**; it
  would touch the Beamer source, the Quarto mirror, CLAUDE.md, Lecture 13,
  `Narration/Lecture09_Part1_script.md` and three HW05 parts (all prose; no parity risk).
- **Lab 9 Part 2** — done. No corrections; the 292-RMSE positional-encoding penalty and the 14.8x
  parameter ratio both matched, as did every carried-in scoreboard value.
- **Lab 9 Part 1** — done, and **restructured** (owner approved Option 1). Step 3's comparison ran
  at a single 30-epoch budget; measured at seven checkpoints the RNN's margin *peaks at exactly
  30 epochs* (+145) and closes to a tie at 100 (-9), with the LSTM still improving. Step 3's claim
  is now bounded, new Step 4 varies the budget, Step 5 *measures* the three data mechanisms
  (91.0% between-series variance; within-series ACF 0.828 -> 0.432; no lead structure in
  snap_days/event_days). Propagated to the deck (2 new frames, 0 overfull), the Quarto mirror
  (parity 17/17), the deck narration (2 new slides, renumbered to 23), Lecture 13 (both formats),
  CLAUDE.md, and HW05 Parts 2 and 3 -> copied to Forecasting-Env.
  *Self-inflicted bug caught by running it:* a dict comprehension refit both seeds inside the
  checkpoint loop (28 networks instead of 4) — right numbers, 7x the runtime. Fixed before ship.
- **Section numbering** — `number-sections: false` across 14 labs + `_TEMPLATE_lab.qmd` + all 11
  homework (owner: "3 Step 1 — Look at it first" was misleading). Homework re-rendered and
  published, 11/11, numbering confirmed gone.
- **Student repo** — all 11 assignments synced to `Forecasting-Env/assignments/`; STUDENT_QUICKSTART
  now opens by naming which of the two repos to clone; two stale `datahurdler.github.io` course
  URLs fixed; `set_course_url.py` extended to span both repos (round-trip verified byte-identical).
- **Lab 11 Part 1** — done. Defect found and fixed: Step 3 printed 1,585 vs 1,578 for the two
  forecast methods, inviting a 7-unit read when the true difference is *exactly zero* (propagating
  a random walk adds zero-mean steps, so both methods share a point forecast). The lab now computes
  the point forecast analytically and reports **1,589** on both rows; simulation is used only for
  the intervals.
- **Lab 11 Part 2** — done. Triggered a **deck-level** correction (owner approved Option 1): the
  deck's centred-model diagnostics (43 divergences, R-hat 1.003, ESS 966) are reproducible from
  nothing in the repo; the lab's own code gives **127 / 1.044 / 413**, and the 30-series variant
  gives 792 / 1.074 / 36. Since R-hat *fails* on every reproducible configuration, the deck's claim
  ("only the divergence count objects") was false as written. Deck, mirror, deck narration, both
  HW06 solution keys and CLAUDE.md now carry measured values, with the claim reworded to what the
  evidence supports: ESS passes at 413, R-hat fails at 1.044 in the way people rationalize, and
  127 divergences against a threshold of zero admits no argument. Also aligned: 8.1x -> 8.2x,
  RMSE 0.048 -> 0.049, mu_b/sd_b 0.078/0.065 -> 0.077/0.066.
- **1,587 -> 1,589** (same principle, owner-endorsed): Lecture 11 Part 1 deck, mirror, CLAUDE.md
  and HW06 Part 1 solutions. Makes the deck's "beat seasonal naive by 4%" *more* exact (4.28% vs
  4.40%).
- **Lab 12** — done, and the course's last lab. No lab defects; every figure matched the deck
  except P(elasticity < -0.5), where the deck said 0.46 and the lab measures **0.446** — aligned
  in deck and mirror on the same principle.
- **Labs 1-3 audit** — an earlier claim that they "predate the current format" was **wrong**. They
  established the format: same headers, same markers, same appendix table. The only difference is
  that Labs 4+ append three italicised "things to know before recording" notes; Labs 1-2 have none
  and Lab 3 has one. Cosmetic, not a defect.

## Status: all 14 lab narration scripts complete

Remaining follow-ups: publish changed decks (Lectures 9 Pt 1, 11 Pt 1, 11 Pt 2, 12, 13); the
book's Phase 0 is now unblocked.
