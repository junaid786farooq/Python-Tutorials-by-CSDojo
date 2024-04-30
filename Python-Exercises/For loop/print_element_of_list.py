# program using a for loop to print the elements of a list.

lst = [x for x in input("Enter elements of list: ").split()]

print("The element of list is:")
for element in lst:
    print(element)