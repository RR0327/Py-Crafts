#Code for Abstraction and Encapsulation

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        self.horn = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started")

car1 =  car()
car1.start()