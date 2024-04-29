# program that takes a list of integers as input from the user and converts it to a string, where each integer in the list is separated by a comma, then prints the resulting string.

num_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
result = ", ".join(map(str, num_list))
print("Converted to string:", result)