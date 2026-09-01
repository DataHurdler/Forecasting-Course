# Lecture 9 Part 2 — Recording Script

**ECON 8310: Business Forecasting · Transformers**

Deck: `Slides/Lecture09_Part2_Transformers.pdf` (20 pages) · Measured runtime: see the timing guide

---

## How to use this document

- **`▶ SLIDE n — Title`** marks where to advance. The number is the PDF page.
- *Italic parentheticals* are stage directions. **[pause]** means stop for a beat.
- Slide 12 lists three advantages; slide 16 shows each one being irrelevant here. That pairing is
  the argument — deliver 12 with genuine enthusiasm so 16 has something to knock down.
- The positional-encoding ablation on slide 16 is the one number students remember. Land it.

---

# ▶ SLIDE 1 — Title page

Lecture 9, Part 2: Transformers.

Last week we built a recurrent network and found something surprising — the plain RNN beat the
LSTM at every window length we tried. Today we build the architecture that displaced both of them
everywhere else in machine learning.

**[pause]**

I want to be honest about the shape of this hour, because it mirrors last week. We're going to
spend most of the lecture on a mechanism that is genuinely one of the most important ideas of the
last decade — attention — and then measure it on our data and find it ties the LSTM.

That's not a reason to skip it. Attention is why the tools you use every day exist. But the gap
between "reshaped an entire field" and "helps with weekly demand forecasting" is exactly the gap
this course exists to teach you to see in advance.

---

# ▶ SLIDE 2 — Lecture Outline

Five parts. What recurrence could not do — two specific constraints. Then attention itself, which
is a weighted lookup and much less mysterious than the formula makes it look. Then the encoder
block, which is attention plus three things you already know. Then the implementation and an
honest measurement. And finally where all six sequence architectures sit relative to each other.

---

# ▶ SLIDE 3 — Section divider: What Recurrence Could Not Do

Two constraints that are built into reading a sequence one step at a time.

---

# ▶ SLIDE 4 — Two Problems Built Into Recurrence

Part 1 left us with a working recurrent forecaster. Both of its remaining problems come from the
same source: it reads strictly left to right.

**The information bottleneck.** Everything the model knows about step three has to survive being
squeezed through every hidden state between three and the end of the window. An LSTM's gates make
that survival more likely — that's what they're for — but the entire history is still being
compressed into one fixed-size vector, over and over.

**The sequential bottleneck.** Step t cannot be computed until step t minus one is finished. That
is a hard constraint, not an implementation detail. A thousand-step sequence takes a thousand
sequential operations no matter how many GPUs you own. Convolutions parallelize beautifully;
recurrence cannot.

**[pause]**

*(Point at the key box.)*

Attention removes both at once, and the idea is almost aggressively simple: let **every position
look directly at every other position**, in one operation.

No compression through intermediate states — position twenty-six reads position three directly.
And no ordering constraint on the computation — all positions are computed simultaneously.

---

# ▶ SLIDE 5 — Section divider: The Attention Mechanism

A learned, weighted lookup — which is a more useful way to read it than the formula suggests.

---

# ▶ SLIDE 6 — Scaled Dot-Product Attention

*(Point at the definition box, then immediately translate it.)*

Here's the formula. Attention of Q, K, V equals softmax of Q K-transpose over root d-k, times V.

That's the whole mechanism. Every Transformer in the world is that line, repeated.

Now let me translate it, because the formula makes it look more exotic than it is. Read it as a
**lookup table with soft matching.**

Each position emits a **query** — that's the "what am I looking for?" vector. Every position also
offers a **key**, which says "here's what I have." And a **value**, which says "here's what I
would contribute if you pick me."

**[pause]**

So: Q times K-transpose scores every query against every key. That's a big matrix of similarity
scores — every position against every position. The softmax turns each row of those scores into
weights that sum to one. And then you multiply by V, which gives you a weighted average of the
values, with more weight wherever query and key matched well.

That's it. Score, normalize, average.

**[pause]**

And it's worth noticing you have built something very close to this already, by hand. In Homework
4, a rolling mean is a weighted average over recent positions — with weights you fixed in advance,
equal across the window. A Fourier term is a weighted combination too, with weights set by a
formula.

Attention is the same *shape* of operation with the weights **learned**, and recomputed for every
input. That's the whole upgrade. Not a new kind of mathematics — a new source for the numbers.

*(Point at the scaling term.)*

Why divide by root d-k? Because dot products grow with dimension. In high dimensions the raw
scores get large, and large inputs push the softmax toward a one-hot distribution — all the weight
on one position — where its gradient is nearly zero and nothing trains. Dividing by root d-k keeps
the scores in a range where the softmax stays soft.

It's a numerical fix, not a conceptual one, but leave it out and the model doesn't learn.

---

# ▶ SLIDE 7 — What That Buys a Forecaster

