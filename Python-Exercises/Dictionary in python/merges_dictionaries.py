# program that takes two dictionaries as input from the user, merges them into a single dictionary, and then prints the merged dictionary.

dict_1 = input("Enter 1st key-value pairs separated by commas (key1:value1, key2:value2...): ").split(',')
dict_2 = input("Enter 2nd key-value pairs separated by commas (key1:value1, key2:value2...): ").split(',')

my_dict_1 = dict(pair1.split(':') for pair1 in dict_1) 
my_dict_2 = dict(pair2.split(':') for pair2 in dict_2) 

my_dict_1.update(my_dict_2)

print(my_dict_1)

# OR

# dict1 = eval(input("Enter the first dictionary (in the format {key1: value1, key2: value2, ...}): "))
# dict2 = eval(input("Enter the second dictionary (in the format {key1: value1, key2: value2, ...}): "))
# merged_dict = {**dict1, **dict2}
# print("Merged dictionary:", merged_dict)