from Files.day15 import MENU, resources


def get_first_resources():
    water = int(resources["water"])
    milk = int(resources["milk"])
    coffee = int(resources["coffee"])

    return water, milk, coffee


def check_resources(order, water, milk, coffee):
    preparation_order = False
    water_ingredient = False
    milk_ingredient = False
    coffee_ingredient = False

    if order == "espresso":
        if water < 50:
            print("Sorry there is not enough water.")
            return preparation_order, water, milk, coffee

        elif coffee < 18:
            print("Sorry there is not enough coffee.")
            return preparation_order, water, milk, coffee

        else:
            water -= 50
            coffee -= 18
            preparation_order = True
            return preparation_order, water, milk, coffee

    elif order == "latte":
        if water < 200:
            print("Sorry there is not enough water.")
            return preparation_order, water, milk, coffee
        elif milk < 150:
            print("Sorry there is not enough milk.")
            return preparation_order, water, milk, coffee
        elif coffee < 24:
            print("Sorry there is not enough coffee.")
            return preparation_order, water, milk, coffee
        else:
            water -= 200
            milk -= 150
            coffee -= 24
            preparation_order = True
            return preparation_order, water, milk, coffee

    elif order == "cappuccino":
        if water < 250:
            print("Sorry there is not enough water.")
            return preparation_order, water, milk, coffee
        elif milk < 100:
            print("Sorry there is not enough milk.")
            return preparation_order, water, milk, coffee
        elif coffee < 24:
            print("Sorry there is not enough coffee.")
            return preparation_order, water, milk, coffee
        else:
            water -= 250
            milk -= 100
            coffee -= 24
            preparation_order = True
            return preparation_order, water, milk, coffee


def check_money(quarters, dimes, nickles, pennies):
    quarters_value = float(0.25)
    dimes_value = float(0.10)
    nickles_value = float(0.05)
    pennies_value = float(0.01)

    total_money = (quarters * quarters_value) + (dimes * dimes_value) + \
                  (nickles * nickles_value) + (pennies * pennies_value)

    return total_money


def coffee_cost(order):
    if order == "espresso":
        cost = float(MENU["espresso"]["cost"])
    elif order == "latte":
        cost = float(MENU["latte"]["cost"])
    elif order == "cappuccino":
        cost = float(MENU["cappuccino"]["cost"])

    return cost


def change_money(total_money, order):
    cost = coffee_cost(order)

    change = total_money - cost

    return change


def coffee_machine():
    water, milk, coffee = get_first_resources()
    machine_on = True
    profit = 0

    while machine_on:
        prompt_input = input("What would you like? (espresso/latte/cappuccino):").lower()
        if prompt_input == "off":
            print("Turning off the coffee machine.")
            machine_on = False
            exit()
        elif prompt_input == "report":
            print(f"Water: {water}")
            print(f"Milk: {milk}")
            print(f"Coffee: {coffee}")
            print(f"Money: {profit}")
        elif (prompt_input == "espresso") or (prompt_input == "latte") or (prompt_input == "cappuccino"):
            order = prompt_input
            preparation, water, milk, coffee = check_resources(order, water, milk, coffee)
            if preparation:
                print("Please insert coins.")
                quarters_insert = float(input("how many quarters?:"))
                dimes_insert = float(input("how many dimes?:"))
                nickles_insert = float(input("how many nickles?:"))
                pennies_insert = float(input("how many pennies?:"))
                money_insert = check_money(quarters_insert, dimes_insert, nickles_insert, pennies_insert)
                order_cost = coffee_cost(order)

                if money_insert < order_cost:
                    print(f"Sorry that's not enough money. Money refunded.")
                else:
                    change = round(change_money(money_insert, order), 2)
                    profit += order_cost
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {order} ☕️. Enjoy!")
        else:
            print("Please select a valid comand")


coffee_machine()