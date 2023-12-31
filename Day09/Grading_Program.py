# Calculating grade by using and manipulating dictionary

student_scores = {"Harry" : 81,
                  "Ron" : 78,
                  "Hermoine" : 99,
                  "David" : 74,
                  "Alister" : 100}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "EE"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
