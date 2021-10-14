class Vehicle:
    def go(self) -> None:
        print("going")

class Car(Vehicle):
    def get_max_people(self) -> int:
        return 8

class Bike(Vehicle):
    def get_num_wheels(self) -> int:
        return 2


c = Car()
c.go()  # should print "going"
print(c.get_max_people())  # should print 8
b = Bike()
b.go()  # should print "going"
print(b.get_num_wheels())  # should print 2