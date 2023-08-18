n=(int)(input("Enter the number of lines: "))

k=1

for i in range(0,n):
    for j in range(0,i):
        print(k,end="  ")
        k+=1
    print()