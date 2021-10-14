class Arrow:
    def __init__(self,a: int, b: str):
        self.a = a
        self.b = b
    
    def get_direction(self) -> str:
        return self.b
    
    def changeDir(self,b: str) -> str:
        self.b = b
        
def set_direction_right(a: Arrow) -> None:
    b = ""
    if a.b == "LEFT":
        b = "RIGHT"
    else:
        b = "RIGHT"
    Arrow.changeDir(a,b)


a1 = Arrow(10, "LEFT")
set_direction_right(a1)
print(a1.get_direction())  # should print "RIGHT"

a2 = Arrow(10, "RIGHT")
set_direction_right(a2)
print(a2.get_direction())  # should print "RIGHT"