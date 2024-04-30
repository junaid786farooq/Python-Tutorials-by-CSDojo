# program that prints a multiplication table (up to 10) using nested for loops.

number = int(input("Enter number for table: "))

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")


"""
for i in range(1, 11):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
"""