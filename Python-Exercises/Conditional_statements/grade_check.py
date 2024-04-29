# program that checks if a student's grade is passing (>=60) or failing (<60).

student_grade = int(input("Enter your grade: "))

if (student_grade >= 60 and student_grade < 100):
    print("Congraduations You are passed.")
elif (student_grade < 60 and student_grade >= 0):
    print("You are fail.")
else:
    print("Please enter a valid input.")
    