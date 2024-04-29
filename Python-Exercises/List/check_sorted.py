# program that takes a list of integers as input from the user and checks if the list is sorted in non-decreasing order, then prints "Sorted" or "Not sorted" accordingly.

num_list = [int(x) for x in input("Enter numbers with spaces: ").split()]

sorted_list = True

for i in range(len(num_list) - 1):
    if num_list[i] > num_list[i + 1]:
        sorted_list = False
        break

if sorted_list:
    print("Sorted")
else:
    print("Not Sorted")
