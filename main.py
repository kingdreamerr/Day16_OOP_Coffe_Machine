from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_in_use = True
coffee_machine = CoffeeMaker()
bank = MoneyMachine()

while is_in_use:
    # get user input
    menu_list = Menu()
    list_of_coffee = menu_list.get_items()
    choice = input(f"What would you like? ({list_of_coffee})").lower()
    drink = Menu().find_drink(choice)
    if choice == "off":
        is_in_use = False
    elif choice == "report":
        coffee_machine.report()
        bank.report()
    else:
        if coffee_machine.is_resource_sufficient(menu_list.find_drink(choice)) and bank.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
