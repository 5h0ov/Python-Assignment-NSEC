temp=input("Enter the list of numbers separated by spaces: ")
list=temp.split()
num=[int(n) for n in list] 
temp=[]
print("The required pairs:",end=" ")
for i in num:
    temp=[]
    for j in num[i::]:
        temp=[]
        if ((i*j)%2) == 1 and i!=j:
            temp.append(i)
            temp.append(j)
            print(temp,end=" ")


