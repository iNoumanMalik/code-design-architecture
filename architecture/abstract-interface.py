from abc import ABC,abstractmethod

#abstract class
class Animal(ABC):
    @abstractmethod #no implementation
    def make_sound(self): #abstract
        pass
    
    def sleep(self): #concrete
        print("Sleeping...")

class Dog(Animal):
    def make_sound(self): #must implement this
        print("Woof!")
        
class Cat(Animal):
    def make_sound(self): #must implement this
        print("Meaw!")


#Interface
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

#unrelated classes are implementing the interfaces
class Bird(Flyable):
    def fly(self):
        print("Bird is flying")

class Airplane(Flyable):
    def fly(self):
        print("Airplane is flying")





# animal = Dog()
# animal.make_sound()
# animal.sleep()


#Polymorphism: Object respond to same method call in a different way
animals = [Dog(),Cat()]
for a in animals:
    a.make_sound()

# bird = Bird()
# bird.fly()

# airplane = Airplane()
# airplane.fly()

flyers = [Airplane(),Bird()]
for f in flyers:
    f.fly()




