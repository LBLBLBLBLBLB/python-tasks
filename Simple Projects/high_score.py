# find a max number in list without max function
students_scores = input("input a list of student scores").split()

for n in range(0, len(students_scores)):
    students_scores[n] = int(students_scores[n])
print(students_scores)

# without max func
max_score = 0
for i in range(0, len(students_scores)):

    if max_score < students_scores[i]:
        max_score = students_scores[i]

print(max_score)