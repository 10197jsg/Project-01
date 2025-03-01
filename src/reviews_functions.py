import pandas as pd

def format_reviews_data():
    
    # Define path to CSV file
    csv_reviews = '../data/IMDB_reviews.csv'
    df_reviews = pd.read_csv(csv_reviews)

    # Group by 'movie_id' and 'is_spoiler', then count the reviews
    movies_grouped = df_reviews.groupby(['movie_id', 'is_spoiler']).size().unstack(fill_value=0)

    # Rename columns for clarity
    movies_grouped.columns = ['not_spoiled_reviews', 'spoiled_reviews']

    # Calculate the total reviews for each movie
    movies_grouped['total_reviews'] = movies_grouped['not_spoiled_reviews'] + movies_grouped['spoiled_reviews']

    # Reset index to convert 'movie_id' into a column
    movies_grouped = movies_grouped.reset_index()

    # Select only the columns 'movie_id', 'spoiled_reviews', and 'total_reviews'
    result_df = movies_grouped[['movie_id', 'spoiled_reviews', 'total_reviews']]

    # Sort by 'total reviews' in descending order
    result_df = movies_grouped.sort_values(by='total_reviews', ascending=False)

    # Calculate 'spoiled reviews' percentage
    result_df_copy = result_df.copy()
    result_df_copy['spoiled_percentage'] = (result_df_copy['spoiled_reviews'] / result_df_copy['total_reviews']) * 100

    return result_df_copy