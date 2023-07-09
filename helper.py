from data import MENU


def process_coins(order):
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
    cost = MENU[order]['cost']

    if total > cost:
        print(f"Here is ${total - cost : .2f} in change.")
        print(f"Here is your {order}. Enjoy!")
    elif total == cost:
        print(f"Thank you. Here is your {order}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


def update_resources(stock, order):
    stock['water'] -= MENU[order]['ingredients']['water']
    if order != 'espresso':
        stock['milk'] -= MENU[order]['ingredients']['milk']
    stock['coffee'] -= MENU[order]['ingredients']['coffee']
    stock['money'] += MENU[order]['cost']
    return stock


def is_empty(stock):
    return stock['water'] < 50 or stock['coffee'] < 18


def check_resources(stock, order):
    if stock['water'] < MENU[order]['ingredients']['water']:
        print(f"Sorry there is not enough water.")
        return False
    elif stock['coffee'] < MENU[order]['ingredients']['coffee']:
        print(f"Sorry there is not enough coffee.")
        return False
    elif order != 'espresso' and stock['milk'] < MENU[order]['ingredients']['milk']:
        print(f"Sorry there is not enough milk.")
        return False
    else:
        return True


def print_report(stock):
    print(f"Water: {stock['water']}ml")
    print(f"Milk: {stock['milk']}ml")
    print(f"Coffee: {stock['coffee']}g")
    print(f"Money: ${stock['money']}")