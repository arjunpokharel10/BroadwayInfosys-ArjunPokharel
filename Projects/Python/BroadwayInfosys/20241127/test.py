values = []
for x in range(10):
    values.append(x)

# values = [x for x in range(10)]
print(values)


# evens = []
# for n in range(50):
#     if n % 2 == 0:
#         evens.append(n)

evens = [n for n in range(50) if n % 2 == 0]
  
print(evens)