# create a tuple after taking integers as input from user
store_in_tuples = input("enter some numbers, separeted by spaces: ")
store_in_tuples = tuple(map(int, store_in_tuples.replace(',',' ').replace('and',' ').split()))

print(store_in_tuples)

# convert the tuple to a list and add an element
store_in_tuples = list(store_in_tuples)
store_in_tuples.append(33)
print(store_in_tuples)


'''
map(int, expression) can be re-written as:
store_in_tuples = tuple(int(_) for _ in store_in_tuples.split())
'''

