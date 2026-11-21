# Movie Recommender

Building a movie recommender for two viewers while learning the mathematics, modeling, and engineering behind recommendation systems.

This is an incremental learning project. Commits document material covered, implementations, experiments, and corrections as the work happens. Notes distinguish examples and hypotheses from measured results.

**Current progress.** Chapter 1 includes a working movie-mean rating predictor with a fallback for movies without training ratings. Five tests cover the predictor using synthetic ratings. Lesson 1.2 introduces filtering and ranking for a shortlist. The recommendation application is pending.

- [Progress log](PROGRESS.md)
- [Chapter 1.1: Observations and baselines](chapters/01-foundations/01-observations-and-baselines.md)
- [Chapter 1.2 — From scores to a shortlist](chapters/01-foundations/02-ranking-and-candidates.md)

The intended result is an application with separate taste profiles, a shared ranked shortlist, and feedback from both viewers. Models will be compared against explicit baselines using held-out data. The choice of final model will depend on the evidence.

The public history grows with the project. There are no completed future chapters or prebuilt application hidden behind the current milestone.
