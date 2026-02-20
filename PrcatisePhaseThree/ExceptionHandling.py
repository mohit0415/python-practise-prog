class Except:
    def __init__(self,a=10,b=2):
        self.a=a
        self.b=b
    def set_A(self,value):
        self.a = value
    def set_B(self,value):
        self.b = value
    def get_A(self):
        return self.a
    def get_B(self):
        return self.b
    def calci(self,a,b):
        try:
            k = a/b
            print(k)
        except Exception as e:
            print("Exception Occired:{}".format(e))
        finally:
            print("resource closed")

ex = Except()

ex.set_A(10)
ex.set_B(20)

ex.calci(ex.get_A(),ex.get_B())
        
