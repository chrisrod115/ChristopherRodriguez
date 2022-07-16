"""
_To-Do List_
    1. we need a random generator
    2. a dictionary of items with: --> {"strings": int_value} --> (finished)
    3. prompt user to choose either higher or lower: user a dictionary {"higher": 1, "lower": 2} --> (done)
    4. if the answer is correct yes or no?
    5. answer correct = yes --> .pop the value from the dictionary
        1. continue the game 
    6. answer incorrect - no --> print("ouch you lost lol")
"""
import random
from game_data import data
from replit import clear
from art import logo,vs
clear()
h_l_dict = {
    "A": "Higher",
    "B": "Lower",
}
comp_a_gen = random.choice(data)
comp_b_gen = random.choice(data)

print(logo)
print(f"Compare A: {comp_a_gen['name']}, a {comp_a_gen['description']},from {comp_a_gen['country']}")
print(vs)
print(f"Compare B: {comp_b_gen['name']}, a {comp_b_gen['description']},from {comp_b_gen['country']}")
user_choice = input(str("Who has more followers: 'A' or 'B'? ")).upper()