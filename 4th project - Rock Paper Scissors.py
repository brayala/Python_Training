from os import system
system("Clear")

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

#Write your code below this line 👇

#Player selection and display

Player_Selection = input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors"'\n')

print ("Your selection")
if Player_Selection == "0":
    print(rock)
elif Player_Selection == "1":
    print(paper)
elif Player_Selection == "2":
    print(scissors)

# Machine selection and display

print ("Machine Selection")
import random
Machine_Selection = str(random.randint(0,2))

if Machine_Selection == "0":
    print(rock)
elif Machine_Selection == "1":
    print(paper)
elif Machine_Selection == "2":
    print(scissors)

# Result

    # List
Rock_loose = "1"
Paper_loose = "2"
Scissor_loose = "0"

if Player_Selection == Machine_Selection:
    print ("It's a draw")
elif Player_Selection == "0" and Machine_Selection == Rock_loose:
    print ("You loose")
elif Player_Selection == "1" and Machine_Selection == Paper_loose:
    print ("You loose")
elif Player_Selection == "2" and Machine_Selection == Scissor_loose:
    print ("You loose")
else:
    print("you win...")

