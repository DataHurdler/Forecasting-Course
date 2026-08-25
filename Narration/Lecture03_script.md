# Lecture 3 — Recording Script

**ECON 8310: Business Forecasting · Generalized Additive Models**

Deck: `Slides/Lecture03_GAMs.pdf` (19 pages) · Measured runtime: **~24 minutes** (22–27 depending on pace)

---

## How to use this document

- **`▶ SLIDE n — Title`** marks where to advance. The number is the PDF page.
- Written to be **spoken**. Short sentences. Contractions are fine.
- *Italic parentheticals* are stage directions — do not read them aloud.
- **[pause]** means actually stop for a beat.
- Change anything that doesn't sound like you.

---

# ▶ SLIDE 1 — Title page

Lecture 3: Generalized Additive Models.

This lecture sits at a hinge in the course. Behind us are the classical time series methods —
exponential smoothing, ARIMA, VAR. Ahead of us, starting next week, are the machine learning
methods: trees, forests, boosting, neural networks.

GAMs are the bridge. They are the last method we'll see that is genuinely nonlinear *and*
genuinely explainable at the same time. After today, every increase in flexibility costs you
something in interpretability.

So this is worth understanding well — partly for its own sake, and partly because it sets up
the tradeoff that the second half of this course keeps making.

**[pause]**

---

# ▶ SLIDE 2 — Lecture Outline

Five parts. The motivation — why we want something between linear and black-box. Then the
structure of a GAM and how smoothing is controlled. Then Prophet, which is a GAM built
specifically for time series. Then pyGAM, for the general case. And the takeaways.

---

# ▶ SLIDE 3 — Section divider: Motivation

*(Divider.)*

Part one. Why we want flexibility without giving up the ability to explain what the model is
doing.

---

# ▶ SLIDE 4 — The Flexibility–Interpretability Tradeoff

Two columns, and this is one of the few genuine side-by-side comparisons in the course.

On the left, **linear models** — regression, ARIMA. Each coefficient has a clear meaning. You
can say "a one-point rise in unemployment lowers sales by four hundred units," and everyone in
the room knows what you mean. The properties are stable and well understood.

But they assume a constant slope everywhere. The effect of unemployment going from 4% to 5% is
assumed identical to it going from 9% to 10%. That's an assumption, and it's usually false.
They miss curvature and threshold effects entirely.

**[pause]**

On the right, **fully nonlinear models** — trees, neural networks. They capture almost any
pattern, and on complex data they're accurate.

But ask why a specific prediction came out the way it did, and you'll struggle. And because
interactions entangle the variables, you can't cleanly separate what any single variable
contributes.

**[pause]**

**GAMs sit between the two.** Each variable gets a flexible, nonlinear relationship. But the
model stays **additive** — the effects are added together, not multiplied or entangled — so
each one can still be plotted and explained on its own.

That is the whole bargain. And the rest of this lecture is about what it costs, because it
does cost something.

---

# ▶ SLIDE 5 — Why Additivity Matters for Interpretation

Let me make the additivity point precise, because it's easy to nod along without seeing what's
at stake.

In a non-additive model, the effect of one variable depends on the value of another. You
cannot describe them separately.

**[pause]**

Concretely. Suppose the truth is $y$ equals $x_1$ squared times $x_2$ squared, plus noise.

Take the derivative with respect to $x_1$: you get two $x_1$ $x_2$-squared. That expression
contains *both* variables.

So there is no answer to "what does $x_1$ do to $y$?" that doesn't begin with "it depends on
$x_2$." Not because we haven't worked hard enough — because the question has no
variable-by-variable answer. The model doesn't decompose.

**[pause]**

Now the GAM. $y$ equals $f_1$ of $x_1$, plus $f_2$ of $x_2$, plus noise.

The marginal effect of $x_1$ is just $f_1$-prime of $x_1$. A function of $x_1$ alone.
Whatever $x_2$ happens to be doing, the answer is the same.

**That is why you can plot each variable's effect separately and hand the plot to a
stakeholder.** One curve per variable, each one true on its own terms.

