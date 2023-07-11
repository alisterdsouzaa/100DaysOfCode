student_scores = input("Input a list of student score : ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
 
# Find the highest score from the list

highest_score = 0;
for score in student_scores:
    if highest_score < score:
        highest_score = score
    # else:
    #     highest_score = highest_score

print(f"Highest Score is : {highest_score} ")
