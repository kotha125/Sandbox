from prac_06.car import Car

def main():
    """Main program to demonstrate the Car class usage."""
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Fuel after adding 20: {limo.fuel}")
    distance_driven = limo.drive(115)
    print(f"Distance actually driven: {distance_driven} km")
    print(limo)

if __name__ == '__main__':
    main()