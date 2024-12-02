
name = input("enter your name: ")
address = input("enter you address: ")
hobbies = input ('enter your hobbies separated by spaces: ')

person_detail = {
    'name' : ' '.join(name.title().split()),
    'address' : ' '.join(address.replace('-',' ').title().split()),
    'hobbies' : list(set(hobbies.replace(',',' ').replace('and',' ').split())), #wrapped within set() to remove duplicate entries
}

print("you are a boring man" if not person_detail['hobbies'] else f"your hobbies are {', '.join(person_detail['hobbies'][:-1])}, and {person_detail['hobbies'][-1]}")


#print(person_detail)





















