from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU = Menu()
report_coffee = CoffeeMaker()
report_money = MoneyMachine()

order_coffee = True

while order_coffee:
    order = input(f"What would you like? ({MENU.get_items()}) ").lower()
    if order == 'report':
        report_coffee.report()
        report_money.report()
    elif order == 'off':
        order_coffee = False
    else:
        menu_item = MENU.find_drink(order)
        if not menu_item is None:
            if report_coffee.is_resource_sufficient(menu_item):
                if report_money.make_payment(menu_item.cost):
                    report_coffee.make_coffee(menu_item)
