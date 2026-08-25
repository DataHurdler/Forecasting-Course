# Lecture 2 — Recording Script

**ECON 8310: Business Forecasting · ARIMA, VAR & Multivariate Models**

Deck: `Slides/Lecture02_ARIMA_VAR.pdf` (19 pages) · Measured runtime: **~30 minutes** (27–33 depending on pace)

---

## How to use this document

- **`▶ SLIDE n — Title`** marks where to advance. The number is the PDF page.
- Written to be **spoken**. Short sentences. Contractions are fine.
- *Italic parentheticals* are stage directions — do not read them aloud.
- **[pause]** means actually stop for a beat.
- Change anything that doesn't sound like you.

---

# ▶ SLIDE 1 — Title page

Welcome back. Lecture 2: ARIMA, VAR, and multivariate models.

Last week we built exponential smoothing. The idea there was that the past enters your
forecast through a smoothed *level* — a running summary of where the series is, updated as
new data arrives.

Today we do something different. Instead of summarizing the past into a level, we model the
**correlation structure** of the series directly. How does today relate to yesterday? To the
day before? To the same month last year? ARIMA answers those questions explicitly.

And then we do something exponential smoothing simply cannot: bring in a *second* series.

**[pause]**

---

# ▶ SLIDE 2 — Lecture Outline

Four parts.

First, stationarity — which is the entry requirement for everything else today. If you skip
it, nothing downstream is valid.

Then ARIMA and its seasonal cousin SARIMA.

Then VAR, for when two series move each other.

And we'll close with the takeaways.

---

# ▶ SLIDE 3 — Section divider: Stationarity and Differencing

*(Divider — read and move on.)*

Part one. Stationarity.

Before fitting any model today, the series has to have a stable mean and variance. Let me
explain what that means and why it isn't optional.

---

# ▶ SLIDE 4 — What Is Stationarity?

Three conditions. A series is **weakly stationary** if the mean is constant over time, the
variance is constant and finite, and the covariance between two points depends only on how
far apart they are — the lag — not on *when* you are.

Read that third condition carefully, because it's the one people skim. It says the
relationship between January and February should be the same as the relationship between
June and July. The gap matters; the location doesn't.

**[pause]**

Now, why does the definition earn its keep?

If the mean drifts, there is no single value to forecast toward. Ask "what is the long-run
level of this series?" and there's no answer — it depends when you ask.

If the variance grows, prediction intervals widen without bound. Your forecast is
technically correct and operationally useless.

Stationarity is what makes the past informative about the future. Every model today rests on
it. When we get to neural networks in Week 7, that assumption is still hiding in there — it's
just less visible.

The usual culprits are trending series — GDP, prices, sales, almost anything measured in
dollars over time — and variance that grows with the level. First-differencing removes a
stochastic trend. A log transform stabilizes variance. Often you need both.

Rule of thumb: visible trend or growing variance means probably not stationary. But test it
formally — ADF or KPSS — rather than trusting your eye.

---

# ▶ SLIDE 5 — Unit Roots and Differencing

Here's the sharpest version of the idea. Take a simple AR(1): today equals phi times
yesterday, plus noise. Everything turns on whether phi is below one, or exactly one.

If the absolute value of phi is **less than one**, a shock decays. Something happens, the
series is knocked off course, and it works its way back. That's a stationary AR(1).

If phi equals **exactly one**, the shock never decays. It's absorbed permanently into the
level of the series. That's a random walk — a unit root.

**[pause]**

That distinction has real consequences. In a mean-reverting series, a bad quarter is a bad
quarter. In a random walk, a bad quarter permanently lowers the level you forecast from,
forever. Same data, completely different business implication.

**First differencing** is the fix: model the change rather than the level. So $d$ equals zero
means the series was already stationary. $d$ equals one means you took one difference. And
capital $D$ equals one means a *seasonal* difference — this December minus last December.

