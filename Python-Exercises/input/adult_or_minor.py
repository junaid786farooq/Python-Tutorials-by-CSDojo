# program that takes user input for their age and prints a message based on whether they are an adult or a minor.

user_name = input("Enter your name: ").capitalize()
user_age = int(input("Enter your age: "))

if (user_age < 18):
    print(f"{user_name} you have a minor age. ")
else:
    print(f"{user_name} you have an adult age. ")