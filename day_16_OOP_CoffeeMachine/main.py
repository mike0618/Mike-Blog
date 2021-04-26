from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo, coffee

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
items = menu.get_items()

print(logo)
while True:
    answer = input(f"What would you like? ({items}): ")

    if answer == "off":
        print("Good bye!")
        break

    elif answer == "report":
        coffee_machine.report()
        money_machine.report()

    else:
        drink = menu.find_drink(answer)
        if drink and coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
                print(coffee)
