# find average height of students
students_height = input("input a list of student heights").split()

for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
print(students_height)

total_height = 0
for i in range(0, len(students_height)):
    total_height += students_height[i]

average_height = round(total_height/len(students_height))
print(average_height)

