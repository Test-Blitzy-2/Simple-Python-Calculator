# Simple Calculator in Python
# This calculator performs basic arithmetic and scientific operations
import math

def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract second number from first"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide first number by second"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    """Function to calculate x raised to the power of y"""
    return math.pow(x, y)

def sqrt(x):
    """Function to calculate the square root of x"""
    if x < 0:
        return "Error! Cannot calculate square root of a negative number."
    return math.sqrt(x)

def sine(x):
    """Function to calculate the sine of an angle in degrees"""
    # Convert degrees to radians before calculation
    radians = math.radians(x)
    return math.sin(radians)

def cosine(x):
    """Function to calculate the cosine of an angle in degrees"""
    # Convert degrees to radians before calculation
    radians = math.radians(x)
    return math.cos(radians)

def logarithm(x):
    """Function to calculate the natural logarithm of x"""
    if x <= 0:
        return "Error! Cannot calculate logarithm of a non-positive number."
    return math.log(x)

# Display available operations
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square Root")
print("7. Sine")
print("8. Cosine")
print("9. Logarithm")

# Take user input for operation
choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

# Determine if the operation requires one or two inputs
if choice in ['1', '2', '3', '4', '5']:
    # Operations requiring two inputs
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        exit()
        
    # Perform calculation based on user's choice
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", power(num1, num2))
    else:
        print("Invalid input. Please choose a valid operation.")
        
elif choice in ['6', '7', '8', '9']:
    # Operations requiring one input
    try:
        num = float(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        exit()
        
    # Perform calculation based on user's choice
    if choice == '6':
        print("Result:", sqrt(num))
    elif choice == '7':
        print("Result:", sine(num))
        print("Note: Input angle was in degrees")
    elif choice == '8':
        print("Result:", cosine(num))
        print("Note: Input angle was in degrees")
    elif choice == '9':
        print("Result:", logarithm(num))
    else:
        print("Invalid input. Please choose a valid operation.")
        
else:
    print("Invalid input. Please choose a valid operation.")