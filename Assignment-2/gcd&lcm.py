a=(int)(input("Enter value of first number(a): "))
b=(int)(input("Enter value of second number(b): "))
m=a;
n=b;

while(m!=n):
    if(m>n):
        m=m-n;
    else:
        n=n-m;

lcm=(int)((a*b)/n)

print("The GCD and LCM of a and b is {} and {} respectively.".format(n,lcm))