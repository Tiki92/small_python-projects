"""Rock Paper Scissors Game"""
from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]
messages = {
  "tie": "Yawn it's a tie!",
  "won": "Yay you won!",
  "lost": "Aww you lost!"
}

def decide_winner(user_choice, computer_choice):
  if user_choice.upper() not in options:
    print("You dind't enter a proper value!")
    exit()
    
  print("The users choice is %s" % (user_choice.upper()))
  print("The computer choice is %s" % (computer_choice))
  
  if user_choice == computer_choice:
    print(messages["tie"])
  elif user_choice == options[0] and computer_choice == options[2]:
    print(messages["won"])
  elif user_choice == options[1] and computer_choice == options[0]:
    print(messages["won"])
  elif user_choice == options[2] and computer_choice == option[1]:
    print(messages["won"])

  else:
    print(messages["lost"])
  
    
def play_RPS():
  user_choice = input("Enter Rock, Paper or Scissors: ")
  user_choice.upper()
  computer_choice = options[randint(0, 2)]
  decide_winner(user_choice, computer_choice)
  
play_RPS()
