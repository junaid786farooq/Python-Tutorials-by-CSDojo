# program that calculates the shipping cost based on the weight of a package and the distance to be shipped. If the weight is less than or equal to 10 kg and the distance is less than or equal to 500 km, the shipping cost is $20. If the weight is less than or equal to 20 kg and the distance is less than or equal to 1000 km, the shipping cost is $30. Otherwise, the shipping cost is $50.

weight = float(input("Enter weight of package in kilogram: "))
distance = float(input("Enter distance in kilometer: "))

if weight <= 10 and distance <= 500:
    shipping_cost = 20
elif weight <= 20 and distance <= 1000:
    shipping_cost = 30
else:
    shipping_cost = 50

print(f"Your shipping cost is {shipping_cost}$")
