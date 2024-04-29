# program that takes a string input from the user and checks if it is a palindrome (reads the same forwards and backwards), then prints "Palindrome" or "Not a palindrome" accordingly.

string = input("Enter string: ")

reverse = string[::-1]

if string == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome.")