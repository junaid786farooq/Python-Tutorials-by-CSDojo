# program that takes a tuple of numbers as input from the user and calculates the sum of all the numbers in the tuple, then prints the sum.

tup = tuple(map(int, input("Enter numbers in spaces: ").split()))

sum_of_num = 0

for x in tup:
    sum_of_num += x

# sum_of_num = sum(tup)

print("Sum of all the numbers in tuple is:", sum_of_num)
