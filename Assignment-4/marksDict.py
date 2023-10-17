# Create an empty dictionary for marks
marksDict = {'English': 0, 'Physics': 0, 'Math': 0, 'Chemistry': 0, 'History': 0}

# Input marks for each subject
for subject in marksDict:
    marks = int(input("Enter marks for {}: ".format(subject)))
    marksDict[subject] = marks

# Find the subject with the highest score
best_subject = max(marksDict, key=lambda key:marksDict[key])
best_score = marksDict[best_subject]

# Find the subject with the lowest score
worst_subject = min(marksDict, key=lambda key:marksDict[key])
worst_score = marksDict[worst_subject]

# Print the results
print(f"Best subject: {best_subject} with a score of {best_score}")
print(f"Worst subject: {worst_subject} with a score of {worst_score}")
