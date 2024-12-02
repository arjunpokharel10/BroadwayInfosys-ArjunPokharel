master_pwd = input("enter a master password: ")

def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                if " | " in data:
                    try:
                        user, passw = data.split(" | ")
                        print(f"User Name: {user}| Password: {passw}")
                    except ValueError:  
                        print(f"error: line could not be split correctly: {data}")
                else:
                    print(f"invalid line format: {data}")
    except FileNotFoundError:
        print("No passwords saved yet!")

def add():
    user_name = input("enter your user name: ")
    password = input("enter your password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(user_name + " | " + password + "\n")
    print(f"Password for username {user_name} added successfully!")
        

while True:
    answer = input("do you want to view your passwords or add a new password: [view/add]").lower()
    if answer == "q":
        break
    
    if answer == "view":
        view()
    elif answer == "add":
        add()
    else:
        print("not a valid option, please enter 'view' to view your passwords or 'add' to add a password: ")