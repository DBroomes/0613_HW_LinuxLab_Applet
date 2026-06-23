#!/bin/bash

# Define paths to your Python scripts in separate directories
SCRIPT1="./python1/passingScore.py"
SCRIPT2="./python2/allowedToDrink.py"
SCRIPT3="./python3/discountApplied.py"

# Function to check file existence and format the menu item
check_and_format() {
    local file_path="$1"
    local label="$2"
    if [ -f "$file_path" ]; then
        echo "$label) $(basename "$file_path") [Found in: $(dirname "$file_path")]"
    else
        echo "$label) [MISSING] $(basename "$file_path") (Expected in: $(dirname "$file_path"))"
    fi
}

# Display the menu
echo "====================================="
echo "  Select a Python Script to Run"
echo "====================================="
check_and_format "$SCRIPT1" "1"
check_and_format "$SCRIPT2" "2"
check_and_format "$SCRIPT3" "3"
echo "4) Quit"
echo "-------------------------------------"

# Loop until a valid selection is made
while true; do
    read -p "Please enter your choice [1-4]: " CHOICE

    case $CHOICE in
        1)
            if [ -f "$SCRIPT1" ]; then
                echo "Running $(basename "$SCRIPT1")..."
                python3 "$SCRIPT1"
                break
            else
                echo "Error: File not found at $SCRIPT1"
            fi
            ;;
        2)
            if [ -f "$SCRIPT2" ]; then
                echo "Running $(basename "$SCRIPT2")..."
                python3 "$SCRIPT2"
                break
            else
                echo "Error: File not found at $SCRIPT2"
            fi
            ;;
        3)
            if [ -f "$SCRIPT3" ]; then
                echo "Running $(basename "$SCRIPT3")..."
                python3 "$SCRIPT3"
                break
            else
                echo "Error: File not found at $SCRIPT3"
            fi
            ;;
        4)
            echo "Exiting script. Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid selection. Please enter a number between 1 and 4."
            ;;
    esac
done
