# Function to find common items in two lists
def find_common(list1, list2):
    common = set(list1) & set(list2)
    return list(common)

# Function to merge two lists without duplicates
def merge_without_dup(list1, list2):
    merged = list(set(list1 + list2))
    return merged

# Input two lists from the user
list1 = input("Enter the first list (comma-separated): ").split(',')
list2 = input("Enter the second list (comma-separated): ").split(',')

# Find common items in the two lists
common = find_common(list1, list2)

# Merge the two lists without duplicates
merged = merge_without_dup(list1, list2)

# Print the results
print("Common items in the two lists:", common)
print("Merged list without duplicates:", merged)
