# Program that calculates the volume of a cylinder using variables for the radius and height.

import math

radius = float(input("Enter the radius of cylinder "))
height = float(input("Enter the height of cylinder "))

volume_of_cylinder = math.pi * (radius ** 2) * height

print("The volume of cylinder is: ", volume_of_cylinder)
