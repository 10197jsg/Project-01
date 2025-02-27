import pandas as pd

def format_reviews_data():
    
    # Define path to CSV file
    csv_reviews = 'IMDB_reviews.csv'
    df_reviews = pd.read_csv(csv_reviews)

    # Group by 'movie_id' and 'is_spoiler', then count the reviews
    movies_grouped = df_reviews.groupby(['movie_id', 'is_spoiler']).size().unstack(fill_value=0)

    # Rename columns for clarity
    movies_grouped.columns = ['not_spoiled_reviews', 'spoiled_reviews']

    # Reset index to convert 'movie_id' into a column
    movies_grouped = movies_grouped.reset_index()

    # Select only the columns 'movie_id' and 'spoiled_reviews'
    result_df = movies_grouped[['movie_id', 'spoiled_reviews']]

    return result_df