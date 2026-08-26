# Lecture 13 — Recording Script

**ECON 8310: Business Forecasting · Synthesis — What the Semester Measured**

Deck: `Slides/Lecture13_Synthesis.pdf` (20 pages) · Measured runtime: see the timing guide

---

## How to use this document

- **`▶ SLIDE n — Title`** marks where to advance. The number is the PDF page.
- *Italic parentheticals* are stage directions. **[pause]** means stop for a beat.
- This deck is **not on the syllabus**. It exists so the online version of the course has a
  closing session, and as a review students can use before the final project.
- Slides 13 and 14 are the heart of it. The split — bugs in the code versus a correct program
  answering the wrong question — is the most durable thing in the hour.

---

# ▶ SLIDE 1 — Title page

Synthesis: what the semester measured.

Twelve lectures, four families of method, one dataset, and a scoreboard that almost nobody would
have predicted in Week 1.

Today is not new material. It's the session where the twelve weeks become one argument — and where
I want to hand you the handful of things that will still be true when every library in this course
has been replaced.

---

# ▶ SLIDE 2 — Lecture Outline

Five parts. What we built, and how the four parts of the course relate. What the results actually
taught — three lessons, each paid for with a measurement. How to choose a method. How to do it
honestly, which is the longest section. And where to go next.

---

# ▶ SLIDE 3 — Section divider: What We Built

Four parts, twelve lectures, one dataset — and a scoreboard nobody would have predicted in Week 1.

---

# ▶ SLIDE 4 — The Arc of the Course

*(Walk the table, then land the reframing underneath it.)*

Four parts. Classical time series, Lectures 1 to 3: **specify a structure** — level, trend, season
— and estimate it. Trees, 4 to 6: **stop specifying**, hand an algorithm features and let it find
the structure. Deep learning, 7 to 9: let the **architecture** encode what kind of structure to
expect. Bayesian, 10 to 12: change the **deliverable** — return a distribution, not a number.

**[pause]**

Now read down that last column again, because there's something there.

This course is not really four toolkits. It's four answers to a single question: **where does the
knowledge in a forecast come from?**

From you, encoded in the model structure. From the data, via a search procedure. From the
architecture's built-in assumptions. Or from a prior, stated openly and then updated.

*(Beat.)*

That framing is what survives when the libraries change. Every method you meet for the rest of your
career sits somewhere on that spectrum, and knowing where tells you what it will be good at and
what it will fail at.

---

# ▶ SLIDE 5 — The Scoreboard

*(Walk the table. Take your time — this slide is the evidence for everything after it.)*

Every model in this course, on the same M5 weekly panel. Same thirty series, same held-out block.

LASSO with forty-six engineered features: **seven forty-four**. XGBoost, tuned: seven eighty-one.
Vanilla RNN on four raw channels: eight forty-two. Random forest: eight ninety-nine. LSTM: nine
eighty-seven. Transformer encoder: nine ninety. 1D CNN: one thousand thirty-two.

And seasonal naive, at the bottom: twenty-one fifty-two.

**[pause]**

*(Now the reading.)*

That ordering is not the one anyone predicts in Week 1.

A **forty-six-coefficient linear model** is at the top. Above gradient boosting, above every
neural architecture we built.

And the two architectures with the most attention and money behind them — the LSTM and the
Transformer — finished **fifth and sixth of eight**, behind a plain RNN with a fraction of their
parameters.

*(Beat.)*

I want to be careful about what that does and doesn't mean, because the wrong lesson is easy to
take. It does not mean Transformers are overrated in general — they reorganized an entire field.
It means they are **mismatched to this problem**, and the rest of this lecture is about learning to
see that mismatch in advance rather than after nine hours of fitting.

---

# ▶ SLIDE 6 — Section divider: What the Results Taught

Three lessons, each paid for with a measurement.

---

# ▶ SLIDE 7 — Lesson 1: The Benchmark Is a Real Competitor

Start with the one that should be most uncomfortable.

In Homework 1, the seasonal-naive benchmark — same week last year, one line of code — **beat every
exponential smoothing and ARIMA model you fitted.**

