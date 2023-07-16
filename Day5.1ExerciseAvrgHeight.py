"""
You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.
"""
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights\n ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#cannot use sum function 
total_height = 0 
for height in student_heights:
    total_height = total_height+height
#print(total_height)

#cannot use len function

students_num = 0 
for student in student_heights:
    students_num = students_num +1
#print(students_num)    

avrg_hgt = round(total_height/students_num)
print(avrg_hgt)