For testing, you have ADF and KPSS, and here's the thing worth remembering: they test
**opposite nulls**. ADF's null hypothesis is that there *is* a unit root. KPSS's null is that
the series *is* stationary. So run both. When they agree, you're confident. When they
disagree, be suspicious — you're probably in a borderline case, and you should look at the
plot again.

**[pause]**

And do not over-difference. If you difference an already-stationary series, you induce
negative autocorrelation that you then have to model away — you've manufactured the very
problem you're now solving. Test *after* differencing, and stop at $d$ equals one once the
result is stationary.

---

# ▶ SLIDE 6 — Why the Rule Exists: Spurious Regression

Before we go on, I want to show you *why* that differencing rule exists — because told as a
rule it sounds like bookkeeping, and it is not.

Look at these two series. Both trending up. They look related. If you saw this in a business
deck you'd assume one drives the other.

They have **nothing to do with each other.** Both are random walks I generated independently.
Different random seeds, no shared shocks, no common cause. There is no relationship to find.

**[pause]**

Now look at the two numbers on the slide, because they're the whole lesson.

The correlation of their *changes* — week to week — is **minus zero point one three**.
Essentially zero. That's the truth: these series are independent.

The correlation of their *levels* is **plus zero point six two**. And the levels are what
you'd hand to a regression.

**[pause]**

Granger and Newbold demonstrated this in 1974. Regress two independent random walks on each
other, and you reject the null of no relationship roughly **three-quarters of the time** at
the five percent level.

Not five percent, as the test promises. Seventy-five.

Think about what that means. Your t-statistic is large. Your R-squared is high. Every
diagnostic you were taught to check looks excellent — and the relationship does not exist.

The regression isn't detecting a relationship between the series. It's detecting that both of
them wander. Two things that drift will drift *somewhere*, and over any finite sample they'll
appear to drift together or apart, and the regression will happily report that as signal.

**[pause]**

This is why economics has a long history of embarrassing published findings between
non-stationary series. And it's why the rule is: **difference first, then regress.**

Once you difference, you're modelling changes rather than levels — and the spurious
correlation goes away, because the changes really are independent. Minus zero point one three.

---

# ▶ SLIDE 7 — ACF and PACF: Model Identification

Two diagnostic plots, and together they tell you what model to fit.

The **autocorrelation function** — the ACF — is the correlation between $y_t$ and $y_{t-k}$.
Straightforward: how does today relate to $k$ periods ago?

The **partial** autocorrelation asks the same question but controls for everything in
between. And that distinction matters more than it sounds. If today correlates with three
days ago purely *because* today correlates with yesterday and yesterday correlates with three
days ago, the ACF will show it and the PACF will not. The PACF isolates the direct link.

**[pause]**

Now the table, which is the practical payoff.

For an **AR(p)** process, the ACF tails off geometrically, and the PACF **cuts off** sharply
after lag $p$. So if the PACF has two clear spikes and then nothing, you're looking at an
AR(2).

For an **MA(q)** it's the mirror image: the ACF cuts off after lag $q$, the PACF tails off.

For an **ARMA**, both tail off — which is less informative, and in practice is why people
reach for automatic order selection.

And for a **random walk**, the ACF decays very slowly and the PACF has one big spike at lag
one. That pattern is your warning sign.

**[pause]**

One rule, and it is absolute. **Always unit-root test and difference before reading either
plot.** The ACF of a non-stationary series decays slowly no matter what the underlying
process is. So a slowly-decaying ACF tells you nothing about $p$ or $q$. It only tells you
that you haven't differenced yet.

Students lose a lot of time reading tea leaves in the ACF of an undifferenced series. Don't.

---

# ▶ SLIDE 8 — What Those Patterns Actually Look Like

Now let's actually look at them, because "tails off" and "cuts off" mean very little until
you've seen the shapes.

Four panels. Top row is an AR(1). Bottom row is an MA(1). Left column is the ACF, right
column the PACF.

**[pause]**

Top left — the ACF of an AR(1). See the geometric decay? Each bar is a constant fraction of
the one before it. It fades out rather than stopping. That's "tails off."

