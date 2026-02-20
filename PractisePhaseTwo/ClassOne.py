class Computer:
    def __init__(self,cpu,ram,os):
        self.cpu=cpu
        self.ram=ram
        self.os=os
    
    def config(self):
        print("Config is {} {} {}".format(self.cpu,self.ram,self.os))




com1 = Computer("i5","16GB","windows")
com2 = Computer("Ryzen 5","32GB","Linux")

com1.config()
com2.config()