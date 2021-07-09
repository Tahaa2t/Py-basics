from art import logo
import os
    
def CheckWinner(Bids_dict):
    i=int(0)
    winner = ""
    for person in Bids_dict:
        if i < Bids_dict[person]:
            i=Bids_dict[person]
            winner = person
    #End for
    print(f"Winner is: {winner} with highest bid: ${i}!")    


os.system('cls')
Bids_dict = {}
done = False
while not done:
    print(logo)
    name = input("Enter your name: ")
    bid = int(input("Enter your Bid: $"))
    Bids_dict[name] = bid

    x = input("Another Bidder? (Yes/No)" ).lower()
    if x == "no":
        done = True
    os.system('cls')

print(logo)
CheckWinner(Bids_dict)