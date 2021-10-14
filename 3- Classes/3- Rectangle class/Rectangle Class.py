class Rectangle:
    def __init__(self,a: int, b: int):
        self.a = a
        self.b = b
    def getArea(self) -> int:
        return self.a * self.b

r1 = Rectangle(5, 10)
print(r1.getArea())  # should print 50

r2 = Rectangle(4, 2)
print(r2.getArea())  # should print 8