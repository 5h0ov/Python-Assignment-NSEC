import random

natural = set(random.sample(range(1, 100), 10))
real= set(random.uniform(1.0, 100.0) for x in range(10))

common = natural & real

print("Arbitrary Natural Numbers:", natural)
print("Arbitrary Real Numbers:", real)
print("Common Numbers:", common)
