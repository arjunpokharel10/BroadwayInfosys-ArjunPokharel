try:
    variables = input('enter a list of integers separated by space: ')
    clean_var = sorted(list(map(int, variables.replace('and', " ").replace(',', " ").split())))
except ValueError:
    print("enter numeric values! ")

# print(variables, clean_var)   # for testing purposes only

print(f"largest: {clean_var[-1]}\nsmallest: {clean_var[0]}")

unique_values = (list(set(clean_var)))
unique_values = sorted(unique_values,reverse=True)

print(unique_values)


# map(int, expression)
# a_list = ['15', '32', '67', '24']
# b_list = list(map(int, a_list))
# does the same thing as this below:
# b_list = int(i) for i in a_list
