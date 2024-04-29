# program that determines if a given year is a leap year.

year = int(input("Enter the Year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is a leap year.")
else:
    print("This is not a leap year.")