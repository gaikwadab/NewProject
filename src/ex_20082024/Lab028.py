# Grade Calculator
# Write a program to calculate your grade upon the your percentage

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# E: 50-59
# F: 40-49

Grade = int(input("Enter your percentage"))

if Grade >= 90 and Grade<=100:  # if 90 <= Grade <= 100:
    print("You scored A grade")

elif Grade >= 80 and Grade<=89:  # if 80 <= Grade <= 89
    print("You scored B grade")

elif Grade >= 70 and Grade<=79:  # if 70 <= Grade <= 79
    print("You scored C grade")

elif Grade >= 60 and Grade <= 69:
    print("You scored D grade")

elif Grade >= 50 and Grade<=59:
    print("You scored D grade")

elif Grade > 100:
    print("You are Fool ")
else:
    print("You are fail")

