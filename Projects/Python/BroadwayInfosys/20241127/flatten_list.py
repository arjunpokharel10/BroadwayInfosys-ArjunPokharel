matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]


# flattened = []

# for m in matrix:
#     for i in m:
#         flattened.append(i)

flattened = [i for m in matrix for i in m]


print(flattened)