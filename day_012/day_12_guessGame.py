from replit import clear
import random
import math
clear()
num_list = list(range(1,101))
hidden_num = []
def store_num():
    hidden_num.append(random.choice(num_list))
    print(hidden_num)
def guess_a_num(lives_left):
    print(hidden_num)
    guess = input("Make a guess: ")
    if guess != hidden_num:
        lives_left -= 1 
    else:
        print("congrats you won!!! NO WAY YOU GESSED THAT YOU HAVE SUPERPOWERS")
        lives_left = 0 
print("Guess a number from 1 to 100.")
user_choice = input("Choose 'easy' or 'hard': ")
if user_choice == "easy":
    store_num()
    lives = 10 
    while lives != 0 or guess_a_num() == hidden_num:
        guess_a_num(lives_left = lives)
        
        
    