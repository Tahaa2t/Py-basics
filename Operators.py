# x = 1 + 2
# x =  4 - 2
# x =  8 * 4
# x =  4 / 3 (gives answer in float)
# x =  3 ** 2 (3 with power of 2)
# x =  3 // 2 (3 divided by 2 but answer in integer)
# a /= 2 (a = a / 2), a += 2 (a = a + 2)

# Pemdas rule: 1)Parameter, 2)Exponent, 3)Multiply, 4)Divide, 5)Addition, 6)Subtraction


#--------------------Working pattern example-------------------
print( 3 * 3 + 3 / 3 - 3)
# print( 9 + 3 / 3 - 3)
# print( 9 + 1.0 - 3)
# print( 10.0 - 3)
# print( 7.0 )
#--------------------------------------------------------------

#--------------------Tip Calculator---------------------

# if bill = $150 and ppl are 5, with 12% tip
# for tip we do 150 * 0.12 and then divide in 5 ppl
# but for directly divide bill + tip among 5 ppl
# we do 150 * (1[total amount] + 0.12[tip amount])
# so, (150 * 1.12)/5

print("Welcome to the tip calculator!!\n")
Bill = float(input("What was the total bill? $"))
percent = int(input("percent of tip (10, 12, 15): "))
ppl = int(input("No. of people: "))

total_div = (Bill*((percent/100)+1))/ppl

print(f"Each person should pay: {round(total_div, 2)}")

#--------------------------------------------------------

#--------------------BMI Calculator---------------------
H = input("Enter height (in m): ")
W = input("Enter weight (in Kg): ")

H=float(H)
W=float(W)


BMI = W/(H**2)
print("Your BMI is: ", int(BMI))    #chopping
print("Your BMI is: ", round(BMI))  #rounding
print("Your BMI is: ", round(BMI, 2))  #rounding and specify decimal places
#---------------------------------------------------------

#------------------adding digits of 2 digit number----------------------------------------------------------

num = input("Enter number: ")       #Enter 2 digit number, input will be in string by default
print(type(num))                    #<class 'str'>
print(int(num[0]) + int(num[1]))    #'int' will convert each index element to integer, then '+' will add both

#------------------------------------------------------------------------------------------------------------