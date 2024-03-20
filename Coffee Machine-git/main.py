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

# defining the variables for use.

# espresso
espresso_w = MENU["espresso"]["ingredients"]["water"]
espresso_c = MENU["espresso"]["ingredients"]["coffee"]
espresso_cost = MENU["espresso"]["cost"]

# latte
latte_w = MENU["latte"]["ingredients"]["water"]
latte_c = MENU["latte"]["ingredients"]["coffee"]
latte_m = MENU["latte"]["ingredients"]["coffee"]
latte_cost = MENU["latte"]["cost"]

# cappuccino
capp_w = MENU["cappuccino"]["ingredients"]["water"]
capp_c = MENU["cappuccino"]["ingredients"]["coffee"]
capp_m = MENU["cappuccino"]["ingredients"]["milk"]
capp_cost = MENU["cappuccino"]["cost"]

# MENU
print(f'''_____MENU_____
1. Espresso - {espresso_cost}
2. Latte - {latte_cost}
3. Cappuccino - {capp_cost}''')

# taking inputs from user
order = input("What would you like? (espresso / latte / cappuccino): ")
quarters = int(input("How many quarters? "))
dime = int(input("How many dimes? "))
nickles = int(input("How many nickles? "))
pennies = int(input("How many pennies? "))

# quarters = $0.25
# dimes    = $0.1
# nickles  = $0.05
# pennies  = $0.01


# functions for beverages
def espresso():
    global resources, espresso_w, espresso_c
    resources['water'] -= espresso_w
    resources['coffee'] -= espresso_c
    return resources


def latte():
    global resources, latte_w, latte_m, latte_c
    resources['water'] -= latte_w
    resources['milk'] -= latte_m
    resources['coffee'] -= latte_c
    return resources


def cappuccino():
    global resources, capp_w, capp_m, capp_c
    resources['water'] -= capp_w
    resources['milk'] -= capp_m
    resources['coffee'] -= capp_c


def calculate():
    global quarters, dime, nickles, pennies
    q_cal = quarters * 0.25
    d_cal = dime * 0.1
    n_cal = nickles * 0.05
    p_cal = pennies * 0.01
    payment = q_cal + d_cal + n_cal + p_cal
    return payment


# for payment calculations
p = calculate()

if order == 'espresso':
    if p == 1.5:
        espresso()
        print('Enjoy your espresso! ☕')
    else:
        print('Not enough money! refunded 💵')
elif order == 'latte':
    if p == 2.5:
        latte()
        print('Enjoy your latte! ☕')
    else:
        print('Not enough money! refunded 💵')
elif order == "cappuccino":
    if p == 3.0:
        cappuccino()
        print('Enjoy your cappuccino! ☕')
    else:
        print('Not enough money! refunded 💵')
else:
    print("sorry, can't make a coffe right now!")
print(resources)
