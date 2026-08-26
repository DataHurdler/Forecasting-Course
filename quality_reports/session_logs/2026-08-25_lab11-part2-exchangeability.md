# Session log — 2026-08-25 — Lab 11 Part 2 and the exchangeability defect

## What changed
- `Labs/Lecture11_Part2_lab.qmd` — new. Renders in ~21s, six MCMC fits.
- `Slides/Lecture11_Part2_Hierarchical.tex` — running example rebuilt on the ten FOODS series;
  two frames added (category table, exchangeability), one added (held-out grading). 19pp, 0 overfull.
- `Homework/HW06_Part2_Hierarchical.qmd` — Part C rebuilt to match; new Q1 (exchangeability) and
  Q4 (held-out grading); 6 questions, 9 prompts.
- `Homework/HW06_Part1_Foundations_TS.qmd`, `CLAUDE.md` — prompt-budget bookkeeping.

## The defect found
Verifying the deck's numbers on pymc 6 reproduced them exactly (11.5x shrinkage), but the
held-out check I added for the lab did not. Cause: `j % 3 == 0` selects **exactly the ten FOODS
series**, because the series are ordered store-major with three categories each. FOODS is the
only category with a real SNAP effect (+0.089 vs +0.006 and +0.011) — SNAP is food assistance.

So the demo starved precisely the series that had an effect, then pooled them toward twenty that
did not. The deck concluded "the hierarchy did not average away a real signal, it removed a fake
one" and recommended not differentiating by store-category. Held-out weeks refute both: the
true FOODS effect is +0.089 and the model reported +0.011 for every one of them, with clean
diagnostics and tight intervals.

## Decision
Rebuild the running example on the ten FOODS series (the defensibly exchangeable set) rather than
patch the thinning. Rationale: fixing only the confound leaves the deeper problem — pooling FOODS
with HOBBIES is wrong regardless of how the thinning is drawn. On the FOODS set the story is
also simply better: `sd_b` = 0.065 (real store variation, not collapsed to zero), full series
keep most of their spread, and held-out RMSE improves 0.126 -> 0.048.

The 30-series failure was not discarded — it became the lab's spine. The lab fits the bad
hierarchy first, admires textbook shrinkage and clean diagnostics, then grades it against
held-out weeks and finds it confidently wrong.

## Tried and abandoned
- Predicted-vs-observed shrinkage weight (precision-weighted-average formula) as the lab's
  payoff. Worked (corr 0.52, thin/full weights 0.0013 vs 0.0434) but with `sd_b` = 0.007 every
  weight sits near zero and the plot is degenerate. The held-out check is the better payoff and
  needed no algebra — which also suits the course's not-math-heavy constraint.
- Out-of-sample RMSE on *units* rather than on the SNAP coefficient: the intercept dominates and
  differences in `b` are invisible.

## Numbers now pinned (deck == lab == homework)
mu_b 0.078 [0.017, 0.150]; sd_b 0.065; shrinkage 8.1x; held-out RMSE unpooled 0.126 vs
hierarchical 0.048 (2.6x); centred 43 divergences vs non-centred 0 at target_accept=0.9, with
R-hat 1.003 and ESS 966 both passing — divergences the only diagnostic that objects.

## Open
- HW05's three parts suggest 22 prompts while each checklist says "<= 15" — same bookkeeping bug
  fixed here for HW06, not yet fixed there.
- Lab 12 is the last lab.

---

# Lab 12 and the L12 elasticity error (same session)

## The defect found
Verifying L12's numbers reproduced its headline results exactly (-0.687 uncontrolled, -0.127
controlled, 5% price rise -> 0.6% fall). But the deck instructed "Standardize the predictors
first" and then called `b_price` an elasticity and built a business scenario on it. Those are
incompatible: with log price divided by its standard deviation, the coefficient is per-SD, not
per-percent.

Measured: sd(log price) = 0.2444, so the true controlled elasticity is -0.493 [-0.596, -0.387],
not -0.127. Every downstream claim was wrong:

- "Inelastic, and clearly negative" -> the elasticity sits ON the -0.5 boundary
- "P(elasticity < -0.5) is approximately 0" -> it is 0.46, very nearly a coin flip
- "5% price rise -> 0.6% fall in units" -> the truth is 2.4%

