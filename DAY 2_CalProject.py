"""
If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
"""


----IF WE KNOW THE VALUES-----

print("Welcome to the tip Calculator.") 
total_bil = input("What was the total bill? \n")
prcntge =input("What per centage tip would you like to give 10,12 or 15? \n")
splt = input("How many people to split the bill? \n")
prhdbill =int(total_bil)/5 *1.12
rnd = round(prhdbill,2)
print (f"Each person should pay :{rnd:.2f}")
---------OR--------------
print("Welcome to the tip Calculator.") 
bil =float(input("What was the total bill? \n $"))
prcntge =int(input("What per centage tip would you like to give 10,12 or 15? \n"))
people =int( input("How many people to split the bill? \n"))
amount_percent =( bil* (100 +prcntge)/100)
prhdbill =( amount_percent/5)
rnd = round(prhdbill,2)
print (f"Each person should pay $:{rnd:.2f}")
