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
c_list = [rock, paper, scissors]
choice = int(input("What would you choose? Type 0 for rock, 1 for paper or 2 for scissors \n"))

random_int = random.randint(0,2)

if choice > 2 or choice < 0:
    print("You entered invalid number. You lose")
else:
    print(f"{c_list[choice]}")
    print(f"Computer choose \n {c_list[random_int]}")

    if choice == random_int:
        print("Match Draw")
    elif (choice == 0) and (random_int == 2):
        print("You win")
    elif (choice == 2) and (random_int == 0):
        print("You Lose")
    elif choice < random_int:
        print("You Lose")
    elif choice > random_int:
        print("You Win")

