class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def set_name(self,value):
        self.name=value
    def set_age(self,value):
        self.age=value
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

stud1=Student("Mohit",15)
stud2=Student("Sai",30)

print(stud1.name)
print(stud1.age)

stud1.set_name("Rahul")
stud1.set_age(20)


print(stud1.get_name())
print(stud1.get_age())




        