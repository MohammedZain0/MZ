import random

rock_ascii =("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper_ascii =("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissors_ascii = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print("Welcome to the Rock,Paper,Scissors game: ")

Enter = input("press Enter to continu or tyoe (Help) for the rulse Help: ").lower()

if Enter == 'help':
    print("""                 ******* RULSE ******
          1) you choose and the computer choos
          2) Rock dmashes Scissors -> Rock Win
          3) Scissors cut paper -> Scissors Win
          4) paper covers Rock -> Paper Win""")
user_choice =input("Enter your choice(rock, paper, Scissors : )").lower()

if user_choice not in ['rock', 'paper','scissors']:
    print(" invaild choice")
else:
    if user_choice == "rock":
        print(f"\n you choice: \n{rock_ascii}")
    elif user_choice == "paper":
        print(f"\n you choice: \n{paper_ascii}")
    elif user_choice == "scissors":
        print(f"\n you choice: \n{Scissors_ascii}")

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    if computer_choice == "rock":
        print(f"\n you choice: \n{rock_ascii}")
    elif computer_choice == "paper":
        print(f"\n you choice: \n{paper_ascii}")
    elif computer_choice == "scissors":
        print(f"\n you choice: \n{Scissors_ascii}")

    if user_choice == computer_choice:
        print("it's a tie")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "paper" and computer_choice == "rock")
        or
        (user_choice == "scissors" and computer_choice == "rock")):
            print("You Win")
    else:
        print("you lose")
    







