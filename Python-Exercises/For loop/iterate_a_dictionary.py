# program that iterates through a dictionary and prints each key-value pair.

dict_1 = input("Enter key-value pairs separated by commas (key1:value1,key2:value2...): ").split(',')

my_dict = dict(pair.split(':') for pair in dict_1)

for key, value in my_dict.items():
    print(f"KEY-{key} : VALUE-{value}")