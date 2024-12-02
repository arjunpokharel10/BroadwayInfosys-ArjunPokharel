user = {}

user.update({'name': ' '.join(input("enter your name: ").title().split())})
user.update({'address': ''.join(input("enter you address: ").replace('-',' ').split())})
user.update({'hobbies': input("enter your hobbies separated by spaces: ").split()})

print(user)

if not user['hobbies']:
    print("you are a boring person!")
