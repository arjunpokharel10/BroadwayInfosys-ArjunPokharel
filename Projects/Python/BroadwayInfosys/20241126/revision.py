# this program is to get user to guess a number between two values

#first import random
#store a randome value to a variable
#get user to guess the number
    #user gets 5 chances, there's reward based on what how many tries it takes them to guess the number correctly



#condition to check if the value matches the random number, maybe while loop: initiate a counter variable? 


import random

count = 0
rem_count = 0
rand_num = random.randint(1,10)

print(rand_num)

reward_dict = {1:'100%',2: '90%', 3: '70%', 4: '50%', 5:'32%'}

while count < 5:

    guess_num = input("guess a number between 1 and 10: ")
    count += 1
    rem_count = 5 - count

    if not guess_num.isnumeric():
        print(f"{guess_num} is not a valid input, try again and guess a number")
        continue
    
    guess_num = int(guess_num)

    if guess_num == rand_num:
        print(f"correct, you guessed it in {count} {'try' if count==0 else 'tries'}, congratulations! and you get {reward_dict[count]}.")
        break
    else:
        if count == 5:
            print(f"you are out of luck, and guesses! the correct number was {rand_num}, better luck next time!")
        else:
            print(f"think {'smaller' if guess_num > rand_num else 'larger'} than than that, try again. you have {rem_count} {'try' if rem_count == 1 else 'tries'} left!")
        
        