Top right — the PACF of the same process. One spike at lag one, and then essentially nothing.
The bars after it sit inside the dashed lines, which are the significance bands. Anything in
there is noise. That's "cuts off," and the lag where it cuts off is your $p$.

**[pause]**

Bottom row, the MA(1), and it's the mirror image. The ACF has one spike then stops. The PACF
decays — and notice it alternates sign, flipping above and below the axis. That alternating
decay is characteristic of an MA process, and it's a pattern you'll start to recognize.

**[pause]**

So the diagnostic is: **find the one that cuts off sharply.**

If the PACF cuts off, you have an AR, and the cut-off lag gives you $p$. If the ACF cuts off,
you have an MA, and it gives you $q$. If neither cuts off — both just fade — you have a mixed
ARMA, and that's when you stop squinting at plots and let `auto_arima` search.

And the dashed bands matter. A bar poking slightly outside them at lag seven is almost
certainly noise. With twenty lags plotted, you expect one of them to breach the band by
chance. Don't build a model around it.

---

# ▶ SLIDE 9 — Section divider: ARIMA Models

Part two. ARIMA — combining differencing with the AR and MA components into one model.

---

# ▶ SLIDE 10 — ARIMA(p, d, q)

Here it is. Take the series, difference it $d$ times, then fit an ARMA with $p$ autoregressive
lags and $q$ moving-average lags.

That's what the three letters mean. $p$ is AR lags, $d$ is differences, $q$ is MA lags.

**[pause]**

What I like about this framework is how much of what you already know turns out to live
inside it.

**ARIMA(0,1,0)** — no AR, one difference, no MA — is a random walk. That's the naive
forecast from Lecture 1.

**ARIMA(1,0,0)** is a plain AR(1).

And **ARIMA(0,1,1)** is algebraically equivalent to simple exponential smoothing. The model
we spent twenty minutes on last week is a single point in this space.

So ARIMA isn't a competitor to what we did in Lecture 1. It's a larger room that contains it.

**[pause]**

Let's do one by hand, because the mechanics are less mysterious once you've turned the crank.

ARIMA(1,1,0) with phi-hat of one-half. We have $y_{100} = 120$ and $y_{99} = 118$. So the
change last period, delta-$y_{100}$, is 2.

The model says the next change is half of the last change: half of 2 is 1. Add that to where
we are: 120 plus 1 equals **121**.

That's it. Differencing means we model the *change*, then add it back to the level.

**[pause]**

A word on where this comes from, because the name will follow you. Box and Jenkins formalized
this in 1970 as a three-stage cycle: **identify** a candidate order from the ACF and PACF,
**estimate** the parameters, then **check** the residuals — and if the residuals fail, go back
to identification. It is a loop, not a pipeline. Half a century later that loop is still the
methodology, and it's why every ARIMA workflow you'll see has the same three stages.

**[pause]**

In Python, `auto_arima` from pmdarima automates the identify step. It searches a grid of
orders and returns whichever minimizes AIC — usually stepwise, so it doesn't try all of them.

Use it. But understand its failure mode: it optimizes a number, and it has no idea what your
data means. I've seen it return an ARIMA(5,2,4) on a series that visibly needs one difference
and an AR(1) — technically the lowest AIC on that sample, and complete nonsense out of
sample. AIC rewards fit with a complexity penalty, and on a short noisy series the penalty
isn't strong enough to stop it.

So: run the search, then look at the ACF and PACF anyway, and ask whether the answer is
sensible. If `auto_arima` returns a second difference and your ADF test said one was enough,
trust the test.

---

# ▶ SLIDE 11 — SARIMA: Adding Seasonal Terms

For monthly or quarterly data, autocorrelation shows up not just at lags one and two, but at
lag $m$, two-$m$, three-$m$ — the seasonal lags. December relates to last December.

