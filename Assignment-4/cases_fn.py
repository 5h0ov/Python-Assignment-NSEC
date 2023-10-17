def count_case(str):
    # Initialize counters for uppercase and lowercase letters
    uc = 0
    lc = 0

    # Iterate through the characters in the input string
    for char in str:
        if char.isupper():
            uc += 1
        elif char.islower():
            lc += 1

    return uc, lc

# Input a string from the user
str = input("Enter a string: ")

# Call the function to count uppercase and lowercase letters
u, l = count_case(str)

# Print the results
print("Uppercase letters:", u)
print("Lowercase letters:", l)
