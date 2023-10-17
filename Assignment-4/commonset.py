import random

# Create two sets of 10 arbitrary natural numbers
nset1 = set({2, 4, 6, 8, 10, 12, 14, 16, 18, 20})
nset2 = set({5, 10, 15, 20, 25, 30, 35, 40, 45, 50})

# Create two sets of 10 arbitrary real numbers
rset1 = set({1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.1})
rset2 = set({4.3, 4.6, 10.5, 6.6, 7.7, 10.8, 0.9, 10.1, 11.1, 12.1})

# Find the common numbers
common_natural = nset1.intersection(nset2)
common_real = rset1.intersection(rset2)

print("Common Natural Numbers:", common_natural)
print("Common Real Numbers:", common_real)
