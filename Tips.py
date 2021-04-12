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