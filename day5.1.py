# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights \n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  # print(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

  studentCount = 0
  StudentAvg = 0 
for i in student_heights:
  studentCount += 1
  StudentAvg += i
print(round(StudentAvg/studentCount))

