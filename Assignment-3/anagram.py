st1 = input("Enter the first string: ")
st2 = input("Enter the second string: ")

anagram = sorted(st1.lower()) == sorted(st2.lower())   # if sorted strings are same then obviously the combinations will be same hence anagrams

if anagram:
    print("The given strings are Anagrams.")
else:
    print("The given strings are not Anagrams.")