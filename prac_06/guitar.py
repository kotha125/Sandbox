from datetime import datetime


class Guitar:
    """Represent a Guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar object with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation like: Gibson L-5 CES (1922) : $16,035.40"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return how old the guitar is in years."""
        return datetime.now().year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, else False."""
        return self.get_age() >= 50
