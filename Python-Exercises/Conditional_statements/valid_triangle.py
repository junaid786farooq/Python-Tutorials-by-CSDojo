# program that prompts the user to enter three sides of a triangle and checks if it is a valid triangle, where the sum of the lengths of any two sides must be greater than the length of the third side.

side1 = float(input("Enter length of first side: "))
side2 = float(input("Enter length of second side: "))
side3 = float(input("Enter length of third side: "))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("Valid triangle")
else:
    print("Invalid triangle.")

