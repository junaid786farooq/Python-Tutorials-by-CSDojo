#  function named power that takes two parameters, base and exponent, and returns the result of raising base to the power of exponent. Test the function with base = 2 and exponent = 3.

def power(base, exponent):
    if exponent < 0:
        return "Exponent must be non_negative."
    elif base == 0 and exponent == 0:
        return "Result is undefined (0^0)."
    else:
        return base ** exponent

while True:
   try:
        base = float(input("Enter base: "))
        exponent = float(input("Enter exponent: "))
        break
   except ValueError:
        print("Please enter numeric values.")

    
result = power(base, exponent)

print(f"Result: {result}")