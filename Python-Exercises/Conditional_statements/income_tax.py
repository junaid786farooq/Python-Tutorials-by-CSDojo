#  program that calculates the tax amount for a given income based on the progressive tax brackets: 10% for income up to $10,000, 15% for income up to $20,000, and 20% for income above $20,000.

income = float(input("Please enter your income $: "))

if income <= 10000:
    tax = 0.1 * income
elif (income <= 20000):
    tax = (0.1 * 10000) + (0.15 * (income - 10000))
else:
    tax = (0.1 * 10000) + (0.15 * 10000) + (0.2 * (income - 20000))

print("Tax amount:", tax)
