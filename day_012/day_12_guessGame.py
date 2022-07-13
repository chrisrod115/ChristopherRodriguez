from replit import clear
from what_are_the_odds import logo
import random
clear()
lives = 10 
num_list = list(range(1,101))
hidden_num = []

def store_num():
    hidden_num.append(random.choice(num_list))
    print(hidden_num)
store_num()

playing = True
while playing != False:
    
    guess = input("Guess a number: ")
    if lives ==0:
        playing = False
    elif guess != hidden_num:
        lives -= 1
    elif guess == hidden_num: 
        print("OMG you found the hidden number!!!")
        playing = False
    print(f"Lives left: {lives}")
    
    
        
        
        
    