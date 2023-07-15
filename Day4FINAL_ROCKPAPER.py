"""
ROCK PAPER SCISSOR GAME
"""

#Write your code below this line 👇
import random
user_input = int(input("What do you want to choose ?0 for Rock 1 for Paper and 2 for Scissor?\n"))
computer_choice = random.randint(0,2) 
print(computer_choice)
if user_input == 0 and computer_choice == 1:
  print("You lose!")
elif user_input == 0 and computer_choice == 2:
  print("You Won!")
elif user_input == 2 and computer_choice == 0:
  print("You lose!") 
elif user_input == 1 and computer_choice == 2:
  print("You lose!")

elif user_input > computer_choice :
  print("You win!")
elif user_input == computer_choice :
  print("Match Draw")
