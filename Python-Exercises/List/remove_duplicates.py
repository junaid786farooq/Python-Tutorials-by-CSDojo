# program that takes a list of numbers as input from the user and removes all duplicates from the list, then prints the modified list.

lst = [int(x) for x in input("Enter numbers with spaces: ").split()]

modified_list = []

for num in lst:
    if num not in modified_list:
        modified_list.append(num)

print("Modified list is:", modified_list)

