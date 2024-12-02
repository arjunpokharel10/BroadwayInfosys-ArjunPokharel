import random

rand_num = random.randint(1, 10)
count = 0
percent_dict = {1: '100%', 2: '90%', 3: '70%', 4: '50%', 5: '32%'}

while count < 5:
    gues_num = input("Guess a number between 1 and 10: ")

    # Validate input #comment by arjun: learn this, why is there if not expression and then continue?? this is confusing. 
    if not gues_num.isnumeric():
        print("Invalid input. Please enter a valid number.")
        continue

    gues_num = int(gues_num)
    count += 1

    if gues_num == rand_num:
        print(f"Congratulations! You guessed it in {count} tries. You get {percent_dict[count]}. Well done!")
        break
    else:
        remaining_tries = 5 - count
        if remaining_tries == 0:
            print(f"You're out of guesses! The correct number was {rand_num}. Better luck next time!")
        else:
            print(f"Wrong guess! You have {remaining_tries} {'try' if remaining_tries == 1 else 'tries'} left. Try again!") 
            # in this expression, learn the if ... == b else ... // one line if else condition. 
