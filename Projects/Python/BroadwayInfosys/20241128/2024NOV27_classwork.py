# simple program to take personal attributes as user inputs, store it in a dictionary, and return a response based on one of the attribues

name = input('enter your name: \n')
address = input('enter your address: \n')
hobbies = input('enter your hobbies [separated by space]: \n')

# storing the cleaned version of the personal attributes collected in the three variables above into a dictionary. 
personal_attributes = {
    'name': ' '.join(name.title().split()),
    'address': ' '.join(address.title().replace('-', ' ').split()),
    'hobbies': list(set(hobbies.replace(',',' ').replace('and',' ').split()))   #use of set function to remove duplicate entries
}

print("you are a boring man!" if not hobbies else f"your hobbies are {', '.join(personal_attributes['hobbies'][:-1])}, and {personal_attributes['hobbies'][-1]}. \n")

