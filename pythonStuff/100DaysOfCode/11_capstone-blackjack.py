"""
The card game Blackjack.
points are from 1-10
Ace = 1 or 11
K, Q, J = 10
Numbered cards are equal to face value 

Design:
    - card values are stored in a list, where position is the card
    - hands are stored as a list and output every card dealt i.e [Ace, 9] -> [Ace, 9, 10]
    - deck is infinite
    - Ace changes value based on total score of hand (1 or 11)
    - 
"""
"""
STEPS:
D    1. Deal player hand and dealer hand
D    1b. if player or dealer or both have blackjack, game is immediately over, determine winner
    2. tell hands and player score, ask if user wants to 'hit' or 'stay' (no splitting since theres no bets)
    3a. if 'hit', add card to player hand and revert back to step 2.
    3b. if player score is over 21, player loses
    3c. if stay, deal dealer hand and show score.
    4a. if dealer hand is 17 or higher, stay
    4b. if dealer hand is 16 or lower, hit and revert back to step 4a. 
"""

import random

def draw_card(hand, deck, cards):
    new_card = cards[random.randint(0,len(cards)-1)]
    return hand.append(new_card)

def calc_score(hand, deck, cards):
    score = 0
    ace_count = 0
    for card in hand:
        if card == 'Ace':
            ace_count += 1
        score += deck[cards.index(card)]
    if score > 21 and ace_count > 0:
        while score > 21 and ace_count > 0:
            score -= 10
            ace_count -= 1
    return score

def declare_winner(player_score, dealer_score):
    if player_score > dealer_score and player_score < 22:
        return "Player wins."
    elif dealer_score > player_score and dealer_score < 22:
        return "Dealer Wins."
    else:
        return "It's a tie."

play = True
while play:
    cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Intro
    print("Welcome to Blackjack.")

    # initial deal
    player_hand = []
    dealer_hand = []
    draw_card(player_hand, deck, cards)
    draw_card(player_hand, deck, cards)
    draw_card(dealer_hand, deck, cards)
    draw_card(dealer_hand, deck, cards)
    player_score = calc_score(player_hand, deck, cards)
    dealer_score = calc_score(dealer_hand, deck, cards)
    print(f"The dealer has [{dealer_hand[0]}, Hidden]")
    print(f"You have {player_hand}")

    # check for blackjack
    if player_score == 21 and dealer_score == 21:
        print("DRAW. Both players have Blackjack.")
    elif player_score == 21 and dealer_score != 21:
        print("Player wins with Blackjack!")
    elif dealer_score == 21 and player_score != 21:
        print("Dealer wins with Blackjack.")
    else:

        # Players turn
        players_turn = True
        while players_turn == True:
            action = input(f"You have {player_score}. Do you want to 'hit' or 'stay'?\n")
            if action == "hit":
                draw_card(player_hand, deck, cards)
                player_score = calc_score(player_hand, deck, cards)
                print(f" You have {player_score} with {player_hand}")
                if player_score > 21:
                    print(f"Player busted. You lose.")
                    players_turn = False
                    action = 'stay'
            elif action == "stay":
                players_turn = False
                print(f"You stayed with {player_score}")


        # dealers turn
        dealers_turn = True
        if player_score > 21:
            dealers_turn = False
        while dealers_turn == True:
            print(f"The dealer has {dealer_score} with {dealer_hand}")
            if dealer_score > 21:
                print("The Dealer busted. You win!")
                dealers_turn = False
            elif dealer_score >= 17:
                print(f"The Dealer stays.")
                dealers_turn = False
                print(declare_winner(player_score, dealer_score))
            else:
                print("Dealer has to hit.")
                draw_card(dealer_hand, deck, cards)
                dealer_score= calc_score(dealer_hand, deck, cards)
    keep_playing = input("Do you want to keep playing? 'y' or 'n': ")
    if keep_playing == 'y':
        continue
    else:
        play = False
