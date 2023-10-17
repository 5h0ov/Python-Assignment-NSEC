# Function to compute the GCD (Greatest Common Divisor)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute the LCM (Least Common Multiple)
def lcm(a, b):
    return (a * b) // gcd(a, b)

# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate GCD and LCM using the defined functions
gcd_result = gcd(num1, num2)
lcm_result = lcm(num1, num2)

# Print the results
print(f"GCD of {num1} and {num2} is {gcd_result}")
print(f"LCM of {num1} and {num2} is {lcm_result}")
