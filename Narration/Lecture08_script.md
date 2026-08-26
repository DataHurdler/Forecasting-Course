# Lecture 8 — Recording Script

**ECON 8310: Business Forecasting · CNN Architectures**

Deck: `Slides/Lecture08_CNNs.pdf` (19 pages) · Measured runtime: see the timing guide

---

## How to use this document

- **`▶ SLIDE n — Title`** marks where to advance. The number is the PDF page.
- *Italic parentheticals* are stage directions. **[pause]** means stop for a beat.
- Slide 7 plants an objection about pooling and slide 15 pays it off with a measurement. Do not
  resolve it early — the delay is what makes the number land.

---

# ▶ SLIDE 1 — Title page

Lecture 8: CNN Architectures.

Last week we built a feedforward network and I told you, fairly bluntly, that it was a competitor
to XGBoost rather than an upgrade. Same flat table going in, no notion of order, and on our data
it loses.

Today the architecture starts doing work. A convolutional network makes an *assumption* about the
structure of its input — that nearby things are related and distant things usually aren't — and
it builds that assumption into the shape of the model rather than into features you engineered by
hand.

**[pause]**

That's the theme of the next two lectures. Not a better optimizer, not more layers. A model whose
*shape* encodes what kind of data it expects.

---

# ▶ SLIDE 2 — Lecture Outline

Four parts. Convolution itself — what a filter is and what it costs. Pooling, which is where I
want you to be suspicious. Then twenty years of image architectures, compressed into the three
ideas that outlived them. And then one-dimensional CNNs on our own time series, with an honest
measurement at the end.

**[pause]**

A word on why we're spending time on image architectures in a forecasting course, since that's a
fair question to have.

Two reasons. The first is that three of their ideas transfer directly, and you'll recognize one of
them again next week inside a completely different model. The second is that the history is a
worked example of the thing this course keeps insisting on: every one of these architectures won
by encoding a *better assumption* about its data, not by being bigger. That's the transferable
lesson, and it happens to be easier to see in pictures than in demand curves.

---

# ▶ SLIDE 3 — Section divider: Convolution — The Core Idea

Two ideas: look locally, and reuse what you learn everywhere.

---

# ▶ SLIDE 4 — Why Convolution?

Start with why a fully connected layer fails on structured input, because the failure is
dramatic.

A two-twenty-four by two-twenty-four image has just over fifty thousand pixels. If you feed that
into a single hidden layer of a thousand neurons, that layer needs **fifty million weights**. For
one layer.

Put that next to last week's network, which had twenty-two thousand six hundred fifty-seven
parameters in total.

**[pause]**

But the cost is not the worst part. The waste is.

That fully connected layer has no notion that neighbouring pixels are related and distant ones
usually are not — it treats pixel one and pixel fifty thousand as equally likely to interact. And
it does not generalize position: a pattern it learns in the top-left corner is stored completely
separately from the same pattern in the bottom-right. It has to learn everything twice.

*(Point at the key box.)*

A convolutional layer fixes both problems with two ideas. **Local connectivity** — each neuron
sees only a small window, called its **receptive field**. And **weight sharing** — the same
filter is applied at every position in the input.

Far fewer parameters, and a pattern learned anywhere is recognized everywhere.

**[pause]**

The analogy that makes it stick: you don't memorize the letter "A" separately for every position
on the page. You learn it once, and you apply that one recognizer everywhere you look. A filter
does exactly that.

**[pause]**

And notice this is the same *kind* of move we've made before, in a different costume. Weight
sharing is a constraint. We are telling the model, before it sees any data, that a pattern
occurring at position ten and the same pattern at position two hundred should be treated
identically. That is a strong assumption, and it is what buys the parameter reduction.

Constraints that encode true structure make models better. Constraints that encode false structure
make them worse, and no amount of training fixes it. Hold that thought — by the end of this
lecture we will have an example of each, on the same dataset.

---

# ▶ SLIDE 5 — How a Convolutional Layer Works

For a sequence — which is what we care about — a one-dimensional convolution slides a filter of
length K along the series, and at each position it takes a dot product.

That's the formula on the slide, and honestly the formula is less useful than the picture: a
small window sliding along, computing one number at each stop.

*(Walk the four hyperparameters.)*

**Kernel size** is the filter length. Bigger means a wider receptive field — more context per
output — and more parameters.

**Stride** is how far the filter jumps between positions. Stride two halves your output length.

**Padding** puts zeros at the edges. Setting padding to `'same'` keeps the output the same length
as the input, which saves you a lot of arithmetic.

