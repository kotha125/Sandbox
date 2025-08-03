from taxi import Taxi

def main():
    # Step 1: Create a new Taxi object (no price per km argument now)
    my_taxi = Taxi("Prius 1", 100)

    # Step 2: Drive the taxi 40 km
    my_taxi.drive(40)

    # Step 3: Print the taxi's details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Step 4: Restart the meter and drive 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)

    # Step 5: Print again
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

if __name__ == "__main__":
    main()

