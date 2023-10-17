# Define a list of numbers
input = input("Enter a list of elements separated using space: ").split()

lst= [int(x) for x in input]

# Use the filter function with a lambda function to filter even numbers
even = list(filter(lambda x: x % 2 == 0, lst))

# Print the even numbers
print("Even numbers from the list:", even)
