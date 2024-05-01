# function called describe_pet that takes two parameters: animal_type and pet_name. Make animal_type a positional parameter and pet_name a keyword parameter with a default value of "Unknown". The function should print a sentence describing the pet, such as "My dog's name is Spot." or "I have an unknown pet." Test the function by calling it with different combinations of arguments.

def describe_pet(animal_type, pet_name = 'Unknown'):
    if pet_name == 'Unknown':
        print(f"I have an unknown {animal_type} pet.")
    else:
        print(f"My {animal_type}'s name is {pet_name}.")


animal_type = input("Enter the type of animal do you have: ")

pet_name = input("Enter the name of your pet (press 'n' for unknown): ").lower()
if pet_name == "n":
    pet_name = 'Unknown'

describe_pet(animal_type, pet_name)
