N=(int)(input("Enter value of N for the series: "))
sum=0

for i in range(1,N+1):
    f=1
    for j in range(1,i+1):
        f=f*j
    sum+= 1/f;

print("The required sum is: {:.2f}".format(sum))
