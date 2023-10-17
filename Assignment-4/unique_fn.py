def find_unique(st):
    # Create an empty list to store unique elements
    unique = []

    # Iterate through the input list
    for item in lst:
        if item not in unique:
            unique.append(item)
        else:
            unique.remove(item)

    return unique

# Input a list from the user
lst = input("Enter a list of elements separated using space: ").split()

# Call the function to find unique elements
unique = find_unique(lst)

# Print the unique elements
print("Unique elements:", unique)
