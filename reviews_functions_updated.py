import pandas as pd

def format_reviews_data(json_path):

    # define path to CSV file
    csv_reviews = '/Users/juditsig/ih/ih-projects/Project-01/IMDB_reviews.csv'
    df_reviews = pd.read_csv(csv_reviews)

    # grouping by 'movie_id' and 'is_spoiler', then count the reviews
    movies_grouped = df_reviews.groupby(['movie_id', 'is_spoiler']).count()

    # pivot the grouped data to transform 'is_spoiler' into columns
    pivoted_df = movies_grouped['review_text'].unstack(fill_value=0)

    # print out the pivoted DataFrame
    print(pivoted_df)