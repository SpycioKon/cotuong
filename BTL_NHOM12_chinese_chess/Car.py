class Car:
    def __init__(self,selected):
        self.selected = selected
        self.x,self.y = self.getPosition()
        pass
    def getPosition(self):
        return 1,2
    def printPosition(self):
        return self.y
x = Car(1)
z = x.printPosition()
print(z)