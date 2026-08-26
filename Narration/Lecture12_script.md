# Lecture 12 — Recording Script

**ECON 8310: Business Forecasting · Bayesian Statistics III — Bayesian Linear Regression**

Deck: `Slides/Lecture12_BayesianRegression.pdf` (16 pages) · Measured runtime: see the timing guide

---

## How to use this document

- **`▶ SLIDE n — Title`** marks where to advance. The number is the PDF page.
- *Italic parentheticals* are stage directions. **[pause]** means stop for a beat.
- Slide 5's "do not standardize log price" is not a style note. It is the lecture's second-biggest
  point, and the lab is built around what happens when you ignore it. Give it real weight.
- Slide 11 is the one students carry into their projects: a *tighter* interval on the wrong model.
  Say "confidently, precisely wrong" out loud.

---

# ▶ SLIDE 1 — Title page

Lecture 12: Bayesian Statistics III — Bayesian Linear Regression.

This is the last technical lecture of the course, and it closes a loop. We started in Lecture 2
with linear regression. We spent Lecture 6 regularizing it. Today we fit the same model one more
time, with priors on the coefficients — and get back something quite different from a table of
estimates and standard errors.

**[pause]**

And along the way we're going to do something this course hasn't done yet: ask what a coefficient
*means*, causally. Not "does it predict" but "if we intervened, what would happen."

That's a different question, it needs a different kind of thinking, and getting it wrong is how
confident analysts produce expensive mistakes.

---

# ▶ SLIDE 2 — Lecture Outline

Four parts. Bayesian linear regression, which is mostly familiar. Then reading a posterior
coefficient — three questions you can ask a distribution that you cannot ask a point estimate.
Then causal structure and DAGs, which is where the coefficient starts meaning something. And then
a map of everything we've built this semester.

---

# ▶ SLIDE 3 — Section divider: Bayesian Linear Regression

The same regression you already know — returning a distribution for every coefficient.

---

# ▶ SLIDE 4 — OLS vs. Bayesian Regression: What Changes?

You have been fitting linear models since Lecture 2, and regularizing them since Lecture 6.

OLS solves for a single best coefficient vector — the closed-form expression on the slide. One
number per predictor, plus a standard error that rests on large-sample theory.

The Bayesian version replaces that with the update rule from Lecture 10: the posterior over beta
is proportional to the likelihood times the prior.

*(Point at the key box.)*

**[pause]**

And the consequence is the thing to hold onto: **every coefficient comes back as a distribution.**

Not an estimate with an error bar computed from an asymptotic formula. A full posterior — a cloud
of plausible values, which you can query however you like.

*(Point at the last paragraph. This is a satisfying callback.)*

**[pause]**

And here's something that should make Lecture 6 click retroactively.

**Regularization is a prior.** A Normal prior on beta is *exactly* Ridge regression. A Laplace
prior — double-exponential, with that sharp peak at zero — is *exactly* LASSO.

The penalty you tuned by cross-validation in Lecture 6 was a statement of belief all along. You
were saying "coefficients are probably small," you just weren't saying it in probability
notation.

Same estimates, two vocabularies. Which is the seventh time this semester one idea has shown up
wearing different clothes.

**[pause]**

And the equivalence is genuinely useful, not just cute. It tells you what a penalty is *assuming*.

Ridge's Normal prior says coefficients are probably small, and symmetric around zero, with no
particular preference for exactly zero. LASSO's Laplace prior has a sharp spike at zero — it says
you believe many coefficients are exactly zero.

That's why LASSO produces sparse solutions and Ridge doesn't. It's not a quirk of the optimizer.
It's the prior doing what you asked. Once you see the penalty as a belief, the behaviour stops
being a rule to memorize and becomes something you can reason about.

---

# ▶ SLIDE 5 — Bayesian Linear Regression in PyMC

Here's the model. Log units regressed on log price, a SNAP indicator, and an event indicator.
Weakly informative Normal priors on every coefficient, Exponential on sigma. Nothing here is new
after Lecture 10.

**[pause]**

