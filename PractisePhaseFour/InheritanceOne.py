import math
class Shape:
    def area(self):
        print("Area Not Implented")

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(math.pi * (math.pow(self.radius,2)))
class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        print(math.pow(self.side,2))

c = Circle(5)
sq = Square(6)

c.area()
sq.area()
        