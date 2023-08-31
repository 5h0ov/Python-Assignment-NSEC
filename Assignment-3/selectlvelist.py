list1 = input("Enter the first list separated by spaces: ").split()
list2 = input("Enter the second list separated by spaces: ").split()

newlist=[x for x in list2 if x not in list1]
    
print("The required list:",newlist)