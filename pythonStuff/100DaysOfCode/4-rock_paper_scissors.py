import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if choice == 0:
    your_hand = "Rock"
elif choice == 1:
    your_hand = "Paper"
elif choice == 2:
    your_hand = "Scissors"

computer_choice = random.randint(0,2)
if computer_choice == 0:
    computer_hand = "Rock"
elif computer_choice == 1:
    computer_hand = "Paper"
elif computer_choice == 2:
    computer_hand = "Scissors"

print(f"You: {your_hand}")
print(f"Computer: {computer_hand}")

if choice == computer_choice:
    print("It's a draw.")
elif choice == 0 and computer_choice == 1:
    print("You Lose.")
elif choice == 0 and computer_choice == 2:
    print("You Win")
elif choice == 1 and computer_choice == 2:
    print("You Lose.")
elif choice == 1 and computer_choice == 0:
    print("You Win")
elif choice == 2 and computer_choice == 0:
    print("You Lose.")
elif choice == 2 and computer_choice == 1:
    print("You Win")
