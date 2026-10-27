from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def sleep(self):
         print("Sleeping...")

class Dog(Animal):
    
    def make_sound(self):
        print("Woof")

    def move(self):
        print("Walking...")

class Cat(Animal):

    def make_sound(self):
            print("Woof")
    
    def move(self):
        print("Walking...")
    
class Bird(Animal):

    def make_sound(self):
            print("Woof")
    
    def move(self):
        print("Walking...")
    
class Fish(Animal):
    pass

dog = Dog()
cat = Cat()
bird = Bird()
fish = Fish()

dog.make_sound()