That was not a trick question or a rigged setup. It is simply what the data supports at that
horizon.

**[pause]**

And across the whole course, the benchmark was beaten, but rarely by the margin the effort implied.

The Bayesian structural model beat it by **four percent**. The GAMs in Homework 2 beat it by
**twelve percent**. The best model on the weekly panel beat it by sixty-five percent — after
forty-six engineered features and a cross-validated penalty.

*(Point at the key box.)*

**[pause]**

So: **compute the benchmark first, every time.**

It costs one line. It is often close. And it is the only number that tells you whether the rest of
your work was worth doing.

*(Point at the last paragraph, and make it about them.)*

This is also the cheapest professional habit you can carry out of this course, and the one most
likely to distinguish you early in a job. A forecast presented without a benchmark is a number
nobody can evaluate — including you, including the person who built it.

If you take one thing from twelve weeks, take that.

---

# ▶ SLIDE 8 — Lesson 2: More Sophisticated Did Not Mean Better

Four times this semester the more advanced method lost. And each time, we could **name the
reason** — which is the part that matters.

*(Walk the table.)*

The **LSTM lost to a plain RNN**, at three window lengths. Gating fixes long-range forgetting; a
twenty-six-week window does not suffer from long-range forgetting. Four times the parameters, no
gain.

The **Transformer lost to an RNN**, with fifteen times the parameters. Its advantages are
advantages *at scale*, and five thousand nine hundred forty windows is not scale.

**CNNs lost to LASSO**, because a seven-week receptive field cannot see an annual lag.

And **tuning made XGBoost worse** — nine fits, and the defaults were three RMSE better.

**[pause]**

*(Point at the disclaimer, and mean it.)*

None of these means the losing method is bad. Every one of them solves a problem this data does not
have. LSTMs earn their gates on long dependency chains. Transformers earn their parameters on
large corpora. Those are real capabilities that simply were not needed here.

*(Beat.)*

**Match the method to the structure of the problem, not to the recency of the paper.**

And notice the standard I'm holding these to. It's not "the fancy model lost, therefore fancy
models are bad." It's "the fancy model lost, and we can say precisely which of its assumptions
didn't apply." That second statement is worth something. The first is just cynicism.

---

# ▶ SLIDE 9 — Lesson 3: One Idea Appeared Six Times

*(This is the intellectual spine of the course. Deliver it slowly.)*

Here's the one I most want you to leave with.

*(Walk the table.)*

Lecture 3: the GAM smoothing penalty, penalizing the wiggliness of a spline. Lecture 4:
cost-complexity pruning, penalizing the number of leaves. Lecture 5: `reg_lambda` and `gamma`,
penalizing leaf weights and leaf count. Lecture 6: Ridge, LASSO, Elastic Net, penalizing
coefficient size. Lecture 7: weight decay and dropout, penalizing network weights. Lecture 11: the
hierarchical prior, penalizing distance from the group mean.

**[pause]**

Six model families that look nothing like each other. Splines, trees, boosted trees, linear
models, neural networks, and a Bayesian hierarchy.

One bargain underneath all of them: **fit against complexity, with a single parameter setting the
exchange rate.**

*(Point at the distinction.)*

And five of those six tune that parameter by cross-validation — you try values and pick one. The
sixth, the hierarchical prior, **estimates** it, with a posterior and its own uncertainty. That
makes it the cleanest version of the idea in the course.

**[pause]**

*(Land the transferability.)*

This is what to remember when the tools change. And they will change — most of the specific
libraries in this course will look dated within a decade.

The **trade between fit and complexity** will not. When you meet a method none of us have heard of
yet, one of the first useful questions is: where is its complexity penalty, and what sets it?

---

# ▶ SLIDE 10 — Section divider: Choosing a Method

---

# ▶ SLIDE 11 — Which Method, When

*(A practical slide. Walk it briskly — students will photograph it.)*

One series, clear seasonality, short history? ETS or ARIMA — and check the benchmark.

Several seasonal cycles at once? GAM or Prophet.

