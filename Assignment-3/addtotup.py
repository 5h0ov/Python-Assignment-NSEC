temp = input("Enter comma-separated numbers: ")
tup = tuple(int(x) for x in temp.split(','))
print("The Tuple:", tup)

print("Enter the element to add to the tuple below(-1 to stop):")
while(1):
    n=(int)(input())
    if n==-1: break
    tup=tup+(n,)

print("The New Tuple:",tup)