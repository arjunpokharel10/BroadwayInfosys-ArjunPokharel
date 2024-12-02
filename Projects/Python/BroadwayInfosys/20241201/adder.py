
def adder(var_a, var_b):
    sum = var_a + var_b
    return sum



try:
    num1 = int(input("enter a number: "))
except ValueError:
    print("enter a valid numeric input as your first number: ")

try:
    num2 = int(input("enter another number: "))
except ValueError:
    print("enter a valid numeric input as your first number: ")

print(f"the sum of {num1} and {num2} is {adder(num1, num2)}")