try:
    x = int(input("enter a number: "))
    y = int(input("enter another number: "))
    z = x / y
except ZeroDivisionError:
    print("you cannot divide by zero")
