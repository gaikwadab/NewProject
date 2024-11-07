# Different type of functions
# User Defined
# 1. The can't return -> non return
# 2.They can return something
# They have parameters
# They don't parameters / arguments

# 1: Function that can't return anything

def no_return():
    print("No value returned")


no_return()


# 2. # No Return Type and with Argument

def nrtwa(name):
    print("Hello", name)


nrtwa("Ashish")

# 3 : Function that return values
num1 = int(input("Enter the number 1"))
num2 = int(input("Enter the number 2"))


def return_value(num1, num2):
    return num1 + num2


result = return_value(num1, num2)
print("addtion is", result)
