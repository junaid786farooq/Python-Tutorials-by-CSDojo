# program that takes a set as input from the user and checks if it is a subset of another set provided by the user, then prints "Subset" or "Not a subset" accordingly.

set1 = set(input("Enter elements of set 1 separated with spaces: ").split())
set2 = set(input("Enter elements of set 2 separated with spaces: ").split())

if set1.issubset(set2):
    print("First set is the subset of second set.")
else:
    print("First set is not subset of second set.")


