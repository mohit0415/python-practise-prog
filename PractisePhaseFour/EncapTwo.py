class Person:
    def __init__(self,age):
        self.__age = age
    def get_Age(self):
        return self.__age
    def set_Age(self,value):
        if(value <= 0):
            raise Exception("Invalid Age")
        else:
            self.__age = value

personOne = Person(10)

try:
    personOne.set_Age(90)
    print(personOne.get_Age())
except Exception as e:
    print(e)