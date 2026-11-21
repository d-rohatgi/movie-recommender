# Chapter 1.1 — Observations, predictions, and baselines

The lesson is in progress. These notes include a movie-mean baseline and a synthetic held-out calculation.

**The prediction task.** Start with historical records containing:

```text
(viewer_id, movie_id, rating)
```

An observation is a recorded measurement. Here, the rating is a response supplied by a viewer after watching a movie. It is a practical proxy for enjoyment, not an objective property of the movie.

The target is the quantity to predict: the rating a particular viewer would give a particular movie. Until that rating is observed, the model's output is an estimate. A predicted rating is not automatically a probability of enjoyment.

**A first baseline.** A baseline is a simple reference method against which later models can be compared. The movie-mean baseline estimates a movie's rating for any new viewer using the average of its ratings in the training data. Training data is the historical evidence allowed when constructing the predictions; later evaluation requires separate evidence.

**Synthetic example.** The following invented ratings illustrate the calculation; they are not real viewer data.

| Movie | Past viewer A | Past viewer B | Mean rating |
| --- | ---: | ---: | ---: |
| Film X | 5 | 1 | 3 |
| Film Y | 3 | 3 | 3 |

For Film X, `(5 + 1) / 2 = 3`. For Film Y, `(3 + 3) / 2 = 3`.

The baseline predicts 3 for both films, regardless of who asks. It uses historical ratings but does not use the new viewer's preferences. Averaging compresses different patterns of responses into the same score. Two ratings per movie are enough to illustrate that compression, but not enough to make confident claims about future viewers.

**What makes a prediction personalized?** A function can accept `viewer_id` while ignoring it internally. Personalization requires the prediction to depend on information about that viewer. Merely adding an argument to an interface does not accomplish this.

**Discussion question.** What information beyond these means would help recommend a film to two new viewers, and why? Distinguish what the table tells us about the past viewers from what is still unknown about the new pair.

### Fitting and evaluation

Use the four ratings above as training data. Suppose a third viewer later gives Film X a 4. Set that row aside as a held-out observation.

1. **Fit.** Compute and store the movie means using the training rows. For Film X the fitted value is `(5 + 1) / 2 = 3`.
2. **Predict.** Use Film X's stored value of 3 as the estimate for the third viewer.
3. **Evaluate.** Compare the estimate with the held-out rating of 4. The absolute error is `abs(4 - 3) = 1` rating point.

Including the 4 when fitting Film X's mean would allow the answer to influence its own prediction. That is data leakage. Keep held-out ratings separate until scoring the fixed predictions.

### A movie with no training ratings

If Film Z has no training ratings, its movie mean is undefined. One fallback is the mean of **all individual training ratings** across movies. Here it is `(5 + 1 + 3 + 3) / 4 = 3`. This is a general estimate for Film Z. A later rating for Film Z can evaluate the fallback under the same holdout rule.

**Project connection.** The example specifies which rows the baseline can use and what it can return for a movie with no training ratings. The implementation and its tests use these rules.

### Evaluating the implemented baseline

This executable example uses a fresh set of synthetic ratings.

```python
from src.baseline import fit_movie_mean, predict_rating

training_rows = [("a", "X", 5), ("b", "X", 3), ("a", "Y", 1)]
held_out = ("c", "X", 2)

model = fit_movie_mean(training_rows)
prediction = predict_rating(model, held_out[1])
absolute_error = abs(prediction - held_out[2])

print(prediction, absolute_error)
```

The verified output is `4.0 2.0`. The training ratings for X give a prediction of `(5 + 3) / 2 = 4`. The held-out rating of 2 enters when computing the absolute error. This single example checks the calculation. Measuring performance across more held-out observations is a later step.
