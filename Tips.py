print("Hello, \"WORLD\" ")   #to add quotation marks in your print statement, write \"text\"


print("Hello"[3]) #3rd index will be printed


x = 123_456_789 #it's a way to write 123,456,789 (interpreted as 123456789)


print(type(x)) #prints the data type of var


str(x) #converts integer variable into a string

y = 2.84546
print("number is: ", int(y))    #chopping: chops off number after decimal, output = 2



print("number is: ", round(y))  #rounding: rounds off number, output = 3



print("number is: ", round(y, 2))  #rounding and specify decimal places, output = 2.84


#Type casting
print(70 + float("100.5"))  #outout = 170.5, bcz it converts string "100.5" to float and adds to 70
print(str("70") + str("100.5"))  #output = 70100.5, bcz 2 'strings' are being concatenated

#lower/upper casing
name = input("Enter name: ")    #Taha
name = name.lower()             #taha
name = name.upper()             #TAHA


#imagine you don't know how many elements are in the list and you have to get last one...
num1 = [1, 2, 3, 4]
print(num1[-1])          #this will help



heights = input("Enter heights divided by space: ").split()    #simple Way to create a list
avg_ht = sum(int(heights))/len(heights)         #simple way to find average
Max_ht = max(heights)                           #simple way to find Maximum height


import math
num1=float(4.2)
math.ceil(num1) #output = 5
math.floor(num1) #output = 4


name = input("Enter name").title()      #sentence case (first alphabet of every word will be uppercase, rest is lowercase)


#use a global variable in function without passing as argument
num2 = 3
def adder():
    global num2
    num2+=1


#find max min in list of dictionaries

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    }]  #we need to find max follower count

m = [x['follower_count'] for x in data]
max(m)
min(m)