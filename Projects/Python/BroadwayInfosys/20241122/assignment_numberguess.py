import random

random_num = random.randint(1,10)
count = 0
remain_guess = 0

reward = {1:'100%', 2: '90%', 3: '70%', 4: '50%', 5: '32%'}

while count < 5:
    guess_num = input("guess a number between 1 and 10: ")

    count += 1
    remain_guess = 5 - count

    if not guess_num.isnumeric():
        print(f"enter a valid number; you have {remain_guess} tries left")
        continue

    guess_num = int(guess_num)

    if random_num == guess_num:
        print(f"congratulation! you guessed the number in {count} {'try' if count == 1 else 'tries'}, and you get {reward[count]} for your effort!")
        break
    else:
        if count == 5:
            print(f"you ran out of guesses. the correct number was {random_num}, better luck next time. ")
        else:
            print(f"wrong guess! you have {remain_guess} guesses left, try again!")

