class Vehicle:
    def run(self,obj):
        obj.start()

class Bike:
    def start(self):
        print("Bike Starting")
class Car:
    def start(self):
        print("Car Starting")

vehicle = Vehicle()

decideObj = Car()


vehicle.run(decideObj)
