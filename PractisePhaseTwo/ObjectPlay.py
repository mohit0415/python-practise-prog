class Computer:
    def __init__(self,cpu,ram,os):
        self.cpu=cpu
        self.ram=ram
        self.os=os
    def config(self):
        self.ram = "100TB"

com1 = Computer("i5","16GB","Windows")
com2 = Computer("Ryzen 5","32GB","Linux")

print(com1.cpu)
print(com2.os)

com1.os="MAC"

print(com1.os)

com1.config()

print(com1.ram)


class Student:

    dept = "CSE"

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def compare(self,other):
        if(self.age == other.age):
            return True
        else:
            return False
    
s1=Student("John",20)
s2=Student("Alice",20)

if s1.compare(s2):
    print("Same Age")
else:
    print("Diffrenet AGe")

print(s1.dept)
print(s2.dept)

Student.dept = "ECE"

print(s1.dept)
print(s2.dept)

class Professor:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

p1=Professor(0,0,0)
p1.m1=85
p1.m2=90
p1.m3=100

print(p1.avg())

users=["admin","guest","guest","user"]

for u in users:
    if(u=="guest"):
        users.remove(u)
print(users)