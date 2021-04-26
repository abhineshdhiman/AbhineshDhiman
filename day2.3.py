# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


yearLeft = 90 - int(age)
daysLeft = yearLeft * 365
weeksLeft =  yearLeft * 52
monthsLeft = yearLeft  *12

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")