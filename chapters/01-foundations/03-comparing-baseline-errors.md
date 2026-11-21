# Chapter 1.3 — Comparing baseline prediction errors

The opening segment is introduced. The evaluation helper is pending.

**Prerequisites and objective.** Use averages, absolute error, and the boundary between training and held-out ratings. Compare two fitted prediction methods by averaging their absolute errors on the same held-out observations. This supplies a way to compare changes to the project's rating predictor.

Mean absolute error, abbreviated MAE, is the average distance between predicted and observed ratings. Its units are rating points. Smaller MAE means smaller average absolute error on the evaluated observations.

### Two baselines fitted on training ratings

All data in this example are synthetic. Ratings use the same 1–5 scale. The tables specify the records used in this calculation.

| Movie | Training ratings | Movie mean |
| --- | --- | ---: |
| X | 5, 3 | 4 |
| Y | 1, 3 | 2 |

The movie-mean baseline predicts 4 for X and 2 for Y. Its fitted values are the per-movie means. The overall-mean baseline predicts `(5 + 3 + 1 + 3) / 4 = 3` for every movie. Its fitted value is a single mean across the individual training ratings.

Fit both methods using only the training rows. Then freeze their fitted values and evaluate them on the same held-out rows.

### A worked held-out comparison

Suppose two later viewers supply these ratings.

| Movie | Observed rating | Movie-mean prediction | Absolute error | Overall-mean prediction | Absolute error |
| --- | ---: | ---: | ---: | ---: | ---: |
| X | 5 | 4 | 1 | 3 | 2 |
| Y | 2 | 2 | 0 | 3 | 1 |

The movie-mean method's MAE is `(1 + 0) / 2 = 0.5` rating points. The overall-mean method's MAE is `(2 + 1) / 2 = 1.5` rating points. This is a comparison on these two synthetic held-out observations.

### Mathematical notation

For one or more held-out ratings, write the calculation as

$$
\operatorname{MAE} = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|
$$

- $n$ is the number of held-out rating observations.
- $i$ identifies one observation, from 1 through $n$.
- $y_i$ is that observation's actual rating, the label.
- $\hat{y}_i$, pronounced "y-hat sub i", is the model's predicted rating for that same observation.

The vertical bars mean absolute value. The summation symbol means add the error for each row, starting at row 1 and ending at row `n`. Dividing by `n` gives the average. The worked example has `n = 2`.

The inputs identifying a prediction include its movie ID. The fitted means come from training. The held-out label enters the error calculation after the prediction is fixed.

**Project connection.** MAE will help compare rating predictors under a shared evaluation protocol. It measures errors in individual ratings. Shortlist quality and both viewers' experiences will receive their own evaluations as the project develops.
