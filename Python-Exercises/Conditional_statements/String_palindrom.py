# program that determines if a given string is a palindrome.

string = input("Enter a string: ")

if (string == string[::-1]):          # For reversing a string
    print("String is a palindrom.")
else:
    print("String is not palindrom.")