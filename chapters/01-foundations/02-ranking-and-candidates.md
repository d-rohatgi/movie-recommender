# Chapter 1.2 — From scores to a shortlist

The lesson is introduced. Ranking implementation is pending.

**Prerequisites and objective.** Use the fitted movie-mean predictor to order eligible movies into a shortlist. This adds a selection step to the rating predictor from Lesson 1.1.

A **candidate set** contains the movie IDs under consideration. An **eligibility rule** determines which candidates can appear in the result. For this exercise, require that neither viewer has seen a recommended movie.

Use each eligible movie's predicted rating as its score. Sort by decreasing score, then return up to `k` films, where `k` is the requested number of results. If scores tie, order the movie IDs alphabetically so repeated calls with the same inputs give the same order.

**Worked example with synthetic data.** The earlier fitted baseline has means X = 4 and Y = 1, and an overall mean of 3. Candidate Z has no training ratings, so the predictor assigns it the fallback score of 3.

| Movie ID | Predicted score | Already seen by |
| --- | ---: | --- |
| X | 4.0 | One viewer |
| Y | 1.0 | Neither viewer |
| Z | 3.0 | Neither viewer |

For a two-film request, filter X out, score the eligible candidates, and order them as Z then Y. If fewer than `k` candidates qualify, return the available eligible films. If none qualify, the shortlist is empty.

**Project connection.** This turns the existing baseline's scores into a reproducible list that follows the exercise's eligibility rule. The movie-mean scores are shared across viewers. Personal preferences will enter later models.

**Implementation exercise.** Define `recommend_movies(model, candidates, seen_by_you, seen_by_partner, k)` to return an ordered list of movie IDs. The model is the fitted baseline. Candidate IDs are unique strings, both seen inputs are sets of movie IDs, and `k` is a nonnegative integer. Reuse `predict_rating` to score candidates, including its fallback for unknown films. Return up to `k` eligible IDs under the ordering rules above. The ranking implementation is pending.
