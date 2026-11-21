# Progress

| Date | Step | Status | Evidence |
| --- | --- | --- | --- |
| 2026-11-16 | Chapter 1.1: observations, predictions, and a movie-mean baseline | Lesson introduced; discussion in progress | [Notes and synthetic worked example](chapters/01-foundations/01-observations-and-baselines.md) |
| 2026-11-16 | Chapter 1.1 — fitting, held-out evaluation, and missing movie history | Worked example covered | [Synthetic held-out calculation and fallback](chapters/01-foundations/01-observations-and-baselines.md#fitting-and-evaluation) |
| 2026-11-16 | Chapter 1.1 — movie-mean prediction functions | Implemented and tested | [Baseline](src/baseline.py), [five synthetic tests](tests/test_baseline.py) |
| 2026-11-20 | Chapter 1.1 — evaluate an implemented prediction | Synthetic example executed | [Verified prediction of 4.0 and absolute error of 2.0](chapters/01-foundations/01-observations-and-baselines.md#evaluating-the-implemented-baseline) |
| 2026-11-20 | Chapter 1.2 — candidates, eligibility, and ranking | Lesson introduced | [Shortlist rules and a synthetic worked example](chapters/01-foundations/02-ranking-and-candidates.md) |

Fitting stores `movie_means` and `overall_mean` as separate fields. `movie_means` maps movie IDs to their means. Prediction uses `overall_mean`, calculated across individual training ratings, for an unseen movie. All five tests pass with `python3 -m unittest discover -s tests -v`.

**Next step.** Implement ranking under the [shortlist contract](chapters/01-foundations/02-ranking-and-candidates.md).
