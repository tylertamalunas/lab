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
        "ingredients": {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            },
        "cost": 5.00
        }

# function to check if there are enough resources to make drink
def check_resources(drink):
    resource_requirement = MENU[drink]['ingredients']
    for k,v in resource_requirement.items():
        if v > resources["ingredients"][k]:
            return f"Sorry there is not enough {k}."

# checks if user deposited enough coins to make a drink
def process_coins(drink):
    print("Deposit Coins:")
    quarters = float(input("Quarters: "))
    dimes = float(input("Dimes: "))
    nickels = float(input("Nickels: "))
    pennies = float(input("Pennies: "))
    total_pay = quarters + dimes + nickels + pennies
    if total_pay < MENU[drink][cost]:
        return "Sorry that's not enough money. Money refunded."
    elif total_pay == MENU[drink][cost]:
        make_coffee(drink, total_pay)
    else:
        make_coffee(drink, total_pay)
        change = total_pay - MENU[drink][cost]
        return f"Here is ${change.:2f} dollars in change."

# makes drink and reduces resource by drink ingredients
def make_coffee(drink, change):
    for k,v in MENU[drink][ingredients]:
        resources[k] -= v
    for v in MENU[drink]["cost"]:
        resources['cost'] += change


run = True
while run:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'espresso':
        check_resources(choice)
    elif choice == 'latte':
        check_resources(choice)
    elif choice == 'cappuccino':
        check_resources(choice)
    elif choice == 'off':
        # end program
        break
    elif choice == 'report':
        # Print report 
        for k,v in resources.items():
            print(f"{k.upper()}: {v}")
    else:
        print("Select an option.")
