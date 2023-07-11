# You are going calculate average of student height from a List of heights.

# student_heights = input("Input a list of student heights. ").split()
#
# for i in range(0, len(student_heights)):
#     student_heights = int(student_heights[i])
# print(student_heights)

student_heights = [123, 187, 178, 145, 156,162]

sum_of_heights = 0
for height in student_heights:
    sum_of_heights += height

print(f"Sum of all the heights of students is : {sum_of_heights}")

student_count = 0

for student in student_heights:
    student_count += 1

print(f"Num of students is list are : {student_count}")

average = round(sum_of_heights / student_count)

print(average)
