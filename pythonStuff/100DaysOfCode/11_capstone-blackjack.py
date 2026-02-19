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
print("Welcome to Blackjack.")
run = True
while run:
    player_hand = []
    dealer_hand = []
    draw_card(player, deck, cards)
    draw_card(player, deck, cards)
    draw_card(dealer, deck, cards)
    draw_card(dealer, deck, cards)