Many engineered features, tabular data? **Regularized regression first**, then XGBoost.

Many parallel series with shared drivers? Gradient boosting with series identifiers.

Genuinely long dependencies and lots of data? Recurrent or attention architectures.

Few observations per group? Hierarchical Bayesian — partial pooling.

The decision needs a probability? Bayesian, for the predictive distribution.

**[pause]**

*(Two notes on the table.)*

Two things about that list.

"Regularized regression first" is not a concession or a beginner's option. It **won our largest
comparison**, and its coefficients can be read aloud in a meeting. Start there and make the
complicated model prove it deserves to replace it.

And the last row is the only one where the **question changes** rather than the accuracy.
Everything above it is a horse race on RMSE. That row is about needing a different kind of answer
— which is the thing Lectures 10 through 12 were really for.

---

# ▶ SLIDE 12 — Section divider: Doing It Honestly

The errors that do not announce themselves.

---

# ▶ SLIDE 13 — Errors That Fail Silently I: the Pipeline

Every error on this slide produces a confident, plausible, **wrong** answer with no error message.
And every one of them is a **bug in the code**.

*(Walk the table.)*

`KFold` on a time series. Random folds put the future into training. Your CV error looks
excellent, and your forecast fails.

Scaling outside the fold. Validation statistics leak into training. Smaller effect, same class of
error.

Rolling features unshifted. A window that includes the current week leaks the target into its own
predictor.

Reading MDI importance. In Homework 3, **pure noise ranked seventeenth of twenty-nine** — above a
real feature — purely because it had many distinct values.

**[pause]**

*(Point at the common thread.)*

The common thread is that the failure is not a crash. It's a number that looks fine.

Which is exactly why the discipline has to be **procedural**. Split by time. Scale inside the
fold. Shift the window. Plant a control.

You do those things because they're on a list, not because something broke — because nothing is
ever going to break.

---

# ▶ SLIDE 14 — Errors That Fail Silently II: the Code Was Fine

*(This is the most important slide in the deck. Slow right down.)*

Now the harder category, and the one that is far more common in professional work.

Here **nothing is wrong with your program.** The model fits. The sampler converges. Every
diagnostic passes. And the answer is still wrong.

*(Walk the four rows deliberately.)*

**Pooling groups that are not exchangeable.** Lecture 11 Part 2's lab pooled ten FOODS series with
twenty that ignore SNAP. Textbook shrinkage, clean diagnostics — and it reported an effect of
plus point-oh-one-one where the held-out weeks said plus point-oh-eight-nine.

**Standardizing a coefficient you then interpret.** Lecture 12: divide log price by its standard
deviation, and `b_price` stops being an elasticity. Identical fit, identical diagnostics, and the
five percent price scenario moves by a factor of **twenty-two**.

**Omitting a confounder.** The naive elasticity was six times too large — *with an interval half the
width* of the correct one. Precision is not accuracy.

**Ignoring R-hat and divergences.** Our first two Bayesian fits returned reasonable-looking
forecasts while failing convergence outright.

**[pause]**

*(Now the line the whole deck is built toward.)*

Look at that list and ask which of them a diagnostic would have caught.

**Only the last one.**

The first three were caught by held-out data, by a DAG drawn before the model, and by asking what
one unit of a variable actually means. None of those is something a library will run for you.
There is no `check_exchangeability()`. There is no warning when your coefficient stops being an
elasticity.

*(Beat.)*

That's the difference between knowing how to call a method and knowing what it assumes. Twelve
weeks of this course have been aimed at the second one.

---

# ▶ SLIDE 15 — What a Defensible Forecast Report Contains

So what does good work actually look like when you hand it to someone?

*(Walk the table.)*

**A benchmark** — computed, not cited. Every model measured against it.

**A time-aware split** — walk-forward or a held-out final block. Never random.

**More than one evaluation.** A single test split can flatter. Homework 4 ranked models the same
way twice, and that's why that ranking is believable.

**The result that went against you** — including tuning that didn't help, and the model you
expected to win.

**An interpretation**, in the units of the business rather than of the loss function.

**[pause]**

