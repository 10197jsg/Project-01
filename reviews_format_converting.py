import pandas as pd

# load JSON file
with open('/Users/juditsig/ih/ih-projects/Project-01/IMDB_reviews.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile, lines=True)

# convert the JSON to CSV
df.to_csv('IMDB_reviews.csv', encoding='utf-8', index=False)