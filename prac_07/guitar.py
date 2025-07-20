class Guitar:
    """Represent a guitar."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        """Return how old the guitar is."""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age(current_year) >= 50

    def __lt__(self, other):
        """Compare guitars by year for sorting."""
        return self.year < other.year
