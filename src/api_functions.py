import requests

def get_IMDB_rating(ratings):

    imdb_rating = None

    for rating in ratings:
        if rating["Source"] == "Internet Movie Database":
            imdb_rating = rating["Value"].replace('/10', '')
            break

    return imdb_rating if imdb_rating else "N/A"



def add_movie_ratings(movies_old):

    movies_df = movies_old.copy()

    imdb_ratings = []

    for index, row in movies_df.iterrows():
        movie_id = row["movie_id"]
        params = {
            "apikey": "e89f7fbc" ,
            "i": movie_id 
        }
            
        url = "https://www.omdbapi.com"

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            ratings = data.get("Ratings", [])
            imdb_rating = get_IMDB_rating(ratings)
            print('el rating...', imdb_rating)
            imdb_ratings.append(imdb_rating)
        else:
            print(f"Error para la película {movie_id}: {response.status_code}")
            imdb_ratings.append("Error")

    movies_df["imdb_rating"] = imdb_ratings

    movies_df["imdb_rating"] = movies_df["imdb_rating"].astype(float)
    return movies_df


# rating_df = add_movie_ratings(df)

# print(rating_df)
