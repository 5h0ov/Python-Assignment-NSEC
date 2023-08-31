st=input("Enter a sentence: ")
word = input("Enter the word to count: ")

count = st.split().count(word)

print("The given word appears {} time(s) in the given sentence.".format(count))