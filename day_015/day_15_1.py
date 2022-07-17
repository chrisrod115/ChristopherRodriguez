from replit import clear
from coffee_menu import MENU, resources

"""
To_do_list:
1. User input what would you like (latte/expresso/cappuccino)
2. 4 functions: 
	1. make_coffee
	2. report 
	3. price_checker
	4. customer_change
3. print out, feedback for the current state that you are in
use drawio states
"""

def report():
    return "report:"


amount = resources
espresso = MENU['espresso']
latte = MENU['latte']
cappuccino = MENU['cappuccino']
cost = MENU['cost']

def make_coffee():
    
    
    
coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
