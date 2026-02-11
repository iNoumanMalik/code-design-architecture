# Problem
#btw following can be class
def user(id,name,age,height,weight,salary,muslim,coder): # first think to notice we have to many parameters most of them can be null
    print("Hello")
    


# user(1,"Nouman") # TypeError: user() missing 6 required positional arguments: 'age', 'height', 'weight', 'salary', 'muslim', and 'coder'
user(1,"Nouman",None,None,None,None,False,True) # It was hard to place write placeholder, position also matters, it is now hard to read, what does False and True means

# Solution - Builder (when we have many optional parameters, when we want clean object creation, when we want order should not matters)

# Step 1 - Create the Product

class User:
    def __init__(self,id,name,age=None,is_active=True):
        self.id = id
        self.name = name
        self.age = age
        self.is_active = is_active
    
    def __str__(self):
        return print(f"Name: {self.name}")
        
# Step 2 - Create the Builder

class UserBuilder:
    def __init__(self):
        self.id = None
        self.name = None
        self.age = None
        self.is_active = True

    def set_name(self,name):
        self.name = name
        return self
    
    def set_id(self,id):
        self.id = id
        return self
    
    def set_age(self,age):
        self.age = age
        return self
    
    
    def build(self):
        return User(self.name,self.id,self.age)
    
    
UserBuilder().set_id(1).set_name("Nouman").set_age(21).build()