#topic for the day: list, set, dictionery, and tuples
# two major difference:
# list is a mutable data type - []
# but tuple is immutable data type - ()
# list is always slower than tuple: why? because immutable data types are usually faster than mutable data types

# cities = ['kathmandu', 'bhaktapur', 'chitwan', 'biratnager']
# cities.append('sunsari')
# print(cities)

# countries = ('nepal', 'australia', 'united states', 'germany', 'switzerland')
# print(countries[-1])

# set does not support indexing, i.e. it stores elements in unordered way. 
#

#################################################################################################
numbers = [1, 2, 3, 4, 2, 3, 2, 4, 7, 5 , 5, 7, 8, 4, 6, 3, 3, 6, 8, 9, 3, 4]

numbers = list(set(numbers))
print(numbers)

#approach 2

numbers_1 = [1, 2, 3, 4, 2, 3, 2, 4, 7, 5 , 5, 7, 8, 4, 6, 3, 3, 6, 8, 9, 3, 4]
new_list = []

for i in numbers_1:
    if i not in new_list:
        new_list.append(i)

print(new_list)

#################################################################################################

#DICTIONERY

personal_details = {
    'name': 'arjun',
    'address': 'bharatpur',
    'hobby': ['coding', 'driving', 'music'],
    'gender': 'male',
    'is_nepali': True,
    'job': None,
    'motercycle': 0 
}

print(f"my name is {personal_details['name']} and i am a {personal_details['gender']} and {'nepali' if personal_details['is_nepali'] else 'not nepali'}, i live in {personal_details['address']}. i love {personal_details['hobby'][0]}. my job is {personal_details['job']}. i also have {personal_details['motercycle']} motercycles.")


# what data types can be keys in a dictionery
# another method to access values: personal_details.get('name')