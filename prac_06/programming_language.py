class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if language uses dynamic typing."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return string representation of ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"