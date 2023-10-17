# Define a list of numbers
input = input("Enter a list of elements separated using space: ").split()

list= [int(x) for x in input]

# Use the max function with a lambda function to find the maximum value
max = max(list, key=lambda x: x)

# Print the maximum value
print("Maximum value from the list:", max)
