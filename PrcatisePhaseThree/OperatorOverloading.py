class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        sub1 = self.m1 + other.m1
        sub2 = self.m2 + other.m2
        s3 = Student(sub1,sub2)
        return s3
    def __str__(self):
        return ('{} {}'.format(self.m1,self.m2))

stud1=Student(10,20)
stud2=Student(30,40)

stud3=stud1+stud2

print(stud3)