"""
write a program to calculate area of circle given it's radius
using the formula area = pi*r^2 (Take Pi as 3.14)

"""
import math

# Logic building formula

# Step 1 Ask for a user input and output
# We have to take r as a input from user then what will be a data type for that -- float
# can we use math function or **

# o/p will be a float with area calculated

#Step 2

# Rough logic ==  area = pi*pow(r,2)

#Step 3  Write logic

area = float(input("Enter the value of radius"))
pi=3.14

area = pi*pow(area,2)

    #or

#area = math.pi * math.pow(area,2)

print(f"Area of the circle is {area:.2f}")



