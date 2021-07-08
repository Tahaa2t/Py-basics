#just like normal disctionary, we give name (key) and it's definition (Value)
#Syntax: dict1 = {key1:value1, key2:value2,...,key-n:value-n}


dict1 = {
"Bug":"An error in a Program",
"Function":"A piece of code that you can easily call",
}

#Usage...
print(dict1["Bug"])    #it will print the value

#append dictionary
dict1["Loop"] = "The action of doing something over and over again"

#initialize empty dictionary
empty_dict = {}

#wipe a dictionary
dict1 = {}

#edit value of a key in a dictionary
dict1["Bug"] = "An insect that can fly"

#loop through dictionary
for thing in dict1:
    print(thing)            #prints KEY
    print(dict1[thing])     #prints VALUE

#-----------------------Grading students-----------------------------

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for stud in student_scores:
    print(stud,end=": ")
    if student_scores[stud] <= 70:
        student_grades[stud] = "Fail"
    elif student_scores[stud] > 70 and student_scores[stud] <=80:
        student_grades[stud] = "Acceptable"
    elif student_scores[stud] > 80 and student_scores[stud] <=90:
        student_grades[stud] = "Exceeds Expectations"
    elif student_scores[stud] > 90 and student_scores[stud] <=100:
        student_grades[stud] = "Outstanding"
    print(student_grades[stud])

#------------------------Nesting Dict and Lists------------------------------

#normal
capitals = {
    "France":"Paris",
    "Germany":"Berlin"
}

#nesting a LIST in DICTIONARY
travel_log = {
    "Framce":["Paris", "Lillie","Dijon"],
    "Germany":["Berlin", "Hamburg", "Stuttgart"]
}

#nesting a DICTIONARY in DICTIONARY

Detailed_travel_log = {
    "Framce":
    {
        "Paris":3,
        "Lillie":2,
        "Dijon":5
    },
    "Germany":
    {
        "Berlin":2, 
        "Hamburg":3, 
        "Stuttgart":3
    }
    
} 

#or

Detailed_travel_log_2 = {
    "Framce":
    {
        "cities visited":["Paris", "Lillie","Dijon"],
        "Total Visits":10
    },
    "Germany":
    {
        "cities visited":["Berlin", "Hamburg", "Stuttgart"],
        "Total Visits":8
    }

}


#nesting a DICTIONARY in LIST

Detailed_travel_log_3 = [
    {
        "Country":"Framce",
        "cities visited":["Paris", "Lillie","Dijon"],
        "Total Visits":10
    },
    {
        "Country":"Germany",
        "cities visited":["Berlin", "Hamburg", "Stuttgart"],
        "Total Visits":8
    }

]


