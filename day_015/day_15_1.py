from replit import clear
from coffee_menu import c_menu, resources

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
clear()
espresso = c_menu['espresso']
latte = c_menu['latte']
cappuccino = c_menu['cappuccino']
amount = resources
print(amount)


def report():
    return "report:"


def coffee_type(user_coffee):
    """Will return the ingredients for user coffee

    Args:
        user_coffee (string): either; Latte, espresso, or cappuccino

    Returns:
        dict: Returns the proper dictionary that the user
        chose.
    """
    if user_coffee == 'espresso':
        return dict(espresso['ingredients'])
    elif user_coffee == 'latte':
        return dict(latte['ingredients'])
    else:
        return cappuccino['ingredients']


def make_coffee(coffee, total):
    res = {key: coffee[key] - total.get(key, 0) for key in coffee.keys()}
    return res
 
    

choose_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
cost = c_menu[choose_coffee]['cost']
coffee = coffee_type(user_coffee=choose_coffee)
print((coffee))
enough = make_coffee(coffee=coffee_type,total= amount)

print(str(enough))