**Filters** is how many *different* patterns you want to learn. That number becomes the channel
count of the output.

**[pause]**

Here's what to hold onto. Each filter learns **one local pattern** — an edge, a spike, a seasonal
dip. What comes out is called a **feature map**, and its high values mark the places where that
pattern was found.

**[pause]**

Two things follow from that, and they're worth stating explicitly because they shape how you read
the results later.

First, the filter's weights are **learned**, not designed. You don't tell it to look for a
promotional spike. You give it a slot for thirty-two patterns and gradient descent decides what
those patterns are. That is the "learned features" promise — the thing that's supposed to replace
your hand-built lag columns.

Second — and this is the constraint — a filter can only see K steps at a time. Stack two layers
and the second one sees a window of windows, so the reach grows, but it grows *slowly*. This is
called the **receptive field**, and I'm naming it now because it is going to be the single most
important number in this lecture.

---

# ▶ SLIDE 6 — Section divider: Pooling and Dropout

---

# ▶ SLIDE 7 — Pooling: Downsampling Feature Maps

**Pooling** reduces a feature map by summarizing each little region with one number. Max pooling
takes the largest value in the window. Average pooling takes the mean. A two-by-two max pool with
stride two cuts the number of values to a quarter.

You buy two things. **Fewer parameters downstream**, because the later layers see a smaller input.
And **translation invariance** — shift the input slightly and the pooled output barely changes,
so the network recognizes a cat whether it's left or right of centre.

**[pause]**

*(Now slow down. This box is the setup for slide 15.)*

And here is where I want you to get suspicious.

Translation invariance is a **feature** for images and a **problem** for forecasting.

Think about what it's actually doing. If a demand spike moved three weeks later, pooling treats
that as noise to be smoothed away. But that shift is not a nuisance — for a forecaster, *when the
spike happened* is very often the entire thing you're trying to predict.

Pooling deliberately discards **where** in the window a pattern occurred. For an image classifier
that's exactly right. For a time series, position is frequently the signal.

**[pause]**

Hold that objection. Don't resolve it yet. We're going to measure precisely what it costs, later
in this lecture.

---

# ▶ SLIDE 8 — Section divider: CNN Architecture Evolution

Twenty years of image models, and the three ideas that outlived them.

---

# ▶ SLIDE 9 — LeNet to VGG: Depth and Small Filters

**LeNet-5**, in 1998, established the template that everything since has followed: alternating
convolution and pooling layers, then fully connected layers at the end. Roughly sixty thousand
parameters, and it read handwritten digits on bank cheques — a real deployed system, in the
nineties.

**VGG**, in 2014, scaled that up and made one sharp simplification. Use **only** three-by-three
filters — but stack a lot of them.

Why does that work? Two stacked three-by-threes see the same receptive field as one five-by-five.
But they use fewer parameters, and you get an extra nonlinearity in between them, which makes the
combination strictly more expressive.

*(Point at the key box.)*

That is the lesson that carried forward: **depth built from small filters beats width built from
large ones.** Cheaper and more expressive. It's why nearly every modern architecture is deep and
narrow rather than shallow and wide.

**[pause]**

VGG's cost was its size — around a hundred thirty-eight million parameters, and most of those
were sitting in the final fully connected layers, not in the convolutions at all. That is exactly
the problem the next two architectures went after.

**[pause]**

That detail is worth pausing on, because it is a good lesson about where cost actually lives. The
convolutions — the part everyone talks about — were relatively cheap, precisely because of weight
sharing. The expensive part was the ordinary dense layers bolted on the end, which have no sharing
at all.

When you profile a model and find the bottleneck, it is very often in the least interesting
component. That's true of forecasting pipelines too: the modelling is rarely what costs you, the
data preparation is.

---

# ▶ SLIDE 10 — Inception and ResNet: Depth That Trains

Two different attacks on that problem.

**Inception** asked a good question: why should a layer commit to one filter size at all? Its
module runs one-by-one, three-by-three and five-by-five convolutions **in parallel** and
concatenates the results, letting the network decide which scale matters. The one-by-one
convolutions do something clever — they cut the channel count first, so the expensive
convolutions operate on a smaller input.

**ResNet** solved a different problem, and it's the one that transfers to us.

Past a certain depth, deeper networks were getting **worse**. Not from overfitting — the training
error was worse too. The gradients were degrading on their way back through many layers.

The fix is one line: y equals F of x, **plus x**. A **residual**, or skip, connection.

**[pause]**

Two ways to read that. Each block now learns the *difference* from its input rather than a whole
new representation — usually an easier job. And the plus-x gives the gradient a direct path
backward, unimpeded by the layers in between.

