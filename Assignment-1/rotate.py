x = (int)(input("Enter first number: "))
y = (int)(input("Enter second number: "))
z = (int)(input("Enter third number: "))

c= x+y+z;
z= c-(z+y);
y= c-(y+x);
x= c-(z+y);

print("The swapped numbers are",x,",",y,"and",z)