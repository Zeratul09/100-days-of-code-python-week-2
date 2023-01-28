student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

#Grading

for student in student_scores.items():
    if student[1] >= 91:
        student_grades[student[0]] = "Outstanding"
    elif student[1] >= 81:
        student_grades[student[0]] = "Exceeds Expectations"
    elif student[1] >= 71:
        student_grades[student[0]] = "Acceptable"
    elif student[1] <= 70:
        student_grades[student[0]] = "Fail"

#print(student_grades)


# 🚨 Don't change the code below 👇
print(student_grades)


#This is the scoring criteria:

    # Scores 91 - 100: Grade = "Outstanding"

    # Scores 81 - 90: Grade = "Exceeds Expectations"

    # Scores 71 - 80: Grade = "Acceptable"

    # Scores 70 or lower: Grade = "Fail"
