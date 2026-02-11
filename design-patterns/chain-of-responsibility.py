# Steps:
# Step 1: Base handler
# Step 2: Concrete handlers
# Step 3: Build the chain

# 1
class Handler:
    def __init__(self, next_handler = None):
        self.next_handler = next_handler
    
    def handle(self,request):
        if self.next_handler:
            return self.next_handler.handle(request)

# 2

class Level1Support(Handler):
    
    def handle(self, request):
        if request == "Basic":
            print("Request solved")
        else:
            print("Request is passing to Level2Support...")
            return super().handle(request) # Parent of Level1 is Level2
        
class Level2Support(Handler):
    
    def handle(self, request):
        if request == "Medium":
            print("Request solved by Level 2 Support Agent")
        else:
            print("Request is passing Manager Support...")
            return super().handle(request) # Parent of Level2 is Manager
        
class ManagerSupport(Handler):
    
    def handle(self, request):
            print("Manager solved it")
     
# 3

manager = ManagerSupport()
level2 = Level2Support(manager)
level1 = Level1Support(level2)

level1.handle("Hard")


