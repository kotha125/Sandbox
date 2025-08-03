from car import Car
import random

class UnreliableCar(Car):
    """Car that may or may not drive depending on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if random chance allows it, based on reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
