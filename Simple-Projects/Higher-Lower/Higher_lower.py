import random
from game_data import data
from art import logo,vs
from os import system
from time import sleep

def chooser(s1,s2):
    select_1 = s1
    select_2 = s2
    diff = False
    while not diff:
        if select_1 != select_2:
            diff = True
        else:
            select_2 = random.choice(data)
        #end if
    #end while    
    global verses
    verses = []
    verses.append(select_1)
    verses.append(select_2)

starter = False
while not starter:
    system('cls')
    print(logo)
    sleep(2)
    verses = []
    score = 0
    wrong = False
    chooser(random.choice(data),random.choice(data))

    while not wrong:
        system('cls')
        print(verses[0]["name"],end=", ")
        print(verses[0]["description"],end=", ")
        print(verses[0]["country"])
        print("Total followers:", verses[0]["follower_count"])

        print(vs)

        print(verses[1]["name"],end=", ")
        print(verses[1]["description"],end=", ")
        print(verses[1]["country"])

        choice = input("How many followers does the second one has (More/Less): ").lower()

        m = [x['follower_count'] for x in verses]

        if (verses[1]['follower_count'] == max(m) and choice == "more") or (verses[1]['follower_count'] != max(m) and choice == "less"):
            score+=1
            print(f"Correct! your score is {score}")
            chooser(verses[1],random.choice(data))   
        else:
            print("Total followers:", verses[1]["follower_count"])
            print(f"Wrong! Your final score is {score}")
            wrong = True
    if input("Wanna play again (yes/no): ") == "no":
        starter = True