And that is also precisely what GAMs give up. If the effect of price genuinely does depend on
whether it's a holiday week, a GAM cannot represent that. We'll come back to it at the end.

---

# ▶ SLIDE 6 — Section divider: GAM Structure and Smoothing

Part two. The structure — additive nonlinear functions, penalized for wiggliness.

---

# ▶ SLIDE 7 — What Is a GAM?

Here's the definition. $y$ equals a constant, plus $f_1$ of $x_1$, plus $f_2$ of $x_2$, and so
on — where each $f$ is a smooth nonlinear function estimated from the data.

Compare that to linear regression, where each term is beta-$j$ *times* $x_j$. We've replaced
a coefficient with a function. That's the entire generalization.

Each $f_j$ is free to be linear, curved, U-shaped, or threshold-like. You don't specify the
shape. The data decides.

**[pause]**

Because the terms are *added* rather than multiplied, the effects stay independent and each
can be visualized on its own. And every function is fitted to minimize prediction error
subject to a smoothness penalty — which is the next slide, and is what stops the curves from
chasing noise.

**[pause]**

A retail example, to make it concrete.

Model weekly sales as $f_1$ of time, capturing the long-run trend. Plus $f_2$ of week-of-year,
capturing seasonality. Plus $f_3$ of unemployment, capturing economic sensitivity.

Three curves. Each plotted and interpreted separately. And none of them requiring you to hold
the others fixed to make sense of it.

Notice this is doing the same decomposition Prophet will do in twenty minutes — trend,
seasonality, external effects. Prophet is a GAM with the time series structure built in.

---

# ▶ SLIDE 8 — What the "Generalized" Actually Means

Someone should have asked this two slides ago, so let me answer it before we go on.

The method is called a **Generalized** Additive Model. So far I've shown you an *additive*
model. Where is the "generalized"?

**[pause]**

Everything we've modelled has been continuous and roughly symmetric — sales in dollars,
demand in units. For that kind of outcome, adding smooth functions together works directly.

But suppose your outcome is a **count**. Units sold at a small store: zero, one, two, seven.
An additive model can happily predict *minus three units*, which is not a thing.

Or suppose it's **binary**. Did this customer churn? Did we stock out? The answer is a
probability, between zero and one, and again an additive model will cheerfully predict one
point four.

**[pause]**

The fix is on the slide. Instead of modelling the mean directly, we model a **transformation**
of the mean — $g$ of the expected value of $y$ equals the additive predictor.

That $g$ is called the **link function**, and it's the entire "generalized."

Look at the table. For continuous symmetric data, the link is the **identity** — do nothing,
which is the case we've been in all along. For counts, the link is the **log**, which means
you model the log of the mean and exponentiate to get back, so the forecast can never go
negative. For binary outcomes, the link is the **logit**, which maps the whole real line into
zero-to-one, so the probability is bounded by construction.

**[pause]**

In pyGAM this is one word: `LinearGAM`, `PoissonGAM`, `LogisticGAM`. Same additive structure,
same splines, same smoothing penalty. Only the link changes.

And if this sounds familiar from a regression course — it should. It's exactly the same idea
as a generalized *linear* model. A GAM is a GLM where the linear terms have been replaced by
smooth functions. That's the whole family tree in one sentence.

---

# ▶ SLIDE 9 — Controlling Smoothness: The Penalty Term

If each $f$ can be any shape, what stops it from being a squiggle that passes through every
data point? This slide.

A GAM minimizes a **penalized** sum of squared errors. Two terms. The first is the ordinary
fit term — squared errors, exactly as in OLS. The second is the penalty.

Look at what's being penalized: the integral of the *squared second derivative*.

The second derivative measures how fast the slope is changing. A straight line has a second
derivative of zero everywhere. A wiggly function has a large second derivative, wiggling in
both directions, and squaring it before integrating means all that wiggle accumulates.

So the penalty charges the model for wiggliness. And lambda sets the price.

**[pause]**

The two extremes are worth holding in mind.

As **lambda goes to zero**, the penalty vanishes. The curve is free to chase every point.
That's overfitting — a model that memorizes your sample.

As **lambda goes to infinity**, the penalty dominates. Any curvature is infinitely expensive,
so every $f$ is forced straight, and the GAM collapses back into ordinary least squares.

So OLS isn't a different method from a GAM. It's a GAM with the smoothness dial turned all
the way up. Everything useful happens in between.

And lambda is chosen by **cross-validation** or GCV — not by eye. You'll hear that refrain all
semester: the tuning parameter is selected against held-out error, never by what looks nice.

**[pause]**

Let me say a little more about splines, because "piecewise polynomials joined at knots" is one
of those phrases that sounds like an answer without being one.

Here's the picture. Take the range of your predictor and put down a handful of points along
it — those are the **knots**. Between each pair of knots, fit a low-order polynomial, usually
a cubic. Then require that where two pieces meet, they join up: same value, same slope, same
curvature. That's what makes it look like one smooth curve rather than a chain of segments.

**[pause]**

The number of knots controls how much wiggle is *available*. Few knots, and the curve can only
bend gently. Many knots, and it can bend almost anywhere.

Now, you might expect that choosing the number of knots is the crucial modelling decision. It
mostly isn't — and this is the elegant part of the penalized approach. You give the model
plenty of knots, more than you think you need, and then let **lambda** control how much of
that available flexibility actually gets used.

So the knots set the ceiling, and lambda sets where under the ceiling you land. That's why
you tune lambda by cross-validation and generally leave the knot count alone. One tuning
decision instead of two — and the one that's easier to make honestly.

---

# ▶ SLIDE 10 — Section divider: Prophet for Time Series GAMs

Part three. Prophet — a GAM built specifically for business time series.

---

# ▶ SLIDE 11 — Prophet: Forecasting at Scale

Taylor and Letham built Prophet at Meta for large-scale forecasting. And it is a GAM in
time-series clothing — look at the decomposition.

$y$ at time $t$ equals trend, plus seasonality, plus holidays, plus noise. Three additive
components. That is the GAM structure from two slides ago, with the terms chosen for what
business time series actually contain.

**[pause]**

**Trend** is piecewise linear or logistic, with *changepoints* — specific dates where the
slope is allowed to shift. That's important, because real business series do change direction:
a new competitor arrives, a store is renovated, a pandemic starts.

**Seasonality** is a Fourier series. That's how Prophet handles weekly and yearly cycles
simultaneously — something none of our Lecture 1 or 2 methods could do.

**Holidays** are irregular events you supply yourself. Black Friday. A product launch. A
lockdown. These aren't periodic, so no seasonal term captures them, and you tell Prophet the
dates directly.

**[pause]**

Now — the design goals were practical rather than statistical. One fit-and-forecast call.
Robust to missing data and outliers. Interpretable, because every component plots on its own.

That's why it spread so quickly among analysts who aren't statisticians.

**[pause]**

Now let me be honest about its track record, because you'll hear Prophet talked about as if
it were state of the art, and it isn't.

In head-to-head comparisons, Prophet frequently **loses** to a well-tuned ARIMA or ETS on
forecast error. Our own textbook says so directly — the authors note that Prophet rarely gives
better accuracy than the alternatives. It did not win the M-competitions. It doesn't top
benchmark leaderboards.

**[pause]**

So why is it in this course, and why is it everywhere in industry?

Because accuracy is not the only thing being optimized. Consider what Prophet actually gives
an analyst: a defensible forecast in twenty minutes, from a series with gaps and outliers,
with a component plot you can put in front of a manager who will ask what drove it.

Getting an ARIMA to that same point takes stationarity testing, order identification,
residual checking, and someone who knows what a PACF is. If you have that person, use ARIMA
and get the better number. If you're one analyst covering four hundred product lines, you do
not have that person four hundred times.

**[pause]**

That's the real lesson, and it goes wider than Prophet. **The best model in a paper and the
best model in an organization are frequently different models**, and the gap between them is
usually maintenance cost and explainability, not accuracy. Part of your job is knowing which
one you're being asked for.

One knob to know: `changepoint_prior_scale`. High means the trend adapts quickly and risks
overfitting. Low means a stable trend. It's the main thing you'll tune.

---

# ▶ SLIDE 12 — Prophet: Code and Workflow

The code is genuinely this short.

Build a dataframe with two columns — `ds` for dates and `y` for values. Prophet insists on
those names. Instantiate, set the changepoint scale and turn on yearly seasonality, and fit.

Then `make_future_dataframe` to extend the index forward, `predict`, and you have a forecast.

**[pause]**

But the call that matters for this course is the last one: **`plot_components`**.

That draws the trend with its changepoints, the yearly seasonal wave, and the day-of-week
pattern as three separate panels. It's the additive structure made visible — you're literally
looking at the terms of the equation, one at a time.

That plot is what you put in front of a manager. Not the forecast line — the components. It
lets them check your model against their own knowledge of the business. "Yes, December looks
right. No, that changepoint in March is wrong, that was the fire." That conversation is worth
more than a small RMSE improvement.

**[pause]**

**Reach for Prophet** on seasonal series with known holiday effects, especially when someone
will ask you to explain the forecast.

**Reach for pyGAM** when you have many correlated external predictors instead — which is where
we're going next.

---

# ▶ SLIDE 13 — Section divider: pyGAM

Part four. pyGAM, for when you have several predictors and want a flexible effect for each.

---

# ▶ SLIDE 14 — pyGAM: Flexible Additive Modeling

Prophet is specialized for time structure. pyGAM is the general case: you specify a smooth
function per predictor and it fits the whole additive model.

The code shows the pattern. Import, then build the model by *adding terms together* — which
is a rather nice piece of API design, because the code mirrors the equation.

**[pause]**

Three term types, and that's the whole vocabulary.

**`s(j)`** is a smooth spline of feature $j$. The flexible nonlinear effect. This is the
default and the reason you're using a GAM.

**`l(j)`** forces a straight line. Worth using deliberately when theory says the effect should
be linear — don't spend flexibility where you don't need it.

**`f(j)`** handles a binary or categorical feature — a factor.

Then `gridsearch` tunes lambda by cross-validation, so you don't pick it yourself.

**[pause]**

One habit I'd ask you to build: after `gridsearch` returns, **look at the curves**. The
search optimizes held-out error, and it will happily give you a curve that's statistically
optimal and economically absurd — sales rising as unemployment rises, say. When that happens
the model isn't broken; it's telling you something is confounded. But you only find out if
you look.

**[pause]**

And there's a specific failure worth naming, because it has a name and it will bite you:
**concurvity**.

You know multicollinearity from regression — two predictors so correlated that the model can't
tell which one is doing the work, so the coefficients go unstable and flip sign between
samples.

Concurvity is the same disease in a GAM, but worse, because the terms are *smooth functions*
rather than straight lines. One smooth term can mimic another even when the raw variables
aren't strongly correlated at all. A smooth function of time and a smooth function of a
trending economic indicator can trace nearly the same shape — and the model has no principled
way to allocate credit between them.

**[pause]**

The symptom is a partial dependence plot that looks wrong or wildly uncertain, and that
changes a lot when you drop an apparently unrelated variable.

The reason it matters more here than in ordinary regression is that GAMs are sold on
interpretability. Under concurvity, the individual curves become unreliable *even when the
overall forecast is fine*. So you get a model that predicts well and explains badly — which
is precisely the thing you chose a GAM to avoid.

pyGAM won't warn you. Check by dropping terms and seeing whether the remaining curves hold
their shape.

---

# ▶ SLIDE 15 — Interpreting GAM Results: Partial Dependence Plots

This is the payoff slide — the thing you actually deliver.

A partial dependence plot shows the estimated function $f$-hat-$j$ across the range of values
actually observed, with confidence bands around it.

Reading the shape is most of the interpretation.

A **flat line** means the variable does nothing for $y$. And notice — in a linear model that
variable might still have had a significant coefficient. Here you see immediately that it
isn't buying you anything.

