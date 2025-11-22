class Die:
    
    def __init__(self, sides: int = 6):
        
        self.sides = sides
    
    def roll_die(self):
        
        import random
        lancio: int = random.randint(1, self.sides)
        
        print(f"Il risultato è: {lancio}")
        
    
d1: Die = Die()
d2: Die = Die(10)
d3: Die = Die(20)

for i in range(11):
    
    d1.roll_die()
    
print("")   
 
for i in range(11):
    
    d2.roll_die()
    
print("")

for i in range(11):
    
    d3.roll_die()