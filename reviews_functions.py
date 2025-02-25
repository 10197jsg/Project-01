import pandas as pd

def format_reviews_data(json_path):

    # define path to JSON files
    # json_reviews = '/Users/juditsig/ih/ih-projects/Project-01/df-imported_IMDB_reviews.json'
    df_reviews = pd.read_json(json_path, lines=True)

    # grouping by 'movie_id' and 'is_spoiler', then count the reviews
    movies_grouped = df_reviews.groupby(['movie_id', 'is_spoiler']).count()

    pivoted_df = movies_grouped['review_text'].unstack(fill_value=0)

    return pivoted_df