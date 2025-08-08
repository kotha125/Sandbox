import json
from movie import Movie

class MovieCollection:
    """A collection of movie objects with JSON save and sorting"""
    def __init__(self):
        self.movies = []

    def load_movies(self, filename):
        """Load movies from a JSON file into the collection"""
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for item in data:
            movie = Movie(item["title"], item["year"], item["category"], item["is_watched"])
            self.movies.append(movie)

    def save_movies(self, filename):
        """Save movies to a JSON file"""
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([movie.to_dict() for movie in self.movies], file, indent=4)

    def add_movie(self, movie):
        self.movies.append(movie)

    def sort(self, key):
        """Sort movies by the given key:Title, Year, Category or Watched"""
        self.movies.sort(key=lambda movie: getattr(movie, key))

    def get_unwatched(self):
        return [movie for movie in self.movies if not movie.is_watched]

    def get_watched(self):
        return [movie for movie in self.movies if movie.is_watched]
