from config import CONFIG
from omdb_api_calls import OMDBAPICalls

# Example configuration dictionary

# Initialize the OMDBAPICalls class with the config_dict
omdb_api = OMDBAPICalls(config_dict=CONFIG)



def fetch_movie_data(movie_title):
    """Fetch movie data using OMDBAPICalls class."""
    result = omdb_api.fetch_movie_data(movie_title)
    return result

# def search_movies(query):
#     """Search for movies by query using OMDBAPICalls class."""
#     return omdb_api.search_movies(query)

# Example usage: Fetch movie data for 'Inception'
if __name__ == "__main__":
    movie_data = fetch_movie_data("Inception")
    print(movie_data)