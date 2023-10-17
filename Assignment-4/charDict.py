# Input a string from the user
input_string = input("Enter a string: ")

# Create an empty dictionary to store character counts
char_count = {}

# Iterate through the characters in the string and update the dictionary
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print the character counts
for char, count in char_count.items():
    print(f"'{char}' appears {count} times in the string.")
