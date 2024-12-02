def user_inputs():
    while True:
        try:
            num_a = int(input("enter a number: "))
            num_b = int(input("enter another number: "))
            break
        except ValueError:
            print("enter numeric values!")
    return num_a, num_b

        
def calculator(var_a, var_b):
    addition = var_a + var_b
    difference = var_a - var_b
    product = var_a * var_b
    division = var_a / var_b
    return addition, difference, product, division


num1, num2 = user_inputs()

result = calculator(num1,num2)
result = {
    'sum': result[0],
    'difference': result[1],
    'product': result[2],
    'division': result[3]
}
print(result)
