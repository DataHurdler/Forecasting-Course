# Lecture 4 — Recording Script

**ECON 8310: Business Forecasting · Decision Trees**

Deck: `Slides/Lecture04_DecisionTrees.pdf` (17 pages) · Measured runtime: **~19 minutes** (17–21 depending on pace)

---

## How to use this document

- **`▶ SLIDE n — Title`** marks where to advance. The number is the PDF page.
- Written to be **spoken**. *Italic parentheticals* are stage directions.
- **[pause]** means actually stop for a beat.
- Change anything that doesn't sound like you.

---

# ▶ SLIDE 1 — Title page

Lecture 4: Decision Trees.

Today the course changes character. Everything in the first three weeks came out of statistics
— exponential smoothing, ARIMA, GAMs. We specified a structure, estimated its parameters, and
read the coefficients.

From here on we're doing machine learning. And the mental shift is this: instead of specifying
a functional form and estimating it, we hand an algorithm a pile of features and let it
discover the structure itself.

**[pause]**

You gain something real. Trees capture interactions and threshold effects automatically,
without you having to know they're there.

You give up something real too. Last week I told you a GAM is additive by construction and
therefore explainable, and that the price of that was no interactions. Today we buy the
interactions back — and start paying in interpretability.

---

# ▶ SLIDE 2 — Lecture Outline

Four parts. Why we go beyond linear models. How a tree actually works. Implementing one in
Python. And where a single tree falls short — which sets up the next two weeks.

---

# ▶ SLIDE 3 — Section divider: Why Go Beyond Linear Models?

*(Divider.)*

Part one. What linear models can't represent.

---

# ▶ SLIDE 4 — The Limits of Linear Models

Three things a constant slope cannot do.

**Interactions.** The effect of advertising during the holiday season isn't the same as its
effect in March. A linear model can only assign advertising one slope. You can add an
interaction term by hand — but only if you already suspected it was there.

**Threshold effects.** Spending might be flat while unemployment sits above five percent, then
move sharply once it drops below. That's a kink. A straight line has no kinks.

**Asymmetry.** Extreme values pull coefficients equally hard in both directions, whether or
not the underlying relationship is symmetric.

**[pause]**

The retail example on the slide ties them together. Monthly sales depend on last year's
same-month sales, on whether it's December, and on the unemployment rate. And the December
effect is *larger* in a strong economy — that's an interaction between seasonality and the
macro environment.

A linear model can represent each of those three variables. It cannot represent the fact that
they modify each other.

**Decision trees capture nonlinearity and interactions automatically.** That's the promise.
The rest of the lecture is about the mechanism and the cost.

---

# ▶ SLIDE 5 — The Bias–Variance Tradeoff

Before the tree itself, the framework we'll use to judge every model from here to December.

Expected mean squared error decomposes into three pieces: bias squared, variance, and
irreducible noise.

**Bias** is systematic error — the model is too simple to represent the truth. A straight line
through a curved relationship has bias, and collecting more data won't fix it.

**Variance** is sensitivity to the particular sample you happened to draw. A model with high
variance would look quite different if you'd collected a different year of data.

**Sigma squared** is irreducible noise. And I want to be precise here, because this gets
misstated: sigma squared is a property of the data-generating process, not of your sample. It
is not "the error you'd remove with better data." More observations shrink variance. Nothing
shrinks sigma squared.

**[pause]**

Now the two columns.

**High bias — underfitting.** Model too simple, misses real patterns, and — this is the
diagnostic — performs badly on *both* training and test sets. If your model is bad on data
it has already seen, it's underfitting.

**High variance — overfitting.** Model too complex, memorizes noise, great on training, bad on
test. The gap between the two is the tell.

**[pause]**

Concretely, from work you've already done. In Homework 1 the undamped Holt model had **low
bias** — it fit the training data's upward trend faithfully — and **high variance** in the
sense that matters here: it was exquisitely sensitive to the trend estimated from that
particular window, and when the trend flattened it was catastrophically wrong. The seasonal
naive benchmark had more bias and far less sensitivity, and it won.

That's the tradeoff, and it wasn't a story about trees. It's the frame for everything.

The goal is the complexity that balances them, and you can only find it out-of-sample. Which
is why Lecture 1 spent so long on that rule.

---

# ▶ SLIDE 6 — Section divider: How Decision Trees Work

Part two. The mechanism — partition the feature space, predict the mean in each region.

---

# ▶ SLIDE 7 — What Is a Decision Tree?

Here's the whole idea in one picture.

A tree asks a series of yes/no questions about the features and arrives at a prediction.