Let me make that concrete for our problem.

You're predicting units for the first week of December. With attention, the model can place high
weight on **last** December, and on the weeks around it, and near-zero weight on an unremarkable
Tuesday in March. It looks where the information is.

Two properties make that genuinely different from anything we've built.

**[pause]**

**The weights are learned, not specified.** You do not tell the model that lag fifty-two matters.
Contrast that with Lecture 6, where you built the `lag52` column by hand and the LASSO penalty
merely decided whether to keep it. Here the model discovers which positions to consult.

**And the path is direct.** Attention reaches week t minus fifty-two in **one** operation. A
recurrent model needs fifty-two successive state updates to get there — and we saw last week what
survives fifty-two multiplications. A CNN needs a receptive field that wide, which it doesn't have.

Distance costs attention nothing. That's the headline.

**[pause]**

There's a third property worth naming, because it matters for how you'd sell this to a
stakeholder. Attention weights are **inspectable**. You can pull out the matrix and look at which
weeks the model consulted when it made a given forecast.

That is not the same as an explanation — a high attention weight tells you where the model looked,
not why it decided what it decided, and there's a real literature arguing about how much to read
into them. But compared with an LSTM's hidden state, which is sixty-four numbers with no
interpretation whatsoever, it's a meaningful step toward a model whose reasoning you can
interrogate.

*(Point at the warning box.)*

**[pause]**

And here's the price, which is real. Scoring every position against every other position is
**quadratic** — order T-squared in both time and memory. At T equals twenty-six, that's
irrelevant. At T equals ten thousand, it is the central engineering constraint of the entire
field, and there's a whole literature on approximating it.

---

# ▶ SLIDE 8 — Multi-Head Attention

One attention operation produces one set of weights — one notion of what is relevant. That's
limiting, because different kinds of relevance coexist in the same sequence.

**Multi-head attention** runs h attention operations in parallel, on different learned projections
of the same input, then concatenates the results.

Each head can specialize. In a forecasting model, one head might track position within the month,
another the annual cycle, another the effect of promotional flags — all attending over the same
window simultaneously.

**[pause]**

*(Point at the cost paragraph — this is the counterintuitive part.)*

And the cost is not what you'd guess.

You might expect eight heads to cost eight times one head. They don't. Each head works in a
**lower-dimensional subspace** — d-model divided by h. So eight heads of sixteen dimensions each
cost about the same as one head of one hundred twenty-eight.

You're not adding capacity. You're partitioning the capacity you already had, and letting
different partitions specialize. The diversity is close to free, which is why nobody uses a single
head.

Our model below uses four heads with d-model of sixty-four — four heads of sixteen dimensions.

---

# ▶ SLIDE 9 — Section divider: The Transformer Encoder

Attention, plus the three pieces that make it trainable.

---

# ▶ SLIDE 10 — The Encoder Block

A Transformer encoder layer is four components in a fixed arrangement, and the good news is that
you already know three of them.

*(Walk the table.)*

**Multi-head attention** — every position attends to every position. That's the new part.

**Residual plus LayerNorm** — z equals LayerNorm of x plus MultiHead of x. That's the ResNet skip
connection from Lecture 8, doing exactly the same job: giving the gradient an additive path home.

**A feed-forward sublayer** — a small MLP applied to each position independently. That is
literally the network from Lecture 7, run at every time step.

**Residual and LayerNorm again**, this time around the feed-forward block.

Stack N of those and you have the encoder. Nothing in the block is new to you except attention
itself.

That is genuinely worth pausing on. The architecture that reorganized machine learning is one new
mechanism, wrapped in a residual connection from 2015 and a two-layer network from the 1980s.

Progress in this field often looks like that from the inside — not a wholesale reinvention, but
one new component slotted into scaffolding that already worked. It's a reason to learn components
rather than model names.

**[pause]**

*(Now set up the next slide. This is a deliberate cliff.)*

And one thing is conspicuously missing. It is not an oversight, and I want you to spot it before
I say it.

Look at every operation in that block. Attention: a weighted average over positions.
Feed-forward: applied to each position independently. LayerNorm: per position. Residual: per
position.

**Nothing in there depends on the *order* of the input.**

---

# ▶ SLIDE 11 — Positional Encoding: Attention Cannot Tell Time

Let's make that precise, because it's the most important slide in the lecture.

Attention computes a weighted average over positions. Averaging does not care about order.
Shuffle the input sequence, and every attention output is **unchanged**.

The technical term is that attention is **permutation-invariant**.

**[pause]**

For language that's fatal — "dog bites man" and "man bites dog" would be identical inputs. For
forecasting it's arguably worse. A model that cannot distinguish last week from thirty weeks ago
is not forecasting at all; it's computing a weighted average of an unordered bag of numbers.

