# Input the value of 'n'
n = int(input("Enter a value for 'n': "))

# Create the dictionary
dict = {}

# Populate the dictionary with (i, i*i) for i from 1 to n
for i in range(1, n + 1):
    dict[i] = i * i

# Print the dictionary
print(dict)
