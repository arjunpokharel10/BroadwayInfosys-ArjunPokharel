from random import randint
computer_generated = randint(1,10)
#print(computer_generated)
guesses = []
probablity =[100,90,70,50,32]
for i in range(5):
    guess = int(input("enter the number\n"))
    guesses.append(guess)
    if guess == computer_generated:
        
        print(f"You won and your score is {probablity[i]}")
        break
    else:
        print(f"failed ")
    
print(guesses)
print(computer_generated)
