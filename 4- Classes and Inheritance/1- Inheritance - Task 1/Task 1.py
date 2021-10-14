class Phone:
    def make_call(self) -> None:
        print("calling")
class Smartphone(Phone):
    def turn_flashlight(self) -> None:
        print("making light")

p = Phone()
p.make_call()  # should print "calling"
q = Smartphone()
q.make_call()  # should print "calling"
q.turn_flashlight()  # should print "making light"