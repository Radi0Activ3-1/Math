# Functions for arithmetic operations
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Division by zero is not allowed"

# Variables for length and width
length = 50  # Assign an appropriate value
width = 30    # Assign an appropriate value

# Calculate the area of the rectangle
area = multiply(length, width)

# Display the formatted message
print("\nThe area of the rectangle with:")
print(f"\tLength: {length}")
print(f"\tWidth:  {width}")
print(f"\nThe area of the rectangle with the length of {length} and width of {width} is:\n\t{area}")