That single change made networks of a hundred layers and more trainable. Skip connections now
appear in essentially every deep architecture — including the Transformers we'll see in Lecture 9,
and, as it turns out, inside the LSTM, which predates ResNet by eighteen years.

**[pause]**

I want to draw out why the addition matters, because we will use this exact argument again next
week and it's easier to absorb twice.

When a gradient travels backward through a chain of layers, each layer *multiplies* it by
something. Multiply enough numbers below one together and you get essentially zero — the signal
dies before it reaches the early layers, so they never learn.

Addition doesn't do that. The plus-x term hands the gradient a route home that skips the
multiplication entirely. Repeated multiplication shrinks; repeated addition doesn't.

Remember that sentence. In Lecture 9 you'll see the LSTM's cell state doing precisely the same
thing, for precisely the same reason, invented eighteen years earlier for time rather than for
depth.

---

# ▶ SLIDE 11 — What Carries Over to Time Series

These architectures were built for images, on problems that look nothing like weekly demand
forecasting. Three of their ideas transfer anyway.

**Small stacked filters.** A width-three filter applied twice sees six weeks of context, with far
fewer weights than one width-six filter would need.

**Skip connections.** Same fix, same problem — gradients that fade as they travel back through
depth.

**Learned features.** You stop hand-engineering lag windows and let the filters find whichever
local shapes actually matter.

**[pause]**

