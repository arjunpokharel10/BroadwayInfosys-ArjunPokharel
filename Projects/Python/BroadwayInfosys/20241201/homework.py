
def num_input():
    while True:
        try:
            num_a = int(input("enter a number: "))
            num_b = int(input("enter another number: "))
            return num_a, num_b
        except ValueError:
            print("try again, please enter valid numeric values!")

def plus(num1 = 1, num2 = 1):
    return (num1 + num2)

def minus(num1 = 1, num2 = 1):
    return (num1 - num2)

def multiply(num1 = 1, num2 = 1):
    return (num1 * num2)

def divide(num1 = 1, num2 = 1):
    return (num1 / num2)

num1, num2 = num_input()

add = plus(num1, num2)
sub = minus(num1, num2)
prod = multiply(num1, num2)
divi = divide(num1, num2)

print(f"sum: {add}\ndifference: {sub}\nproduct: {prod}\ndivide: {divi}\n")