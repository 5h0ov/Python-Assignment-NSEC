def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Input a number from the user
num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")
