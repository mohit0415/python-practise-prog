from abc import ABC,abstractmethod

class Behaviour(ABC):

    @abstractmethod
    def talk(self):
        pass

class Person(Behaviour):
    def talk(self):
        print("speaking")

class Dog(Behaviour):
    def talk(self):
        print("Barking")

com1 = Dog()

com1.talk()

