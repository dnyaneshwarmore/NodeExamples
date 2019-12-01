class Robot():
    def __init__(self, name):
        self.name = name

    def printName(self):
        print("My name is ", self.name)

class Physician(Robot):
    pass

x = Robot("Dnyaneshwar")
y = Physician("More")

x.printName()
y.printName()