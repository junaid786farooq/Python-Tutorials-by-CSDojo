name = input("Enter your name: ").capitalize()
height_m = float(input("Enter height in meter: "))
weight_kg = float(input("Enter weight in kilograms: "))

bmi = weight_kg / height_m ** 2

print(f"{name} your BMI is {bmi}")

if bmi < 25:
    print("You are not overweight.")
else:
    print("You are overweight.")