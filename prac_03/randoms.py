import random

# Line 1: random.randint(5, 20)
print(random.randint(5, 20))
# What did you see on line 1?
# --> Random integers like: 6, 13, 20, etc.
# Smallest number: 5
# Largest number: 20

# Line 2: random.randrange(3, 10, 2)
print(random.randrange(3, 10, 2))
# What did you see on line 2?
# --> Random odd numbers like: 3, 5, 7, 9
# Smallest number: 3
# Largest number: 9
# Could line 2 have produced a 4?
# --> No, because with step=2 from 3, only odd numbers are possible.

# Line 3: random.uniform(2.5, 5.5)
print(random.uniform(2.5, 5.5))
# What did you see on line 3?
# --> Random float values like: 3.78, 4.12, 5.01, etc.
# Smallest number: 2.5
# Largest number: 5.5

# Write code to produce a random number between 1 and 100 inclusive:
print(random.randint(1, 100))