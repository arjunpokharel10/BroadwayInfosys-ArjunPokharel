# program to let users guess a number between a range, and if correctly guessed, assign a score

import random

# range of min and max number values to pass through the randint argument
minimum_range = 0
maximum_range = 10

random_number = random.randint(minimum_range, maximum_range)


# initialising variables as counters
max_attempts = 5
attempts = 0                            
remaining_attempts = max_attempts       


# dictionary to store attemps to score mapping
score_map = {
    1: '100%',
    2: '90%',
    3: '70%',
    4: '50%',
    5: '32%',
}

# TO TEST THE PROGRAM - TO BE DISCARDED LATER
print(random_number)


while attempts < max_attempts:
    guess_number = input(f"guess a number between {minimum_range} and {maximum_range}: ")

    # before converting the input, checking if the string is numeric to avoid type-casting errors
    if not guess_number.isnumeric():
        print(f"{guess_number} is not a valid input, enter a NUMERIC value! \n")
        continue

    # updating variable only after numberic value was type-casted to an integer    
    guess_number = int(guess_number)
    attempts += 1
    remaining_attempts -= 1


    # main logic within this block of code
    if guess_number == random_number:
        print(f"congratulations! {random_number} is the correct number. you guessed it in {attempts} {'try' if attempts == 1 else 'tries'} so you get {score_map[attempts]}.")
        break
    else:
        if remaining_attempts == 0:
            print(f"you are out of attempts, you lose! the correct number was {random_number}.")
        else:
            print(f"{guess_number} is not the correct number! guess again, you have {remaining_attempts} {'guess' if remaining_attempts == 1 else 'guesses'} remaining! \n")