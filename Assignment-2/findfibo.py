N=(int)(input("Enter the number to find(N): "))
if(N==0):
    print("N is present")
    exit(1)

t1=1
t2=1
nextTerm=0
flag=0

for i in range(0,N):
    if(t1==N):
        print("N is present")
        flag=1
        break
    nextTerm=t1+t2
    t1=t2
    t2=nextTerm

if(flag!=1):
    print("N is not present")