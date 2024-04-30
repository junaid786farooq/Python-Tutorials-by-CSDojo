# program to count the number of vowels (a, e, i, o, u) in a given string using a for loop.

string = input("Enter a string: ").lower()

vowels = "aeiou"

count = 0

for x in string:
    if x in vowels:
       count += 1

print("The total number of vowels in your string is:", count)