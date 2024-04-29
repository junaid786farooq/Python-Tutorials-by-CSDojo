# program that takes a list of integers as input from the user and prints the sum of all the numbers in the list.

input_numbers = input("Enter elements separated by spaces: ")

number_list = list(map(int,input_numbers.split()))

total = 0
for x in number_list:
    total += x

print("Total of all numbers of list is:", total)