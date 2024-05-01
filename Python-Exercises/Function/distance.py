#  function called calculate_distance that calculates the distance between two points in a two-dimensional plane. The function should take four parameters: x1, y1, x2, and y2, representing the coordinates of the two points. Include a docstring in the function to explain its purpose and usage. Test the function with different coordinate pairs.

import math

def calculate_distance(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points in a two-dimensional plane.

    Parameters:
    x1 (float): The x-coordinate of the first point.
    y1 (float): The y-coordinate of the first point.
    x2 (float): The x-coordinate of the second point.
    y2 (float): The y-coordinate of the second point.

    Returns:
    float: The Euclidean distance between the two points.
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

while True:
    try:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        break
    except ValueError:
        print("Please enter a valid numeric value!")

print(f"The distance between two points in a two-dimensional plane: {calculate_distance(x1, y1, x2, y2)}")