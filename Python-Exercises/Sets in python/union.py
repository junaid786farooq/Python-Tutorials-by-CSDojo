# program that takes two sets as input from the user, calculates their union, and prints the result.

set_1 = set(input("Enter elements of set 1st separated by spaces: ").split())
set_2 = set(input("Enter elements of set 2nd separated by spaces: ").split())

union = set_1.union(set_2)

print(f"Intersection of:\n{set_1} U {set_2} = {union}")