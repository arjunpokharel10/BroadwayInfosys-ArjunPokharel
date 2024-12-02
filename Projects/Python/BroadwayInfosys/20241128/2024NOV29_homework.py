# program to let users guess a number between a range, and if correctly guessed, assign a score

import random

# range of min and max number values to pass through the randint argument
minimum_range = 0
maximum_range = 100

random_number = random.randint(minimum_range, maximum_range)

max_attempts = 5
attempts = 0                     # initialising guess count to 0
remaining_attempts = max_attempts      # initialising remaining counts to max_attempts


score_map = {
    1: '100%',
    2: '90%',
    3: '70%',
    4: '50%',
    5: '32%',
}

print(random_number)

# main loop 
while attempts < max_attempts:
    guess_number = input(f"guess a number between {minimum_range} and {maximum_range}: ")

    # before converting the input, checking if the string is numeric to avoid type-casting errors
    if not guess_number.isnumeric():
        continue

    # updating variable only after numberic value was type casted to an integer    
    guess_number = int(guess_number)
    attempts += 1
    remaining_attempts -= 1

    # to exit the program if attempts have been exhausted
    if remaining_attempts == 0:
        print(f"game over, the correct number was {random_number}.")
        break

    # continue to the next iteration of the loop if guessed number is incorrect    
    if not guess_number == random_number:
        print(f"{guess_number} is not the correct number! guess again, you have {remaining_attempts} {'guess' if remaining_attempts == 1 else 'guesses'} remaining!")
        continue

    # to end the program if the guess is correct    
    print(f"congratulations! {random_number} is the correct number. you guessed it in {attempts} {'try' if attempts == 1 else 'tries'} so you get {score_map[attempts]}.")
    break