*(Point at the fourth row.)*

That fourth row is the one that distinguishes professional work, and it's the one that feels
counterintuitive when you're junior.

A report where **every** result confirms the author's expectation is not a report anyone should act
on. Either the author got lucky, or they stopped looking, or they're not telling you everything.
Reporting what went against you is what makes the rest of it credible.

*(Last paragraph.)*

And you have practised this all semester, whether or not it felt like it. The assignments were
built so that the obvious answer is frequently the wrong one — and the credit was for **noticing**,
not for getting the flattering number.

---

# ▶ SLIDE 16 — Where You Do This Yourself

Which brings us to the final project, because it asks for exactly the report on the previous slide,
on data of your choosing.

*(Walk the requirements.)*

**Three methods, from at least two parts of the course.** Classical, trees, deep learning,
Bayesian. Three variations on one family does not satisfy this — the comparison has to be between
approaches that differ *in kind*.

**Plus a benchmark**, which does not count toward the three and is not optional. Lesson 1 is why.

**Walk-forward validation** for every comparison. Not a random split, and not once.

**A recommendation a non-specialist can act on**, in business units, with the uncertainty attached.

**A methods reflection** — which model won, and what about *your* data made it win.

**[pause]**

*(Point at the last row and make the standard explicit.)*

That last row is not a formality, and it's where the grade actually lives.

Every scoreboard in this course came with a **reason**. The LSTM lost because gating solves a
problem this data doesn't have. The CNN lost because seven weeks can't see an annual lag. The
Transformer lost because its advantages are advantages at scale.

A project that reports a ranking without a reason has done the computation but not the work.

---

# ▶ SLIDE 17 — Section divider: Where to Go Next

---

# ▶ SLIDE 18 — What This Course Did Not Cover

Some honest gaps, so you know what you don't know.

*(Walk the table.)*

**Hierarchical reconciliation** — making store forecasts add up to regional totals. Genuinely
different from Lecture 11's hierarchy, and FPP Chapter 11 covers it.

**Intermittent demand** — series that are mostly zeros. Croston's method and its relatives. Very
common in spare parts and slow-moving SKUs, and none of our methods handle it well.

**Structural breaks** — when the future stops resembling the past.

**Causal inference** — DAGs told us confounders exist. Estimating causal effects credibly is a
separate course.

**Foundation models** — pretrained forecasters applied zero-shot. Moving fast; FPP-Py Chapter 15 is
a starting point.

**[pause]**

*(Point at the third row and close hard on it.)*

The third row is the one most likely to matter in your career, so let me be explicit about why.

**Every model in this course assumes the future resembles the past.** Every single one. And when
that stops being true — a pandemic, a competitor entering, a supply shock, a pricing change — the
model does not tell you.

Worse: **the benchmark fails at exactly the same moment**, so your usual safety net goes with it.
Your forecast is wrong, your comparison is wrong, and everything still looks internally consistent.

Detecting that early is its own field, and it's worth knowing that field exists.

---

# ▶ SLIDE 19 — Closing

*(Seven points. Steady pace. This is the last thing they hear.)*

One. **Compute the benchmark first.** It's often close, and it's the only number that says whether
your work was worth doing.

Two. **Match the method to the problem**, not to the paper's publication date. The most advanced
model on our data finished sixth.

Three. **One idea recurs**: fit against complexity, with a parameter setting the rate. Six times,
under six names.

Four. **Split by time, always.** The leakage errors in this field don't crash — they return a
better-looking number.

Five. **Diagnostics check the model you wrote, not whether it was the right one.** Convergence,
R-hat and ESS all passed on the two worst answers this course produced. Held-out data caught them.

Six. **Report what went against you.** It's the part that makes the rest credible.

Seven. **Know what your forecast is for.** A point estimate and a predictive distribution answer
different questions, and only one of them supports a decision under uncertainty.

**[pause]**

*(The last line. Say it plainly and stop.)*

The libraries will change. The habits are the transferable part.

Thank you — and good luck with the project.

---

# ▶ SLIDE 20 — References

*(Advance and close. No narration needed.)*
