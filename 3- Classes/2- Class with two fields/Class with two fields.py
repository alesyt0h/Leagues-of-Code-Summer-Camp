class Student:
    def __init__(self,name: str,age: int):
        self.name = name
        self.age = age

s = Student("John", 16)
print(s.name)  # should print "John"
print(s.age)  # should print 16