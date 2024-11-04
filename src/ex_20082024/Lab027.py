# Compare the maximum number in 3 numbers

num1 = int(input("Enter the Number 1\n"))
num2 = int(input("Enter the Number 2\n"))
num3 = int(input("Enter the Number 3\n"))

if num1 > num2 and num1 > num3:
    print("Maximum Number is ", num1)
elif num2 > num1 and num2 > num3:
    print("Maximum Number is ", num2)
else:
    print("Maximum number is ", num3)
