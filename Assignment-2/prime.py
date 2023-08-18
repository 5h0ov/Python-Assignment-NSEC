n=(int)(input("Enter a number: "))

if(n>1):
    prime= True
for j in range(2,int(n ** 0.5)+1):
    if(n%j==0):
        prime= False
        break;
    
if(prime):
    print("It is a prime number.")
else:
    print("It is not a prime number")