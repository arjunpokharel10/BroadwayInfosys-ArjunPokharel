import random

minimum_range = 1
maximum_range = 10
random_number = random.randint(minimum_range, maximum_range)

maximum_attempts = 5
current_attempt = 0

score_map = {
    1: '100%',
    2: '90%',
    3: '70%',
    4: '50%',
    5: '32%'
}

print(random_number)

while current_attempt < maximum_attempts:
    
    try:
        guessed_number = int(input("enter a number: "))
        
        if guessed_number == random_number:
            current_attempt += 1
            print(f"correct, you guessed it. {random_number} is the correct number! \nyou guessed it in {current_attempt} attempts so you get {score_map[current_attempt]}!")
            break
        else:
            current_attempt += 1
            remaining_attempts = maximum_attempts - current_attempt
            if remaining_attempts > 0:
                print(f"wrong guess! try again, you have {remaining_attempts} attempts left.")
            else:
                print(f"you are out of attempts! {random_number} was the correct number! ")
    except ValueError:
        print(f"invalid entry! try guessing a number between {minimum_range} and {maximum_range}.")