from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi with a flagfall and fanciness multiplier."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return fare including flagfall, rounded to nearest 10 cents."""
        fare = super().get_fare() + self.flagfall
        return round(fare, 1)  # Round to nearest 10c

    def __str__(self):
        """Return string like Taxi + extra info for SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