SARIMA handles this by adding a second set of AR and MA polynomials operating at the seasonal
frequency. The notation gets heavy — $p$, $d$, $q$ in lowercase, then capital $P$, $D$, $Q$,
then $m$ in brackets — but the idea is simple.

**Think of it as two ARIMA models running at different time scales.** The lowercase part
handles week-to-week dynamics. The uppercase part handles year-over-year. They're fitted
together.

**[pause]**

The practical workflow is four steps.

ADF and KPSS to choose $d$. A seasonal unit root test to choose capital $D$. Then ACF and
PACF on the differenced series to guide the four order parameters. Then minimize AIC and
check the residual ACF with a Ljung-Box test.

**[pause]**

That last step is the one people skip, so let me explain what it's actually doing.

The Ljung-Box test asks: **are the residuals white noise?** It takes the autocorrelations of
the residuals across the first several lags and tests whether they are *jointly* zero.

The null hypothesis is that they are — that nothing is left. So here, unusually, you *want* a
large p-value. Failing to reject is the good outcome. That trips people up, because in most
tests you're hunting for significance.

**[pause]**

And think about why it matters. If your residuals still have autocorrelation, there's
structure in the data your model hasn't captured. Today's error tells you something about
tomorrow's error — which means your forecast is leaving information on the table, and your
prediction intervals are too narrow, because they assume the errors are independent.

So a model can have a great AIC and still fail Ljung-Box. AIC compares models to each other.
Ljung-Box asks whether *this* model is adequate on its own terms. They're different
questions, and you want both answered.

For monthly retail data with trend and December seasonality, SARIMA(1,1,1)(0,1,1)[12] is a
strong starting point. Not because it's optimal, but because it's a good default to beat
before you try anything more elaborate.

---

# ▶ SLIDE 12 — Section divider: VAR Models

Part three. VAR — when two series influence each other, model them together.

---

# ▶ SLIDE 13 — Why Use Multiple Series?

Everything so far — all of Lecture 1, everything today — uses only the series' own history.
$y$ predicted from past $y$.

But business variables are linked, and often the link runs forward in time. Consumer
sentiment today moves retail spending next month. Interest rates today move housing starts
within two quarters. Advertising spend this week moves sales over the following few.

**[pause]**

The principle underneath all of it is this: **if $x_t$ carries information about $y_{t+h}$ that
is not already in $y_t$'s own history, then including $x_t$ reduces forecast error.**

Note the qualifier — "not already in $y$'s own history." That's doing real work. If $x$ is
just a lagged reflection of $y$, it adds nothing. It has to bring genuinely new information.

Granger causality is the formal test of exactly that claim, and we get to it in two slides.

**[pause]**

That leaves you a modelling choice, and it turns on whether influence runs one way or both.

**VAR** treats everything symmetrically. Every variable predicts every other variable. No
variable is privileged. Use it when the influence genuinely runs in both directions.

**ARIMAX** is one-directional. $x$ drives $y$, and not the reverse. Use it when the causal
story is clear — but note the third bullet, because it's the catch we'll come back to: ARIMAX
needs a forecast of $x$ itself.

---

# ▶ SLIDE 14 — The VAR(p) Model

Here's the structure for two series. Two equations, and each one regresses on the lags of
*both* variables.

Look at where the value is: the **cross terms**. $a_{12}$ is how much $y_2$ yesterday predicts
$y_1$ today. That coefficient is precisely what a univariate AR throws away — it has no place
to put it.

And here's the elegant part. If $a_{12}$ and $a_{21}$ both come back at zero, the system
collapses into two separate AR models. You've learned something: these series don't inform
each other. That's a finding, not a failure.

Each equation is estimated by ordinary least squares — it really is just regression — and the
order $p$ is chosen by BIC.

**[pause]**

It's worth knowing why this model exists, because it was a reaction to something.

Christopher Sims proposed VAR in 1980, in a paper arguing that the large structural
macroeconomic models of the day rested on assumptions nobody could defend. To identify those
models, economists had to declare in advance which variables affected which — and Sims argued
those restrictions were, in his word, incredible. Not wrong. Unbelievable.

