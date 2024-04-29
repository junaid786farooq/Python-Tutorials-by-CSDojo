# program that determines if a triangle is equilateral, isosceles, or scalene based on the lengths of its sides.

side1 = float(input("Enter length of first side: "))
side2 = float(input("Enter length of second side: "))
side3 = float(input("Enter length of third side: "))

if (side1 == side2 == side3):
    print("This is an equilateral triangle.")
elif (side1 == side2 or side1 == side3 or side2 == side3):
    print("Isosceles triangle")
else:
    print("Scalene Triangle")