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
Under normal circumstances, you should expect a reply from me within 24 hours.

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

### How the Two Editions Line Up
Chapters 1 through 13 carry the **same numbers and titles** in both editions, so for the first two-thirds of the course you can read either one and we will be on the same page.

Two differences matter:

- **Chapter 12 is numbered differently.** In FPP-Py, §12.4 is *Bootstrapping and bagging*. In FPP3, §12.4 is *Neural network models* and bootstrapping/bagging is §12.5. When I assign a section from Chapter 12, I give both numbers.
- **Chapters 14 and 15 exist only in the Python edition.** These are the two extra chapters, and they are exactly the ones covering the second half of our course: Ch. 14 *Neural networks* and Ch. 15 *Foundation forecasting models*. There is no R equivalent.

This is the practical reason for the Python recommendation. Through Lecture 6 the choice of language is yours. From **Lecture 7 onward the readings exist only in Python**, and so does all of our course code.

There is one gap FPP cannot fill: it contains no tree-based methods and no regularization. For Lectures 4 through 6 we use a second free textbook:

- *An Introduction to Statistical Learning with Applications in Python* (**ISLP**), free PDF at [https://www.statlearning.com/](https://www.statlearning.com/)

ISLP is by four of the same statisticians behind the standard graduate reference in this area, it is written at our level, and every chapter ends with a Python lab. Its Chapter 8 covers decision trees, bagging, random forests, and boosting together; its Chapter 6 covers regularization. That is Lectures 4 through 6 almost exactly.

Neither book covers Bayesian methods. For Lectures 10 through 12 we use a third free textbook:

- *Bayesian Modeling and Computation in Python* (**BMCP**), by Martin, Kumar and Lao, free online at [https://bayesiancomputationbook.com/](https://bayesiancomputationbook.com/)

BMCP is written by PyMC core developers, and every example is PyMC and ArviZ code — the exact libraries we use. It is the closest thing to a purpose-built text for our last three lectures: Chapter 1 covers priors and prior predictive checks, Chapter 2 covers the MCMC diagnostics you will be asked to report, §4.5–4.6 covers pooling and hierarchical models, and §6.4.3 is *Bayesian Structural Time Series* by name.

A note on level. BMCP is mathematically heavier than FPP in places, and **you are not responsible for the derivations**. Read the assigned sections for the ideas and the code, run the examples, and treat the rest as reference. The slides define what you are accountable for; BMCP shows you the same ideas in working PyMC.

Two further free resources, both referenced in our materials:

- **XGBoost, "Introduction to Boosted Trees"** — [https://xgboost.readthedocs.io/en/stable/tutorials/model.html](https://xgboost.readthedocs.io/en/stable/tutorials/model.html). Derives the regularized objective and the split-gain formula we cover in Lecture 5.
- **Molnar, *Interpretable Machine Learning*** — [https://christophm.github.io/interpretable-ml-book/](https://christophm.github.io/interpretable-ml-book/). Ch. 9 (decision trees), Ch. 19 (partial dependence), Ch. 23 (permutation feature importance). Useful for Lectures 3 through 5.

Per-week readings are in the **weekly schedule** at the end of this syllabus.

<!--
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
-->

## Software
All lecture code and all assignments use Python. You should have a working Python 3.10+ environment with the following packages before the first class:

```
jupyter, pandas, numpy, matplotlib, statsmodels, prophet, pygam,
scikit-learn, xgboost, torch, pymc, arviz
```

**`jupyter` is not optional.** Quarto runs your Python through a Jupyter kernel, so without it `quarto render` fails before executing a single cell — even though nothing in your code imports it.

**macOS users need one extra step for XGBoost:** `brew install libomp`, once, before Week 5. Without it `import xgboost` fails with an OpenMP error.

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

All homework is submitted through the course repository, and is due **before class begins** on the date shown in the weekly schedule.
A submission pushed after that time is late and will not be accepted.

<!--
### Homework
You must answer all homework questions.
At least one question will be checked for credit, except for homework assignments that are graded for completion.
If you really do not know how to proceed with a homework question, you should email me.
-->

There are 7 homework assignments worth **300 points in total**. They are not equally weighted —
points follow the scope of the assignment, and three of them are submitted in parts across
multiple weeks with each part carrying its own share.

| HW | Covers | Parts and points | Total |
|---|---|---|---|
| 1 | Lectures 1–2 | Pt 1 — 12 · Pt 2 — 23 | 35 |
| 2 | Lecture 3 | single submission | 30 |
| 3 | Lectures 4–5 | single submission | 35 |
| 4 | Lecture 6 | single submission | 35 |
| 5 | Lectures 7–9 | Pt 1 — 27 · Pt 2 — 29 · Pt 3 — 9 | 65 |
| 6 | Lectures 10–11 | Pt 1 — 28 · Pt 2 — 22 | 50 |
| 7 | Lecture 12 | single submission | 50 |
| | | | **300** |

Each part has its own Codex context prompt and its own prompt budget. Due dates are in the
**weekly schedule** at the end of this syllabus.

### How to Submit Homework

All homework is submitted through your own copy of the course environment repository
([DataHurdler/Forecasting-Env](https://github.com/DataHurdler/Forecasting-Env)). Submission is a
**git push** — there is no upload, and nothing is emailed.

For each assignment, your submission folder must contain **four** things:

| File | What it is |
|---|---|
| `HWxx.qmd` | The assignment document with your code and written answers filled in |
| `HWxx.html` | The rendered output. **It must render from a clean restart** — if it does not run, it is not a submission |
| `PROMPT_LOG.jsonl` | Every Codex interaction for that assignment, one JSON object per line |
| `INITIAL_PROMPT.md` | The context prompt you pasted at the start of the session |

Assignments that ask for a business recommendation also require a short **`REPORT.md`**.

**Naming and placement.** One folder per submission, named for the assignment exactly as it appears in the schedule — `hw01_part1`, `hw05_part2`, and so on. The validation script in the environment repository checks this for you before you push; run it.

**Commits.** Make one commit per Codex prompt, with the message
`hw05 prompt 3: fit the LSTM and report RMSE`. The commit history is part of the record: it shows where the work came from and in what order, and it is what makes the prompt budget meaningful rather than an honour system.

**Timing.** Due **before class begins** on the date in the weekly schedule. Push time is submission time — a push at 6:01pm on the due date is late. Exceptions need at least 24 hours' notice unless it is a genuine emergency.

**The single most common way to lose points** is submitting a `.qmd` that does not render. Restart your kernel and render the whole document before you push, every time.

### Final Project
The final project is completed in **groups of no more than 3 students** and is worth 100 points — a quarter of the course grade.
Groups are formed by Week 4 and submitted to me for approval.

**Dataset.** You have two options, and both are fully acceptable — neither is the "easy" route.

1. **Bring your own.** A real business dataset of your group's choosing.
2. **Use the dataset I supply.** I expect to provide a real, non-public sales dataset from a
   working website. If you take this option you skip the sourcing work, but you inherit its
   quirks — and cleaning a dataset nobody has tidied for you is itself part of the job.

I will confirm the supplied dataset's availability by **Week 4**, when groups are due. If you are
bringing your own, it must:

- Be a time series or convertible to one (daily, weekly or monthly observations)
- Have at least 100 time periods
- Support a clear, specific business forecasting question — "forecast weekly demand for SKU X to
  support inventory decisions," not "predict a number"

Bring your dataset choice to the proposal in Week 9. If sourcing your own stalls, switch to the
supplied dataset rather than losing weeks — tell me and it is not a penalty.

**Required content.** The final report must:
1. Fit at least **three forecasting methods**, drawn from at least **two** of the four parts of
   this course, plus a **benchmark**. The four parts are:

   | Part | Lectures | Examples |
   |---|---|---|
   | Classical time series | 1–3 | ETS, ARIMA, VAR, Prophet, pyGAM |
   | Trees and regularization | 4–6 | Random forest, XGBoost, LASSO, Elastic Net |
   | Deep learning | 7–9 | FFN, 1D CNN, RNN, LSTM, Transformer |
   | Bayesian | 10–12 | Structural time series, hierarchical, Bayesian regression |

   The **benchmark does not count** toward the three and is not optional. Use seasonal naive, or
   another one-line rule appropriate to your series, and report it alongside every model. A
   report without a benchmark cannot show that any of its work was worth doing.

   Three methods from one part — say XGBoost, random forest and LASSO — does **not** satisfy this.
   The point is to compare approaches that differ in kind, not in tuning.
2. Use **walk-forward cross-validation** for all model comparisons
3. Include a **business recommendation section** written for a non-technical decision-maker — actionable, jargon-free, and grounded in your results
4. Include a **methods reflection** explaining which model performed best and connecting that result to characteristics of your specific dataset

**Deliverables.**

| Deliverable | Due | Points |
|---|---|---|
| Group formation | Week 4 (Sep. 17) | 5 |
| Project proposal — 1–2 pages: dataset, business question, planned methods, preliminary EDA | Week 9 (Oct. 22) | 20 |
| In-class presentation | Week 17 (Dec. 17) | 25 |
| Final report | Dec. 18 | 50 |

**Final report format.** Submit as a rendered Quarto HTML file (`.qmd` + `.html`) through the course repository.
The report should include all code, outputs, and written analysis in a single self-contained document.
There is no page limit, but conciseness is valued: a well-organized 15–20 page report is better than a disorganized 40-page one.
The full grading rubric is **`ECON8310_Project_Rubric.md`**, distributed with the course materials. Read it before writing the proposal.

### Points and Letter Grades
| Component | Points | Share |
|---|---|---|
| Homework (7 assignments, 11 submissions) | 300 | 75% |
| Final project | 100 | 25% |
| **Total** | **400** | |

Your letter grade will be assigned as follows:
- A: 360 points or higher
- B: 320-359 points
- C: 280-319 points
- D: 240-279 points
- F: 239 points or less

## A Note on Difficulty and Pacing
This course covers a wide range of methods — from classical statistics to deep learning to Bayesian inference.
Some weeks will be more familiar to you than others depending on your background.
Work with each other so you can complement each other.

The methods build on each other. Falling behind in one week makes the next harder.
Use office hours early and often.

## Important Dates
See the [UNO Academic Calendar](https://www.unomaha.edu/registrar/academic-calendar.php) for all important dates.

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
- _When: The Scientific Secrets of Perfect Timing_ by Daniel Pink
- _Range: Why Generalists Triumph in a Specialized World_ by David Epstein

## Disclaimer
While this document is designed to be as accurate as possible, learning is a dynamic process and I reserve the right to change some details.
For example, if the class has trouble understanding a specific topic, I might take some extra time and go into more detail about it, which may result in cutting down time from other topics.
<!-- Send me a cat photo for four extra points. -->

## Weekly Schedule

Assignments are due **before class begins**. Readings are listed under each week.

**Week 1 · Aug 27** — Lecture 1: Introduction, Exponential Smoothing & Forecast Evaluation
*Reading:* FPP Ch. 1, Ch. 2, §5.1–5.10, Ch. 8

**Week 2 · Sep 3** — Lecture 2: ARIMA, VAR & Multivariate Models
*6:00–7:30pm:* **Industry panel and Q&A** with two business professionals, followed by time to mingle. Lecture 2 runs after the panel. **Lab 2 is self-paced this week** — it is on the course site and you work through it on your own time.
*Reading:* FPP Ch. 9, §10.1–10.3, §10.6, §12.3
*Due:* Homework 1 Part 1

**Week 3 · Sep 10** — Lecture 3: Generalized Additive Models
*Reading:* FPP §7.4, §7.7, §12.1–12.2
*Due:* Homework 1 Part 2

**Week 4 · Sep 17** — Lecture 4: Decision Trees
*Reading:* ISLP §8.1
*Due:* Homework 2 · **Final project groups due**

**Week 5 · Sep 24** — Lecture 5: Tree Ensembles — Random Forests & Boosted Trees
*Reading:* ISLP §8.2; XGBoost "Introduction to Boosted Trees"; FPP §12.4 Python ed. / §12.5 R ed. for the bagging intuition
**Online, asynchronous — no in-person meeting.** The lecture is posted as a recording and the lab is self-paced; both are on the course site, and office hours run as usual. Nothing is due this week, and Homework 3 is due the following week — so this is the week to work on it.

**Week 6 · Oct 1** — Lecture 6: Regularization & Model Selection
*Reading:* ISLP Ch. 6; FPP §7.5
*Due:* Homework 3 · *Also:* final project grading rubric (`ECON8310_Project_Rubric.md`) walked through in class

**Week 7 · Oct 8** — Lecture 7: Introduction to Neural Networks
*Reading:* FPP-Py §14.1–14.2, §14.4–14.5, §14.7
*Due:* Homework 4

**Week 8 · Oct 15** — Lecture 8: CNN Architectures
*Reading:* FPP-Py §14.3

**Week 9 · Oct 22** — Lecture 9 Part 1: RNNs and LSTMs
*Reading:* FPP-Py §14.3, §14.6
*Due:* Homework 5 Part 1 · **Final project proposal due**

**Week 10 · Oct 29** — Lecture 9 Part 2: Transformers
*Reading:* FPP-Py Ch. 15

**Week 11 · Nov 5** — Lecture 10: Bayesian Statistics I — Foundations
*Reading:* BMCP Ch. 1 (inference, priors, prior predictive checks) and Ch. 2 (MCMC diagnostics); FPP §5.5, §5.9 for framing
*Due:* Homework 5 Part 2

**Week 12 · Nov 12** — Lecture 11 Part 1: Bayesian Statistics II — Time Series
*Reading:* BMCP §6.2, §6.4 (time series as regression; state space and Bayesian structural time series)
*Due:* Homework 5 Part 3

**Week 13 · Nov 19** — Lecture 11 Part 2: Bayesian Statistics II — Hierarchical Models
*Reading:* BMCP §4.5–4.6 (pooling, multilevel and hierarchical models)
*Not this:* FPP Ch. 11 is also titled *hierarchical*, but it is about forecast **reconciliation** — making sub-series forecasts add up to their totals. This week is about partial pooling, where groups share information through a common prior. Different topic; read Ch. 11 on its own terms, not as preparation for this lecture.
*Due:* Homework 6 Part 1

**Week 14 · Nov 26** — **Thanksgiving break, no class**

**Week 15 · Dec 3** — Lecture 12: Bayesian Statistics III — Bayesian Linear Regression
*Reading:* BMCP §3.2–3.3 (linear and multiple regression, counterfactuals); FPP Ch. 7 as the frequentist benchmark
*Due:* Homework 6 Part 2

**Week 16 · Dec 10** — Lecture 13: Synthesis — What the Semester Measured
*Reading:* FPP Ch. 13
**No lab this week.** The session is the course synthesis followed by project work time — bring your project and your questions.
*Due:* Homework 7

**Final Exam Week · Dec 17** — **Final project presentations** (5:30-7:30pm)

**Dec 18** — **Final project report due**
Please try your best to submit early.
