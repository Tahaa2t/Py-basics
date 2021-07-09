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



#return value from function

def func1():    #definition
    x=10+5
    return x

calc = func1()  #calling
print(calc)
#----------Full name--------------

def func2(f_name,l_name):
    full_name = f_name.title()  #title() converts any sentence into "Sentence Case"
    full_name+= " "
    full_name+= l_name.title()
    return full_name

f_name = "TaHA"
l_name = "tAnNVEEr"
name = func2(f_name,l_name)
print(f"full name is: {name}")

#------------another way---------------

def func2(f_name,l_name):
    
    return f"{f_name.title()} {l_name.title()}"

f_name = "TaHA"
l_name = "tAnNVEEr"
name = func2(f_name,l_name)
print(f"full name is: {name}")


#---------------------DocString-----------------------

def func3():
    """ This function           
    returns my name """     #This is a docstring, used to define what this function do
    return "Taha Tanveer"

name = func3()              #hover over func3(), it will show docstring as discription of function


