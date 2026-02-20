class A:
    def feature1(self):
        print("The Feature 1")
    def fetaure2(self):
        print("The Feature 2")
    def __init__(self):
        print("In A method")

class B:
    def fetaure3(self):
        print("The Feature 3")
    def __init__(self):
        super().__init__()
        print("In B Method")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("C Method")

c=C()