# 🚨 Don't change the code below 👇
height = input("enter your height in m: \n")
weight = input("enter your weight in kg: \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

weightInt = int(weight)
heightFloat = float(height)
bmiIndex = int(weightInt / (heightFloat*heightFloat))
print("Your BMI Index is: " + str(bmiIndex))