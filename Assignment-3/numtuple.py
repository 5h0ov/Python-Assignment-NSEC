temp = input("Enter comma-separated numbers: ")
tup = tuple(int(x) for x in temp.split(','))

print("The Tuple:", tup)
