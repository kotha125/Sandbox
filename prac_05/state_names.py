states = {
    "NSW": "New South Wales",
    "QLD": "Queensland",
    "NT": "Northern Territory",
}

# Print all states nicely aligned
for code, name in states.items():
    print(f"{code:<3} is {name}")

state = input("Enter state code: ").upper()

# Validate if the entered state code exists in dictionary
if state in states:
    print(states[state])
else:
    print("Invalid state code")
