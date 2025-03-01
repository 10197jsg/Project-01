import seaborn as sns
import matplotlib.pyplot as plt

def print_scatterplot1(movies_w_ratings):
    
    # Scatterplot for numerical variables
    sns.scatterplot(x = "imdb_rating", y = "spoiled_reviews", data = movies_w_ratings)
    plt.show()

def print_scatterplot2(movies_w_ratings):

    # Scatterplot for numerical variables
    sns.scatterplot(x = "imdb_rating", y = "spoiled_percentage", data = movies_w_ratings)
    plt.show()

def print_lineplot(movies_w_ratings):

    # Lineplot for numerical variables
    sns.lineplot(x = "imdb_rating", y = "spoiled_percentage", data = movies_w_ratings)
    plt.show()