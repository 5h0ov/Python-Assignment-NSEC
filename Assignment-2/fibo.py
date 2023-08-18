N=(int)(input("Enter the number of terms(N): "))

print("0",end=" ")

t1=1
t2=1
nextTerm=0

for i in range(1,N):
    print(t1,end=" ")
    nextTerm=t1+t2
    t1=t2
    t2=nextTerm