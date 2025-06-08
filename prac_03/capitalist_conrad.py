import random

# --- Constants ---
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "stock_prices.txt"

# --- Variables ---
price = INITIAL_PRICE
number_of_days = 0

# Open file for writing
out_file = open(FILENAME, 'w')

# Write starting price to file
print(f"Starting price: ${price:,.2f}", file=out_file)

# --- Main Loop ---
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    number_of_days += 1

    if random.randint(1, 2) == 1:  # Increase
        price_change = random.uniform(0, MAX_INCREASE)
    else:  # Decrease
        price_change = -random.uniform(0, MAX_DECREASE)

    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file
out_file.close()