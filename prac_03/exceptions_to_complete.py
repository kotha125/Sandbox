# TODO: Add a while loop to keep asking until a valid integer is entered
valid_input = False
while not valid_input:
    try:
        result = int(input("Enter a valid integer: "))
        valid_input = True
    except ValueError:
        print("Please enter a valid integer.")

# TODO: Print the result once a valid input has been received
print(f"You entered: {result}")