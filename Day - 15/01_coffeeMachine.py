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
    "money": 0
}

def print_report():
    for item in resources:
        if item in ['water','milk']:
            print(f"{item.capitalize()} : {resources[item]}ml")
        elif item == 'coffee':
            print(f"{item.capitalize()} : {resources[item]}g")
        elif item == 'money':
            print(f"{item.capitalize()} : ${resources[item]}")

def update_report(order_name):
    for item in MENU[order_name]["ingredients"]:
        resources[item] -= MENU[order_name]["ingredients"][item]
    resources['money'] = MENU[order_name]['cost']

def validate_money(order_name):
    print("Please insert coins!!")
    quarter = int(input("How many quarters? : "))
    dime = int(input("How many dimes? : "))
    nickle = int(input("How many nickles? : "))
    penny = int(input("How many pennies? : "))
    provided_money = (penny * 0.01) + (nickle * 0.05) + (dime * 0.10) + (quarter * 0.25)
    required_money = MENU[order_name]["cost"]

    if provided_money >= required_money :
        print(f"Here is {provided_money - required_money} in change.")
        print(f"Here is your {order_name}. Enjoy!!")
        update_report(order_name)
    else:
        print("Sorry, that's not enough money. Money refunded!!")


def validate_ingredients(order_name):
    required_quantity = MENU[order_name]["ingredients"]
    not_suff_item = []
    for item in required_quantity:
        if required_quantity[item] > resources[item]:
            not_suff_item.append(item)
            break
    return not_suff_item

order_coffee = True

while order_coffee:
    order = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if order == 'report':
        print_report()
    elif order == 'off':
        order_coffee = False
    else:
        if order in MENU:
            insufficient_items = validate_ingredients(order)
            if len(insufficient_items) == 0:
                validate_money(order)
            else:
                print(f"Sorry!! There is not enough {",".join(insufficient_items)}")