His alternative: stop pretending you know the structure. Let every variable depend on the
lagged values of every variable, symmetrically, and let the data speak.

He shared the Nobel Prize for it in 2011.

**[pause]**

I mention this because it frames what a VAR is *for*. It is deliberately agnostic. That's its
strength — you impose almost nothing — and it's also why it can't answer causal questions on
its own, and why the parameter count explodes. You traded assumptions for parameters.

**[pause]**

Now the warning, and this one bites people in practice.

**Parameter explosion.** A VAR with $k$ variables and $p$ lags has $k$-squared times $p$
coefficients. It's quadratic in the number of variables.

Five variables, four lags: one hundred coefficients.

Sit with that number. A monthly business series over ten years gives you a hundred and twenty
observations. You'd be estimating a hundred parameters from a hundred and twenty data points.
That model will fit your sample beautifully and forecast like a coin flip.

So keep $k$ at four or fewer, unless you're using a regularized LASSO-VAR — which is the kind
of thing Lecture 6 gives you the tools for.

---

# ▶ SLIDE 15 — Granger Causality Test

The formal definition: $x$ **Granger-causes** $y$ if past values of $x$ help predict $y$
beyond what $y$'s own past already explains.

That final clause is the whole test. Not "does $x$ predict $y$" — but "does $x$ add anything
once we've already used $y$'s own history?"

The procedure is a straightforward F-test. Fit the $y$-equation with the $x$-lags and without
them. Test whether all the $x$-lag coefficients are jointly zero. Reject, and $x$
Granger-causes $y$.

**[pause]**

Here's a concrete question we run in the lab: does unemployment Granger-cause retail sales?
The null is that every unemployment lag is zero in the retail equation.

And notice we're using macroeconomic series here rather than store sales. That's deliberate.

Two Walmart stores in the same state absolutely *do* move together — you'll find a
significant Granger test between them in the homework. The problem is that finding tells you
almost nothing, because both stores are responding to the same regional promotions and the
same weather. The test fires, and you still cannot say which one drives the other.

**[pause]**

Now, I ran the unemployment question before writing this slide, and I want to tell you what
came back, because it is better than the tidy answer I expected.

On the full sample, 1992 to today, the test is significant — and unemployment looks like the
stronger driver. Exactly the story everyone expects. People lose jobs, people stop spending.

Then drop the COVID window and rerun. The intuitive direction weakens sharply. Restrict to
before 2020 and it **disappears entirely** — not significant at any lag.

Meanwhile the *reverse* direction — retail sales predicting unemployment — is rock solid in
every single sample.

**[pause]**

Sit with that, because there are two lessons in it and both are worth more than the tidy
answer would have been.

The first is economic, and it's obvious in hindsight: retail sales are a coincident-to-leading
indicator, and unemployment is a lagging one. Spending falls first. Layoffs follow. The data
was telling us the sequence, and my intuition had it backwards.

The second is methodological, and it's the one I want you to carry into your own work. On the
full sample you would have reported a strong, intuitive, publishable finding. It was being
driven by one enormous shared shock. One episode, in a thirty-four-year sample, flipping the
headline result.

You'll do all three windows yourself in the lab.

**[pause]**

Now the caveat, and I want you to take it seriously because it is the single most abused
result in applied forecasting.

**Granger causality is not structural causality.**

It tests *predictive content*. It does not establish that $x$ mechanically brings $y$ about.

A rooster reliably predicts sunrise. The rooster Granger-causes the sunrise. The rooster does
not cause the sunrise.

So report it as "predictive of." Never "causes." Say it the careful way and you will never
have to walk a claim back in front of a room of executives.

**[pause]**

One more thing before we leave ARIMA and VAR, and it's something these models give you that
we've barely mentioned: **prediction intervals**.

Everything we've produced so far is a point forecast — a single number. But every one of
these models also produces a distribution, and `statsmodels` will hand you an eighty or
ninety-five percent interval alongside the point.

