import unittest

from src import baseline


UNEVEN_TRAINING_ROWS = (
    ("viewer-a", "P", 1),
    ("viewer-b", "P", 4),
    ("viewer-c", "Q", 5),
)


class FitMovieMeanTests(unittest.TestCase):
    def test_fits_from_a_one_shot_iterator(self):
        model = baseline.fit_movie_mean(iter(UNEVEN_TRAINING_ROWS))

        self.assertIsNotNone(model)

    def test_rejects_empty_training_data(self):
        with self.assertRaises(ValueError):
            baseline.fit_movie_mean(iter(()))


class PredictRatingTests(unittest.TestCase):
    def test_predicts_the_fitted_mean_for_each_known_movie(self):
        model = baseline.fit_movie_mean(iter(UNEVEN_TRAINING_ROWS))

        for movie_id, expected in (("P", 2.5), ("Q", 5.0)):
            with self.subTest(movie_id=movie_id):
                prediction = baseline.predict_rating(model, movie_id)
                self.assertIsInstance(prediction, float)
                self.assertAlmostEqual(prediction, expected)

    def test_uses_the_mean_of_individual_ratings_for_an_unknown_movie(self):
        model = baseline.fit_movie_mean(iter(UNEVEN_TRAINING_ROWS))

        prediction = baseline.predict_rating(model, "R")

        self.assertIsInstance(prediction, float)
        self.assertAlmostEqual(prediction, 10 / 3)

    def test_counts_both_ratings_from_a_repeated_viewer_movie_pair(self):
        training_rows = (
            ("viewer-a", "P", 1),
            ("viewer-a", "P", 5),
            ("viewer-b", "Q", 5),
        )
        model = baseline.fit_movie_mean(iter(training_rows))

        self.assertAlmostEqual(baseline.predict_rating(model, "P"), 3.0)
        self.assertAlmostEqual(baseline.predict_rating(model, "R"), 11 / 3)
