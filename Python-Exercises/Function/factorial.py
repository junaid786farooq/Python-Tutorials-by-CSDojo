# function to find factorial

def factorial(num):
    if num == 1 or num == 0:
        return 1
    elif num < 0:
        return "Number must be non-negative."
    else:
        return num * factorial(num - 1)
    
while True:
    try:
        num = float(input("Enter number for factorial: "))
        break
    except ValueError:
        print("please enter numeric value.")

result = factorial(num)
print(result)
