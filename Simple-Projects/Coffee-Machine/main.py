from coffee_data import MENU
from art import LOGO
from os import system



def display_report(rep):
    for item in rep:
        print(f"{item.title()}: {rep[item]}",end="")
        if item == "water" or item == "milk":
            print("ml")
        if item == "coffee":
            print("g")
        if item == "money":
            print("$")


def check_res(ch,rep):
    if ch == "espresso":
        if MENU[ch]["ingredients"]["water"] <= rep["water"] and MENU[ch]["ingredients"]["coffee"] <= rep["coffee"]:
            MENU[ch]["ingredients"]["water"] -= rep["water"]
            MENU[ch]["ingredients"]["coffee"] -= rep["coffee"]
            return True
        else:
            return False
    else:
        if MENU[ch]["ingredients"]["water"] <= rep["water"] and MENU[ch]["ingredients"]["coffee"] <= rep["coffee"] and MENU[ch]["ingredients"]["milk"] <= rep["milk"]:
            rep["water"] -= MENU[ch]["ingredients"]["water"] 
            rep["coffee"] -= MENU[ch]["ingredients"]["coffee"]
            rep["milk"] -= MENU[ch]["ingredients"]["milk"]
            return True
        else:
            return False


def get_check_money(ch,rep):
    print(f"Your {ch.title()} is on it's way, it would be $",end="")
    print(MENU[ch]["cost"])
#TODO 4. ask for money in coins
    q = int(input("Enter quarters: "))
    d = int(input("Enter dimes: "))
    n = int(input("Enter nikle: "))
    p = int(input("Enter pennies: "))
    
    total = 0.25*q + 0.1*d + 0.05*n + 0.01*p
    if total >= MENU[ch]["cost"]:
        rep["money"] += MENU[ch]["cost"]
        return round(total - MENU[ch]["cost"],2)

    else:
        return -1

def Want():
    ans = input("Want coffee? (y,n): ").lower()
    if ans == "y":
        return True
    else:
        False


report = {
    "water":300,
    "milk":200,
    "coffee":100,
    "money":int(0)
}
change = 0
Use = True

while Use:
    print(LOGO)
#TODO 1. ask user the type of coffee
    choice = input("What type of coffee you'd like? (Espresso/Latte/Cappuccino): ").lower()
#TODO 2. print the report
    if choice == "report":
        display_report(report)
    elif choice != "espresso" and choice != "latte" and choice != "Cappuccino":
        print("Enter Valid Coffee...!")
#TODO 3. checks the resourses
    else:
        if check_res(choice,report) == True:
#TODO 5. check if money is sufficient
            change = get_check_money(choice,report)
            if change == -1:
                print("Not enough cash, refunding all Money...")
            else:
                print(f"here's your change of ${change}, Enjoy your coffee!")
        else:
            print(f"Not enough resources for {choice.title()}, try another time.")
    Use = Want()
    system('cls')








