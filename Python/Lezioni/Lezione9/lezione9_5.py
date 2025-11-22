class Animal:
    
    def __init__(self, name, legs):
        
        self.name = name
        self.legs = legs
       
    def setLegs(self, legs: int):
        
        self.legs = legs
        
    def getLegs(self):
        
        return self.legs
    
    def printInfo(self):
        
        print(f"Nome: {self.name}\nGambe: {self.legs}\n")
    
    
obj1 = Animal("Dog", 4)
obj2 = Animal("bird", 2)

print(obj1.name)
print(obj2.name)

obj1.setLegs(3)

print(obj1.getLegs())
print(obj2.getLegs())

obj1.printInfo()
obj2.printInfo()