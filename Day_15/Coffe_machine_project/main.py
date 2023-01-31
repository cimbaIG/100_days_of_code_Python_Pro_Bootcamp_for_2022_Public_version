MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def turn_off_machine():
    return True

def print_report():
    """Print the current resource values."""
    for key in resources:
        if key == "Money":
            print(f"{key.capitalize()}: {'$' + str(resources[key])}")
        else:        
            print(f"{key.capitalize()}: {resources[key]}")

# Check what happens for espresso where milk is not needed
def sufficient_resources(drink_ingredients):
    for ingredients in drink_ingredients:
        if drink_ingredients[ingredients] > resources[ingredients]:
            print(f"Sorry there is not enough {ingredients}.")
            return False
        return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    to_pay = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return to_pay

# Total money is not updating properly! To be resolved...
def successful_transaction(given_money, coffee_cost):
    if given_money >= coffee_cost:
        exchange = round(given_money - coffee_cost, 2)
        print(f"Here is ${exchange} dollars in change.")
        global total_money
        total_money += coffee_cost
        resources["Money"] = total_money
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink, drink_ingredients):
    for ingredients in drink_ingredients:
        resources[ingredients] -= drink_ingredients[ingredients]
    print(f"Here is your {drink}. Enjoy!")

total_money = 0
turn_off = False
while turn_off == False:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "report":
        print_report()
    elif user_choice == "off":
        turn_off = turn_off_machine()
    else:
        if sufficient_resources(MENU[user_choice]["ingredients"]):
            to_pay = process_coins()
            if successful_transaction(to_pay, MENU[user_choice]["cost"]):
                make_coffee(user_choice, MENU[user_choice]["ingredients"])

""" MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    '''Returns True when order can be made, False if ingredients are insufficient.'''
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    '''Returns the total calculated from coins inserted.'''
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    '''Return True when the payment is accepted, or False if money is insufficient.'''
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    '''Deduct the required ingredients from the resources.'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"]) """