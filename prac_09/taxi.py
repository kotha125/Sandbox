from car import Car  # Assuming Car is in car.py


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    price_per_km = 1.23  # class variable

    def __init__(self, name, fuel):
        """Initialise a Taxi with name and fuel."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like Car plus current fare distance."""
        return f"{super().__str__()} plus {self.current_fare_distance}km on current fare"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Reset the fare distance."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like a regular car but add distance to fare."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven