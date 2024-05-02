# program that takes two numbers as input from the user and calculates their quotient. Implement error handling to catch the ZeroDivisionError if the second number is zero and print a message to the user.

while True:
    try:
        num1 = float(input("Enter nominator: "))
        num2 = float(input("Enter denominator: "))
        if isinstance(num1, (int,float)) and isinstance(num2, (int,float)):
            if num2 == 0:
                raise ZeroDivisionError("Error: Division by zero is not allowed!")
            else:
                quotient = num1 / num2
                print("Quotient:", quotient)
        else:
            print("Valueerror...:)")
        break
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    except ValueError:
        print("Value Error: Please enter numeric values!")