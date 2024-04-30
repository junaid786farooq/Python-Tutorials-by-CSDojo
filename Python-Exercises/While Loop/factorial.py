# program to find the factorial of a given number using a while loop.

num = int(input("Enter number for fectorial: "))
fact = 1
while num > 0:
    fact *= num
    num -= 1 
print("Factorial:", fact)

