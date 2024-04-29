# program that takes a tuple of strings as input from the user and prints the length of each string in the tuple.

string_tuple = tuple(input("Enter a tuple of string separated by spaces: ").split())

lengths = [len(s) for s in string_tuple]

print("Length of each string in tuple is:", lengths)