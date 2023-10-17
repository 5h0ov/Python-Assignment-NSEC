# Function to convert a hexadecimal number to binary
def hex_to_binary(hex_number):
    try:
        decimal_number = int(hex_number, 16)
        binary_number = bin(decimal_number)[2:]
        return binary_number
    except ValueError:
        return "Invalid hexadecimal input"

# Function to convert a hexadecimal number to decimal
def hex_to_decimal(hex_number):
    try:
        decimal_number = int(hex_number, 16)
        return decimal_number
    except ValueError:
        return "Invalid hexadecimal input"

# Input a hexadecimal number from the user
hexadecimal_input = input("Enter a hexadecimal number: ")

# Convert the hexadecimal number to binary and decimal
binary_result = hex_to_binary(hexadecimal_input)
decimal_result = hex_to_decimal(hexadecimal_input)

# Print the results
print(f"Hexadecimal: {hexadecimal_input}")
print(f"Binary: {binary_result}")
print(f"Decimal: {decimal_result}")
