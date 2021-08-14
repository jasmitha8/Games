from menu import MENU
from menu import resources
import menu


def check_resources(drink):
    for item in drink:
        if drink[item] >= resources[item]:
            print("Not enough {item}. Sorry.")
            return False
        return True


def transaction(total_amt, cost):
    if total_amt == cost:
        menu.profit += cost
        print("Money accepted")
        return True
    elif total_amt > cost:
        change = round(total_amt - cost, 2)
        menu.profit += cost
        print(f"Here's your change ${change}")
        return True
    else:
        print(f"Not enough money. ${total_amt} refunded ")
        return False

def money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    quarters = quarters * 0.25
    dimes = dimes * 0.1
    nickels = nickels * 0.05
    pennies = pennies * 0.01
    coins = quarters + dimes + nickels + pennies
    return coins


def make_coffee(coffee):
    for items in coffee:
        resources[items] -= coffee[items]
    print("Here's your coffee. Enjoy!")


def user():
    flag = True
    while flag:
        option = input("What would you like? (espresso/latte/cappuccino): ")
        if option.lower() == "report":
            for items in resources:
                print(f"{items}: {resources[items]}")
            print(f"Money: {menu.profit}")
        elif option.lower() == "off":
            flag = False
        else:
            drink = MENU[option]
            print(option)
            print(f"{MENU[option]}")
            if check_resources(drink["ingredients"]):
                total_amt = money()
                successful = transaction(total_amt, drink['cost'])
                if successful:
                    make_coffee(drink['ingredients'])
            user()

user()


