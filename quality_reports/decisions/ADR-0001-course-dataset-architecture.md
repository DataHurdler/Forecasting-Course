# ADR-0001: Course Dataset Architecture

**Status:** ACCEPTED
**Date:** 2026-08-24
**Context:** Course-wide data strategy — triggered by a Holt-Winters fit in HW01 that cannot run on the current dataset

## Problem

The course needs a dataset spine used **both for in-class worked examples and for homework**.
Using the same data in lecture and in assignments is the point: students see a method
demonstrated on a series in class, then apply the next method to the same series themselves,
so differences across methods are attributable to the method rather than to the data.

**Today there is no continuity at all.** Lecture examples quote results on **RSXFS** — a
monthly FRED retail-sales series, see L02, L05, L08 — while homework uses **Rossmann**, a
weekly store panel. A student cannot carry one example across the two, and the numbers on the
slides come from data they never touch.

The current choice for homework (Rossmann Store Sales, 30 stores × ~134 weekly observations,
Jan 2013 – Jul 2015) is also too short: Holt-Winters with a 52-week season needs 2m = 104 observations to initialize, which
leaves almost no test set and caused HW01 Q2 to specify a fit that cannot execute.

The four method families in this course want incompatible things from data:

| Need | Driven by |
|---|---|
| >= 2 full seasonal cycles, ideally many | L01 ETS |
| Multiple series that genuinely influence each other | L02 VAR / Granger |
| Exogenous regressors | L02 ARIMAX, L06 regularization |
| Daily granularity + holidays + several seasonalities | L03 GAM / Prophet |
| Wide tabular feature set | L04–L06 trees |
| Large observation count, many parallel series | L07–L09 deep learning |
| Explicit group structure for partial pooling | L11 hierarchical Bayes |
| Interpretable covariates for a DAG | L12 Bayesian regression |

No single public dataset satisfies all of these well.

## Options considered

### Option A: Keep Rossmann

Stay with the current dataset and work around its length.

**Pro:** Zero migration cost; `prep_rossmann.py` and 53 references across slides and homework already exist.
**Con:** ~134 weeks cannot support a 52-week season with a usable test set; no real hierarchy;
weekly only, so Prophet's multiple-seasonality story cannot be told; too small for deep learning.

### Option B: M5 / Walmart as a single spine

Use the M5 Forecasting–Accuracy dataset for everything.

**Pro:** 1,941 days (~5.3 years); 42,840 series across 12 aggregation levels on two crossed
hierarchies (state→store, category→dept→item); calendar with events and SNAP; weekly
`sell_prices`; free on Zenodo and via Nixtla `datasetsforecast`, so **no Kaggle login**;
Walmart is immediately legible to MBA students.
**Con:** Large raw download; retail stores do not meaningfully Granger-cause one another, so
L02 would be taught on data where the honest answer is "no relationship"; single-seasonality
retail understates what Prophet is for.

### Option C: M5 spine + targeted supplements

M5 as the spine, with additional datasets introduced only where M5 demonstrably cannot show
something.

**Pro:** Keeps one dataset as the through-line for cross-method comparison, while each
supplement earns its place by covering a specific gap — and the *reason* for each supplement
is itself a teachable point about matching data to method.
**Con:** Students meet more than one data format; slightly more prep code.

### Option D: Favorita as the spine

Corporación Favorita Grocery Sales (Ecuador, 2013–2017).

**Pro:** Daily; hierarchy via store clusters; holidays; a daily **oil price** giving a genuine
macro→retail transmission channel; a documented magnitude-7.8 earthquake on 2016-04-16 that
visibly distorts sales for weeks.
**Con:** 125M rows raw; Kaggle-only; shorter than M5; overlaps M5 almost entirely in shape.

## Decision

**Chose:** Option C — M5 spine with targeted supplements.

**Rationale:** A single spine is what makes cross-method comparison meaningful — students see
ETS, ARIMA, XGBoost, an LSTM, and a Bayesian model on the *same* series and can attribute
differences to method rather than to data. M5 is the only candidate long enough to make the
52-week season work with room to spare, and the only one with a real hierarchy for L11. Where
M5 genuinely cannot demonstrate something, a supplement is introduced deliberately and the
reason is stated to students.

## The architecture

| Dataset | Role | Why not the spine |
|---|---|---|
| **M5 / Walmart** | Spine, L01–L12 | — |
| **FRED** macro series | L02 VAR & Granger causality | Retail stores do not cause each other; retail sales, unemployment, CPI, and consumer sentiment do. Free API, no login, `pandas_datareader` support. |
| **Electricity demand** (half-hourly) | L03 multiple seasonality | Daily + weekly + yearly at once is what Prophet and GAMs are for; retail shows only one. Monash Forecasting Repository, free, no login. |
| **Favorita** | Week 16 cameo + final-project seed | Provides a **dated exogenous shock** (2016-04-16 earthquake) that M5 has no equivalent of. Used to close the course: every method fails together, because the future stopped resembling the past. Also a good project dataset — different enough from the spine that students must transfer rather than copy lecture code. |

## Consequences

- **These datasets are used in lecture as well as in homework.** Worked examples on slides,
  live-coded demonstrations, and assignment questions all draw on the same series, so a
  student can carry one running example through the whole semester.
- **The datasets are introduced in a standalone document**, `ECON8310_Datasets.md`, not in a
  Lecture 1 slide. A slide was drafted and then reverted: the material is reference content
  students return to all semester, and it needs more room than a slide allows — where to
  download each set, what is in each file, and why each supplement exists. The *why there is
  more than one* framing is the point of the document, and it is a teaching point rather than
  an apology.
- `scripts/prep_rossmann.py` is replaced by a new `prep_m5.py` that subsets M5. A comparable
  subset (10 stores × 3 categories, daily) is ~58,000 rows against the current ~4,000.
- Existing slide examples that quote Rossmann numbers (L02, L05, L08) must be re-run against
  M5, not merely renamed — the RMSE figures currently on those slides would otherwise be wrong.
- The Holt-Winters constraint in HW01 Part 1 becomes non-binding: ~277 weekly observations
  against the 104 required. The runtime assertion stays as a guard.
- ~53 Rossmann references must be updated: 3 lecture decks (L02, L05, L08), 8 homework files,
  and the prep script.
- **No lecture currently teaches structural breaks or intervention analysis.** The Week 16
  Favorita cameo would be its only appearance, and pairs with the already-assigned FPP Ch. 13
  (§13.9, outliers and missing values).
- HW02–HW07 should not be restructured until the migration happens, or that work is done twice.
- The same applies to `Labs/` (in-class hands-on exercises, one per lecture, `LectureNN_lab.qmd`).
  The folder, README, and template are in place and are dataset-agnostic; the individual labs
  should be authored against M5 rather than written twice.

## Rejected alternatives — why not

- **A (keep Rossmann):** the dataset is structurally too short for a 52-week season; the HW01
  bug was a symptom, not an isolated mistake.
- **B (M5 alone):** would force L02 to teach Granger causality on series with no real causal
  relationship, and understate what Prophet is for.
- **D (Favorita spine):** duplicates M5's shape while being shorter, larger to download, and
  Kaggle-gated. Its one unique asset — the earthquake — is retained as a cameo under Option C.
