import random

word_list = ["camel", "dog", "obituary"]
word = random.choice(word_list)
shown_word = ['_'] * len(word)
print("Let's play a game of Hangman.")
play = True
player_lives = 6
guessed_letters = []
# PICKING RANDOM WORD AND CHECKING ANSWER
# 1. randomly choose a word from word_list
# 2. ask user to guess a letter
# 3. check if letter is in word, print "right" if it is and "wrong" if it isnt
# REPLACING BLANKS WITH GUESSES

# RUN THE GAME
while play:
    print(f"Word to guess: {''.join(shown_word)}")
    user_guess = input("Guess a letter: ").lower()
    if user_guess in guessed_letters:
        print("You alreayd guessed that, try again.")
    else:
        guessed_letters.append(user_guess)

        if user_guess in word:
            for char in range(len(word)):
                if user_guess == word[char]:
                    shown_word[char] = user_guess
            print(f"{''.join(shown_word)}") 
        else:
            player_lives -= 1
            print(f"You guessed {user_guess}, that's not in the word. You lose a life")
        print(f"**********{player_lives}/6 LIVES LEFT**********")
        if player_lives == 0:
            print(f"The word was {word}. YOU LOSE")
            play = False
        if '_' not in shown_word:
            print(f"The word is {''.join(shown_word)}. YOU WIN!")
            play = False

