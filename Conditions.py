#-----------------------------simple if else ------------------------------------
#BMI calculator
height = float(input("Enter height in cm: "))
weight = float(input("Enter weight in kg: "))

height = height/100

bmi = round(weight/(height**2))     #round = round off to nearest whole number

if bmi < 18.5:
    print(f"{bmi}: Underweight")
elif bmi < 25:                      #else if() <---cpp = elif <---Python
    print(f"{bmi}: Normal weight")
elif bmi < 30:
    print(f"{bmi}: overweight")
elif bmi < 35:
    print(f"{bmi}: obese")
elif bmi >= 35:
    print(f"{bmi}: overweight")
else:
    print("Enter correct weight")

#------------------------------Nested if else---------------------------------------
#Roller coaster ride,
# if heignt >= 120cm and age >= 10, charge 10$
# if heignt >= 120cm and age < 10, charge 7$
# if height < 120cm, not allowed

print("Welcome to rollercoaster")
height = int(input("Enter height in cm: "))
age = int(input("Enter age: "))
if height >= 120:   #>=, <=, >, <, ==, !=
    if age >= 10:
        print("You're good to go, 10$")
    elif age <10:
        print("You're good to go, 7$")
else:
    print("nope...!")

#for multiple conditions, use 'and'/'or'
# eg: if age < 10 and age >= 5: ...