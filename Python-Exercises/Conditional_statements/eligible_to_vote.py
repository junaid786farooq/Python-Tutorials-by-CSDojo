# program that prompts the user to enter their age and checks if they are eligible to vote. If they are 18 or older, the program should ask if they are registered voters. If they are registered, it should print "You are eligible to vote." If they are not registered, it should print "Please register to vote."

age = float(input("Please enter your age: "))

if age >= 18:
    registered = input("You are registered vote (yes/no): ").lower()
    if registered == "yes":
        print("You are eligible to vote.")
    else:
        print("Please register to vote.")
else:
    print("You are not eligible to vote.")
