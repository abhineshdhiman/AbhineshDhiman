# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? \n"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if(year % 4 == 0):
  if(year %100 == 0):
    if(year %400 == 0):
      print("Year is Leap Year")
    else:
      print("Not a leap Year")
  else:
      print("leap year")
else:
     print("not a leap year")
