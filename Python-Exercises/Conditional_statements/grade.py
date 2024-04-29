# Program that determines the grade (A, B, C, D, or F) based on a student's score.

marks = int(input("Enter the marks of student: "))

if (90 <= marks <=100):
    print("Grade = 'A'")
elif (90 > marks >= 80):
    print("Grade = 'B'")
elif (80 > marks >= 70):
    print("Grade = 'C'")
elif (70 > marks >= 50):
    print("Grade = 'D'")
else:
    print("Grade = 'F'")