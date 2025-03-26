import time
import random
import os

def tartaruga(pos: int = 1):
    
    mossa: int = random.randint(1, 10)
            
    if mossa <= 5:
            
        # aumenta 3 quadrati passo veloce
                    
        pos += 3
            
    elif mossa >= 6 and mossa <= 7:
            
        #scivolata arretra 6 quadrati (no sotto l'1)
                    
        pos -= 6
        
        if pos < 1:
                
            pos = 1
    
    elif mossa >= 8:
            
        # aumenta 1 quadrato passo lento
                    
        pos += 1
            
    return pos
            
    
def lepre(pos: int = 1):
    
    mossa: int = random.randint(1, 10)
        
    if mossa >= 3 and mossa <= 4:
            
        #Grande balzo avanza di 9 quadrati.
                    
        pos += 9
        
    if mossa == 5:
            
        # Grande scivolata arretra di 12 quadrati. (no sotto l'1)
                    
        pos -= 12
            
        if pos < 1:
                
            pos = 1
            
    if mossa >= 6 and mossa <= 8:
            
        #Piccolo balzo avanza di 1 quadrato.
                
        pos += 1
        
    if mossa >= 8 and mossa <= 10:
            
        #Piccola scivolata arretra di 2 quadrati. (no sotto l'1)
                    
        pos -= 2
            
        if pos < 1:
            
            pos = 1
                
    return pos
            
    
# def visualizza_posizioni(lista: list[str]):
    
#     lista_HL: list[str] = []
        
#     for i in range(71):
        
#         lista_HL.append("_")
        
#     for j in lista:
        
#         if 

def gara(pos_t, pos_l):
    
    pista: list[str] = ["_"] * 70
        
    for i in range(len(pista)):
        
        if pos_t != pos_l:
            
            pista[pos_t - 1] = "T"
            pista[pos_l - 1] = "L"
        
        else:
            
            pista[pos_l - 1] = "OUCH!!!"
            
        print(*pista)
    
    
if __name__ == "__main__":

    print("'BANG !!!!! AND THEY'RE OFF !!!!!'")
   

    while True:
        
        time.sleep(1)
        
        pos_t: int = tartaruga()
        
        pos_l: int = lepre()
        
        gara(pos_t, pos_l)
        
        print("\n##############################################################################\n")
        
        #time.sleep(1)
        #os.system('clear')
        
        