from unreliable_car import UnreliableCar

def main():
    reliable_car = UnreliableCar("Reliable", 100, 100)  # should always drive
    unreliable_car = UnreliableCar("Unreliable", 100, 10)  # rarely drives

    print("Testing reliable car (100% reliable):")
    total_driven = 0
    for _ in range(10):
        total_driven += reliable_car.drive(10)
    print(f"Total driven: {total_driven} km (should be 100)")

    print("\nTesting unreliable car (10% reliable):")
    total_driven = 0
    for _ in range(100):
        total_driven += unreliable_car.drive(1)
    print(f"Total driven (out of 100 tries): {total_driven} km")

if __name__ == "__main__":
    main()
