# Input a string from the user
str = input("Enter a string: ")

cc = {}

for char in str:
    if char in cc:
        cc[char] += 1
    else:
        cc[char] = 1
print(cc)

