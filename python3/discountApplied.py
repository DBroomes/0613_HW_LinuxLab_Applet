# Initialize the variable to store the validated integer
cart_total = None

# Continuously prompt the user until a valid integer is provided
while True:
    user_input = input("Please enter an the total items in cart (20 - 200): ")

    try:
        # Step 1: Attempt to convert the input string into a whole number
        number = int(user_input)

        # Step 2: Check if the number falls within the inclusive range of 20 to 200
        if 20 <= number <= 200:
            cart_total = number
            print(f"Success! Your number {cart_total} has been saved.")
            break  # Break out of the loop since the input is valid
        else:
            print("Out of range! The number must be between 20 and 200. Please try again.")

    except ValueError:
        # Handle cases where conversion to int fails (e.g., text, decimals, or blank inputs)
        print("Invalid data type! You must enter a whole number. Letters and decimals are not allowed.")


# Variables

discount_applied = False

# Operator (>) and Conditional (if)
if cart_total > 100:
    discount_applied = True
    print("Discount applied!")
    cart_total = cart_total - 15  # Arithmetic operator (-)
else:
    print("No discount applied.")
print(cart_total)
