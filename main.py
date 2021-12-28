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


import random
choices = [rock, paper, scissors]

while True:
    human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

    computer_choice = random.randint(0, 2)

    # 0 = rock
    # 1 = paper
    # 2 = scissor
    if (human_choice == 1 and computer_choice == 0) or (human_choice == 0 and computer_choice == 2) or (human_choice == 2 and computer_choice == 1):
      print(f"You chose \n{choices[human_choice]}")
      print(f"Computer chose \n{choices[computer_choice]}")
      print("You Win!")
    elif (human_choice == 0 and computer_choice == 1) or (human_choice == 2 and computer_choice == 0) or (human_choice == 1 and computer_choice == 2):
      print(f"You chose \n{choices[human_choice]}")
      print(f"Computer chose \n{choices[computer_choice]}")
      print("You Lose!")
    elif computer_choice == human_choice:
      print(f"You chose \n{choices[human_choice]}")
      print(f"Computer chose \n{choices[computer_choice]}")
      print("It's a Draw!")
    elif human_choice > 2:
      print("Invalid choice. Computer Wins!")
    
    option = input("Do you want to play again? (y/n) : ")
    if option == "n":
        break
