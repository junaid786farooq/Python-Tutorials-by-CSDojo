#  program that takes a string input from the user and counts the number of vowels (a, e, i, o, u) in the string, then prints the count.

count = 0
string = input("Enter string: ").lower()

for x in string:
    if x.lower() in "aeiou":
        count += 1

print("The number of vowels in given string is:", count)