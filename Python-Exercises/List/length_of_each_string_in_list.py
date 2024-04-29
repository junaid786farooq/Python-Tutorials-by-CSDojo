# program that takes a list of strings as input from the user and prints the length of each string in the list.

string_list = input("Enter a list of strings sparated by a spaces: ").split()

lengths = [len(s) for s in string_list]

print(lengths)