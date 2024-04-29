# program that takes a dictionary as input from the user and checks if a specific key exists in the dictionary, then prints "Key found" or "Key not found" accordingly.

dict_1 = input("Enter 1st key-value pairs separated by commas (key1:value1, key2:value2...): ").split(', ')

my_dict = dict(pair.split(':') for pair in dict_1)

if "rollno" in my_dict:
    print("Key found")
else:
    print("Key not found")
    