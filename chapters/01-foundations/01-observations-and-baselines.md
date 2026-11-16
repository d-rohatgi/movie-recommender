# Chapter 1.1 — Observations, predictions, and baselines

Status: lesson introduced; discussion in progress. These notes record the opening lesson and its example, not a completed implementation or assessment.

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

**Project connection.** This defines the intended behavior and limitations of the first baseline. Implementation and comparative evaluation are future work.
