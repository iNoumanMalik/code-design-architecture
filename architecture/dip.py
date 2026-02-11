#dependency inversion principle

#without dip:
class MySqlDatabase:
    def save(self,user):
        print("user stored")
        
class UserService: #High level Business Model is highly dependent on MySqlDatabase which is Low level model
    mydb = MySqlDatabase()
    def __init__(self,user):
        mydb.save(user)
        

#with dip:
class Database(): #created interface
    def save(self, user): raise NotImplemented #abstract method
    
class MySql(Database): #Low level model is dependent on abstract methods
    def save(self, user):
        print("User Saved")
        
class UserService(): #High level module is not aware of internal behavior of MySql
    def __init__(self,db:Database):
        self.db = db
        
    def register_user(user):
        self.db.save(user)
        

service = UserService(MySql()) #Dependency Injection