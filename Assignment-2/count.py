cp=0  # Count Prime(p)
cc=0  # Count Composite(c)


while(1):
    n=(int)(input("Enter a number(-1 to stop): "))

    if(n>1):
        prime= True
    elif(n==1):
        prime= False
    else:
        break

    for j in range(2,int(n ** 0.5)+1):
        if(n%j==0):
            prime= False
            break;
        
    if(prime):
        cp+=1
    else:
        cc+=1   

print("The number of prime and composite numbers you entered are {} and {} respectively.".format(cp,cc))