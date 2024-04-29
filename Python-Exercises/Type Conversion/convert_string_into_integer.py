# program that takes a string input from the user and converts it to an integer, then prints the result. Handle the case where the input string is not a valid integer.

num_str = input("Enter a number: ")

try:
    num = int(num_str)
    print("Converted to integer:", num)
except Exception as e:
    print("Some error occurred:", e)