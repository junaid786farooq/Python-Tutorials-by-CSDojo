# <var> = (false_val, true_val) [<condition>]

age = int(input("Enter your age: "))

vote = ("No", "Yes") [age >= 18]
print(vote)

salary = float(input("Enter your salary: "))

tax = salary * (0.2, 0.1) [salary <= 50000]
print(tax)