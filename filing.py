
#-----------------Reading from file-------------------------------

#Normal way to open  and close a file

file = open("py_file.txt")  #it will give error if no file exist with that name
contents = file.read()
print(contents)
file.close()


#this works same but you don't need to close file in the end
with open("py_file.txt") as file:
    contents = file.read()
    print(contents)
#when we open without providing a mode, it opens in read only mode

#---------------------Writing in file----------------------------

with open("py_file.txt", mode="w") as file:   #we must provide a writing mode for it
    file.write("New text.")


#---------------------Append in file----------------------------

with open("py_file.txt", mode="a") as file:
    file.write("\nNew text.")


#-------------------------------------------------------------
with open("py_file2.txt", mode="w") as file:    #just like in cpp, it creates a new file if there's no file with that name, only when we use Write mode
    file.write("\nNew text.")