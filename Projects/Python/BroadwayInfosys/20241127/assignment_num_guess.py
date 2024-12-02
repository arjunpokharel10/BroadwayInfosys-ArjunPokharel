import random

attempts = 5
range = [1, 10]
percentage = {1: '100%', 2: '90%', 3: '70%', 4: '50%', 5: '60%'}
guess_count = 0
remaining_guess_count = attempts - guess_count

rand_num = random.randint(range[0], range[1])

while guess_count < 5:
    guess_num = input('guess a number: ')
    if not guess_num.isnumeric():           #this is to check if the input is numeric before converting to integer. 
        print(f"{guess_num} is not a valid input, please enter an integer!")
        continue
    guess_num = int(guess_num)              #converts the numeric string into integer. 

    if guess_num == rand_num:
        print(f"correct, you guessed it in {guess_count} {'attempt' if guess_count == 1 else 'attempts'}, you get {percentage[guess_count]}.")
        break
    else:

        

print(rand_num)

