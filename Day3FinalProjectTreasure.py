"""
Head over to replit.com
https://replit.com/@appbrewery/treasure-island-start?v=1
Coding Rooms is very handy for our exercises. However, the end-of-day projects are more free-form. You can experiment and play with this project. Customise it. Get as creative as you like. There is no exact output for you to match. There are no tests for you to pass. These assignments are not graded.
"""
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

#Write your code below this line 👇
first_ques = input("Where you'll go? Left or Right\n")
if first_ques.lower() == "Left".lower() :
    second_ques = input("What do  you want to do now ?Wait or Swim?\n")
    if second_ques.lower() == "Wait".lower():
        final_ques = input("Which door you like to open?Red ,Yellow orBlue?\n")
        if final_ques.lower()== "Yellow".lower():                    
            print("Yey! You got a Diamond!")
        else:
            print("YOU LOSE THE GAME!")
        
    else:
        print(f"Oops! Shark got you , Game Over!")
else:
    print(f"You dropped in a hole ,Game Over!")
