# ask for a name and bid, then ask if there is another bidder. If yes, clear screen and ask name and bid again, if NO, print highest bidder with bid value. 
import os

print("Welcome to the super secret auction.")
winner_not_declared =  True
bids = {
        # {"name" : bid}
        }

while winner_not_declared:
    name = input("What is your name?: ").title()
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    next_bid = input("Is there another bidder? ('yes' or 'no'): ").lower()

    if next_bid == 'yes':
        #clear screen
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
    else:
        winner_not_declared = False

max_bid = 0
max_bidder = ''
for k, v in bids.items():
    if v > max_bid:
        max_bid = v 
        max_bidder = k
print(f"The winner is {max_bidder} with a bid of ${max_bid}!")