*(Walk the diagram.)*

Start at the top. Was last year's same-month sales below thirty-eight thousand? If yes, go
left, and we're done — the forecast is twenty-eight thousand four hundred.

If no, go right, and there's a second question: was last month above fifty-two thousand? If
yes, forecast forty-four thousand one hundred. If no, sixty-one thousand three hundred.

That's it. Every prediction is the answer at the bottom of one path.

**[pause]**

Four properties worth naming.

It's **non-parametric** — no functional form is assumed anywhere. It's **nonlinear**, and
notice it captures a threshold effect natively, which is what a linear model couldn't do.
It's **interpretable**, because you can trace the exact path. And it's **scale-invariant** —
no standardization needed, because the tree only ever asks "is this value above or below a
threshold," and that question doesn't care about units.

That last one will matter in Lecture 6, where standardization becomes mandatory.

And the warning at the bottom is the whole reason Lectures 5 and 6 exist: a single deep tree
overfits severely.

---

# ▶ SLIDE 8 — The CART Algorithm

How does the tree decide what to ask?

CART builds greedily, top to bottom. At each node it searches over **every feature and every
possible threshold**, and picks the split that most reduces within-region variance.

Look at what's being minimized: the sum of squared deviations from the mean in the left region
plus the same in the right. Split the data in two, and ask how much total variability you
removed.

**[pause]**

Hold onto the word **greedily** — the next slide is entirely about what it costs.

The prediction at a leaf is just the mean of the training observations that landed there.

**[pause]**

The framing I'd offer: at every node the algorithm is asking *"what is the single yes/no
question that best separates high-sales months from low-sales months?"* Then it repeats that
question within each group.

**[pause]**

Let me turn the crank once, on our actual data, because the arithmetic is less mysterious than
the notation.

Take CA_1 food sales — two hundred seventy-three weeks. Before any split, the mean is about
nineteen thousand eight hundred units, and the total sum of squared deviations around that mean
is roughly **one point nine billion**. That number is large because units are large and we're
squaring; ignore its scale and watch what happens to it.

Now the algorithm tries every feature and every threshold. The winner is: *was the four-week
lag at or below eighteen thousand six hundred?*

That splits the data into eighty-five weeks on the left, averaging about **sixteen thousand
nine hundred**, and one hundred eighty-eight weeks on the right, averaging about **twenty-one
thousand one hundred**.

Add up the squared deviations *within* each of those two groups and you get about **nine
hundred million**.

**[pause]**

One point nine billion down to nine hundred million. **A single yes/no question removed
fifty-two percent of the variance.**

That's the entire algorithm. Ask the question that removes the most variance, then repeat
inside each group, then repeat again — until the groups get too small or you hit the depth cap.

For classification, replace variance with Gini impurity or entropy. Same algorithm, different
measure of how mixed a region is.

---

# ▶ SLIDE 9 — Greedy Is Not Optimal — and That Matters

I want to slow down on "greedy," because it is the single most important word on the previous
slide and it is easy to hear it as a criticism when it is really a description.

CART is **exhaustive at each node**. It really does try every feature and every cut point — no
shortcuts, no sampling. So it is not lazy.

What it never does is **look ahead**. It evaluates one split, commits to it, and moves down.

**[pause]**

The table shows what that costs. Suppose splitting on price removes forty percent of the
variance right now. Splitting on promotion removes thirty-eight — slightly worse. But *because*
of how promotion divides the data, it sets up two further splits that would together remove
another fifty percent.

Forty-plus-twelve, versus thirty-eight-plus-fifty. Fifty-two against eighty-eight.

CART takes the forty. Not because it weighed the options and chose badly — because it has no
mechanism to see the fifty coming at all.

**[pause]**

So the tree you fit is **not the optimal tree**. It is the result of a sequence of locally
optimal decisions, and those are genuinely different objects.

The obvious question is why we tolerate that. The answer is that finding the truly optimal tree
is computationally intractable for any realistic number of features — the search space explodes
combinatorially. So the greedy approximation isn't a shortcut somebody settled for; it's what
makes trees usable at all.

Two consequences to carry forward, and both matter for the next three weeks.

First, **a tree can miss structure that is really there** — not from lack of data, but from the
order in which it asked its questions.

Second, and this is the one that pays off next week: a small change in the data can send the
whole greedy sequence down a different path. That is the instability we turn to right now.

---

# ▶ SLIDE 10 — Depth Controls the Bias–Variance Tradeoff

Now connect the tree back to slide 5.