The uncontrolled elasticity is -2.805, not -0.687. The confounding *lesson* survives unharmed
(5.7x too large instead of 5.4x, interval still half the width), which is why the error was
invisible: every relative claim held, only the absolute ones broke.

Also fixed: the controlled fit had ESS 184 / r_hat 1.02 -- it would have failed HW07's own
diagnostic gate. Centring log price within series fixes it (ESS 3,097) without changing the
answer, and is the causally correct estimand anyway (within-series price variation is the
variation a manager can create).

## Decision
Deck refit unstandardized with within-series centring. The ROPE lesson got *better*: "the data
cannot settle whether demand is elastic or inelastic, 46/54" is a far more useful demonstration
than "the effect is obviously small."

HW07 carried the identical bug (it built `lp_z` then called it an elasticity). Rewritten, with a
callout naming the trap explicitly.

Lab 12 makes the trap its centrepiece: fit correctly, then standardize and watch the scenario
answer move by 22x with clean diagnostics throughout. Note the lab standardizes the *centred*
log price (sd 0.0455), so its distortion is 22x rather than the deck's 5x -- the smaller the sd
you divide by, the bigger the error.

## Verified numbers (deck == lab == homework)
uncontrolled -2.805 [-2.856, -2.756]; controlled -0.493 [-0.596, -0.387], ESS 3,097;
b_trend 0.110 [0.107, 0.113]/yr; b_snap 0.036 [0.027, 0.046]; b_event -0.003 [-0.011, 0.004];
P(e<0)=1.00, P(e<-0.5)=0.46; +5% price -> units -2.38% [-2.87,-1.87], revenue +2.50%, P(rev up)=1.00.

## Open / deferred
- GitHub Pages shows a published date of January 1, 2026 on the labs. Owner asked to leave it
  until the mirroring pass; fix it then.
- Agreed order from here: update Lecture 13, then build the full Quarto mirror and publish.

---

# The mirror pass and the site build (2026-08-25/26)

## What changed
- All 15 decks now have Quarto mirrors. Seven were new (L09 Pt1/Pt2, L10, L11 Pt1/Pt2, L12, L13);
  L07 and L08 were rebuilt from scratch rather than patched.
- `scripts/check_mirror_parity.py` is new: it parses Beamer frame titles (handling nested braces
  and stripping `\parencite{...}`) and compares the count against the mirror's `## ` headings.
- `docs/` rebuilt: 16 weeks plus finals week, syllabus / datasets / project rubric published as
  styled HTML, all 11 homework submissions, all 14 labs.
- `scripts/sync_to_docs.sh` rewritten with targets (all / slides / labs / homework / docs / one
  lecture). The old version knew nothing about labs, homework or documents and copied R scripts
  from a directory this Python course does not have.
- `docs/workflow-guide.html` unpublished (owner approved).

## Defects the pass found
The mirror pass is a read-every-line pass, so it caught cross-deck drift no single-deck review
would have:

- L07's mirror was 2 slides short and predated a deck restructure; L08's was 2 short and had
  none of the measured results (the 1,032 RMSE table, the 500-RMSE pooling penalty).
- L09 Pt1 **and** Pt2 both showed the 1D CNN at 1,202 RMSE. L08 and L13 say 1,032.
- L09 Pt1 cited the pooling penalty as 230 RMSE -- the pre-correction figure.
- L09 Pt1's takeaway said the LSTM lost "at two window lengths" against a three-row table.
- L09 Pt2's takeaway said the Transformer "beat the LSTM" where the body says it ties -- and the
  tie was quoted against 998 (the LSTM at 52 weeks) when both models ran at 26 weeks (987).
- Every published lab and homework page was dated **January 1, 2026**: `date: "Fall 2026"` is not
  parseable, and Quarto fell back silently. 26 files. The term moved into the subtitle.
- CLAUDE.md carried two stale measurements of its own (positional-encoding ablation; L11 Pt2
  shrinkage figures).

## Correction to an earlier entry in this log
A "STALE" flag from comparing git commit times said the Lecture 1 mirror was out of date. It is
not -- parity holds (16 = 16) and the published HTML postdates the deck. Commit-time comparison
is the wrong instrument; `check_mirror_parity.py` is the right one, and it reports L01-L06 clean.

## Open
- Student repo `Forecasting-Env`: `policy/homework_limits.json` fix committed locally, **not
  pushed** (owner deferred). Also there: `assignments/hw01_rubric.md` grades an essay assignment
  from an earlier course design, and HW02-HW07 have no scaffolding.
