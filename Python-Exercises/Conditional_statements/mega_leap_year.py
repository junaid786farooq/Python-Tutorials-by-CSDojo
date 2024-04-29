# program that determines if a given year is a "mega leap year," which occurs if the year is divisible by 4000 or is a leap year divisible by 400 but not divisible by 200.

year = int(input("Enter the year: "))

if (year % 4000 == 0) or (year % 400 == 0 and year % 200 != 0):
    print("Mega leap Year")
else:
    print("Not a mega leap year.")
