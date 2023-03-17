class Animal:
    def __init__(self,name):
        self.name = name
    def talk(self):
        raise NotImplementedError("Error")

class Cat(Animal):
    def talk(self):
        return "meow"

class Dog(Animal):
    def talk(self):
        return "woof"

# Animal.talk("Dog") # it will give erro

animals  = [
    Cat("Rekha"),
    Cat("Sonia"),
    Dog("Moti"),
    Cat("Rupa"),
    Dog("Gabber")
    
]
for animal in animals:
    print(animal.name, " - ",animal.talk())