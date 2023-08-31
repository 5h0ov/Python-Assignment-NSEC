lst=  ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
m=["h","i","j"]

lst[2][1][2].extend(m)

print("The required modified list: ",lst)