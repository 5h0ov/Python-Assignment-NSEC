n=(int)(input("Enter value of n for the range 1 to n: "))
sum=0

for i in range(2,n):
    if(i>1):
        prime= True
    for j in range(2,int(i ** 0.5)+1):
        if(i%j==0):
            prime= False
            break
    sum+=i
    
print("The sum of all the prime numbers in that given range is",sum)