"""Build a movie shortlist using the fitted rating baseline."""

from src.baseline import predict_rating


def recommend_movies(model, candidates, seen_by_you, seen_by_partner, k):
    """Return up to k eligible movie IDs, ordered by predicted rating.

    candidates is an iterable of unique string movie IDs. Both seen inputs
    are sets of movie IDs. Assume k is a nonnegative integer.

    Exclude any movie seen by either viewer. Score eligible movies with
    predict_rating, including its fallback for unknown movies. Sort by
    decreasing score, breaking ties alphabetically by movie ID.

    Return a list. Return all eligible films when fewer than k qualify,
    and an empty list when k is zero or no films qualify.
    """
#     shortlist = recommend_movies(
#     model,
#     candidates=["X", "Y", "Z"],
#     seen_by_you={"X"},
#     seen_by_partner=set(),
#     k=2,
# )
# return {
#         "movie_means": movie_means,
#         "overall_mean": total / tally,
#     }
    if k == 0:
        return []
    movies_to_consider = set(candidates) - seen_by_you - seen_by_partner

    res = []
    for movie in movies_to_consider:
        res.append((predict_rating(model, movie), movie))

    sorted_res = sorted(res, key= lambda item: (-item[0], item[1]))

    return [x[1] for x in sorted_res[0:k]]
