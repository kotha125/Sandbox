def main():
    """Main function to run the income report generator."""
    number_of_months = int(input("How many months? "))
    incomes = []

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes)


def print_income_report(incomes):
    """Print a formatted income report given a list of incomes."""
    print("\nIncome Report")
    print("-------------")

    cumulative_total = 0
    for month, income in enumerate(incomes, start=1):
        cumulative_total += income
        print(f"Month {month:2} - Income: ${income:10.2f}    Total: ${cumulative_total:10.2f}")


main()
