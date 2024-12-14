class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return None

class Cat(Animal):
    def sound(self):
            return "Мяу"
    
class Dog(Animal):
    def sound(self):
        return "Гав"     

dog = Dog("Bob")
cat = Cat("Tom")

print(dog.sound())
print(cat.sound())