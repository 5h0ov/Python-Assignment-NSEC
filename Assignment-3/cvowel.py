st=input("Enter a sentence: ")
c=0
for i in st.lower():
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        c+=1

print("The number of vowels present in that sentence is",c)