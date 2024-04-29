# program that takes two lists of integers as input from the user and concatenates them into a single list, then prints the concatenated list.

lst1 = input("Enter first list of number separated by spaces: ")
lst2 = input("Enter first second of number separated by spaces: ")

int_list1 = list(map(int, lst1.split()))
int_list2 = list(map(int, lst2.split()))

concate_lists = int_list1 + int_list2

print("Concatenated lists:", concate_lists)