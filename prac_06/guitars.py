from guitar import Guitar
# guitars.py
def main():
    print("My guitars!")
    guitars = []

    name = input("Name: ")
    while name != "":
        year = get_valid_int("Year: ")
        cost = get_valid_float("Cost: $")
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ")

    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_label = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_label}")
    else:
        print("\nNo guitars entered.")


def get_valid_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number < 0:
                print("Number must be >= 0")
            else:
                return number
        except ValueError:
            print("Invalid input; enter a valid number")


def get_valid_float(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number < 0:
                print("Number must be >= 0")
            else:
                return number
        except ValueError:
            print("Invalid input; enter a valid number")


if __name__ == '__main__':
    main()
