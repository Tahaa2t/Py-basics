import random               #library for randomization


a = random.randint(1,3)     #gives a random number as 1-3 inclusively (including 1 and 3)
b = random.random()         #gives a float number as [0,1). Notice that 1 is exlusive
b = random.random()*5       #float [0,5)


love_compatibility = random.random()*100
print(f"Your compatibility with your loved one is: {round(love_compatibility,2)}%")


#-----------------------------Providing Seed value manually----------------------------------------
#simple head/tail program
seed_in = int(input("Enter Seed: "))        #Example 54324325429
random.seed(seed_in)                        #genrates Seed
coin = random.randint(1,100)
print(coin)
if coin % 2 == 0:
    print("Heads!")
else:
    print("Tails!")

#-----------------------------Combining Lists and Randomization--------------------------------------
#Decide who will pay the bill for Lunch

test_seed = int(input("Enter seed: "))
random.seed(test_seed)      #seed generation

people = input("Enter names divided by \", \" ")    #entering List by Split method
people_list = people.split(", ")        
list_len = len(people_list)             #len(list_var) shows number of elements in list

choice = random.randint(0,list_len-1)   #choosing a person randomly

print(f"{people_list[choice]} will pay the bill!")

#------------------------Simple way of randomly selecting element from list---------------------------

choice = random.choice(people_list)     #automatically chooses a random element

#-----------------------Rock-Paper-Scissors-------------------------------

print("🌑 ---- 📃 --- ✂️")

select = ["🌑","📃","✂️"]
ch_player = int(input("Enter choice:\n1)rock\n2)paper\n3)scissors\n\n"))
ch_player=select[ch_player-1]

ch_comp = random.choice(select)

print(f"Player's choice: {ch_player}\nComp's choice: {ch_comp}")
if ch_player == "🌑":
    if ch_comp == "📃":
        print("Comp Win!")
    elif ch_comp == "✂️":
        print("Player Win!")
    else:
        print("Drawww!")
elif ch_player == "📃":
    if ch_comp == "✂️":
        print("Comp Win!")
    elif ch_comp == "🌑":
        print("Player Win!")
    else:
        print("Drawww!")
elif ch_player == "✂️":
    if ch_comp == "🌑":
        print("Comp Win!")
    elif ch_comp == "📃":
        print("Player Win!")
    else:
        print("Drawww!")

#Check other Random commands from Google
