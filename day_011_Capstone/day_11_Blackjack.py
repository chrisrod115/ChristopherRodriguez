"""
This program is a BlackJack gambling game. 
"""
import random as rnd
def blackjack():
    cards = {
        "user_cards": [],
        "dealer_cards": [],
        "deck": [1,2,3,4,5,6,7,8,9,10,11]
    }
    shuffle_deck = rnd(cards["deck"])
    for i in range(2):
        
    

playing = True
while playing != False:
    wanna_play = input("Do you want to play a blackjack game 'y' or 'n': ")
    if wanna_play == 'y':
        blackjack
    elif wanna_play == 'n':
        print("Goodbye!")
        playing = False
    else:
        print("Not an option try again")
        continue
        

