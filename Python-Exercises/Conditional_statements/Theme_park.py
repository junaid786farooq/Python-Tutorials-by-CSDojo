# program that calculates the cost of admission to a theme park based on the age of the visitor.

age = int(input("Please enter your age: "))

if age < 3:
    print("Admission is free.")
elif age > 3 and age <= 12:          # or 3 < age >= 12
    print("Child admission: $10")
elif age > 65:
    print("Senior admission: $15")
else:
    print("Adult admission: $20")