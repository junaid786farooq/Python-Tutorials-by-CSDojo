# program that takes two sets as input from the user, calculates their intersection, and prints the result.

set_1 = set(input("Enter elements of set 1st separated by spaces: ").split())
set_2 = set(input("Enter elements of set 2nd separated by spaces: ").split())

intersection = set_1.intersection(set_2)

print(f"Intersection of:\n{set_1} ∩ {set_2} = {intersection}")