# Class is a blueprint of an object 
class Animal():
    #constructor -- initializer -- defining attrivutes of the class
    def __init__(self, name, color, species):
        self.name = name
        self.color = color
        self.species = species
    
    def sound(self): 
        print("I don't make a sound. ")

class Bird(Animal):
    def __init__(self, name, color, species, canFly):
        super().__init__( name, color, species)
        self.canFly = canFly
    
    def sound(self):
        print("tweet tweet")

class Fish(Animal):
    def __init__(self, name, color, species, freshwater):
        super().__init__( name, color, species)
        self.freshwater = freshwater
    
    def safeToPutInHomeTank(self):
        if self.safeToPutInHomeTank:
            print('My name is', self.name,"put me in the tank")
        else:
            print('My name is', self.name,"put me in the ocean")

class Cat(Animal):
    pass
class Dog(Animal):
    pass



cat = Animal("Felix", "brown", "feline")
dog = Animal("Rover", "golden", "canine")
bird = Bird("Tweety", "yellow", "avian", True)
fish = Fish("Nemo", "orange", "clown fish", False)
Dori = Fish("Dori", "Blue", "Angle fish", False)

cat.sound()
dog.sound()
bird.sound()
fish.sound()
