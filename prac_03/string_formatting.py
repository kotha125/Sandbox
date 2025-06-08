name = "Gibson L-5 CES"
year = 1922
cost = 16035.95

# Example string formatting
print("My guitar: {} ({}), worth ${:,.2f}".format(name, year, cost))
print(f"My guitar: {name} ({year}), worth ${cost:,.2f}")

numbers = [1, 19, 123456, 4]
for i in range(len(numbers)):
    print("Number {:>3}".format(numbers[i]))

# Custom output with f-string
print(f"{year} {name} for about ${cost:,.0f}!")

# Powers of 2 with aligned formatting
for i in range(11):
    print(f"2 ^ {i:>2} is {2 ** i:>4}")