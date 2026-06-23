# Initialize the variable to store the validated integer
Score = None

# Continuously prompt the user until a valid integer is provided
while True:
    user_input = input("Please enter an Score (1 - 100): ")

    try:
        # Step 1: Attempt to convert the input string into a whole number
        number = int(user_input)

        # Step 2: Check if the number falls within the inclusive range of 1 to 100
        if 1 <= number <= 100:
            Score = number
            print(f"Success! Your number {Score} has been saved.")
            break  # Break out of the loop since the input is valid
        else:
            print("Out of range! The number must be between 1 and 100. Please try again.")

    except ValueError:
        # Handle cases where conversion to int fails (e.g., text, decimals, or blank inputs)
        print("Invalid data type! You must enter a whole number. Letters and decimals are not allowed.")

# 2. Operator: Comparing the variable to a value using the #"greater than or equal to" (>=) operator
# 3. Conditional: Using an "if-else" structure to make a #decision
if Score >= 70:
    print("Pass")
else:
    print("Fail")
