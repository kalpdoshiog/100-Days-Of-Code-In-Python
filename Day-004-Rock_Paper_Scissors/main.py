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

list_of_rock_paper_scissor = [rock, paper, scissors]
computer_choice = random.randint(0,2)


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors. \n"))


if user_choice < 0 or user_choice > 2:
    print("Invalid choice")
else:
    print(f"Your choice: \n{list_of_rock_paper_scissor[user_choice]}")


    print("Computer Choice: ")
    print(list_of_rock_paper_scissor[computer_choice])

    if user_choice == computer_choice:
        print("It's a Draw!!!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You Win!!!")
    else:
        print("You Lose!!!")
