class Observer:
    def update(self,message): # we need this interface for polymorphism
        pass
    
class Subscriber(Observer):
    def __init__(self,name):
        self.name = name
        
    def update(self,message):
        print(f"{self.name} received message {message}")
        
class Channel:
    def __init__(self):
        self.subscribers = []
    
    def add_subscriber(self, observer):
        self.subscribers.append(observer)
    
    #notify doesn't know the internal behavior of how message is sent, it just pass message 
    def notify(self,message):
        for sub in self.subscribers:
            sub.update(message)
    
def main():
    channel = Channel() # through channel we can add observers and notify that observers
    
    sub1 = Subscriber("Nouman")
    sub2 = Subscriber("Yashfa")
    sub3 = Subscriber("Asfand")
    
    channel.add_subscriber(sub1)
    channel.add_subscriber(sub2)
    channel.add_subscriber(sub3)
    
    channel.notify("Black Friday Sale Alert! Upto 50% on all products.")
    
    
main()
        