from replit import clear
from coffee_menu import MENU, resources

"""
To_do_list:
1. User input what would you like (latte/expresso/cappuccino)
2. 4 functions: 
	1. enough_resources
	2. report 
	3. price_checker
	4. customer_change
3. print out, feedback for the current state that you are in
use drawio states
"""
clear()
amount = resources
profit = 0


def report():
    """Returns the amount of resources left in the machine. 
    """
    print(f"water {amount['water']}")
    print(f"milk {amount['milk']}")
    print(f"coffee {amount['coffee']}")
    print(f"Money: ${profit}")


def enough_resources(coffee):
    """Determines if there are enough resources in the machine in order to make a coffee. 

    Args:
        coffee (choose_coffee): user inputs a coffee they want; latte, espresso, or cappuccino.

    Returns:
        bool: either True or False.
    """
    for items in coffee:
        if coffee[items] >= resources[items]:
            print(f"Sorry there is not enough {items}")
            return False
    return True


def process_coins(): 
    """Returns the total number of coins inserted

    Returns:
        float: The total amount the user enters. 
    """
    print("please insert coins!")
    total = int(input(f"how many quarters?: ")) * 0.25
    total += int(input(f"how many dimes?: ")) * 0.10
    total += int(input(f"how many nickels?: ")) * 0.05
    total += int(input(f"how many pennies?: ")) * 0.01
    return total
    

def transaction_successful(cost,pay):
    """Determines if user entered enough coins.

    Args:
        cost (drink): The cost of the specific drink.
        pay (payment): The total payment that the user entered. 

    Returns:
        bool: Either True or False
    """
    if int(cost)>pay:
        print("Insufficient payment,money returned.")
        return False
    else:
        change = round(cost-pay,2)
        print(f"Here is this ${change} in change!") 
        global profit
        profit += cost        
        return True
        
        
def make_coffee(drink_name, order_ingredients):
    """Takes the ingredients that are in the coffee and subtract them from the resources.

    Args:
        drink_name (choose_coffee): Name of the coffee.
        order_ingredients (drink): Drink ingredients.
    """
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {drink_name}")
    
    
machine_on = True
while machine_on != False:
    choose_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choose_coffee == "off":
        print("goodbye!")
        machine_on = False
        continue
    elif choose_coffee == "report":
        report()
        continue
    else:
        drink = MENU[choose_coffee]
        if enough_resources(coffee=drink['ingredients']):
            payment =   process_coins() 
            if transaction_successful(cost = drink['cost'],pay = payment):
                make_coffee(drink_name=choose_coffee,order_ingredients=drink['ingredients'])



