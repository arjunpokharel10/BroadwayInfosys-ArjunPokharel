from random import randint
computer_generated_random_number=randint(1,10)
SCORES={
  "1":100,
  "2":90,
  "3":70,
  "4":50,
  "5":32
}
TOTAL_TRIES={
  "1":"First try",
  "2":"Second try",
  "3":"Third try",
  "4":"Fourth try",
  "5":"Fifth try"
}
maximum_attempt=5
user_name=input("Player, please enter your name:")
user_name=user_name.title()
permission=input(f"Hello! {user_name}. Are you ready to play a guessing game?")
if permission.upper().startswith("N"):
  print(f"Exiting the game. Have a nice day {user_name}.")
else:
  print(f"Great! {user_name} you have {maximum_attempt} tries to guess the number.")
  for guessing_attempts in range(1,maximum_attempt+1):
    try:
      user_input_number= int(input(f"{user_name}, Enter a number(1-10)"))
      if user_input_number==computer_generated_random_number:
        score=SCORES[str(guessing_attempts)]
        attempt_message=TOTAL_TRIES[str(guessing_attempts)]
        print(f"Congratulations! You won {user_name} and received {score} within {attempt_message} tries.")
        break
      else:
        print(f"Sorry! {user_name} you guessed wrong number.")
    except ValueError:
      print(f"{user_name}, you entered an invalid number. Please check your number and try again.")
  else:
    print(f"Sorry {user_name}, you've used all your attempts. The correct number was {computer_generated_random_number}. Best of luck for the next time! ")