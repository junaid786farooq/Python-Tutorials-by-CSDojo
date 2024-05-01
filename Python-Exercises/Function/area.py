# Define a function called calculate_area that takes two parameters length and width and returns the area of a rectangle. Test the function with length = 5 and width = 10.

def calculate_area(length, width):
    return length * width

length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))

area = calculate_area(length, width)


print("The area of rectangle is:", area)