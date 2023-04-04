# Define global variables for primary colors
RED = "red"
BLUE = "blue"
YELLOW = "yellow"

# Take inputs from user
color1 = input("Enter the first primary color: ").lower()
color2 = input("Enter the second primary color: ").lower()

# Check if inputs are valid
if color1 not in [RED, BLUE, YELLOW]:
    print("Error: Invalid Color1")
elif color2 not in [RED, BLUE, YELLOW]:
    print("Error: Invalid Color2")
elif color1 == color2:
    print("Error: The two colors you entered are same")
else:
    # Mix the two primary colors to get secondary color
    if color1 == RED:
        if color2 == BLUE:
            print("Purple")
        elif color2 == YELLOW:
            print("Orange")
    elif color1 == BLUE:
        if color2 == RED:
            print("Purple")
        elif color2 == YELLOW:
            print("Green")
    elif color1 == YELLOW:
        if color2 == RED:
            print("Orange")
        elif color2 == BLUE:
            print("Green")