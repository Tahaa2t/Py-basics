class User:     #definition of class
#    pass        #means we'll define later
    def __init__(self,user_id, username): #constructor
    #    pass
    #    print("New user created")   #everytime object is created, this function is called

        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    
    def follow(self,user):                #method always need a self parameter  
        self.following +=1
        user.followers +=1
        
    
    
    
    # def __init__(self):
    #     self.user_id = int(0)
    #     self.username = "N/A"

# user_1 = User()

#defining attributes
# user_1.id = 101
# user_1.username = "Ali"

#user_2 = User(int(100),"Ali")
#print(user_2.username, user_2.user_id)


user_1 = User(123,"Sameen")
user_2 = User(100,"Ali")
user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)