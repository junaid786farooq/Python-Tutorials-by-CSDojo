# program that continuously prompts the user to enter a number until they enter 0. After each input, print the square of the number.

while True:
    num = int(input("Enter number for square: "))
    if num != 0:
        square = num**2
        print("Square:", square)
    if num == 0:
       break

# OR
# while True:
#     num = int(input("Enter a number (0 to exit): "))
#     if num == 0:
#         break
#     print("Square:", num ** 2)    