# output = ['even' if x % 2 == 0 else 'odd' for x in range(10) if x % 3 == 0]

# print(output)





# result = {}

# for i in range(1,11):
#     if i % 2 == 0:
#         result[i] = 'even'
#     else:
#         result[i] = 'odd'



result = {i: 'even' if i % 2 == 0 else 'odd' for i in range(1,11)}
print(result)