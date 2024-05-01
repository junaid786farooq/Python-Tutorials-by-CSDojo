# function called greet that takes two parameters: name (a string) and greeting (a string) with a default value of "Hello". The function should print the greeting message followed by the name. Test the function by calling it with different names and greetings.

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

name = input("Enter your name: ").capitalize()

greet(name, "Hi thanks for visiting")
greet("Junaid")
greet(name)