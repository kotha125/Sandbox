from guitar import Guitar
CURRENT_YEAR = 2024
FILENAME = "guitars.csv"


def main():
    guitars = load_guitars(FILENAME)
    print("These are my guitars:")
    display_guitars(guitars)

    # Let user add more guitars
    print("\nAdd your new guitars:")
    guitars += get_new_guitars()

    # Sort guitars by year
    guitars.sort()

    # Display sorted list
    print("\nThese are my guitars (sorted):")
    display_guitars(guitars)

    # Save to file
    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display a list of guitars with formatting."""
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(CURRENT_YEAR) else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def get_new_guitars():
    """Prompt user to enter new guitars."""
    new_guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        new_guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ")
    return new_guitars


def save_guitars(filename, guitars):
    """Save guitars to CSV file."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