A **depth-one stump** asks one question. Massive bias, almost no variance.

A **full tree** with one observation per leaf reproduces the training data exactly. Zero bias,
extreme variance — it has memorized rather than learned.

Between them sits the depth that minimizes total error, and the table shows the shape. Five to
ten is usually the useful range.

**[pause]**

So: here is why trees are unstable, which matters enormously next week.

Change one training observation. If that changes the split at the root — and it easily can,
because the algorithm is picking the single best threshold — then *every prediction below it*
changes. Not slightly. The whole structure downstream is different.

That's not a flaw in the implementation. It's inherent to a greedy hierarchical partition. And
it is precisely the property that averaging will exploit in Lecture 5.

Tune with `max_depth` and `min_samples_leaf`, selected by `TimeSeriesSplit` cross-validation.

---

# ▶ SLIDE 11 — Two Ways to Stop a Tree Overfitting

`max_depth` is the blunt instrument — it caps the tree in advance, before you know how deep it
needed to go. Two other controls do the job better, and they usually get one line each in a
table, which is not enough.

**`min_samples_leaf`** is the one I'd reach for first. Leave it at the default of one and the
tree may build a leaf holding a single observation, whose "prediction" is that one observation's
value. That is memorization with extra steps. Set it to ten and every prediction is an average
over at least ten weeks — smoother, and far more honest about what the data supports.

**`ccp_alpha`** works the other way around. Grow the tree out fully, *then* charge a penalty per
leaf and cut back the branches that don't pay for themselves. Larger alpha, smaller tree.

**[pause]**

Look at what cost-complexity pruning actually minimizes: fit on the left, a penalty proportional
to the number of leaves on the right, and alpha setting the exchange rate between them.

You have seen this before. That is the GAM smoothing penalty from Lecture 3 with a different
symbol on it — fit against complexity, one parameter tuning the trade. And you'll meet it a
third time in Lecture 6, as Ridge and LASSO.

Three model families that look nothing alike, one idea underneath. I'd rather you remember the
idea than the three implementations, because the idea is what transfers.

And alpha is chosen the same way every time: by cross-validation. Which for us means
`TimeSeriesSplit`.

---

# ▶ SLIDE 12 — Section divider: Implementing Decision Trees in Python

Part three. One class, a few hyperparameters.

---

# ▶ SLIDE 13 — Decision Tree Regression in Python

The code is short.

Import `DecisionTreeRegressor`. Build lag features. Instantiate with `max_depth=5`,
`min_samples_leaf=10`, and `random_state=42`. Fit. Predict.

The table gives you the four hyperparameters worth knowing. Two of them — `min_samples_leaf`
and `ccp_alpha` — we just spent a slide on. `max_depth` caps the depth. And `max_features` does
feature subsampling: remember that one, because it becomes the central idea next week.

**[pause]**

And the line at the bottom, which you've now heard in every lecture: cross-validate with
`TimeSeriesSplit`, never `KFold`. Random folds leak the future into the training set.

I'll keep saying it because it's the error that survives longest. It doesn't produce a crash
or a warning — it produces a number that looks better than the truth.

---

# ▶ SLIDE 14 — Feature Importance

A tree will tell you which variables it found useful.

Impurity-based importance sums, for each feature, the total variance reduction across every
split where that feature was used, weighted by how many observations passed through. Then
normalize so it sums to one.

On our weekly Walmart data a depth-five tree ranks them like this: the **four-week lag**
dominates at about zero point six two, then the **same week last year** at zero point one five,
then **last week** at zero point one three, and then **SNAP benefit days** and **price**, both
around zero point zero four.

Notice how concentrated that is — one feature takes almost two-thirds of the total. That is
characteristic of a single tree, and it is a symptom of the greediness we discussed: the root
split commits to one feature and everything below inherits that choice. Next week you'll see
the same table from a random forest, and the mass is spread much more evenly.

Read that as a screening device. It says which variables the tree leaned on — a fast way to
narrow forty candidate predictors down to eight worth thinking about.

And notice SNAP appearing at all, because it's the kind of thing this method is good for.
Nobody specified that food sales respond to benefit disbursement days. The tree found it, and
ranked it level with price. That's a real business finding no linear specification would have
surfaced unless someone already thought to look.

**[pause]**

But be careful, because impurity importance is **biased toward high-cardinality features**.

Look at our own table. `avg_price` is continuous — it offers hundreds of distinct split points,
so the algorithm gets hundreds of chances to find one that happens to help. `snap_days` takes a
handful of integer values, and `event_days` fewer still. Price gets more opportunities to look
useful purely because it has more thresholds to try, not because it carries more signal.

