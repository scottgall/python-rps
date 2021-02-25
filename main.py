import random

print("Let's play Rock Paper Scissors!")

options = {"r": "rock", "p": "paper", "s": "scissors"}
wins = {"r": "s", "p": "r", "s": "p"}

computer_choice = random.choice(list(options.keys()))
user_choice = input("Make your choice: (r)ock, (p)aper, (s)cissors? --> ")

if user_choice not in list(options.keys()):
  print("I don't understand that.")
  print("Next time, choose 'r', 'p', or 's'.")
elif user_choice == computer_choice:
  print("You chose {}. The computer chose {}.".format(options[user_choice], options[computer_choice]))
  print("Tie!")
elif wins[user_choice] == computer_choice:
  print("you chose {}. The computer chose {}.".format(options[user_choice], options[computer_choice]))
  print("Yay! You won!")
else:
  print("you chose {}. The computer chose {}.".format(options[user_choice], options[computer_choice]))
  print("Sorry. You lost.")