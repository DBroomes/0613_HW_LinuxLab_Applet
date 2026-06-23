# Initialize the variable to store the validated integer
Age = None

# Continuously prompt the user until a valid integer is provided
while True:
    user_input = input("Please enter an Age (11 - 100): ")

    try:
        # Step 1: Attempt to convert the input string into a whole number
        number = int(user_input)

        # Step 2: Check if the number falls within the inclusive range of 1 to 100
        if 11 <= number <= 100:
            Age = number
            print(f"Success! Your number {Age} has been saved.")
            break  # Break out of the loop since the input is valid
        else:
            print("Out of range! The number must be between 11 and 100. Please try again.")

    except ValueError:
        # Handle cases where conversion to int fails (e.g., text, decimals, or blank inputs)
        print("Invalid data type! You must enter a whole number. Letters and decimals are not allowed.")

# Operator (<) and Conditional (if-else)
if Age < 21:
    print("Access denied.")
else:
    print("Access granted.")
