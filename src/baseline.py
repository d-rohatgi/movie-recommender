from collections import defaultdict

def fit_movie_mean(training_rows) -> {}:

    movie_map = defaultdict(list)
    dupe_reviews = set()
    total = 0
    tally =0
    #(viewer_id, movie_id, rating) tuples
    for row in training_rows:
        total += row[2]
        tally +=1
        if row[2] is None:
            raise ValueError("None Rating given")
        #if (row[0], row[1]) not in dupe_reviews:
        movie_map[row[1]].append(row[2])
        #dupe_reviews.add((row[0], row[1]))

    movie_means  = {}
    for movie_id, reviews in movie_map.items():
        movie_means[movie_id] = (sum(reviews)/len(reviews))

    if len(movie_map) == 0:
        raise ValueError("None Rating given")
    movie_means[0] = total/tally
    return movie_means


def predict_rating(model, movie_id):
    if movie_id in model:
        return model[movie_id]
    else:
        return model[0]
