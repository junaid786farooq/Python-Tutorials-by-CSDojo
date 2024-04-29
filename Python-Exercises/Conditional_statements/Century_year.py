# program that determines if a given year is a century year (ending in 00) and if it is a leap year.

year = int(input("Enter the year: "))

if (year % 100 == 0):
    if (year % 400 == 0):
        print("Century year and leap year.")
    else:
        print("century year but not a Leap year.")
else:
    print("Not a century year.")