Use them. A forecast of forty thousand units means one thing if the interval is
thirty-nine to forty-one, and something completely different if it's twenty-five to
fifty-five. Same point forecast. Entirely different inventory decision.

**[pause]**

And notice how the intervals behave as the horizon grows: they **widen**, and for a
differenced series they widen without bound. That is the model being honest. It's telling you
that a random walk has no long-run level to forecast toward, so far enough out, it genuinely
does not know.

A point forecast hides that. An interval shows it. When we get to Bayesian methods in Week 10,
we stop treating the interval as an add-on and make the whole distribution the output.

---

# ▶ SLIDE 16 — ARIMAX: Exogenous Variables with ARIMA Errors

Last model today. When one variable clearly *drives* another rather than the relationship
being symmetric, use ARIMAX.

The structure: regress $y$ on your exogenous predictors in the usual way, and then let the
*errors* follow an ARIMA process. That second part is what makes it more than ordinary
regression. Regression on time series data almost always leaves autocorrelated residuals, and
ARIMAX gives that autocorrelation somewhere legitimate to live instead of quietly breaking
your standard errors.

**[pause]**

Use it when three things hold. The causal direction is clear — advertising drives sales, not
the other way. You already have $x$, or can forecast it. And adding $x$ actually reduces
cross-validated forecast error — check that, rather than assuming it. Adding a predictor
does not automatically help.

**[pause]**

And now the catch that surprises people.

To forecast $y$ at time $t+h$, you need $x$ at time $t+h$. A forecast of your own predictor.

Think about what that means operationally. You build a beautiful model of sales driven by
unemployment. It fits wonderfully. Then someone asks for next quarter's sales — and you
realize you first need next quarter's unemployment, which is its own forecasting problem, with
its own error, which now propagates into yours.

If you can't forecast $x$, ARIMAX buys you nothing at forecast time. Use a VAR instead,
because a VAR generates forecasts for all its variables simultaneously. It solves the problem
by construction.

---

# ▶ SLIDE 17 — Section divider: Key Takeaways and Roadmap

Let's pull it together.

---

# ▶ SLIDE 18 — Key Takeaways

Five things.

**One.** Stationarity is required before fitting anything today. Test with ADF and KPSS —
opposite nulls, so run both. First-differencing removes a stochastic trend.

**Two.** ACF identifies MA order, PACF identifies AR order. Always inspect *after*
differencing, never before.

**Three.** ARIMA combines differencing with AR and MA components, and it contains the naive
forecast and simple exponential smoothing as special cases. SARIMA adds seasonal polynomials.
Use `auto_arima`, but keep your eyes open.

**Four.** VAR models all variables symmetrically and captures the cross-dynamics a univariate
model discards. Keep $k$ at four or fewer. Granger causality tests predictive content — and
predictive content only.

**Five.** ARIMAX adds exogenous predictors. Use it when the causal direction is clear and $x$
is genuinely forecastable.

**[pause]**

If you take one thing: **stationarity first.** Almost every ARIMA mistake I see traces back
to someone reading an ACF they should never have looked at.

---

# ▶ SLIDE 19 — References

Readings are in the syllabus — Chapter 9 for ARIMA, Chapter 10 for dynamic regression, and
section 12.3 for VAR. Either edition works; the chapter numbers are the same.

Next week: Generalized Additive Models. We keep the interpretability we've had so far, but
give up the assumption that effects have to be straight lines.

See you then.

---

## Timing guide

| Segment | Slides | Target |
|---|---|---:|
| Opening & stationarity | 1–8 | ~14 min |
| ARIMA & SARIMA | 9–11 | ~6 min |
| VAR, Granger, ARIMAX | 12–16 | ~15 min |
| Close | 17–19 | ~3 min |

If you need to compress, slide 9's four-step workflow survives trimming. Do **not** compress
slides 5, 6, or 13 — the differencing rule, the "difference before you read the ACF" rule,
and the Granger caveat are the three things students most reliably get wrong.
