from src.omdb_api_calls import OMDBAPICalls

# Example configuration dictionary

# Initialize the OMDBAPICalls class with the config_dict


def fetch_movie_data(movie_title, api_config):
    """Fetch movie data using OMDBAPICalls class."""
    omdb_api = OMDBAPICalls(config_dict=api_config)
    result = omdb_api.get_data_by_movie_title(movie_title=movie_title)
    return result.json()


def search_movies(query, api_config):
    """Search for movies by query using OMDBAPICalls class."""
    omdb_api = OMDBAPICalls(config_dict=api_config)
    result = omdb_api.search_api_call(query=query)
    return result.json()

# Example usage: Fetch movie data for 'Inception'
