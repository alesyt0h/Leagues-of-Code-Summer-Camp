class Arrow:
    def __init__(self,a: int, b: str):
        self.a = a
        self.b = b
    
    def get_x(self) -> str:
        return self.a
    
    def changePos(self,a: int) -> int:
        self.a = a
        
def move_arrow_zero(a: Arrow, to_x: int) -> None:
    Arrow.changePos(a,to_x)

a1 = Arrow(0, "LEFT")
move_arrow_zero(a1, 2)
print(a1.get_x())  # should print 2

a2 = Arrow(0, "RIGHT")
move_arrow_zero(a2, -3)
print(a2.get_x())  # should print -3    