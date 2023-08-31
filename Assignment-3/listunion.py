list1 = input("Enter the first list separated by spaces: ").split()
list2 = input("Enter the second list separated by spaces: ").split()

# union = list1 + [num for num in list2 if num not in list1]   <-- idk why this didn't work for multiple 1s
union=list(set(list1 + list2))  # works with everything 

print("Union of the two lists:", union)