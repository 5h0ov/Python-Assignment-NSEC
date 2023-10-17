# Input the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Use filter with a lambda function to find numbers divisible by 5 and 7
divisible = list(filter(lambda x: x % 5 == 0 and x % 7 == 0, range(start, end + 1)))

# Print the numbers divisible by 5 and 7
print("Numbers divisible by 5 and 7 in the range:", divisible)
