"""
ROCK PAPER SCISSOR GAME
"""
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
images = [rock , paper , scissors]

import random

user_input = int(input("What do you want to choose ?0 for Rock 1 for Paper and 2 for Scissor?\n")) 
if user_input >= 3 or user_input<0   :
  print("You typed a wrong number ,You lose!")
else:
  print(images[user_input])

  computer_choice = random.randint(0,2) 

  print(f"computer_choice:{computer_choice}")
  print(images[computer_choice])


    
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



 

