height = float(input("enter your height in m: \n"))
weight = float(input("enter your weight in kg: \n"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

weightInt = weight
heightFloat = height
bmiIndex = round(weightInt / (heightFloat*heightFloat),2)
print(f"Your BMI Index is:  {bmiIndex}")
if(bmiIndex <= 18.5):
  print("You are Underweight")
elif(bmiIndex >18.5 and bmiIndex <=25):
    print("You have a normal weight")
elif(bmiIndex >25 and bmiIndex <=30):
  print("you are slightly overweight")
elif(bmiIndex >30 and bmiIndex <=35):
  print("you are obese")
elif(bmiIndex > 18.5):
  print("You are clinically obese.")