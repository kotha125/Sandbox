# Example list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
print(f"Squares: {squares}")

# TODO 1: Write a list comprehension to create a list of the even numbers from the list 'numbers'
even_numbers = [number for number in numbers if number % 2 == 0]
print(f"Even numbers: {even_numbers}")

# TODO 2: Write a list comprehension to create a list of strings from a list of names, all in lowercase
names = ["Alice", "Bob", "Charlie", "Diana"]
lowercase_names = [name.lower() for name in names]
print(f"Lowercase names: {lowercase_names}")

# TODO 3: Write a list comprehension to create a list of the lengths of each name in the list 'names'
name_lengths = [len(name) for name in names]
print(f"Name lengths: {name_lengths}")

# TODO 4: Write a list comprehension to create a list of names longer than 3 characters
long_names = [name for name in names if len(name) > 3]
print(f"Names longer than 3 characters: {long_names}")
