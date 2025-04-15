from src.extract import fetch_movie_data, search_movies
from src.config import CONFIG


def main():
    # Example usage: fetch a specific movie
    movie_title = "Inception"
    query = 'Bat'

    print(f"Fetching data for: {movie_title}")
    raw_data = fetch_movie_data(movie_title, api_config=CONFIG)

    print(raw_data['Title'])
    print(raw_data['Ratings'])

    # Transform the data (if you’ve built a transform module)
    # transformed_data = transform_movie_data(raw_data)

    # Load the data (e.g., save to a JSON file)
    # save_data_to_json(transformed_data, f"data/{movie_title}.json")

    print("\nSearching for related movies...")
    search_results = search_movies(query=query, api_config=CONFIG)
    # print(search_results)

    print(search_results)


if __name__ == "__main__":
    main()
