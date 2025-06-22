# Constant
HEX_COLOURS = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "black": "#000000",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a",
    "burlywood": "#deb887"
}

# Prompt user for input until they enter a blank line
colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in HEX_COLOURS:
        print(f"The code for {colour_name.title()} is {HEX_COLOURS[colour_name]}")
    else:
        print("Invalid colour name.")
    colour_name = input("Enter colour name: ").lower()

print("Goodbye!")
