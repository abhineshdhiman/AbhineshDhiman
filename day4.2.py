# Split string method
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


import random
randomIndex = random.randint(0,len(names)-1)
randomName =names[randomIndex]
print(f"{randomName} is going to buy the meal today!")