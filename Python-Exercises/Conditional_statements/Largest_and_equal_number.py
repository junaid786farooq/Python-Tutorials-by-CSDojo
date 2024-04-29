# program that asks the user to enter three integers and determines the largest among them. However, if two or more numbers are equal and larger than the third, print "Two or more numbers are equal and larger than the third."

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 == num2 == num3:
    print("All numbers are equal.")
else:
    largest = max(num1, num2, num3)
    if (num1 == num2 == largest) or (num1 == num3 == largest) or (num2 == num3 == largest):
        print("Two or more numbers are equal and larger than the third.")
    else:
        print("Largest number:", largest)
