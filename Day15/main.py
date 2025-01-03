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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
n="ingredients"
def is_resourceinsufficent(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            return False
        return True
def process_coin():
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
def is_transaction_successful(money_received,Drinks_cost):
    if money_received>Drinks_cost:
        change=money_received-Drinks_cost
        print(change)
        global profit
        profit+=Drinks_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def make_coffee(drink_name,order_of_ingrident):
    print(f"Here is your {drink_name} ☕️. Enjoy!")
    for i in order_of_ingrident:
        resources[i]-=order_of_ingrident[i]
is_on=True
while is_on:
    choice=input("​What would you like? (espresso/latte/cappuccino): ")
    if choice=='off':
        is_on=False
    elif choice=='report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink=MENU[choice]
        payment=process_coin()
        if is_resourceinsufficent(drink['ingredients']):

            if is_transaction_successful(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])





