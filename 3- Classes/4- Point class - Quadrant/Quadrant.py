class Point:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y
    def getQuadrant(self) -> int:
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4


p1 = Point(1, -2)
print(p1.getQuadrant())  # should print 4

p2 = Point(10, 4)
print(p2.getQuadrant())  # should print 1
