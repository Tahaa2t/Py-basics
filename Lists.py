nums = [1, 2, 3, 4]
floats = [1.1, 1.2, 1.3, 1.4]
strings = ["Apple", "mango", "orange", "peach"]

nums.append(23)     #apending 1 element
strings.extend(["strawberry", "blueberry", "guava"])    #append with another list

#print(nums) #prints whole list
#print(strings[3])   #prints the element on given index

#-------------------------dynamically making a list------------------------------
people = input("Enter names divided by \", \" ")    #Example string "Taha, Tahir, Zubair"

people_list = people.split(", ")       #to tell what is dividing the elements of list
print(people)       #prints as a string, every character is new element of string
print(people_list)  #prints by dividing the whole names as elements

#-------------------------Nested Lists------------------------------

fruits = ["Mangoes", "apples", "grapes"]
vegies = ["potato", "tomato", "carrot"]

edibles = [fruits, vegies]  #nested list

print(edibles)