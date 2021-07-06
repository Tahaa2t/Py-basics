fruits = ["apple","mango", "grapes"]
for fruit in fruits:    #assigns each element to variable "fruit" in each iteration
    print(fruit, end=" ")

x=0
for i in range(0,10):   #loop of 10 iterations. Adding 1 in i at every iteration (i starts from 0 ends at 9)
    x+=10

for i in range(0,10,2):   #loop of 10/2 iterations. i value updates by adding 2 in every iteration
    x+=10


#-----------------Add even numbers between 1-100-------------------------------
total=0
for i in range(2,101,2):
    total+=i
print(total)


#---------------------------FizzBuzz---------------------------------------
#for a multiple of 3, print Fizz. For multiple of 5, print Buzz. For multiple of both, print FizzBuzz, else print the number
a_list = list(range(1,101))
for i in a_list:
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0 and i%5!=0:
        print("Fizz")
    elif i%3!=0 and i%5==0:
        print("Buzz")
    elif i%3!=0 and i%5!=0:
        print(i)

#-------------------------Password Generator------------------------------

import string
import random
letters = list(string.ascii_lowercase)      #make list of all lowercase
letters2 = list(string.ascii_uppercase)     #make list of all uppercase
letters.extend(letters2)                    #extend lowercase with uppercase

numbers = list(range(0,10))                 #make a list of numbers 0-9

symbols = list(string.punctuation)          #list of symbols

let = int(input("Enter number of letters: "))
num = int(input("Enter number of numbers: "))
sym = int(input("Enter number of symbols: "))

password = []                               #list with no elements


for i in range(0,let):                      #for random letters
    password.append(random.choice(letters))

for i in range(0,num):                      #for random numbers
    password.append(str(random.choice(numbers)))

for i in range(0,sym):                      #for random symbols
    password.append(random.choice(symbols))

random.shuffle(password)                    #shuffle the elements from list

pass_str = ""                               #empty string
for char in password:
    pass_str += char                        

print(f"Your Password is: {pass_str}",end=" ")  #password generated
