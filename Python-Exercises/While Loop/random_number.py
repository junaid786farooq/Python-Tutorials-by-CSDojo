# program that simulates a simple guessing game. Generate a random number between 1 and 100, then prompt the user to guess the number. Continue prompting the user for guesses until they correctly guess the number. Display the number of attempts it took to guess correctly at the end.

import random

random_number = random.randint(1,100)

while True:
    user_number = int(input("Guess the number...: "))
    if user_number == random_number:
        break
    elif user_number < random_number:
        print("Your number is too low! Try again.")
    else:
        print("Your number is too high! Try again.")


print(f"You Won!.. Congratulations on your success!...")