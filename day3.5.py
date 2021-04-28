# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combinedString = (name1 +name2).lower()

# For True.
t = combinedString.count('t')
r = combinedString.count('r')
u = combinedString.count('u')
e = combinedString.count('e')
# For Love
l = combinedString.count('l')
o = combinedString.count('o')
v = combinedString.count('v')

true = t + r  + u + e
love = l + o + v + e

#Love Percentage

lovePercentage = int(str(true) + str (love))
if lovePercentage <= 10 or lovePercentage >= 90:
  print(f"Your score is {lovePercentage}, you go together like coke and mentos.")
if lovePercentage >=40 or lovePercentage <=80:
  print(f"Your score is {lovePercentage}, you are alright together")
else:
  print(f"Your score is {lovePercentage}.")