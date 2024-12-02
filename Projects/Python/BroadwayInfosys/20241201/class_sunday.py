# functions
# everyone can write a function, but only a good programmer write a really good function. what are those principles that make you a great programmer? 
# function is a block of (reusable) code that performs a specific task. 

# example:

def greet_user():       # function defination
    print("hello user") # block of code

greet_user()            # function call


# passing argument

def greet_users(name):
    print(f"hello, {name}!")

name = "arjun"
greet_users(name)


def greet_username(name, address):
    count = 0
    while count < 3:
        print(f"hello {name} from {address}!")
        count += 1

greet_username("arjun", "bharatpur")    #this way of passing argument is called positional argument

def grt_urname(name, address):
    for _ in range(3):
        print(f"hello {name} from {address}!")

grt_urname(address='sydney', name='bhadra') # this way of explicitly passing arguments is called keyword argument, positions don't matter in this explicit way of passing arguments





