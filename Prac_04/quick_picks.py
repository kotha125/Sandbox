import random

# Constants
NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    num_picks = int(input("How many quick picks? "))
    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        # Print numbers right-aligned in 2-character width
        print(" ".join(f"{number:2}" for number in quick_pick))

def generate_quick_pick():
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers

if __name__ == "__main__":
    main()
