# Class is a blueprint of an object 
class Animal():
    #constructor -- initializer -- defining attrivutes of the class
    def _init_(self, name, color, species):
        self.name = name
        self.color = color
        self.species = species
    
    def sound(): 
        print("I don't make a sound. ")

class Bird(Animal):
    pass

cat = Animal("felix", "brown", "feline")
dog = Animal("rover", "golden", "canine")
bird = Animal("Tweety", "yellow", "avian")
fish = Animal("Nemo", "orange", "clown fish")

cat.sound()
dog.sound()
bird.sound()
fish.sound()
