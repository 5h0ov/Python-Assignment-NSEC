temp=input("Enter the list of numbers separated by spaces: ")
list=temp.split()
num=[int(n) for n in list]    # converting each string from input list and storing in new list of integers

print("The list you entered: ",num)
min=max=num[0]

for i in num:
    if i<min:
        min=i
    if i>max:
        max=i

print("Maximum Number:",max)
print("Minimum Number:",min)
