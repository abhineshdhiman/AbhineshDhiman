rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
gameImages = [rock,paper,scissors]
choice=int(input("What do you choose 0 for rock,1 for paper and 2 for seccisors\n"))
print('You Choose\n' + gameImages[choice])
randomChoice = random.randint(0,2)
print('Computer Choose\n' + gameImages[randomChoice])
if choice >= 3 or choice < 0: 
  print("You typed an invalid number, you lose!") 
elif choice == 0 and randomChoice == 2:
  print("You win!")
elif randomChoice == 0 and choice == 2:
  print("You lose")
elif randomChoice > choice:
  print("You lose")
elif choice > randomChoice:
  print("You win!")
elif randomChoice == choice:
  print("It's a draw")
