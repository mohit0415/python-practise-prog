
class Addition:
    def calculate(self,a,b):
        print(a+b)

class Subtraction:
    def calculate(self,a,b):
        print(a-b)


class Calculation:
    def calc(self,calci,a,b):
        calci.calculate(a,b)

calculating = Calculation()

obj = Subtraction()

calculating.calc(obj,5,2)

