P=(float)(input("Enter the principal amount: "))
T=(float)(input("Enter the time/duration in years: "))

if(P<200000):
    I= (P*10*T)/100
elif(200000<=P<=1000000):
    I= (P*12*T)/100
else:
    I= (P*15*T)/100

print("The calculated interest is Rs.",I)