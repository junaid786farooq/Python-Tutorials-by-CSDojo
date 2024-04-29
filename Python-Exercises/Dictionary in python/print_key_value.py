# program that takes a dictionary as input from the user and prints the keys and values separately.

pairs = input("Enter key value pairs separated by commas (key1:value1, key2:value2...): ").split(',')

my_dict = dict(pair.split(':') for pair in pairs)

print("Keys:",my_dict.keys())
print("Values:",my_dict.values())
