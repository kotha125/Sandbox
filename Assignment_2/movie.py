class Movie:
    """Class representing a movie"""
    def __init__(self, title, year, category, is_watched=False):
        """Construct a movie object"""
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def mark_watched(self):
        """Mark the movie as watched"""
        self.is_watched = True

    def __str__(self):
        status = "watched" if self.is_watched else "unwatched"
        return f"{self.title} ({self.year}) : {self.category} ({status})"

    def to_dict(self):
        """Return string representing of the movie"""
        return {
            "title": self.title,
            "year": self.year,
            "category": self.category,
            "is_watched": self.is_watched
        }

