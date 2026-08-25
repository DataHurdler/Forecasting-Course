ECON 8310 Business Forecasting
=========================================
### Fall 2026 (August 24 - December 18, 2026)

## Class Time, Location, and Flow
- Thursday, 6-8:40pm, Mammel 115
- A typical class is divided into three parts:
  - Review assignments or topics from the previous class
  - Learn theories of new techniques (lecture)
  - Try new techniques on computer (lab)

## Instructor Contact Information
- Zijun Luo, PhD
- Mammel Hall 228V
- [zluo@unomaha.edu](mailto:zluo@unomaha.edu)

## Office Hours
- Designated hours: Tuesday, 1-3pm
- Outside designated hours: Email me for appointments
- Zoom possible but not encouraged

For questions about homework, please post to the Canvas discussion board so that all students benefit from the answer.
For personal or grade-related matters, email me directly.

## Course Description
**From [Academic Catalog](https://catalog.unomaha.edu/undergraduate/coursesaz/econ/)**: The course will cover forecasting tools and applications applied to business settings. The first half of the course will cover traditional Econometric forecasting methods and the second half of the course will focus on predictive analytics models and machine learning. Time in the computer lab will be focused on teaching students how to implement the models discussed in lectures.

**From Claude**: This course develops practical forecasting skills for graduate students in business, economics, and data science. Students learn to apply a broad suite of methods — from classical time series models to machine learning and Bayesian inference — to real business forecasting problems. Emphasis is on implementation in Python, interpretation of model outputs for business decision-making, and critical comparison of methods across different forecasting contexts.

**A Word about AI**: This course is designed to fully integrate modern AI tools, in both teaching and learning. I use AI a lot. When I have used AI in this course, I would let you know I did. And you should do the same. If you have not given much thoughts about AI as a student and a business profession, I found the commencement speech given by Dr. Angela Duckworth inspiring. You can watch it [here](https://youtu.be/DeXBEDXJMaQ). A more formal delineation of this course's AI policy will be given later in this syllabus as well as in assignments throughout the semester as needed.

## Who Am I?
I began my academic career with full-time faculty positions at various universities, including UNO.
In the summer of 2022, I left academia and worked as a senior data scientist at an AdTech start-up named Zeenk, a statistical analyst at the Nebraska Department of Health and Human Services, and most recently, a quantitative analyst at Farm Credit Services of America.
I returned to the University of Nebraska at Omaha as an assistant professor of economics in Fall 2025.
You can learn more about my teaching, research, and hobbies on my personal website: [https://www.luozijun.com/](https://www.luozijun.com/).

## 20-Minute In-Person Meeting
1. Go to [this link](https://docs.google.com/spreadsheets/d/1hAtn20hMbHiHCeosNgofzSXGSkyp6vmOUbZsiGwit8I/edit?usp=sharing)
2. Pick a green slot that works for you and make it into a color other than red or green. This way, your classmates know someone has signed up for that spot
3. Add the time to your calendar
4. Email me after you have picked your spot and tell me what date and time you have picked
5. In your email, include a short introduction of yourself, your goal for this semester, or anything you would like to let me know ahead of our meeting
<!--
Each student is required to sign up for a 10-minute meeting with me in the first two weeks (August 24 to September 7) of the term.
Go to [this link](https://calendly.com/luozijun/fall-2026-10-minute-meeting) to select a time slot.
It is anonymous and only I will see your name and time chosen.
Please email me a one-paragraph biography before we meet.
-->

## Course Goals
(Course goals were written with help from Claude.)<br>
With your cooperation and dedication, by the end of the semester, you will be able to

1. Apply exponential smoothing, ARIMA, and VAR models to univariate and multivariate business time series, and evaluate their forecast accuracy using walk-forward cross-validation.
2. Build Generalized Additive Models (GAMs) and use Prophet to decompose trend, seasonality, and external regressors.
3. Engineer features from time series data and apply decision trees, random forests, and gradient boosting to tabular forecasting problems.
4. Design, train, and evaluate feedforward networks, CNNs, LSTMs, and Transformer encoders for sequence forecasting using PyTorch.
5. Apply Bayesian inference to specify priors, compute posteriors, and generate calibrated probabilistic forecasts using PyMC.
6. Communicate model results and business recommendations to both technical and non-technical audiences.

## Prerequisites
Graduate standing.
Familiarity with basic statistics (regression, hypothesis testing) and introductory programming is assumed.
No prior knowledge of machine learning or time series analysis is required.

## Textbook
The textbook I chose has both an R version and a Python version, although the Python version is newer and has two extra chapters. You are *highly encouraged* to use Python, but I understand that many basic forecasting tasks can be done in R, if that is the programming language you are already familiar with. When we get to the more advanced techniques, i.e., neural networks, Python is the only way to go. 
- *Forecasting: Principles and Practice, the Pythonic Way* (**FPP-Py**), available online at [https://otexts.com/fpppy/](https://otexts.com/fpppy/)
- *Forecasting: Principles and Practice (3rd ed)* (**FPP3**, the R edition), available online at [https://otexts.com/fpp3/](https://otexts.com/fpp3/)

There is one gap FPP cannot fill: it contains no tree-based methods and no regularization. For Lectures 4 through 6 we use a second free textbook:

- *An Introduction to Statistical Learning with Applications in Python* (**ISLP**), free PDF at [https://www.statlearning.com/](https://www.statlearning.com/)

ISLP is by four of the same statisticians behind the standard graduate reference in this area, it is written at exactly our level, and every chapter ends with a Python lab. Its Chapter 8 covers decision trees, bagging, random forests, and boosting together; its Chapter 6 covers regularization. That is Lectures 4 through 6 almost exactly.

Neither book covers Bayesian methods. For Lectures 10 through 12 we use a third free textbook:

- *Bayesian Modeling and Computation in Python* (**BMCP**), by Martin, Kumar and Lao, free online at [https://bayesiancomputationbook.com/](https://bayesiancomputationbook.com/)

BMCP is written by PyMC core developers, and every example is PyMC and ArviZ code — the exact libraries we use. It is the closest thing to a purpose-built text for our last three lectures: Chapter 1 covers priors and prior predictive checks, Chapter 2 covers the MCMC diagnostics you will be asked to report, §4.5–4.6 covers pooling and hierarchical models, and §6.4.3 is *Bayesian Structural Time Series* by name.

A note on level. BMCP is mathematically heavier than FPP in places, and **you are not responsible for the derivations**. Read the assigned sections for the ideas and the code, run the examples, and treat the rest as reference. The slides define what you are accountable for; BMCP shows you the same ideas in working PyMC.

### How the Two Editions Line Up
Chapters 1 through 13 carry the **same numbers and titles** in both editions, so for the first two-thirds of the course you can read either one and we will be on the same page.

Two differences matter:

- **Chapter 12 is numbered differently.** In FPP-Py, §12.4 is *Bootstrapping and bagging*. In FPP3, §12.4 is *Neural network models* and bootstrapping/bagging is §12.5. When I assign a section from Chapter 12, I give both numbers.
- **Chapters 14 and 15 exist only in the Python edition.** These are the two extra chapters, and they are exactly the ones covering the second half of our course: Ch. 14 *Neural networks* and Ch. 15 *Foundation forecasting models*. There is no R equivalent.

This is the practical reason for the Python recommendation. Through Lecture 6 the choice of language is yours. From **Lecture 7 onward the readings exist only in Python**, and so does all of our course code.

### Reading Map
| Lecture | Topic | FPP-Py (Python) | FPP3 (R) | Also |
|---|---|---|---|---|
| 1 | Intro, Exponential Smoothing & Evaluation | Ch. 1; Ch. 2; §5.1–5.10; Ch. 8 | Same | |
| 2 | ARIMA, VAR & Multivariate | Ch. 9; §10.1–10.3, §10.6; §12.3 | Same | |
| 3 | Generalized Additive Models | §7.4, §7.7; §12.1–12.2 | Same | |
| 4 | Decision Trees | — | — | **ISLP §8.1** |
| 5 | Tree Ensembles: Random Forests & Boosted Trees | §12.4 (bagging idea only) | §12.5 (bagging idea only) | **ISLP §8.2**; XGBoost tutorial |
| 6 | Regularization & Model Selection | §7.5 | Same | **ISLP Ch. 6** |
| 7 | Introduction to Neural Networks | §14.1–14.2, §14.4–14.5, §14.7 | *Not covered* | |
| 8 | CNN Architectures | §14.3 | *Not covered* | |
| 9 (Pt 1) | RNNs & LSTMs | §14.3, §14.6 | *Not covered* | |
| 9 (Pt 2) | Attention & Transformers | Ch. 15 | *Not covered* | |
| 10 | Bayesian Statistics I | §5.5, §5.9 (framing only) | Same | **BMCP Ch. 1; Ch. 2** |
| 11 | Bayesian Statistics II | — | — | **BMCP §6.2, §6.4; §4.5–4.6** |
| 12 | Bayesian Statistics III | Ch. 7 (review) | Same | **BMCP §3.2–3.3** |

Two further free resources, both linked from Canvas:

- **XGBoost, "Introduction to Boosted Trees"** — [https://xgboost.readthedocs.io/en/stable/tutorials/model.html](https://xgboost.readthedocs.io/en/stable/tutorials/model.html). Derives the regularized objective and the split-gain formula we cover in Lecture 5.
- **Molnar, *Interpretable Machine Learning*** — [https://christophm.github.io/interpretable-ml-book/](https://christophm.github.io/interpretable-ml-book/). Ch. 9 (decision trees), Ch. 19 (partial dependence), Ch. 23 (permutation feature importance). Useful for Lectures 3 through 5.

### What the Textbook Does *Not* Cover
The textbook is our anchor, not our boundary. Several topics we cover have no FPP chapter, and for those the lecture slides are your primary source:

- **Everything tree-based (Lectures 4–5).** FPP covers **no** tree methods — not decision trees, not random forests, not gradient boosting or XGBoost. This is what ISLP Ch. 8 is for.

    FPP §12.4 (§12.5 in the R edition) is still worth reading for Lecture 5. It covers *bagging* — averaging forecasts across bootstrapped versions of a series — which is the ensembling idea random forests rest on. It is the idea only: FPP bags ETS models fitted to resampled series, not trees, and there is no feature subsampling. Read it for the intuition about why averaging many noisy models helps.

- **Regularization (Lecture 6).** FPP has no Ridge, LASSO, or Elastic Net; ISLP Ch. 6 covers all three. FPP §7.5 *Selecting predictors* is genuinely useful here, because Lecture 6 opens with exactly that material — adjusted R², AIC, AICc, BIC, and best-subset or stepwise search — before showing why shrinkage replaces it. Read §7.5 as the classical answer we are about to improve on.
- **All Bayesian methods (Lectures 10–12).** FPP is written from a frequentist perspective throughout. Its sections on distributional forecasts and prediction intervals (§5.5, §5.9) are useful framing for why we want full predictive distributions, but the book does no Bayesian inference. **BMCP is the text for these three weeks**, and unlike Lectures 4–6 it is not a supplement — it is the primary reading.

    One topic stays slide-only: the **DAGs** in Lecture 12. BMCP does not cover causal graphs. If you want to go further, Richard McElreath's *Statistical Rethinking* lecture series is free on YouTube and is the standard treatment.
- **The Diebold-Mariano test (Lecture 1) and Granger causality (Lecture 2).**
- **The internals of neural architectures (Lectures 7–9).** FPP-Py Ch. 14 is written at the level of *which model to use and how to call it* through the `neuralforecast` library. We go a layer deeper — backpropagation, convolution arithmetic, LSTM gates, scaled dot-product attention — and write our models directly in PyTorch.

**A warning about the word "hierarchical."** FPP Chapter 11 is titled *Forecasting hierarchical and grouped time series*, and Lecture 11 is *Bayesian Statistics II — Time Series & Hierarchical Models*. **These are different things.** FPP Ch. 11 is about forecast reconciliation: making forecasts of sub-series add up to forecasts of their totals. Our Lecture 11 is about partial pooling, where groups share information through a common prior. Chapter 11 is genuinely worth reading, but do not read it expecting Lecture 11.

## Software
All lecture code and all assignments use Python. You should have a working Python 3.10+ environment with the following packages before the first class:

```
pandas, numpy, matplotlib, statsmodels, prophet, pygam,
scikit-learn, xgboost, torch, pymc, arviz
```

Installation instructions and a test script are provided in the course repository.

## Course Materials
All lecture slides (PDF and interactive HTML), homework assignments, and data files are distributed through the course website and Canvas.

The course runs on one main dataset, with three others introduced where that one cannot demonstrate something. **`ECON8310_Datasets.md`** explains what each dataset is, where to download it, and why it is in the course. Read it before Homework 1.
The textbooks above are free online.
There is nothing you need to buy for this course.

## How to Be Successful in this Course
- Read this syllabus
- Study all course materials
- Come to classes
- Complete all the assignments
- Ask questions <!-- - Email me a link to a drone video for three extra points -->
- *DON'T* wait until the last minute to complete homework assignments

## Academic Integrity and Behavior
All students are required to adhere to the highest standards of academic integrity and behavior and must satisfy the [**UNO Academic Integrity Policy**](http://www.unomaha.edu/student-life/student-conduct-and-community-standards/policies/academic-integrity.php) and [**Student Code of Conduct**](http://www.unomaha.edu/student-life/student-conduct-and-community-standards/policies/code-of-conduct.php).
It is the student's responsibility to read, understand and abide by these policies.

Beyond the AI tools described in the next section:
- Do not share code or written responses with other students.
- Do not submit another student's work as your own.
- Citations are required for any external sources used in written sections.

## AI Use Policy
This is the fuller delineation promised above.

This course explicitly permits and encourages the use of AI coding assistants (such as Codex, GitHub Copilot, Claude, or ChatGPT) for homework assignments.
The course infrastructure is built around this: each assignment includes a required initial prompt and a **prompt budget** — a maximum number of AI interactions for that assignment.

**You are responsible for your results.** AI tools help write code; you are responsible for understanding and explaining the output. Grading emphasizes:

- Correct interpretation of model results in business language
- Reasoned justification of methodological choices
- Diagnosing unexpected or poor results rather than accepting them uncritically
- Written reflection questions that require genuine understanding

**Prompt logging is required.** You must maintain a `PROMPT_LOG.jsonl` file recording every AI interaction for each assignment.
Submissions without a complete prompt log will receive a grade deduction.

**Written responses must be your own.** Analytical interpretation and business recommendation sections must be written by you, not generated by AI.
Using AI to write your interpretations defeats the purpose of the assignment and violates the spirit (though not the letter) of this policy.

## Course Evaluation
A tentative weekly course schedule is at the end of this syllabus.

Exceptions for any assignment should be communicated at least 24 hours ahead of the due time, unless it is an emergency situation.
No late homework is otherwise accepted.

All homework is submitted through the course repository, and is due **before class begins**
on the date shown in the weekly schedule. A submission pushed after that time is late and will
not be accepted.

### Homework
You must answer all homework questions.
At least one question will be checked for credit, except for homework assignments that are graded for completion.
If you really do not know how to proceed with a homework question, you should email me.

There are 7 homework assignments, each worth 20 points, for a total of 140 points.
Several assignments are submitted in parts across multiple weeks. **The parts of an assignment
split that assignment's 20 points between them** — they are not 20 points each. Each part has its
own Codex context prompt and its own prompt budget. See the weekly schedule below for due dates.
Each assignment is a Quarto (`.qmd`) document rendered to HTML and submitted through the course repository, together with your `PROMPT_LOG.jsonl` and a short `REPORT.md` containing your business recommendation.

| Assignment | Topics | Lectures | Due |
|---|---|---|---|
| 1 (Part 1) | Exponential smoothing | 1 | Week 2 |
| 1 (Part 2) | ARIMA, VAR, method comparison | 2 | Week 3 |
| 2 | Generalized Additive Models, Prophet | 3 | Week 4 |
| 3 | Decision trees, random forests | 4–5 | Week 6 |
| 4 | Boosted trees, regularization | 6 | Week 7 |
| 5 | Neural networks, CNNs, RNNs/Transformers | 7–9 | Part 1: Week 9 · Part 2: Week 11 · Part 3: Week 12 |
| 6 | Bayesian foundations, Bayesian time series | 10–11 | Part 1: Week 13 · Part 2: Week 15 |
| 7 | Bayesian linear regression | 12 | Week 16 |

### Pop Quizzes
Throughout the semester, there are 3 pop quizzes, each is worth 20 points, for a total of 60 points.

### Final Project
The final project is completed in **groups of 2–3 students** and is worth 200 points.
Groups are formed by Week 4 and submitted to me for approval.

**Dataset requirements.** Each group selects a real business dataset of its choosing. The dataset must:
- Be a time series or convertible to one (e.g., daily, weekly, or monthly observations)
- Have at least 100 time periods
- Have a clear, specific business forecasting question (e.g., "forecast weekly demand for SKU X to support inventory decisions" — not just "predict a number")

**Required content.** The final report must:
1. Fit at least **3 methods drawn from at least 2 different parts of the course** (e.g., one classical time series method, one tree-based method, and one neural network or Bayesian model)
2. Use **walk-forward cross-validation** for all model comparisons
3. Include a **business recommendation section** written for a non-technical decision-maker — actionable, jargon-free, and grounded in your results
4. Include a **methods reflection** explaining which model performed best and connecting that result to characteristics of your specific dataset

**Deliverables.**

| Deliverable | Due | Points |
|---|---|---|
| Group formation | Week 4 (Sep. 17) | 10 |
| Project proposal — 1–2 pages: dataset, business question, planned methods, preliminary EDA | Week 9 (Oct. 22) | 40 |
| In-class presentation | Week 17 (Dec. 17) | 30 |
| Final report | Dec. 18 | 120 |

**Final report format.** Submit as a rendered Quarto HTML file (`.qmd` + `.html`) through the course repository.
The report should include all code, outputs, and written analysis in a single self-contained document.
There is no page limit, but conciseness is valued: a well-organized 15–20 page report is better than a disorganized 40-page one.
The grading rubric will be distributed by Week 6.

### Points and Letter Grades
| Component | Points |
|---|---|
| Homework (7 × 20) | 140 |
| Pop quizzes (3 × 20) | 60 |
| Final project | 200 |
| **Total** | **400** |

Students with full attendance will be awareded 10 extra points. There are time-sensitive extra point opportunities throughout the semester. Please pay attention to annoucements in-class or on Canvas.

Your letter grade will be assigned as follows:
- A+: 392 points or higher
- A: 364-391 points
- B+: 352-363 points
- B: 324-351 points
- C+: 312-323 points
- C: 284-311 points
- D: 244-283 points
- F: 243 points or less

## A Note on Difficulty and Pacing
This course covers a wide range of methods — from classical statistics to deep learning to Bayesian inference.
Some weeks will be more familiar to you than others depending on your background.
Students with a data science background may find Lectures 1–2 straightforward and Lectures 10–12 more challenging.
Economics students may find the reverse.
MBA students will find Lectures 1–3 most accessible and should expect to invest extra time in Lectures 7–12.

The methods build on each other. Falling behind in one week makes the next harder.
Use office hours early and often.

## Important Dates
See the [UNO Academic Calendar](https://www.unomaha.edu/registrar/academic-calendar.php) for all important dates.

Dates that affect this course specifically:

- **Sep. 24, 2026** — no in-person meeting; Week 5 is delivered online (see the schedule below)
- **Nov. 26, 2026** — Thanksgiving break, no class
- **Dec. 17, 2026** — final project presentations, 5:30–7:30pm
- **Dec. 18, 2026** — final project report due

Withdrawal deadlines and university closures are on the academic calendar linked above.

<!--
## CBA Business Core Three-Attempt Rule
Effective Fall 2002, a student may only attempt each required business core course three times. This course is in the business core.
Any grade earned, excluding CR, W, NC, NR, I, IP, AU, S, U or R will count as an attempt for the three times limit.
The Undergraduate Program Council will only consider appeals of the three-attempt rule when the circumstances for the appeal are documented and the reason for the appeal is extraordinary.
-->

## Accessibility Services Center Statement
Reasonable accommodations are provided for students who are registered with Accessibility Services Center (ASC) and make their requests sufficiently in advance.
For more information, please contact ASC (Location: HK 104, Phone: 402.554.2872, Email: [unoaccessibility@unomaha.edu](mailto:unoaccessibility@unomaha.edu))

## Book Nook
I love to read. Here are two books I have enjoyed reading:
- _Beginners_ by Tom Vanderbilt
- _Range_ by David Epstein

## Disclaimer
While this document is designed to be as accurate as possible, learning is a dynamic process and I reserve the right to change some details.
For example, if the class has trouble understanding a specific topic, I might take some extra time and go into more detail about it, which may result in cutting down time from other topics.
<!-- Send me a cat photo for four extra points. -->

## Tentative Weekly Course Schedule

### Week 1 (Aug. 27, 2026)
- Lecture 1: Introduction, Exponential Smoothing & Forecast Evaluation
- Reading: FPP Ch. 1, Ch. 2, §5.1–5.10, Ch. 8

### Week 2 (Sep. 3, 2026)
- Assignment 1 (Part 1) due before class
- Roundtable with business professionals (6-7pm)
- Lecture 2: ARIMA, VAR & Multivariate Models
- Reading: FPP Ch. 9, §10.1–10.3, §10.6, §12.3

### Week 3 (Sep. 10, 2026)
- Assignment 1 (Part 2) due before class
- Lecture 3: Generalized Additive Models
- Reading: FPP §7.4, §7.7, §12.1–12.2

### Week 4 (Sep. 17, 2026)
- Assignment 2 due before class
- **Final project groups due**
- Lecture 4: Decision Trees
- Reading: ISLP §8.1

### Week 5 (Sep. 24, 2026) — **online, asynchronous**
- **No in-person meeting.** The lecture is posted as a recording and the lab is self-paced; both
  are on the course site. Office hours run as usual.
- Nothing is due this week, and Assignment 3 is due the following week — so this is the week to
  work on it.
- Lecture 5: Tree Ensembles — Random Forests & Boosted Trees
- Reading: ISLP §8.2; XGBoost "Introduction to Boosted Trees"; FPP §12.4 Python ed. / §12.5 R ed. for the bagging intuition

### Week 6 (Oct. 1, 2026)
- Assignment 3 due before class
- Final project grading rubric distributed
- Lecture 6: Regularization & Model Selection
- Reading: ISLP Ch. 6; FPP §7.5

### Week 7 (Oct. 8, 2026)
- Assignment 4 due before class
- Lecture 7: Introduction to Neural Networks
- Reading: FPP-Py §14.1–14.2, §14.4–14.5, §14.7 (**Python edition only**)

### Week 8 (Oct. 15, 2026)
- Lecture 8: CNN Architectures
- Reading: FPP-Py §14.3 (**Python edition only**)

### Week 9 (Oct. 22, 2026)
- Assignment 5 (Part 1) due before class
- **Final project proposal due**
- Lecture 9 (Part 1): RNNs and LSTMs
- Reading: FPP-Py §14.3, §14.6 (**Python edition only**)

### Week 10 (Oct. 29, 2026)
- Lecture 9 (Part 2): Transformers
- Reading: FPP-Py Ch. 15 (**Python edition only**)

### Week 11 (Nov. 5, 2026)
- Assignment 5 (Part 2) due before class
- Lecture 10: Bayesian Statistics I — Foundations
- Reading: **BMCP Ch. 1** (Bayesian inference, priors, prior predictive checks) and **Ch. 2** (MCMC diagnostics). FPP §5.5, §5.9 for framing.

### Week 12 (Nov. 12, 2026)
- Assignment 5 (Part 3) due before class
- Lecture 11: Bayesian Statistics II — Time Series & Hierarchical Models
- Reading: **BMCP §6.2 and §6.4** (time series as regression; state space and Bayesian structural time series)

### Week 13 (Nov. 19, 2026)
- Assignment 6 (Part 1) due before class
- Lecture 11 (cont.): Bayesian Statistics II — Time Series & Hierarchical Models
- Reading: **BMCP §4.5–4.6** (pooling, multilevel and hierarchical models)

### Week 14 (Nov. 26, 2026)
Thanksgiving break. No class.

### Week 15 (Dec. 3, 2026)
- Assignment 6 (Part 2) due before class
- Lecture 12: Bayesian Statistics III — Bayesian Linear Regression
- Reading: **BMCP §3.2–3.3** (linear and multiple regression, counterfactuals). FPP Ch. 7 as the frequentist benchmark.

### Week 16 (Dec. 10, 2026)
- Assignment 7 due before class
- Final thoughts on forecasting, econometrics, and ML/AI
- Final project work session / consultations
- Reading: FPP Ch. 13

### Week 17 (Dec. 17, 2026)
- **Final project presentations, 5:30-7:30pm**

### Dec. 18, 2026
- **Final project report due**
