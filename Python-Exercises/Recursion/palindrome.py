# a recursive function called is_palindrome that checks whether a given string is a palindrome (reads the same forwards and backwards). Test the function with different strings.

def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1: -1])
    
string = input("Enter a string for checking palindrome: ")

print(f"Is {string} a palindrome? {is_palindrome(string)}")