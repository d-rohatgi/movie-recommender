import unittest

from src.baseline import fit_movie_mean
from src import ranking


class RecommendMoviesTests(unittest.TestCase):
    def setUp(self):
        # A and C score 4.5, B scores 5, D scores 4.25, and E scores 3.
        # The overall mean is 43 / 10 = 4.3, between A/C and D.
        self.model = fit_movie_mean([
            ("viewer-a", "A", 4),
            ("viewer-b", "A", 5),
            ("viewer-a", "B", 5),
            ("viewer-a", "C", 4),
            ("viewer-b", "C", 5),
            ("viewer-a", "D", 4),
            ("viewer-b", "D", 4),
            ("viewer-c", "D", 4),
            ("viewer-d", "D", 5),
            ("viewer-a", "E", 3),
        ])

    def test_filters_both_viewers_seen_movies_before_limiting(self):
        result = ranking.recommend_movies(
            self.model, ["B", "A", "E", "D", "C"], {"A"}, {"B"}, 2
        )

        self.assertEqual(result, ["C", "D"])

    def test_breaks_score_ties_alphabetically(self):
        result = ranking.recommend_movies(
            self.model, ["C", "A"], set(), set(), 2
        )

        self.assertEqual(result, ["A", "C"])

    def test_unknown_candidate_uses_the_fitted_fallback(self):
        result = ranking.recommend_movies(
            self.model, ["E", "unknown", "D"], set(), set(), 3
        )

        self.assertEqual(result, ["unknown", "D", "E"])

    def test_returns_available_movies_when_fewer_than_k_qualify(self):
        result = ranking.recommend_movies(
            self.model, ["A", "B"], {"B"}, set(), 5
        )

        self.assertEqual(result, ["A"])

    def test_returns_empty_when_all_candidates_have_been_seen(self):
        result = ranking.recommend_movies(
            self.model, ["A", "B", "C"], {"A"}, {"B", "C"}, 2
        )

        self.assertEqual(result, [])

    def test_returns_empty_for_no_candidates(self):
        result = ranking.recommend_movies(
            self.model, iter(()), set(), set(), 2
        )

        self.assertEqual(result, [])

    def test_returns_empty_when_zero_movies_are_requested(self):
        result = ranking.recommend_movies(
            self.model, ["A", "B"], set(), set(), 0
        )

        self.assertEqual(result, [])

    def test_ranks_only_supplied_candidates_from_an_iterator(self):
        result = ranking.recommend_movies(
            self.model, iter(["E", "D"]), set(), set(), 2
        )

        self.assertEqual(result, ["D", "E"])
