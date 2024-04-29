# program that takes a string input from the user containing a list of numbers separated by commas (e.g., "1, 2, 3") and converts it to a list of integers, then prints the list.

string = input("Enter a list of numbers separated by commas: ")

num_list = [int(x.strip()) for x in string.split(",")]

print("Converts it to a list of integers:",num_list)