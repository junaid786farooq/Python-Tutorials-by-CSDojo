# program that takes key-value pairs as input from the user and creates a dictionary, then prints the dictionary.

pairs = input("Enter key-value pairs separated by commas (key1:value1, key2:value2, ...): ").split(',')

my_dict = dict(pair.split(':') for pair in pairs)

print(my_dict)