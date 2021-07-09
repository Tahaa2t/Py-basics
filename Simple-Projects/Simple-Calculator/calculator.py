from art import logo
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

def calculator():
    num1 = round(float(input("Enter 1st number: ")),4)

    end = False
    choice=0
    while not end:

        num2 = round(float(input("Enter next number: ")),4)

        for op in calc_dict:
            print(op,end="  ")

        operator = input("Enter operator from list: ")
        caller = calc_dict[operator]
        answer = round(caller(num1,num2),4)
        print(f"{num1} {operator} {num2} = {answer}")

        choice = float(input("\n1) calculate another number\n2)restart calculator\n3)end\n"))
        if choice != 1:
            end = True
        num1=answer
    if choice == 2:
        return False
    elif choice == 3:
        return True 


print(logo)
calc_dict ={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
    }
Full_end = False
while not Full_end:
    Full_end = calculator()

