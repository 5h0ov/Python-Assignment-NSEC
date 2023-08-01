import math
print("\nA quadratic eqn looks like this: a*(x^2) + b*x + c = 0\n")
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Calculate the discriminant
d = b**2 - 4*a*c

if d > 0:
    # Real and distinct roots
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Real and distinct roots: {}, {}".format(root1, root2))
elif d == 0:
    # Real and equal roots
    root = -b / (2*a)
    print("Real and equal roots: {}".format(root))
else:
    # Complex roots
    real = -b / (2*a)
    imagine = math.sqrt(abs(d)) / (2*a)
    print("Complex roots: {} + {}j, {} - {}j".format(real, imagine, real, imagine))
