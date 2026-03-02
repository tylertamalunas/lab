import random

answer = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# difficulty selection
difficulty = input("Choose a difficulty. Type 'easy' or 'hard'\n")
if difficulty == 'easy':
    guesses = 10
elif difficulty == 'hard':
    guesses = 5

while guesses > 0:
    print(f"You have {guesses} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess < answer:
        print(f"Too low. Guess again")
        guesses -= 1 
    elif user_guess > answer:
        print(f"Too high. Guess again")
        guesses -= 1 
    else:
        print(f"You guessed correct! The answer was {answer}.")
        guesses = -1

if guesses == 0:
    print("You've run out of guesses. You lose.")
