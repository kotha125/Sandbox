# 1. Ask the user for their name and write it to name.txt using open and close
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# 2. Read the name from name.txt and greet the user using open and close
in_file = open("name.txt", "r")
name = in_file.read().strip()  # use .strip() to remove any extra newline
in_file.close()
print(f"Hi {name}!")

# 3. Read first two numbers from numbers.txt, add them and print the result
with open("numbers.txt", "r") as in_file:
    line1 = in_file.readline()
    line2 = in_file.readline()
    result = int(line1) + int(line2)
print(result)  # Expected output: 59

# 4. Read all numbers from numbers.txt and print the total
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)  # Should print the sum of all numbers (e.g., 17 + 42 + 400 = 459)