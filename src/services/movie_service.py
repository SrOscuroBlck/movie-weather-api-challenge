import requests
import os

TMDB_API_TOKEN = os.getenv("TMDB_API_TOKEN")

def get_movie_details(title):
    """
    Fetches detailed information about a movie by its title.
    
    Args:
        title (str): The title of the movie to search for.
    
    Returns:
        dict: A dictionary containing details about the movie, including:
              - title (str): Official movie title.
              - release_date (str): Movie release date in 'YYYY-MM-DD' format.
              - genres (list): List of genre names.
              - overview (str): Movie overview or description.
              - runtime (int or str): Movie runtime in minutes or 'N/A' if not available.

    Raises:
        ValueError: If the movie is not found or there are issues with the API request.
    """
    search_url = f"https://api.themoviedb.org/3/search/movie?query={title}"
    headers = {
        "Authorization": f"Bearer {TMDB_API_TOKEN}",
        "Content-Type": "application/json;charset=utf-8"
    }

    # Search for the movie by title
    response = requests.get(search_url, headers=headers)
    response.raise_for_status()
    movies = response.json().get("results", [])
    if not movies:
        raise ValueError("Movie not found.")
    
    # Fetch detailed information for the first result
    movie_id = movies[0]["id"]
    detail_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(detail_url, headers=headers)
    response.raise_for_status()
    movie_details = response.json()

    # Map genre IDs to genre names
    genre_mapping = get_genres()
    genres = [genre_mapping.get(genre["id"], "Unknown") for genre in movie_details.get("genres", [])]

    # Return relevant details about the movie
    return {
        "title": movie_details["title"],
        "release_date": movie_details["release_date"],
        "genres": genres,
        "overview": movie_details.get("overview", "No overview available."),
        "runtime": movie_details.get("runtime", "N/A"),
    }


GENRE_CACHE = None

def get_genres():
    """
    Fetches and caches the list of movie genres from the TMDB API.

    Returns:
        dict: A dictionary mapping genre IDs to genre names.
    """
    global GENRE_CACHE
    if GENRE_CACHE is not None:
        return GENRE_CACHE  # Return cached genres

    url = "https://api.themoviedb.org/3/genre/movie/list"
    headers = {
        "Authorization": f"Bearer {TMDB_API_TOKEN}",
        "Content-Type": "application/json;charset=utf-8"
    }

    # Request the genre list from the TMDB API
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Ensure the request was successful
    genres = response.json().get("genres", [])

    # Cache the mapping of genre IDs to genre names
    GENRE_CACHE = {genre["id"]: genre["name"] for genre in genres}
    return GENRE_CACHE
