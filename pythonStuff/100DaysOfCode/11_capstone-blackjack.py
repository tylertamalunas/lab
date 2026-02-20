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
    new_card = cards[random.randint(0,len(cards))]
    return new_hand.append(new_card)

def calc_score(hand, deck, cards):
    score = 0
    for card in hand:
        score += deck[cards.index(card)]
    return score
    




cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
run = True
while run:
    print("Welcome to Blackjack.")
    player_hand = []
    dealer_hand = []
    draw_card(player, deck, cards)
    draw_card(player, deck, cards)
    draw_card(dealer, deck, cards)
    draw_card(dealer, deck, cards)
    player_score = calc_score(player_hand, deck, cards)
    dealer_score = calc_score(dealer_hand, deck, cards)
    print(f"The dealer has [{dealer_hand[0], Hidden}]")
    print(f"You have {player_hand}")
    if dealer_score == 21 and player_score == 21:
        print("DRAW. Dealer and Player both have Blackjack.")
        print(f"Dealer: {dealer_hand}")
        print(f"You: player_hand}")
    elif player_score == 21:
        print("WINNER. Player has Blackjack!")
        print(f"You: {player_hand}")
    elif dealer_score == 21:
        print("LOSE. Dealer has Blackjack!")
        print(f"Dealer: {dealer_hand}")
    action = 'hit'
    else:
        while player_score <=21
            action = input(f"You have {player_score}. Do you want to 'hit' or 'stay'? ")
            if action == hit:
                draw_card(player, deck, cards)
                player_score = calc_score(player_hand, deck, cards)
            else:

