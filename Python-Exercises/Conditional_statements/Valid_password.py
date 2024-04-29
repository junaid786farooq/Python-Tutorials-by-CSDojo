# program that checks if a given string is a valid password, which must contain at least 8 characters, including at least one uppercase letter, one lowercase letter, one digit, and one special character (!@#$%^&*).

import re

password = input("Enter password: ")

if (len(password) >= 8) and (re.search("[A-Z]", password)) and \
    (re.search("[A-Z]", password)) and (re.search("[a-z]", password))and \
    (re.search("[1-9]", password)) and (re.search("[!@#$%^&*]", password)):
    print("A Valid Password")
else:
    print("Not a valid password")
