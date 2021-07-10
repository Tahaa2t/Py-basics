import random
import os
from art import logo
def Winner(P,D):
    """to check who is the winner"""
    if P :
        return "You're BUST!, Dealer Won!"
    elif D :
        return "Dealer is BUST!, You Won!"
    elif add_cards(player_cards) > add_cards(dealer_cards):
        if add_cards(player_cards)==21:
            return"You got BlackJack!, you Won!"
        else:
            return "You're closer to 21, you Won!"
    elif add_cards(player_cards) < add_cards(dealer_cards):
        if add_cards(dealer_cards) == 21:
            return "Dealer got BlackJack!, you Lost!"
        else:
            return "Dealer is closer to 21, you Lost!"
    elif add_cards(player_cards) == add_cards(dealer_cards):
        return "Match is draw!"

def deal_card(listt):
    """For dealing cards from deck"""
    listt.append(random.choice(cards))
    if listt[-1] == 11:
        if add_cards(listt)  > 21:
            listt[-1] = 1
        #end if
    #end if
#end def
def add_cards(listt):
    """Adding all the cards player/dealer has"""
    return sum(listt)
#end def



cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

ender = False
if input("Do you want to play BlackJack? (yes/no): ").lower() == "no":
    ender = True

while not ender:
    player_cards = []
    dealer_cards = []
    stand = False
    P_Bust = False
    D_Bust = False

    os.system('cls')
    print(logo)

    print("\nDealing first 2 cards: \n---------------------\n")
    for i in range(2):
        deal_card(player_cards)
        deal_card(dealer_cards)

    print(f"Your cards: {player_cards} = {add_cards(player_cards)}\nDealer cards: [{dealer_cards[0]},?]")
    if add_cards(player_cards) == 21:
        stand = True
    print("\nYour Turn:\n----------------\n")
    while not stand:

        choice = input("Hit another card? (yes/no): ").lower()
        if choice == "no":
            stand = True
        elif choice == "yes":
            deal_card(player_cards)

        print(f"\nYour cards: {player_cards} = {add_cards(player_cards)}\nDealer cards: [{dealer_cards[0]},?]")
        if add_cards(player_cards) > 21:
            stand = True
            P_Bust = True
    #End while

    if not P_Bust:
        print("\nDealer's Turn:\n----------------\n")
        print(f"\nYour cards: {player_cards} = {add_cards(player_cards)}\nDealer cards: {dealer_cards} = {add_cards(dealer_cards)}")
        while add_cards(dealer_cards)<17:
            deal_card(dealer_cards)
            print(f"\nYour cards: {player_cards} = {add_cards(player_cards)}\nDealer cards: {dealer_cards} = {add_cards(dealer_cards)}")
            if add_cards(dealer_cards) > 21:
                D_Bust = True

    print("\nRESULTS!\n---------\n")

    print(Winner(P_Bust,D_Bust))
    
    if input("Do you want to play again? (yes/no): ").lower() == "no":
        ender = True
