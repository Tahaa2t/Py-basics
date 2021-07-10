import random
from art import logo

def check_diff():
    global diff
    if diff == "easy":
        return 10
    elif diff == "hard":
        return 5
    else:
        return 0

def guess_check(guess,rand):
    global chances
    if guess > rand:
        print("Too High,",end = " ")
        chances-=1
        if chances != 0:
            print("guess again!")
        else:
            print("You've run out of chances!")
        return False
    elif guess < rand:
        print("Too Low,",end = " ")
        chances-=1
        if chances != 0:
             print("guess again!")
        else:
            print("You've run out of chances!")
        return False
    elif guess == rand:
        print(f"Correct guess! the number was {rand}")
        return True

print(logo)

rand = random.randint(1,100)
print("I've selected a number from 1 - 100. Can you guess it??\n Mode? (easy/hard)")
diff = input(" Difficulty? (easy/hard): ").lower()

flag = False
while not flag:
    chances = check_diff()
    if chances != 0:
        flag = True
    else:
        diff = input("Enter correct difficulty (easy/hard): ").lower()


won = False

while not won and chances != 0:
    guess = int(input(f"Guess Number, {chances} chances remaining: "))
    won = guess_check(guess,rand)
    
if won == True:
    print("You Won!")
else:
    print("You Lose!")