"""

Estimate time: 45 minutes
Actual time: 55 minutes

"""

FILENAME = "wimbledon.csv"

def load_data(filename):
    """Load data from CSV and return a list of lists: [year, champion, country]."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # skip header line
        for line in in_file:
            line = line.strip()
            if line:
                parts = line.split(",")
                # Some champion names or countries might have commas, but assuming simple CSV here
                year = parts[0]
                champion = parts[1]
                country = parts[2]
                data.append([year, champion, country])
    return data

def count_champions(data):
    """Return a dictionary mapping champion names to number of wins."""
    counts = {}
    for _, champion, _ in data:
        counts[champion] = counts.get(champion, 0) + 1
    return counts

def get_countries(data):
    """Return a sorted list of unique country codes."""
    countries = set()
    for _, _, country in data:
        countries.add(country)
    return sorted(countries)

def print_report(champion_counts, countries):
    """Print the champions with counts and the countries list."""
    print("Wimbledon Champions: ")
    for champion, count in champion_counts.items():
        print(f"{champion} {count}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(countries))

def main():
    data = load_data(FILENAME)
    champion_counts = count_champions(data)
    countries = get_countries(data)
    print_report(champion_counts, countries)

if __name__ == "__main__":
    main()
