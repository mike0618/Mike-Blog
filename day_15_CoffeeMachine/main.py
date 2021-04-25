from art import coffee, logo
from data import MENU, resources, COINS


def check_resources(item, execute=False):
    """
    Resource check function and it can takes ingredients.
    :param item: type of coffee
    :param execute: if True it takes ingredients
    :return: True if enough resources
    """
    ingredients = MENU[item]["ingredients"]
    enough = True
    for ingredient in ingredients:
        if not execute and ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            enough = False
        elif execute:
            resources[ingredient] -= ingredients[ingredient]
    return enough


def coffee_machine():
    print(logo)
    total_money = 0
    while True:
        answer = input("What would you like? (espresso/latte/cappuccino): ")

        if answer == "off":
            print("Good bye!")
            return answer

        elif answer == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${total_money:.2f}")

        elif answer == "espresso" or answer == "latte" or answer == "cappuccino":
            if check_resources(answer):
                print("Please insert coins.")
                inserted_money = 0
                cost = MENU[answer]["cost"]
                for coin in COINS:
                    number = 0
                    strnumber = input(f"How many {coin}?: ")
                    if strnumber.isdigit():
                        number = int(strnumber)
                    inserted_money += number * COINS[coin]
                if inserted_money < cost:
                    print(f"Sorry that's not enough money. ${inserted_money:.2f} refunded.")
                else:
                    total_money += cost
                    if inserted_money > cost:
                        refund = inserted_money - cost
                        print(f"Here is ${refund:.2f} dollars in change.")
                    check_resources(answer, True)
                    print(f"Here is your {answer}. ☕ Enjoy!")
                    print(coffee)
        else:
            print("Input is incorrect.")

if __name__ == '__main__':
    coffee_machine()
