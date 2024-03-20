# Coffee Machine

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

# initial values
total_income = 0


# defining functions for the drinks
def espresso():
    resources["water"] -= 50
    resources["coffee"] -= 18
    print("Enjoy your espresso! ☕")
    return resources


def latte():
    resources["water"] -= 100
    resources["milk"] -= 150
    resources["coffee"] -= 24
    print("Enjoy your latte! ☕")
    return resources


def cappuccino():
    resources["water"] -= 250
    resources["milk"] -= 100
    resources["coffee"] -= 24
    print("Enjoy your cappuccino! ☕")
    return resources


def report():
    global total_income
    for attribute, value in resources.items():
        print('{} : {}'.format(attribute, value))
    print(f"income : ${total_income}")


def off():
    print("Shutting down! ⏳")
    exit()


def calculate(quarter, dime, nickel, pennie):
    global total_income
    qs = quarter * 0.25
    ds = dime * 0.1
    ns = nickel * 0.05
    ps = pennie * 0.01
    total_payment = qs + ds + ns + ps
    return total_payment


def machine():
    global total_income
    order = input("What is your order? (espresso, latte, cappuccino): ")

    if order == 'espresso':
        if resources['water'] <= 50:
            print("Sorry! not enough Water.")
            return
        elif resources['coffee'] <= 18:
            print("Sorry! not enough Coffee.")
            return
        q = int(input("How many quarters: "))
        d = int(input("How many dimes: "))
        n = int(input("How many nickels: "))
        p = int(input("How many pennies: "))
        tp = calculate(q, d, n, p)
        if tp >= 1.5:
            if tp > 1.5:
                change_e = tp - 1.5
                tp_e = tp-change_e
                total_income += tp_e
                print(f"Here is ${round(change_e, 2)}, your change!")
        else:
            print("Transaction unsuccessful, money refunded!")
            return
        espresso()

    if order == 'latte':
        if resources['water'] <= 100:
            print("Sorry! not enough Water.")
            return
        elif resources['milk'] <= 150:
            print("Sorry! not enough Milk.")
            return
        elif resources['coffee'] <= 24:
            print("Sorry! not enough Coffee.")
            return
        q = int(input("How many quarters: "))
        d = int(input("How many dimes: "))
        n = int(input("How many nickels: "))
        p = int(input("How many pennies: "))
        tp = calculate(q, d, n, p)
        if tp >= 2.5:
            if tp > 2.5:
                change_l = tp - 2.5
                tp_l = tp - change_l
                total_income += tp_l
                print(f"Here is ${round(change_l, 2)}, your change!")
        else:
            print("Transaction unsuccessful, money refunded!")
            return
        latte()

    if order == "cappuccino":
        if resources['water'] <= 250:
            print("Sorry! not enough Water.")
            return
        elif resources['milk'] <= 100:
            print("Sorry! not enough Milk.")
            return
        elif resources['coffee'] <= 24:
            print("Sorry! not enough Coffee.")
            return
        q = int(input("How many quarters: "))
        d = int(input("How many dimes: "))
        n = int(input("How many nickels: "))
        p = int(input("How many pennies: "))
        tp = calculate(q, d, n, p)
        if tp >= 3.0:
            if tp > 3.0:
                change_c = tp - 3.0
                tp_c = tp - change_c
                total_income += tp_c
                print(f"Here is ${round(change_c, 2)}, your change!")
        else:
            print("Transaction unsuccessful, money refunded!")
            return
        cappuccino()

    if order == "report":
        report()
        return

    if order == "off":
        off()


cont = True

while cont:
    machine()
