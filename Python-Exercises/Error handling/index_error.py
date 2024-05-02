# program that tries to access the third element of a list containing only two elements. Implement error handling to catch the IndexError and print a message to the user.

lst = [4, 8, 1]

try:
    third_element= lst[3]
    print("Third element of list is: ", third_element)
except IndexError:
    print("Error: Index out of range..!")