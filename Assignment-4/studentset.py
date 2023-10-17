cultural_committee = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Isabel", "Jack"}
sports_committee = {"David", "Eve", "Frank", "George", "Hannah", "Isabel", "John", "Katie", "Liam", "Mary"}

not_common = cultural_committee.symmetric_difference(sports_committee)

print("Students not common in both committees:")
for student in not_common:
    print(student,end=" ")