- Narrations for L07-L13, and solution keys for HW05/06/07, remain unwritten.

---

# Closing state (2026-08-26)

Everything below was true when this log was committed.

## Done since the entries above
- All 15 lecture recording scripts written (L01-L06 pre-existing; L07-L13 added), 150-234
  words/slide, slide numbers verified against each PDF via `scripts/check_mirror_parity.py`
  page maps.
- Site published and live at https://datahurdler.github.io/Forecasting-Course/ — 16 weeks plus
  finals, assignments integrated into each week, syllabus/datasets/rubric as HTML.
- `main` fast-forwarded to carry the whole redesign; the four merged branches (`fall2026`,
  `fall2026-syllabus-and-tree-restructure`, `origin/fall2026`,
  `origin/sync-upstream-template-v2.5.1`) are deleted. `pre-fall2026-site` tags the old `main`
  if that state is ever needed.
- The January 1, 2026 date bug fixed on all 26 lab and homework pages.

## Still open
1. **Student repo `Forecasting-Env`** — `policy/homework_limits.json` fix committed locally but
   **not pushed**; `assignments/hw01_rubric.md` grades an essay assignment from an earlier course
   design; HW02-HW07 have no scaffolding. Students submit HW01 Part 1 on **Sep 3**, so the
   budgets file is the time-critical one.
2. **Six solution keys and six solution narrations** — HW05 Pt1/Pt2/Pt3, HW06 Pt1/Pt2, HW07.
   HW01-HW04 are done. First needed around **Oct 22**.
3. **The supplied project dataset** — the syllabus commits to confirming availability by
   **Week 4, Sep 17**. The only outstanding item with a date already published to students.
4. **Video generation from slides + scripts** — investigated, deferred. `say` cannot reach the
   installed Siri voice (proved: all Siri identifiers fall back to Samantha, byte-identical
   output). The viable path is a GUI-built Shortcut driven by `shortcuts run`, unverified.

---

# Student submission repo — gap analysis and decisions (2026-08-26)

## Owner decision
The initial prompt embedded in each assignment `.qmd` is the **single source of truth** for
Codex setup. `prompts/REQUIRED_INITIAL_PROMPT.md` in Forecasting-Env stops being a thing
students paste and becomes an explainer.

Done: all 11 `.qmd` prompts now carry the repository rules (log schema, one commit per prompt
with the message format, PROMPT_LIMIT_REACHED behaviour, locked paths), with each assignment's
own folder name, commit prefix and budget substituted in. Verified the budget in the rules block
matches the budget stated above it in all eleven.

## Blocking gaps found in Forecasting-Env (a student cannot do HW1 today)
1. **No assignment `.qmd` reaches the student.** The env repo has only `assignments/hw01_prompt.md`
   — an essay assignment ("forecasting use cases", citations) from an earlier course design. The
   course site publishes rendered `.html` only, never the `.qmd` source. There is no path from
   "clone the repo" to "have the file to fill in."
2. **No way to create the data.** Every assignment reads `data/processed/m5_weekly.csv`, produced
   by `scripts/prep_m5.py`, which exists only in the course repo. Env repo has `.gitkeep` only.
3. **`assignments/hw01_rubric.md`** grades the essay assignment, not HW01 Part 1.

## Naming inconsistency (repo-wide)
`README.md`, `STUDENT_QUICKSTART.md`, `submissions/README.md` and
`prompts/REQUIRED_INITIAL_PROMPT.md` all use `hwNN` and `hwNN prompt <id>`, which cannot express
the part-based scheme (`hw01_part1`, `hw05_part2`) now used by the assignments, the submission
folders, and `policy/homework_limits.json`.

## Still unpushed in Forecasting-Env
`55344c7` — the `homework_limits.json` correction. Students push HW01 Part 1 on **Sep 3**.

## Website / hosting (owner is considering a move)
luozijun.com is a Quarto site on Hostinger with a GitHub repo; a local clone exists at
`~/Documents/GitHub/luozijun.com/`. Key fact established: **GitHub Pages cannot serve a subpath
of another domain**, but if the user-site repo (`DataHurdler.github.io`) carries the custom
domain, every project repo is served at `luozijun.com/<repo>/` automatically. No
`DataHurdler.github.io` repo exists yet. `scripts/set_course_url.py` now makes the URL change a
one-command operation whichever way this goes.
