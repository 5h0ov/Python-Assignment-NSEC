st=input("Enter a string: ")
lch=st[-1]

st = st.replace(lch,'*')
st1 = st[0:-1]+lch

print("The required edited string is:",st1)