*(Now the warning. This is the lecture's second-biggest point — do not rush it.)*

But look at the bolded line, because it runs against a habit you have built all semester.

**Do not standardize log price.**

You have standardized predictors in nearly every model since Lecture 6. It makes penalties
comparable, it helps samplers, it's a good default. And here it will quietly destroy your answer.

Here's why. With units and price both in logs, `b_price` is an **elasticity** — the percent change
in demand per percent change in price. That is a quantity a category manager already uses and can
act on directly.

Standardize log price, and the coefficient becomes "change in log units per **standard deviation**
of log price." Still a valid number. No longer an elasticity. And every percentage claim you build
on it downstream will be wrong by exactly the factor you divided by.

**[pause]**

*(Beat.)*

The lab does this deliberately, and the business answer moves by a factor of twenty-two. With
clean diagnostics throughout. No warning of any kind.

*(Point at the centring note.)*

One thing you *should* do: subtract each series' own mean log price. That's **centring**, not
scaling — it shifts the variable without changing its units, so the elasticity survives intact. And
it fixed our sampling badly: effective sample size went from one hundred eighty-four to three
thousand ninety-seven.

Centre, don't scale. That's the rule.

**[pause]**

And there's a general principle underneath it that outlives this example.

Ask, for every transformation you apply: **does my coefficient still answer the question I asked?**

Logging both sides gives you an elasticity, which is interpretable. Centring preserves it.
Scaling destroys it. Taking a difference changes it into something else again.

None of those are wrong operations. What's wrong is applying one out of habit and then reading the
coefficient as though you hadn't. The transformation and the interpretation have to be decided
together — and if you can't say what one unit of your variable *is*, you cannot say what your
coefficient means.

---

# ▶ SLIDE 6 — Section divider: Reading the Posterior

Three questions you can ask a distribution that you cannot ask a point estimate.

---

# ▶ SLIDE 7 — Reading a Posterior Coefficient

Here's the fitted model, controlling for series and trend.

*(Walk the table.)*

`b_price`: minus point-four-nine-three, HDI from minus point-five-nine-six to minus
point-three-eight-seven. Right near the elastic boundary — we'll come back to that.

`b_trend`: point-one-one-zero, a tight interval. About eleven percent growth per year.

`b_snap`: point-oh-three-six. About a three-point-seven percent SNAP-week lift — consistent with
what the hierarchy told us last week.

`b_event`: minus point-oh-oh-three, interval from minus point-oh-one-one to plus point-oh-oh-four.
**Spans zero.**

**[pause]**

Quick note on the **HDI** — highest density interval. It's the shortest interval containing
ninety-four percent of the posterior. And unlike a confidence interval, it means what everyone
wants it to mean: there is a ninety-four percent probability the coefficient is in there.

*(Point at the last paragraph.)*

**[pause]**

Now, the last row is the useful one, and I want to be precise about why.

`b_event`'s interval spans zero, so the data do not establish a direction. Events might raise
demand slightly; they might lower it slightly.

That is a **more honest report** than "not statistically significant," and it's more informative
too. Because it also tells you the effect is **small** — at most about half a percent either way.

"Not significant" conflates two completely different situations: an effect you can't detect
because it's tiny, and an effect you can't detect because your data is thin. The interval
distinguishes them. Here it's the first.

**[pause]**

And those two situations call for opposite actions, which is why conflating them is expensive.

An effect that is genuinely tiny means stop investigating — you have your answer, and it's that
events don't matter much for this series. An effect you cannot detect because the data is thin
means collect more data, or find a better design, because the question is still open.

A p-value above point-oh-five is compatible with both, and gives you no way to tell which you're
in. The interval tells you immediately: narrow and centred on zero is the first, wide and spanning
zero is the second.

---

# ▶ SLIDE 8 — Asking the Posterior a Direct Question

Because the posterior is a set of samples, any question about beta is answered by **counting**.

*(Point at the code box.)*

Pull the samples into an array. Then: what fraction are below zero? What fraction are below minus
point-five? What fraction sit between minus point-five and zero?

Three one-line questions, three direct answers. No test statistic, no null hypothesis, no table.

**[pause]**

*(Now the results — and the second one is the interesting one.)*

On our fit, the probability the elasticity is below zero is **one point zero zero**. Every single
posterior sample is negative. Demand falls when price rises, and there is no doubt about it
whatsoever.

Fine. That's the boring question, and a p-value would have told you something similar.

Now the interesting one. The probability the elasticity is below minus point-five — the boundary
between elastic and inelastic demand, which is a genuine business threshold — is **point four
six.**

Forty-six percent. Essentially a coin flip.

**[pause]**

*(Point at the key box.)*

So the data **cannot settle** whether demand is elastic or inelastic. And that is the honest,
useful, actionable finding — because "should we treat this product as price-sensitive?" is a
decision that hinges on exactly that threshold.

Two different findings, and a p-value conflates them. "Statistically significant" reports only the
**direction**. The question the business actually asks is *how big*, and the answer is
forty-six/fifty-four.

No significance test would ever have given you that number.

**[pause]**

*(Worth making concrete, since students will ask what to do with 0.46.)*

And a reasonable question is what a manager actually does with forty-six percent.

They do not get a yes or a no, and that's the point — the honest answer is that the evidence is
balanced. What they get is the ability to reason about the *consequences* of being wrong in each
direction. If treating the product as elastic and being wrong is cheap, and treating it as
inelastic and being wrong is expensive, then a forty-six percent probability is more than enough
to act on the cautious side.

That's a decision-theoretic argument, and it needs a probability as an input. A significance test
cannot supply one.

*(Muted note.)*

Asking how much posterior mass falls inside a range of negligible values has a name — a **ROPE**,
a region of practical equivalence. Homework 7 asks you to compute one.

---

# ▶ SLIDE 9 — Section divider: Causal Structure and DAGs

Which coefficients mean what you think they mean.

---

# ▶ SLIDE 10 — Directed Acyclic Graphs

Everything so far has been about *estimating* a coefficient well. Now: what does it mean?

A **DAG** is a picture of what you believe causes what. Nodes are variables, arrows run from cause
to effect, and acyclic means nothing causes itself.

Crucially, you draw it **before** the model, from domain knowledge. And its purpose is specific:
it tells you **which variables belong in the regression.**

*(Walk the two definitions.)*

A **confounder** causes both your predictor and your outcome. You **must** control for it —
otherwise its influence gets absorbed into your coefficient and you attribute someone else's
effect to your variable.

A **collider** is caused by both. And controlling for a collider **creates** a spurious association
that was not there to begin with.

**[pause]**

*(Point at the consequence.)*

That second row is why "add every control you have" is bad advice, and it surprises people.

More controls is not safer. Conditioning on a collider actively manufactures a relationship out of
nothing. So which variables to include is a question about **causal structure** — and no amount of
model fit, no cross-validation score, no information criterion will answer it. Two models can fit
identically and mean opposite things.

*(Point at the muted caveat, and deliver it plainly.)*

**[pause]**

One honest limit. Whether a given DAG is *right* is a substantive question about your business,
not a statistical one. This course uses DAGs to reason about **what a coefficient means**.
Estimating causal effects credibly — instruments, natural experiments, all of that — is a separate
subject and a separate course.

---

# ▶ SLIDE 11 — Confounding, Measured

Let's make that concrete on our own data, because the size of the effect is startling.

Our panel has thirty store-category series. Categories differ in **both** typical price and typical
volume — hobby items cost more per unit and sell fewer of them. So series identity is an arrow into
price *and* an arrow into units.

That is a textbook confounder.

*(Walk the table.)*

Fit the elasticity with price, SNAP and events only: **minus two point eight zero five.**

Add series effects and a trend: **minus point four nine three.**

**[pause]**

*(Now the punchline. Slow down.)*

The uncontrolled estimate is nearly **six times too large**. It claims demand collapses when price
rises — a one percent price increase costing almost three percent of volume.

And here's the part I want you to remember for the rest of your career.

It is **not noisier**. Look at the intervals. The uncontrolled one runs from minus two
eight-five-six to minus two seven-five-six — that's a width of about point one. The controlled one
is roughly point two wide.

**The wrong answer has an interval half the width of the right one.**

*(Point at the warning box.)*

**[pause]**

It is confidently, precisely wrong. And nothing in the output flags it.

A tight credible interval says the model is **sure**. It says nothing whatsoever about whether the
model is answering **your question**.

Bayesian machinery does not protect you from omitting a confounder. Neither does more data — more
data would tighten that wrong interval further. Only the DAG protects you, and the DAG is drawn
before you fit anything.

---

# ▶ SLIDE 12 — Scenario Analysis with Posterior Samples

Here's the payoff for having a distribution instead of a number.

Because the posterior is samples, you can push a business scenario through it and get back a
**distribution of outcomes**.

*(Point at the code.)*

Three lines. Pull the elasticity samples. Apply the price change to each one. Report the mean and
the interval.

**[pause]**

With an elasticity near minus point four nine three, a five percent price rise implies roughly a
**two point four percent fall in units** — with ninety-four percent of the posterior between minus
two point nine and minus one point nine percent.

So you can report the pessimistic end, which is what a planner actually wants. Not "demand will
fall about two percent" but "demand will fall about two percent, and it's unlikely to be worse
than three."

*(Point at the decision paragraph.)*

**[pause]**

And then the decision follows directly. Revenue rises if the volume loss is smaller than the price
gain. Compute that for every posterior sample and count.

Here: revenue rises by about **two and a half percent** on average, and the probability that
revenue rises is **one point zero zero** — every single posterior sample.

*(Beat.)*

Now notice something subtle, because it's the kind of thing that makes this worth doing. That
conclusion holds **even though** the elasticity might well be past minus point five. Two facts that
sound contradictory — "we can't tell if demand is elastic" and "raising price definitely increases
revenue" — are both true, simultaneously, and the posterior lets you say both.

*(Muted note.)*

With one caveat, and it's the one from slide 10. This is valid only to the extent the **DAG** is.
It's a causal claim about intervening on price, and it inherits every assumption in that diagram.

---

# ▶ SLIDE 13 — Section divider: Course Synthesis and Next Steps

From classical time series to Bayesian hierarchical models: a complete forecasting toolkit.

---

# ▶ SLIDE 14 — Course Method Map

*(Walk the table at a steady pace. Students will photograph this slide.)*

Everything we've built, on four axes: what data it takes, what uncertainty it gives you, how
interpretable it is, and what it's good at.

ETS and ARIMA — univariate series, confidence intervals, highly interpretable, fast and automatic.
And remember the benchmark beat every one of them in Homework 1, which is the first thing this
table should remind you of.

GAMs and Prophet — series plus predictors, limited uncertainty, interpretable, good at nonlinear
and interpretable together.

Decision trees — tabular, no uncertainty, but a rule-based explanation anyone can read.

Random forests — robust, minimal tuning, OOB gives you something.

XGBoost — best tabular accuracy in this course, and low interpretability.

Feedforward nets and CNNs — smooth functions, fast, opaque.

LSTMs and Transformers — sequences and long-range dependencies, very low interpretability.

Bayesian — any data, **full posterior**, highly interpretable, and strongest exactly where samples
are small.

**[pause]**

*(Point at the key box.)*

**No single method dominates.** That's the honest summary of eleven weeks, and it's what the
scoreboard has been telling you all semester.

Choose on four things: your data type and size, whether you need uncertainty quantified, whether
someone needs to understand the model, and how fast you need it deployed.

And in practice, **combine**. A very common production pattern is XGBoost for the point forecast,
because it's accurate, plus a Bayesian model for the intervals, because they're honest. You are
not obliged to pick one column of that table.

---

# ▶ SLIDE 15 — Lecture 12: Key Takeaways

One. Bayesian linear regression places priors on coefficients and returns a full posterior for
each one. A Normal prior *is* Ridge; a Laplace prior *is* LASSO.

Two. Posterior coefficient plots give you the mean, the HDI, and the probability the coefficient
exceeds any threshold you care about — richer than a p-value, and answering the question people
actually ask.

Three. **DAGs** make causal structure explicit, identifying confounders you must include and
colliders you must exclude. Draw the DAG before specifying the regression.

Four. Scenario analysis with posterior samples: push any counterfactual through the posterior draws
and get a full distribution for that scenario, not a point projection.

Five. No single method is best for all forecasting problems. Build intuition for when to reach for
each one, and combine them when the stakes justify it.

**[pause]**

*(Close the course.)*

And the one to carry out of this room, which is really the lesson of the whole semester.

The uncontrolled elasticity was six times too large, with an interval **half the width** of the
correct one. Precision is not accuracy. A confident model is not a correct model. And the thing
that caught it was not a diagnostic, not a score, not a cross-validation fold — it was a picture
you draw before fitting anything, from what you know about the business.

That habit is the most transferable thing in this course.

---

# ▶ SLIDE 16 — References

*(Advance and close. No narration needed.)*
