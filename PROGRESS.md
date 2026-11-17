# Progress

| Date | Step | Status | Evidence |
| --- | --- | --- | --- |
| 2026-11-16 | Chapter 1.1: observations, predictions, and a movie-mean baseline | Lesson introduced; discussion in progress | [Notes and synthetic worked example](chapters/01-foundations/01-observations-and-baselines.md) |
| 2026-11-16 | Chapter 1.1 — fitting, held-out evaluation, and missing movie history | Worked example covered | [Synthetic held-out calculation and fallback](chapters/01-foundations/01-observations-and-baselines.md#fitting-and-evaluation) |
| 2026-11-16 | Chapter 1.1 — movie-mean prediction functions | Implemented and tested | [Baseline](src/baseline.py), [five synthetic tests](tests/test_baseline.py) |

Fitting calculates a mean per movie and an overall mean across individual training ratings. Prediction returns the overall mean for an unseen movie. All five tests pass with `python3 -m unittest discover -s tests -v`.

**Next step.** Use the implemented predictor to score a held-out rating.
