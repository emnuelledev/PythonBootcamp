# 
import random

person = ["rock", "paper", "scissors"]

computer_choice = random.choice(person)

choice = input("What do you choose? Type 'rock', 'paper' or 'scissors': ")

if choice == computer_choice:
    print(f"Computer chose {computer_choice}. It's a draw!")
elif choice == "rock" and computer_choice == "scissors":
    print(f"Computer chose {computer_choice}. You win!")
elif choice == "paper" and computer_choice == "rock":
    print(f"Computer chose {computer_choice}. You win!")
elif choice == "scissors" and computer_choice == "paper":
    print(f"Computer chose {computer_choice}. You win!")
else:
    print(f"Computer chose {computer_choice}. You lose!")