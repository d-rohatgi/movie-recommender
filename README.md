# Movie Recommender

Building a movie recommender for two viewers while learning the mathematics, modeling, and engineering behind recommendation systems.

This is an incremental learning project. Commits document material covered, implementations, experiments, and corrections as the work happens. Notes distinguish examples and hypotheses from measured results.

**Current progress.** Chapter 1 includes a working movie-mean baseline for rating predictions and ordered shortlists. It filters films seen by either viewer and uses a fallback for movies without training ratings. Thirteen tests cover the baseline using synthetic data. Lesson 1.3 introduces mean absolute error for comparing predictors. The recommendation application is pending.

- [Progress log](PROGRESS.md)
- [Chapter 1.1: Observations and baselines](chapters/01-foundations/01-observations-and-baselines.md)
- [Chapter 1.2 — From scores to a shortlist](chapters/01-foundations/02-ranking-and-candidates.md)
- [Chapter 1.3 — Comparing baseline prediction errors](chapters/01-foundations/03-comparing-baseline-errors.md)

The intended result is an application with separate taste profiles, a shared ranked shortlist, and feedback from both viewers. Models will be compared against explicit baselines using held-out data. The choice of final model will depend on the evidence.

The public history grows with the project. There are no completed future chapters or prebuilt application hidden behind the current milestone.
