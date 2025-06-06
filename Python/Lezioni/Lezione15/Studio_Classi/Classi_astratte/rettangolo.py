from formaGenerica import FormaGenerica

class Rettangolo(FormaGenerica):
    
    def __init__(self):
        super().__init__()
        self.setShape("Rettangolo")
        
    def draw(self) -> None:
        
        print(f"\n{self.getShape()}:\n")
        
        for i in range(5):
            
            for j in range(5*2):
                
                #lato a e lato b del rettangolo 
                if i == 0 or i == 5 - 1:
                    
                    print("*", end = " ")
                    
                #lato b e lato c del rettangolo
                
                elif j == 0 or j == (5 * 2) - 1:
                    
                    print("*", end = " ")
                    
                #stampare spazio bianco
                
                else:
                    
                    print(" ", end = " ")
                    
            print("\n", end = "")
