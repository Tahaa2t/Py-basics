def first_funct():      #function definition
    print("hello")

first_funct()           #function calling

def para_funct(name):   #Function with parameter
    print(f"hello {name}")

para_funct("Taha")


def adding(num1, num2):
    print(f"{num1}+{num2} = {num1+num2}")

adding(int(4),int(6))

#------------------check Prime number-----------------------
def PrimeCheck(num):
    check = True
    i=int(2)
    while i < num and check == True:
        if num%i == 0:
            check = False
        i+=1

    if check == True:
        print("It is a Prime Number")
    else:
        print("It is not a prime number")


n = int(input("Enter number: "))
PrimeCheck(n)


#---------------area calculation-----------------------------
import math
def area_calc(ht,wd,cov):
    total_cans = (ht*wd)/cov
    print(f"Total amount cans to be used are: {math.ceil(total_cans)}") #if 20.1 is answer, we still need 22 cans so we use ceiling function "math.ceil(num)" instead of" round(num,0)"

width = int(input("Enter Width: "))
height = int(input("Enter Height: "))
cover = int(input("total coverage by 1 can: "))

area_calc(height,width,cover)

