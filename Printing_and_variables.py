#print(...) prints stuff
print("Hello, World")
print('Hello, World')
print("Hello, \"WORLD\" ")   #to add quotation marks in your print statement
# input("...") always take input in string
country = input("What's the name of the country you grew up in\n")  #takes input in variable country as a string

pet = input("What's the name of your first pet\n")

age = int(input("Age of your pet: "))                       #int(input(...))whatever you input, int makes it integer

weight = float(input("Age of your pet: "))                  # we can use int, float, str, etc etc


print("Your band name could be:",country,pet)               #to print varibles in print statement

print(f"Your band name could be: {country} {pet}")          #another way of writing,  use f before quotation marks
                                                            #and write variables in {}


#-------------------------------------TIP----------------------------------------------
print("Your band name could be:",country,pet), #then automatically spaces are added
print("Your band name could be:"+country+pet), #then no automatic spaces 

#--------------------------------------------------------------------------------------


#-------TO SHOW LENGTH OF STRING---------------

print(len(input("Enter Name"))) #You enter name, it shows the length of string

#how this program works:
#1) print(len(input("Enter Name")))
#2) print(len("Taha"))
#3) print("4")
#output: 4
#----------------------------------------------