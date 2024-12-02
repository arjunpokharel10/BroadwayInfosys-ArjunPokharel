#assignment: ask users to input a password, and rate the password strong, weak etc. based on length, and capital letters. 

user_pw = input("create a strong password: ")
score = 0
pw_len = len(user_pw)
pw_upp = 0
for i in user_pw:
    if i.isupper():
        pw_upp += 1

#pw_upper = sum(1 for i in user_pw if i.isupper()) #this makes use of list comprehension, this is more pythonic. 

if pw_len >=8:
    count = pw_len - 8
    count += pw_upp
else:
    count = pw_upp

if count > 9:
    print("you are a superhuman!")
elif count > 5:
    print("your password is strong")
else:
    print("your passwword is weak")
