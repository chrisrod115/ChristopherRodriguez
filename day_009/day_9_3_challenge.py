from secrets import choice
import logo as logo_art
from replit import clear
print(logo_art)
user_name = input("what is your name: ")
user_bid = input("what is your bid: ")
other_bid = input("are there any other bids, type 1 for 'yes' or 2 for 'no': ")
choices = {
    "yes": 1,
    "no" : 2,
}

bidders = {}
still_bidding = True
while still_bidding != False:
    if choices["yes"]:
        continue
    elif choices["no"]:
        print(f"the highest bid {}")