So the fix is to add position information **to the input itself**, before attention ever sees it.

*(Point at the sinusoid formulas.)*

The original paper uses fixed sinusoids at different frequencies — sines on the even dimensions,
cosines on the odd ones, with wavelengths that grow geometrically.

Two properties make that work. Each position gets a **distinct** pattern across dimensions, so the
model can tell positions apart. And **nearby positions get similar patterns**, so the model can
learn relative distance rather than just absolute index. You can also learn the position vectors
instead of fixing them; both are used in practice.

**[pause]**

We measure exactly what removing this costs, on the slide after next. Hold the question.

---

# ▶ SLIDE 12 — Why Transformers Took Over

*(Deliver this slide with real enthusiasm. Slide 16 needs something to argue with.)*

Three properties, in the order they actually mattered commercially.

**Parallelism.** Every position is computed at once. Training scales across hardware in a way
recurrence never could. And I want to be clear that this — more than accuracy — is why the
architecture won. It could absorb far more data and far more compute per unit of wall-clock time
than an RNN. When your competitive advantage is training on more data, the architecture that
trains faster wins by default.

**Direct long-range paths.** Any position reaches any other in one step. There is no distance at
which information degrades. Compare the ten-to-the-minus-nine we computed last week.

**Scale.** The architecture kept getting better as parameters and data grew, well past the point
where earlier architectures plateaued. That property is the entire foundation of the last five
years of AI. BERT is an encoder stack used for understanding; GPT is a decoder stack used for
generation. Both are this block, repeated.

**[pause]**

*(Now plant the doubt.)*

Read that list again with a forecaster's eye, though.

Every single one of those advantages is about **large data and long sequences**.

Hold that against what we actually have: a twenty-six-week window, and five thousand nine hundred
forty training examples.

---

# ▶ SLIDE 13 — Section divider: Transformers for Time Series

The implementation, the measurement, and an honest reading of it.

---

# ▶ SLIDE 14 — Transformer Encoder in PyTorch

`nn.TransformerEncoderLayer` gives you the entire block — multi-head attention, both residuals,
both LayerNorms, the feed-forward sublayer. `nn.TransformerEncoder` stacks N of them. You add a
linear layer to project your features up to d-model, and another to project down to one output.

Note `batch_first=True` again, giving `(batch, seq_len, features)` — same as the LSTM, opposite of
`Conv1d`.

**[pause]**

*(This is the practical warning. Emphasize it.)*

And here is the one that will cost someone in this room a weekend.

`nn.TransformerEncoderLayer` gives you the whole block — **but not the positional encoding.**

You add that yourself. It's the `+ self.pe` on the forward pass. And if you forget it, PyTorch
does not complain. There's no error, no warning, no shape mismatch. The model trains perfectly
happily on an unordered bag of weeks and returns a forecast.

It's a **silent failure**, which by now you should recognize as the most dangerous kind. We'll
quantify it in two slides.

**[pause]**

Add it to the catalogue we've been building all semester. `KFold` on a time series. Scaling
outside the fold. A rolling feature you forgot to shift. `shuffle=True` on a DataLoader whose rows
are ordered in time. And now a Transformer with no positional encoding.

Not one of those raises an exception. Every one of them returns a plausible number. The only
defense is procedural — you check them because they're on a list, not because something broke.

*(Point at the muted note.)*

One aside: for multi-step forecasting you also need a causal mask, so position t can't attend to
positions after it. We're doing one-step-ahead, so we don't need it here — but if you extend this
in your project, that's the thing to look up.

---

# ▶ SLIDE 15 — Does It Work?

*(Walk the table. Same panel, same test block as everything since Homework 3.)*

LASSO with forty-six engineered features: seven forty-four. XGBoost: seven eighty-one. Vanilla
RNN: eight forty-two, on four and a half thousand parameters. Random forest: eight ninety-nine.
LSTM: nine eighty-seven. **Transformer encoder, two layers: nine ninety** — on sixty-seven
thousand parameters. Best CNN: one thousand thirty-two. Seasonal naive: twenty-one fifty-two.

**[pause]**

So: the Transformer beats the CNN, and it **ties the LSTM** — nine ninety against nine
eighty-seven, a difference far smaller than the run-to-run spread. Calling that a win in either
direction would be reading noise.

And it loses to a vanilla RNN holding **one-fifteenth** as many parameters. And to a
forty-six-coefficient linear model.

*(Beat.)*

That is the state-of-the-art architecture of the last decade, finishing sixth of eight on our
data. Next slide is why, and the reason is not that we implemented it badly.

**[pause]**

Look at the parameter column once before we move on, because the trend across the whole table is
the real story of these three lectures.

Four and a half thousand parameters bought eight forty-two. Eighteen thousand bought nine
eighty-seven. Sixty-seven thousand bought nine ninety. And forty-six coefficients bought seven
forty-four.

