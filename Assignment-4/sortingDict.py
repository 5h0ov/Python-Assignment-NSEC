# Initialize an empty dictionary
unsorted_dict = {}

# Prompt the user to enter key-value pairs
n = int(input("Enter the number of key-value pairs: "))

for i in range(n):
    key = input("Enter the key: ")
    value = int(input("Enter the value: "))
    
    # Add the key and value to the dictionary
    unsorted_dict[key] = value

# Sort the dictionary by values in ascending order
sorted_dict = dict(sorted(unsorted_dict.items(), key=lambda item: item[1]))

# Print the sorted dictionary
print("Sorted Dictionary in Ascending Order:")
for key, value in sorted_dict.items():
    print(key, value)
