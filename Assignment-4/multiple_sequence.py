from functools import reduce

# Create a sequence of 30 integers
sequence = list(range(1, 31))

# Use filter to reduce the sequence to even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, sequence))

# Use map to calculate the inverse (1/x) of even numbers
inverse_numbers = list(map(lambda x: 1 / x, even_numbers))

# Use reduce to find the sum of the inverse numbers
total_inverse = reduce(lambda x, y: x + y, inverse_numbers)

# Print the results
print("Even numbers:", even_numbers)
print("Inverse of even numbers:", inverse_numbers)
print("Sum of inverses:", total_inverse)
