# program that takes a set as input from the user and calculates its length, then prints the length of the set.

set = set(input("Enter elements of set separated by spaces: ").split())

length = len(set)

print("The length of set is:", length)