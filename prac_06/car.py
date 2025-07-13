class Car:
    def __init__(self, name="", fuel=0):
        """Initialise a Car instance with name, fuel and odometer set to 0."""
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """Return a string representation of the car."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

    def add_fuel(self, amount):
        """Add amount to the fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance, reducing fuel and increasing odometer."""
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            distance_driven = distance
            self.fuel -= distance
        self.odometer += distance_driven
        return distance_driven