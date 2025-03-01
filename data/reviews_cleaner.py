import pandas as pd
import numpy as np

# define path to JSON files
json_reviews = '/Users/juditsig/ih/ih-projects/Project-01/df-imported_IMDB_reviews.json'
df_reviews = pd.read_json(json_reviews, lines=True)
print(df_reviews.head())

# find if null in df
df_reviews.isna().any()

# hid 'rating' column
df_reviews.drop(columns= ['rating'], inplace=True)
print(df_reviews)