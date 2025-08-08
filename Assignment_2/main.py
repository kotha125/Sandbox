"""
CP1404 Assignment 2- Must see movies 2.0 GUI Program

"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from moviecollection import MovieCollection
from movie import Movie

FILENAME = 'movies.json'

class MoviesApp(App):
    """Main app class for the Movie GUI application"""
    def build(self):
        self.title = "Must-See Movies 2.0"
        self.root = Builder.load_file('movies.kv')
        self.movie_collection = MovieCollection()
        self.movie_collection.load_movies(FILENAME)
        self.display_movies()
        return self.root

    def display_movies(self):
        """Display movies buttons in the GUI"""
        self.root.ids.movie_grid.clear_widgets()
        for movie in self.movie_collection.movies:
            btn = Button(
                text=str(movie),
                size_hint_y=None,
                height=40,
                background_color=(0, 1, 0, 1) if not movie.is_watched else (1, 1, 1, 1)
            )
            btn.bind(on_release=self.mark_movie_watched)
            self.root.ids.movie_grid.add_widget(btn)

    def mark_movie_watched(self, instance):
        """Mark a movie as watched when its button is clicked"""
        movie_str = instance.text
        for movie in self.movie_collection.movies:
            if str(movie) == movie_str:
                if movie.is_watched:
                    self.root.ids.status_label.text = f"You have already watched {movie.title}"
                else:
                    movie.mark_watched()
                    self.root.ids.status_label.text = f"You watched {movie.title}"
                break
        self.display_movies()

    def add_movie(self):
        """Add a new movie from the input fields"""
        title = self.root.ids.title_input.text.strip()
        year = self.root.ids.year_input.text.strip()
        category = self.root.ids.category_input.text.strip()
        if not title or not year or not category:
            self.root.ids.status_label.text = "All fields must be completed"
            return
        try:
            year = int(year)
            if year < 1:
                raise ValueError
        except ValueError:
            self.root.ids.status_label.text = "Please enter a valid year"
            return
        new_movie = Movie(title, year, category)
        self.movie_collection.add_movie(new_movie)
        self.root.ids.status_label.text = f"{title} ({category} from {year}) added."
        self.display_movies()

    def sort_movies(self, key):
        """Clear all text input fields and message label"""
        self.movie_collection.sort(key)
        self.display_movies()

    def on_stop(self):
        """Save movies to file when the app is closed"""
        self.movie_collection.save_movies(FILENAME)

if __name__ == '__main__':
    MoviesApp().run()
