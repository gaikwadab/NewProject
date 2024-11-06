# Program to find a leap year

year = int(input("Enter the year you want to check\n"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is Leap year")
else:
    print(f"{year} is Not a leap year")
