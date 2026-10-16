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
    "coffee": 100,
}

def make_coffee(order):
    """This will make coffee only if when money and resources are sufficient"""
    drink_detail = MENU.get(order)
    ingredients = drink_detail["ingredients"]
    for ingredient_name, ingredient_value in ingredients.items():
        resources[ingredient_name] -= ingredient_value

def calculate_coins(inserted_quarters, inserted_dimes, inserted_nickles, inserted_pennies):
    """This calculates and return total coins received by user."""
    quarters = 0.25 * inserted_quarters
    dimes = 0.10 * inserted_dimes
    nickles = 0.05 * inserted_nickles
    pennies = 0.01 * inserted_pennies

    total_coins = quarters + dimes + nickles + pennies
    return total_coins

def enough_money_received(money, order):
    """This verifies received money and cost of product and returns feedback"""
    drink_cost = MENU.get(order)
    cost = drink_cost["cost"]
    if money < cost:
        print("Sorry that's not enough money. Money refunded.")
    elif money == cost:
        resources["Money"] += money
        make_coffee(user_input)
    elif money > cost:
        extra_money = money - cost
        resources["Money"] += cost
        print(f"Here is ${round(extra_money, 2)} dollars in change.")
        make_coffee(user_input)

def customer_order(order):
    """This takes order item/name"""
    if order == "espresso":
        sufficient_resources(user_input)
    elif order == "latte":
        sufficient_resources(user_input)
    elif order == "cappuccino":
        sufficient_resources(user_input)

def sufficient_resources(order):
    """This check sufficient ingredients are present or not for the ordered item and returns feedback."""
    drink_detail = MENU.get(order)
    ingredients = drink_detail["ingredients"]

    for ingredient_name, ingredient_value in ingredients.items():
        if resources[ingredient_name] < ingredient_value:
            print(f"Sorry there is not enough {ingredient_name}.")
            return False


    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?:"))
    total_money = calculate_coins(inserted_quarters=quarters, inserted_dimes=dimes, inserted_nickles=nickles, inserted_pennies=pennies)

    enough_money_received(money=total_money, order=user_input)
    return None


resources["Money"] = 0

dispense_coffee = True
while dispense_coffee:

    # TODO: 1. Ask user what would you like? (Espresso, latte, cappuccino).
    user_input = input("What would you like? (Espresso, Latte, or Cappuccino): ").lower()
    customer_order(user_input)

    # TODO: 2. Turn off the coffee machine by entering "off" to the prompt.
    if user_input == "off":
        print("Turning coffee machine off. Bye Bye!!")
        dispense_coffee = False

    # TODO 3. Print report.
    elif user_input == "report":
        for ingredients_name, value in resources.items():
            print(f"{ingredients_name.capitalize()}: {value}")