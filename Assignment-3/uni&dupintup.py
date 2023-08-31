temp = input("Enter comma-separated numbers: ")
tup = tuple(int(x) for x in temp.split(','))
print("The Tuple:", tup)

unique=()
dup=()
for i in tup:
    if i in unique:
        dup=dup+(i,)
    else:
        unique=unique+(i,)

print("The Unique Elements are: ",tuple(x for x in unique if x not in dup))
print("The Duplicate Elements are: ",dup)
