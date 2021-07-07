import random
import os
import time
import Logo_art
import List_of_words
print(Logo_art.Logo)
time.sleep(2)
os.system('cls')


chosen = random.choice(List_of_words.words)

liner = []
for i in chosen:
    liner.append("_")

end_of_game=False
found=False
present = False
lives = 0
print(Logo_art.stages[lives])
print(liner)
while not end_of_game:
    
    guess = input("guess the character: ")
    for i in range(len(liner)):
        if chosen[i]==guess:
            found = True
            if liner[i]==guess:
                present = True
            #end if
            liner[i] = guess
        #end if   
    #for End    
    os.system('cls')
    if found == False:
        print(f"the letter {guess} isn't present in it, You lost a life")
        lives+=1
    elif present == True:
        print(f"You already selected letter {guess}, try something else")
    #end if

    print(Logo_art.stages[lives])
    print(liner)
    found = False
    present = False
    if lives == 6:
        end_of_game=True
        print(f"The word is '{chosen}'. You Loose!")
    elif "_" not in liner:
        end_of_game=True
        print("The word is \"{chosen}\", You Won!")
    #end if
#end while