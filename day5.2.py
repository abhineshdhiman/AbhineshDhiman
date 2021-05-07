# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split(',')
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇


import math
maxValue = 0 
minValue = math.inf
for i in student_scores:
  if(i>maxValue):
    maxValue = i
  if(i<minValue):
    minValue = i
   
  
print(f"The Maximum Score is {maxValue}")
print(f"The Minimum Score is {minValue}")
