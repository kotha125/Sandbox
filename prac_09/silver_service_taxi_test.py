from silver_service_taxi import SilverServiceTaxi

# Test: SilverServiceTaxi with fanciness of 2, 18km trip
fancy_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
fancy_taxi.drive(18)
fare = fancy_taxi.get_fare()
print(fancy_taxi)
print(f"Fare: ${fare:.2f}")
assert fare == 48.8, f"Expected $48.80, got ${fare:.2f}"