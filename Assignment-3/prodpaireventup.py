temp = input("Enter comma-separated numbers: ")
tup = tuple(int(x) for x in temp.split(','))
print("The Tuple:", tup)

print("The required pairs:",end=" ")
for i in tup:
    temp=()
    for j in tup[i::]:
        temp=()
        if ((i*j)%2) == 0 and i!=j:
            temp=temp+(i,)
            temp=temp+(j,)
            print(temp,end=" ")