A **rising curve** means a positive effect, but not at a constant rate. That's the case a
linear model would report as a single number and get wrong at both ends.

A **U-shape** means there's an optimal level, and both too little and too much are worse.
Inventory works like this. So does advertising spend. A linear model finds a slope near zero
here and concludes the variable doesn't matter — which is exactly backwards.

**[pause]**

Watch the bands as well as the curve. They widen wherever the data thin out, which is usually
at the extremes — exactly where a reader is most tempted to extrapolate. If the band is wide,
the curve there is a guess. Say so.

**[pause]**

And this is what makes a GAM worth its accuracy cost. The output isn't a number. It's a
sentence someone can act on: *"as unemployment rises from 5% to 10%, predicted sales fall by
X percent — and the decline steepens past 8%."*

That second clause is the part no linear model could ever have told them.

---

# ▶ SLIDE 16 — Section divider: Key Takeaways and Roadmap

Let's pull it together — and set up where the course goes next.

---

# ▶ SLIDE 17 — GAMs vs. Other Methods: When to Choose Each

This table is the honest summary of the whole course so far, and it's worth reading down the
columns rather than across.

ARIMA and ETS: not nonlinear, no interactions, highly interpretable, univariate time series.
Linear regression: same, with manual interactions if you build them.

GAM: **nonlinear, yes. Interactions, no. Interpretable, high.**

Random Forest: nonlinear and interactions, medium interpretability. XGBoost: same, but low.

**[pause]**

The column that decides it is usually **Interactions**.

A GAM is additive by construction. That's the source of its interpretability, and it's also a
hard limit. If the effect of price genuinely depends on whether it's a holiday week, a GAM
cannot represent that. A tree can — that's exactly what a tree does, and it's why the next
three lectures exist.

So the additivity is a bargain, not a free lunch. You buy explainability with the ability to
model interactions.

**[pause]**

**Choose a GAM when** you must explain each predictor's effect. When those effects are curved
rather than straight. When a time series has complex trend and seasonality — reach for
Prophet. And when interpretability matters more than the last few points of accuracy.

That last clause is the honest one. On tabular data, XGBoost will usually win on RMSE. Lecture
6 is where we take that seriously and stop pretending otherwise.

---

# ▶ SLIDE 18 — Lecture 3: Key Takeaways

Five things.

**One.** GAMs give nonlinear flexibility while keeping interpretability, because the model is
additive. Each variable's effect can be visualized and explained independently.

**Two.** The smoothness penalty prevents overfitting. Lambda trades fit against smoothness,
and it's chosen by cross-validation — never by eye.

**Three.** Prophet decomposes a series into trend, seasonality, and holidays using a GAM.
Ideal for business series with seasonal patterns and known irregular events.

**Four.** pyGAM handles the general case. `s()` for smooth, `l()` for linear, `f()` for
categorical, and `gridsearch` for lambda.

**Five.** Partial dependence plots are what make results actionable. They're what you deliver.

**[pause]**

And the meta-point, which matters more than any of the five: this is the last method in the
course that is both genuinely nonlinear and genuinely explainable. From next week, every
increase in flexibility costs you something in interpretability, and part of your job as a
forecaster is deciding when that trade is worth making.

---

# ▶ SLIDE 19 — References

Readings are in the syllabus — section 7.7 for regression splines, and 12.1 and 12.2 for
complex seasonality and Prophet.

Next week: Decision Trees. We move to tree-based methods, and the first thing we gain is
exactly what we gave up today — interactions, captured automatically.

See you then.

---

## Timing guide

| Segment | Slides | Target |
|---|---|---:|
| Opening & motivation | 1–5 | ~9 min |
| GAM structure, links & smoothing | 6–9 | ~10 min |
| Prophet | 10–12 | ~9 min |
| pyGAM & interpretation | 13–15 | ~9 min |
| Close | 16–19 | ~5 min |

If you need to compress, slide 13's term-type list survives trimming. Do **not** compress
slides 5, 14, or 16 — the additivity argument, the partial dependence plot, and the
interactions tradeoff are the three ideas this lecture exists to deliver.
