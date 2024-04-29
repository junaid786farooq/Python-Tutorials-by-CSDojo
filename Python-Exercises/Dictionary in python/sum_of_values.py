# program that takes a dictionary as input from the user and calculates the sum of all the values in the dictionary, then prints the sum.

# Example input: {"a": 10, "b": 20, "c": 30}
dict_1 = eval(input("Enter 1st key-value pairs separated by commas ('key1':value1, 'key2':value2...): "))

# Make sure the values are numerical
if all(isinstance(value, (int, float)) for value in dict_1.values()):
    sum_values = sum(dict_1.values())
    print("Sum of values:", sum_values)
else:
    print("Please ensure that all values in dictionary are numerical.")
