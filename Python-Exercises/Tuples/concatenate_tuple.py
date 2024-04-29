# program that takes two tuples of integers as input from the user, concatenates them into a single tuple, then prints the concatenated tuple.

tup1 = tuple(map(int, input("Enter tuple of integers with spaces: ").split()))
tup2 = tuple(map(int, input("Enter tuple of integers with spaces: ").split()))

concatenate_tuple = tup1 + tup2

print("Concatenated Tuple:", concatenate_tuple)