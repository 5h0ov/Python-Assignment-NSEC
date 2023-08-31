lst=[]
print("Enter the items of the list below: ")
for i in range(0,16):
    lst.append(input())

print("The list you entered: ",lst)
print("The modified list(after removing duplicates): ",list(set(lst)))

