"""
You are going to write a program that will mark a spot with an X.

In the starting code, you will find a variable called map.

"""

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
m =[["⬜️","️⬜️","️⬜️"],["⬜️","⬜️","️⬜️"],["⬜️️","⬜️️","⬜️️"]]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizonal = int(position[0]) #2
vertical = int(position[1])#3
row= map[vertical - 1] 
row[horizonal-1]="X"





#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

