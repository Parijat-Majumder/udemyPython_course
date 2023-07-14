"""
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.
"""
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line

left_yr = 90 -int(age) 
total_days = left_yr *365 
totalwk = left_yr *52
totalmn = left_yr*12
print(f"You have {total_days} days , {totalwk } weeks and {totalmn } months left")

