# import random
# import my_module

# random_integer = random.randint(1, 10)

# print(random_integer)

# print(my_module.pi)

# random_float = random.random() * 5
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# states_of_america = ["Delaware", "Pennsylvania"]
# states_of_america[1] = "Pencilvania"
# states_of_america.append("Angelaland")
# states_of_america.extend(["Angelaland", "Jack Bauer Land"])
# print(states_of_america)

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples",
#                "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])

import random
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

# Write your code below this line 👇
choices = [rock, paper, scissors]
user = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user >=3 or user < 0:
    print("You typed an invalid number. Try again!")
else:
    print(choices[user])

    computer = random.randint(0, 2)
    print("Computer chose: ")
    print(choices[computer])


    if user == 0 and computer == 2:
        print("You Win!")
    elif computer == 0 and user == 2:
        print("You lose!")
    elif computer > user:
        print("You Lose!")
    elif user > computer:
        print("You win!")
    elif user == computer:
        print("No winner. It is a tie!")
