from decimal import Decimal

# Integer
# Integers are whole numbers, positive or negative, without any decimal point.
# Example:
my_int = 10
print(f"Integer: {my_int}, Type: {type(my_int)}")

# Basic operations with integers
a = 5
b = 2
print(f"Addition: {a + b}")  # Output: 7
print(f"Subtraction: {a - b}") # Output: 3
print(f"Multiplication: {a * b}")# Output: 10
print(f"Division: {a / b}")      # Output: 2.5 (Note: division always returns a float)
print(f"Floor Division: {a // b}")# Output: 2 (Integer division)
print(f"Modulus: {a % b}")     # Output: 1 (Remainder)
print(f"Exponentiation: {a ** b}")# Output: 25 (a raised to the power of b)

# Float
# Floats are numbers with a decimal point.
# Example:
my_float = 3.14
print(f"Float: {my_float}, Type: {type(my_float)}")

# Basic operations with floats (similar to integers)
c = 7.5
d = 2.5
print(f"Addition: {c + d}")
print(f"Subtraction: {c - d}")
print(f"Multiplication: {c * d}")
print(f"Division: {c / d}")

# Decimal
# Decimal numbers are used when precision is important, such as in financial calculations.

my_decimal = Decimal('3.14159')
print(f"Decimal: {my_decimal}, Type: {type(my_decimal)}")

# Operations with Decimals
e = Decimal('10.5')
f = Decimal('2.1')
print(f"Decimal Addition: {e + f}")
print(f"Decimal Subtraction: {e - f}")
print(f"Decimal Multiplication: {e * f}")
print(f"Decimal Division: {e / f}")

# Hexadecimal
# Hexadecimal numbers are base-16 numbers, using digits 0-9 and letters A-F.
# They are prefixed with '0x'.
my_hex = 0x1A  # 1A in hex is 26 in decimal
print(f"Hexadecimal: {my_hex}, Type: {type(my_hex)}")

# Binary
# Binary numbers are base-2 numbers, using digits 0 and 1.
# They are prefixed with '0b'.
my_binary = 0b1010  # 1010 in binary is 10 in decimal
print(f"Binary: {my_binary}, Type: {type(my_binary)}")

# Converting between number systems
# Convert integer to hexadecimal string
print(f"Integer to Hex: {hex(255)}")  # Output: 0xff

# Convert integer to binary string
print(f"Integer to Binary: {bin(10)}")   # Output: 0b1010

# Convert hexadecimal string to integer
print(f"Hex to Integer: {int('0xff', 16)}") # Output: 255

# Convert binary string to integer
print(f"Binary to Integer: {int('0b1010', 2)}")  # Output: 10