*(And now name the one that doesn't.)*

One idea does **not** transfer, and it's the one we flagged twenty minutes ago: pooling for
translation invariance.

An image classifier should not care where the cat is. A forecaster usually should care very much
where the spike was.

**[pause]**

So we're carrying two assumptions into the next section, and they are not equally good.

**Locality** — that nearby time steps are more related than distant ones — is largely *true* of
demand data. Last week matters more than the week before. Good assumption.

**Translation invariance** — that where a pattern occurred doesn't matter — is largely *false* for
forecasting. Good assumption for images, bad one here.

A CNN gives you both, bundled together, because they came from the same field. Part of using one
well is knowing which half you actually wanted.

---

# ▶ SLIDE 12 — Section divider: 1D CNNs for Time Series

The same machinery, along a time axis — and what it costs.

---

# ▶ SLIDE 13 — Why Use a 1D CNN for Forecasting?

Here's the setup. A one-dimensional CNN takes a **window** of the recent past — say twenty-six
weeks — across several channels, and predicts the next value. Each channel is one series: units,
SNAP days, event flags, price.

The appeal is that you stop choosing lags. Instead of deciding that lag one, lag four and lag
fifty-two are the ones that matter, you hand the model the whole window and let the filters work
out which local shapes predict what comes next.

*(Point at the key box.)*

Two advantages that are genuinely real. It's far cheaper than a fully connected network on the
same window — that's weight sharing again. And it handles **many parallel series** naturally,
because the same filters apply to every store-category at once.

**[pause]**

*(Now the catch, and flag it as the reason for the result on slide 15.)*

But the catch is the receptive field, and it's serious.

Stack a width-five filter and a width-three filter and you see about **seven weeks** of context.
That's it. Annual seasonality sits fifty-two weeks away, and no reasonable stack of small filters
is going to reach that far.

So you have two options. Add dilation — filters with gaps in them, which reach further for the
same parameter count. Or feed the annual lag in as its own channel, which is a confession that
you're doing feature engineering after all.

**[pause]**

And notice what that second option costs you rhetorically. The entire pitch for a CNN was "stop
choosing lags, let the filters find the structure." The moment you hand it `lag_52` as a channel
because the receptive field can't reach, you have given that pitch back. You're now doing feature
engineering *and* paying for a neural network.

That is not a reason never to use one. It is a reason to be clear-eyed about what the architecture
is actually buying you on a given problem.

Remember that number — seven weeks. It explains the results two slides from now.

---

# ▶ SLIDE 14 — 1D CNN Forecasting Pipeline in PyTorch

Six lines. Two convolutions with ReLUs, a pooling step, a flatten, and a linear layer down to one
number.

One thing that trips everyone up: the input shape is `(batch, channels, time)`. Channels come
**before** time. That is the transpose of how the data naturally sits in a dataframe, and it's
also the opposite of what `nn.LSTM` wants next week. You will get this wrong at least once; the
error message is unhelpful.

Everything from Lecture 7 still applies. Adam with weight decay. `zero_grad()` every batch.
`shuffle=False`. Split by time, not at random.

*(Point at the muted note.)*

And note what `AdaptiveAvgPool1d(1)` does: it averages across the *entire* time axis, collapsing
it to a single number per channel.

Watch what that costs on the next slide.

---

# ▶ SLIDE 15 — Does It Actually Work?

*(This is the payoff slide. Walk the table, then land both punchlines.)*

Same weekly panel. Twenty-six-week windows, four channels, thirty store-category series, the same
test block as Homework 4 — so these numbers are directly comparable to work you've already done.

LASSO, with forty-six engineered features: seven forty-four. XGBoost: seven eighty-one. Random
forest: eight ninety-nine.

Then the CNNs. Flatten head: one thousand thirty-two. Global max pool: fourteen eighteen. Global
average pool: fifteen thirty-four.

Seasonal naive, at the bottom: twenty-one fifty-two.

**[pause]**

Two things to take from this.

First — **every CNN variant loses to a forty-six-coefficient linear model.** Not narrowly. And now
you know why: a seven-week receptive field cannot see the annual lag that LASSO was simply handed
as a column. The architecture's assumption about locality is wrong for this data.

Second, and this is the one I promised you.

*(Point at the last paragraph.)*

Swapping average pooling for `Flatten` — which keeps *where* each pattern occurred, instead of
averaging it away — is worth about **five hundred RMSE**. Three seeds each, against a run-to-run
spread of roughly eighty. That gap is real.

That's the objection from slide 7, measured. Pooling threw away position, and position was
carrying signal.

**[pause]**

And I want to be careful about how far to push that conclusion, because there's a tempting
overreach here.

This does **not** mean pooling is bad. It means pooling encodes an assumption — that position is
irrelevant — and on this dataset that assumption is false. Run the same experiment on image
classification and the sign would flip, decisively.

That's the shape of nearly every result in this course. There is no ranking of methods that holds
across problems. There's a match, or a mismatch, between what the method assumes and what the data
is. Your job is to know what your method assumes — which is much harder than knowing how to call
it, and much more valuable.

---

# ▶ SLIDE 16 — Section divider: Key Takeaways

---

# ▶ SLIDE 17 — CNN Architecture Summary

*(Table, then the two paragraphs. The second is the more useful one.)*

The lineage in one table. LeNet gave us the template. VGG: small filters, stacked deep. Inception:
parallel filter sizes, and one-by-ones to control cost. ResNet: skip connections, which made real
depth trainable. And the 1D CNN, which is that same machinery run along a time axis.

**Reach for a 1D CNN** when local shape matters more than exact position, when you have many
parallel series, or as a cheap feature extractor that feeds something else.

That third use is underrated, incidentally. You don't have to use a CNN as the whole model. A
common production pattern is to let convolutions compress a long raw window into a handful of
learned summary features, then feed *those* into gradient boosting alongside your engineered
columns. You get the pattern discovery without betting the forecast on it.

**Do not reach for one** when the dominant signal is at a long lag, when you already have well
engineered tabular features, or when a stakeholder needs to read the model and understand it.

**[pause]**

And be honest about what that second list covers. On the evidence we just saw, it describes most
of what we forecast in this course.

**[pause]**

Which raises the obvious question: why teach it, then?

Because the receptive field problem is not a fact about CNNs, it's a fact about *this data* — a
strong annual cycle and a short window. Change either one and the answer changes. And because
convolution is a component, not just a model: it shows up inside architectures you'll meet later,
in production forecasting systems, and in every paper on the subject. Knowing what it assumes is
what lets you predict, before fitting anything, whether it will work on a problem you haven't
seen yet.

That prediction — made in advance, from structure rather than from trying it — is the skill this
course is actually training.

---

# ▶ SLIDE 18 — Lecture 8: Key Takeaways

One. Convolution is local connectivity plus weight sharing. A pattern is learned once and detected
everywhere, at a fraction of the parameters.

Two. Pooling buys translation invariance — which an image classifier wants and a forecaster
usually does not. Measured cost on our data: about five hundred RMSE.

Three. The architecture history reduces to three transferable ideas: small filters stacked deep,
skip connections for trainable depth, and learned rather than hand-engineered features.

Four. A 1D CNN takes a window across channels and predicts the next step. Its weakness is the
receptive field — seven weeks of context cannot see an annual lag.

And five. On our panel, every CNN variant lost to a forty-six-coefficient LASSO. Architecture has
to fit the problem. It is not a ladder you climb.

**[pause]**

Next time: RNNs and LSTMs. Architectures built to carry state through time — which is precisely
what the receptive field could not do.

---

# ▶ SLIDE 19 — References

*(Advance and close. No narration needed.)*
