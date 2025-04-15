from requests import request, Response


class OMDBAPICalls:
    """Handles all API requests to OMDb based on the provided configuration."""

    def __init__(self, config_dict):
        """
        Initializes the OMDBAPICalls class with a configuration dictionary.
        The dictionary should contain the API base URL and endpoints.


        """
        self.api_url = config_dict.get("OMDB_API_URL")
        # self.movie_endpoint = config_dict.get("MOVIE_ENDPOINT", '?apikey={apikey}&t={movie_title}')
        # self.search_endpoint = config_dict.get("SEARCH_ENDPOINT", '?apikey={apikey}&s={query}')
        self.params = {'apikey': config_dict.get("OMDB_API_KEY")}

    def request_handler(self, method, endpoint):
        """
        Handles the HTTP requests using the requests library.

        :param endpoint: The specific API endpoint (movie or search)
        :param params: The query parameters to be sent with the request.
        :return: The JSON response from the API.
        """
 # Ensure API key is always included
        response = request(method=method, url=endpoint, params=self.params)

        return response

    def get_data_by_movie_title(self, movie_title):
        """Fetch movie data by title."""
        self.params['t'] = movie_title
        response = self.request_handler(method='GET', endpoint=self.api_url)
        return response

    def search_api_call(self, query):
        """Search for movies by query."""
        self.params['t'] = query
        response = self.request_handler(method='GET', endpoint=self.api_url)
        return response
