# BIM Calculator Function

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / height_m ** 2
    print(f"{name} your BMI is {bmi}")
    if bmi < 25:
        print("You are not overweight.")
    else:
        print("You are overweight.")


bmi_calculator("Junaid", 2, 67)
bmi_calculator("Usman", 2, 110)
bmi_calculator("Mudasir", 2.3, 69)