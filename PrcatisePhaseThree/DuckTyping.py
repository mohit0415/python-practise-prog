

class Dog:
    def shout(self):
        print("DOG is BARKING")

class Cat:
    def shout(self):
        print("CAT iS BARKING")


class Animal:
    def bark(self,breed):
        breed.shout()

animal = Animal()

breed = Cat()

animal.bark(breed)


        