Which means the gap between price at zero point zero four and SNAP at zero point zero four is
not something I'd read anything into at all — and if anything, the bias runs in price's favor.

Permutation importance is the honest alternative: shuffle one column, and measure how much
accuracy falls. Slower, and worth it whenever the ranking will inform a decision. We'll use it
properly next week.

---

# ▶ SLIDE 15 — Interpreting and Communicating Tree Predictions

This is the tree's real advantage, and it's worth dwelling on because you lose it steadily from
here.

You can explain **why** a specific prediction came out the way it did.

*(Read the manager quote from the slide.)*

Notice what that explanation is: it's just the decision path, read aloud. Last year's
same-month sales were above thirty-eight thousand. Last month was above fifty-two thousand.
When both hold, the average outcome in our training data was sixty-one thousand three hundred.

No coefficients. No "holding all else constant." A sequence of conditions and an average.

**[pause]**

`plot_tree` or `export_text` will produce this for you.

And here's why it matters commercially. A manager who can see the splits can tell you when the
model is wrong — "that threshold is picking up the year we had the fire, not a real pattern."
You cannot get that feedback from a model nobody can read. It's the cheapest source of domain
knowledge you have, and every method after this one makes it harder to access.

---

# ▶ SLIDE 16 — Section divider: Limitations and Preview

Part four. Where a single tree falls short.

---

# ▶ SLIDE 17 — When a Single Tree Falls Short

Strengths on the left, and they're real: interpretable, no scaling needed, captures
nonlinearity, handles missing values, fast to train.

Weaknesses on the right, and the first one is fatal.

**High variance.** We covered the mechanism on slide 9 — small data changes give a very
different tree.

**Flat predictions within each leaf.** Every observation in a leaf gets the identical forecast.
The prediction surface is a step function.

**Cannot extrapolate beyond the training range.** This one deserves a beat. A tree predicts the
mean of a leaf, and no leaf can contain values it never saw. So on a trending series, a tree
will flatten out exactly when you need it to keep climbing. If your sales have grown every year
and you ask a tree to forecast next year, it will predict something inside the range it already
knows.

Put a number on it. CA_1 food sales grew about twenty-nine percent over five years. Train a
tree on the first four and ask it for year five, and the highest value it can possibly output
is the highest leaf mean it learned — a number from the *old*, lower range. It will
systematically under-forecast, and no amount of tuning fixes it, because the model has no
representation of "up."

An ARIMA with a drift term has no such problem. It will happily forecast values it has never
seen.

That limitation never goes away. Random forests have it. XGBoost has it. It's a property of
trees, and it's why the classical methods from weeks one and two don't simply become obsolete
today.

**[pause]**

And the ensemble solution, which is next week: average many trees trained on different
bootstrap samples. Variance falls sharply while the feature-importance interpretability
survives — typically twenty to forty percent better RMSE than a single tree.

---

# ▶ SLIDE 18 — Lecture 4: Key Takeaways

Five things.

**One.** Linear models cannot capture interactions or threshold effects. Trees can, without
your specifying them in advance.

**Two.** The bias–variance tradeoff: too-simple underfits, too-deep overfits. Tune with
`max_depth` and `min_samples_leaf`.

**Three.** CART greedily minimizes within-region variance at each split. The prediction is the
mean of the leaf.

**Four.** Trees are interpretable — you can trace the exact path to any prediction.

**Five.** Single trees have high variance. Ensembles solve this, and that's Lecture 5.

**[pause]**

If you take one thing: **a tree is a step function that cannot extrapolate.** Everything good
and everything bad about today follows from that sentence.

---

# ▶ SLIDE 19 — References

Reading is ISLP section 8.1 — the basics of decision trees. That's the chapter we'll live in
for the next two weeks as well.

Next time: Tree Ensembles. We take this unstable, high-variance model and turn its instability
into an advantage.

See you then.

---

## Timing guide

| Segment | Slides | Target |
|---|---|---:|
| Opening & why beyond linear | 1–5 | ~5 min |
| How trees work | 6–11 | ~10 min |
| Python & interpretation | 12–15 | ~5 min |
| Limitations & close | 16–19 | ~2 min |
| **Total** | | **~22 min** |

If you're compressing, slide 13's hyperparameter table survives trimming — slide 11 has already
covered the two parameters that matter. Do **not** compress slides 9, 10, or 17: the greedy
approximation, the instability it produces, and the extrapolation limit are the three things
Lectures 5 and 6 are built on.
