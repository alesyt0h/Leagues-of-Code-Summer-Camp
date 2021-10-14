class Robot:
    def __init__(self,x: int, y: int, dir: str):
        self.x = x
        self.y = y
        self.dir = dir
    
    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y
    
    def changePos(self,x: int,y: int) -> int:
        self.x = x
        self.y = y
        
        
def move_robot(r: Robot, to_x: int, to_y: int) -> None:
    Robot.changePos(r,to_x,to_y)


r = Robot(10, 2, "RIGHT")
move_robot(r, 2, -1)
print(r.get_x())  # should print 2
print(r.get_y())  # should print -1