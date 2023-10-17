# Initialize two empty dictionaries
dict1 = {}
dict2 = {}

# Input the first dictionary from the user
n1 = int(input("Enter the number of key-value pairs for the first dictionary: "))
for i in range(n1):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    dict1[key] = value

# Input the second dictionary from the user
n2 = int(input("Enter the number of key-value pairs for the second dictionary: "))
for i in range(n2):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    dict2[key] = value

# Merge the two dictionaries using the update method
dict1.update(dict2)

# Print the merged dictionary
print("Merged Dictionary:")
print(dict1)
