try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"{numerator} / {denominator} is {fraction}")

    # When will a ValueError occur?
    # A ValueError occurs if the user inputs something that can't be converted to an integer,
    # such as letters or symbols (e.g., "abc" or "!@#").

    # When will a ZeroDivisionError occur?
    # A ZeroDivisionError occurs if the user enters 0 for the denominator.

    # Could you change the code to avoid the possibility of a ZeroDivisionError?
    # Yes, by checking if the denominator is 0 before performing the division.