Model size and accuracy are running in **opposite directions** on this dataset. That is not a
universal law — on a large enough corpus the ordering flips entirely, which is precisely why these
architectures exist. But on the data in front of you, more capacity has bought worse forecasts
every single time.

---

# ▶ SLIDE 16 — Reading That Result Honestly

Go back to slide twelve — the three advantages — and take them one at a time against this problem.

*(Walk the table.)*

**Parallel computation.** Completely real. And completely irrelevant here: the RNN trains in
seconds either way. Parallelism matters when training time is your binding constraint. Ours is
about ninety seconds.

**Direct long-range paths.** Real, and worth very little when the signal is dominated by the
recent past. Attention's superpower is reaching week t minus fifty-two cheaply. Our data mostly
wants week t minus one.

**Scales with data.** True, and five thousand nine hundred forty training windows is simply not
the regime where that pays. Transformers overtake other architectures somewhere, but that
somewhere is orders of magnitude from here.

**[pause]**

*(Now the ablation. This is the number they'll remember.)*

But I don't want you to leave thinking the mechanism did nothing, because one part of it is doing
very visible work — and we can measure it.

Take the same model and remove the positional encoding. Now it has to forecast from an unordered
bag of twenty-six weeks.

*(Point at the two-row table.)*

With positional encoding: nine ninety. Without: **one thousand two hundred eighty-two.**

That's a penalty of **two hundred ninety-two RMSE** — which drops it below even the 1D CNN.

**[pause]**

That gap is the price of permutation invariance, and it's the reason the sinusoids exist. It also
tells you the model genuinely is using temporal position when you give it to it.

And remember: forgetting that one line produces no error message. It produces a model that is
twenty-nine percent worse and looks completely normal.

---

# ▶ SLIDE 17 — Section divider: Key Takeaways

Six architectures, one series, and what the ranking actually taught us.

---

# ▶ SLIDE 18 — Sequence Architecture Comparison

*(Table, then the two paragraphs.)*

Four architectures on three axes. Long range: the CNN sees its receptive field only, the RNN about
ten to thirty steps, the LSTM hundreds, the Transformer unlimited — at quadratic cost. Parallel:
CNN yes, RNN no, LSTM no, Transformer yes. Data needed: modest, modest, more, and much more.

**[pause]**

Choose by the **structure of your problem**, not by the recency of the architecture.

Short window, signal in recent lags? A plain RNN — or honestly, a linear model with good features,
which is what won here. Long sequences, abundant data, dependencies at arbitrary distance? A
Transformer, and nothing else comes close.

*(Point at the last paragraph.)*

That second case is language. Which is exactly why this architecture reshaped that field, and why
it has been much slower to displace gradient boosting in tabular forecasting — where, notably, the
M5 competition itself was won by ensembles of the methods you learned in Lectures 5 and 6.

Not by a Transformer. By gradient boosting.

**[pause]**

*(A closing thought worth offering.)*

Let me anticipate a reasonable objection: if this architecture loses here, why spend an hour on it?

Two answers. The first is that you now have a *reason* — you can say, before fitting anything,
that a twenty-six-week window with recent-lag signal and six thousand training examples is not the
regime where attention pays. That prediction-in-advance is worth far more than the fitted number.

The second is that most of you will encounter this architecture outside forecasting, in tools you
use daily. Understanding that it is a soft lookup with learned weights, that it is
permutation-invariant unless told otherwise, and that its advantages are advantages at scale —
that understanding transfers well beyond this course.

---

# ▶ SLIDE 19 — Lecture 9 Part 2: Key Takeaways

One. Attention is a learned soft lookup: score every query against every key, softmax the scores,
average the values. Distance in the sequence costs nothing.

Two. The price is quadratic in sequence length — irrelevant at twenty-six steps, the central
constraint at ten thousand.

Three. Multi-head attention runs several notions of relevance in parallel, at roughly the cost of
one, by splitting the dimension rather than adding to it.

Four. An encoder block is attention plus residual plus LayerNorm plus a feed-forward sublayer.
Only attention is new — the residuals are ResNet, the sublayer is Lecture 7.

Five. Attention is **permutation-invariant**, so position has to be added explicitly. PyTorch does
not do it for you, and omitting it fails silently — two hundred ninety-two RMSE, no error message.

And six. On our panel the Transformer tied the LSTM, beat the CNN, and lost to a vanilla RNN with
one-fifteenth the parameters. Its advantages are advantages **at scale**, and this problem has
none of the scale.

**[pause]**

Next time we change the question entirely. For ten weeks every model has handed you one number per
period. Bayesian methods hand you a distribution — and that turns out to answer questions a point
forecast simply cannot.

---

# ▶ SLIDE 20 — References

*(Advance and close. No narration needed.)*
