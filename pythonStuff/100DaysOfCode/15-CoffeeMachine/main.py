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
            "water": 500,
            "milk": 500,
            "coffee": 100,
            },
        "money": 25.00
        }

# function to check if there are enough resources to make drink
def check_resources(drink):
    resource_requirement = MENU[drink]['ingredients']
    for k,v in resource_requirement.items():
        if v > resources["ingredients"][k]:
            print(f"Sorry there is not enough {k}.")
            return False
    return True

# checks if user deposited enough coins to make a drink
def process_coins(drink):
    print("Deposit Coins:")
    quarters = float(input("Quarters: "))
    dimes = float(input("Dimes: "))
    nickels = float(input("Nickels: "))
    pennies = float(input("Pennies: "))
    total_pay = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    if total_pay < MENU[drink]['cost']:
        print("Sorry that's not enough money. Money refunded.")
    elif total_pay == MENU[drink]['cost']:
        make_coffee(drink, MENU[drink]['cost'])
    else:
        change = total_pay - MENU[drink]['cost']
        print(f"Here is ${change:.2f} dollars in change.")
        make_coffee(drink, MENU[drink]['cost'])

# makes drink and reduces resource by drink ingredients
def make_coffee(drink, change):
    for k,v in MENU[drink]['ingredients'].items():
        resources['ingredients'][k] -= v
    resources['money'] += change
    print(f"Your {drink.title()} is ready.")

run = True
while run:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        # end program
        break
    elif choice == 'report':
        # Print report 
        print(f"Water: {resources['ingredients']['water']}ml")
        print(f"Milk: {resources['ingredients']['milk']}ml")
        print(f"Coffee: {resources['ingredients']['coffee']}g")
        print(f"Money: ${resources['money']:.2f}")
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        if check_resources(choice) == True:
            process_coins(choice)
    else:
        print("Select an option.")
