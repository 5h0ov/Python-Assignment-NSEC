list1 = input("Enter the first list separated by spaces: ").split()
list2 = input("Enter the second list separated by spaces: ").split()

concat = [i for i in list1] + [i for i in list2]  # list comprehension

print("\nConcatenated List:", concat)
