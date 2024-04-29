# program that simulates a rock-paper-scissors game against the computer, where the user inputs their choice and the computer randomly selects its choice.

import random

user_choice = input("Enter your choice (rock, paper, scissors): ")
computer_choice = random.choice(["rock", "paper", "scissors"])

print("Choice of computer:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie")
elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")