import random
import time
from sys import exit

#> <

def tartaruga(pos: int, cont: int, meteo: str, energia: int):
    
    lancio: int = random.randint(1, 10)
    
    if (cont % 20) < 10:
        
        meteo = "Soleggiato"
        
        if lancio <= 5:
            
            energia -= 5
            
            if 0 < energia <= 100:
                
                pos += 3
                
            elif energia <= 0:
                
                energia += 10
                
            else:
                
                energia = 100
                
        elif lancio == 6 or lancio == 7:
            
            energia -= 10
            
            if 0 < energia <= 100:
                
                pos -= 6
                
            elif energia <= 0:
                
                energia += 10
                
            else:
                
                energia = 100
                
            if pos < 1:
                
                    pos = 1
                 
        else:
            
            energia -= 3
            
            if 0 < energia <= 100:
                
                pos -= 1
                
            elif energia <= 0:
                
                energia += 10
                
            else:
                
                energia = 100
                
            if pos < 1:
                
                    pos = 1
            
    else:
        
        if lancio <= 5:
            
            energia -= 5
            
            if 0 < energia <= 100:
                
                pos += 3 - 1
                
            elif energia <= 0:
                
                energia += 10
                
            else:
                
                energia = 100
                
        elif lancio == 6 or lancio == 7:
            
            energia -= 10
            
            if 0 < energia <= 100:
                
                pos -= 6 - 1
                
            elif energia <= 0:
                
                energia += 10
                
            else:
                
                energia = 100
                
            if pos < 1:
                
                    pos = 1
                 
        else:
            
            energia -= 3
            
            if 0 < energia <= 100:
                
                pos -= 1 - 1
                
            elif energia <= 0:
                
                energia += 10
                
            else:
                
                energia = 100
                
            if pos < 1:
                
                    pos = 1
        
    return pos, meteo, energia


def lepre(pos: int, cont: int, meteo: str, energia: int):
    
    lancio: int = random.randint(1, 10)
    
    if (cont % 20) < 10:
        
        meteo = "Soleggiato"
    
        if lancio <= 2:
            
            energia += 10   
                
            if energia > 100:
                
                energia = 100
    
        if lancio == 3 or lancio == 4:
            
            energia -= 15
            
            if 0 < energia <= 100:
                
                pos += 9
        
        elif lancio == 5:
            
            energia -= 20
            
            if 0 < energia <= 100:
                
                pos -= 12
                
                if pos < 1:
                    
                    pos = 1
            
        elif 6 <= lancio <= 8:
            
            energia -= 5
            
            if 0 < energia <= 100:
                
                pos += 1
                
            elif energia > 100:
                
                energia = 100
                
        else:
            
            energia -= 8
            
            if 0 < energia <= 100:
                
                pos -= 2
                
                if pos < 1:
                
                    pos = 1
                
            elif energia > 100:
                
                energia = 100
                
    else:
        
        meteo = "Pioggia"
        
        if lancio == 3 or lancio == 4:
            
            pos += 9 - 1
        
        elif lancio == 5:
            
            pos -= 12 - 1
            
            if pos < 1:
                
                pos = 1
                
        elif 6 <= lancio <= 8:
            
            pos += 1 - 1
                
        else:
            
            pos -= 2 - 1
            
            if pos < 1:
                
                pos = 1
        
    return pos, meteo


def gara(pos_t: int, pos_l: int, cicli: int, meteo: str):
    
    pista: list[str] = ["_"] * 70
    
    if pos_t >= 70 and pos_l >= 70:
        
        pos_t = pos_l = 70
        pista[-1] = "OUCH!!!"
        
        print(*pista)
        
        print(f"\nPosizione tartaruga = {pos_t}               Posizione lepre = {pos_l}                Cicli = {cicli}                 Meteo = {meteo}  {'☀️' if meteo == 'Soleggiato' else '🌧️'}")
        
        print("\n\nIT'S A TIE.\n")
    
    elif pos_t >= 70:
        
        pos_t = 70
        pista[-1] = "T"
        pista[pos_l - 1] = "L"
        
        print(*pista)
        
        print(f"\nPosizione tartaruga = {pos_t}               Posizione lepre = {pos_l}                Cicli = {cicli}                 Meteo = {meteo}  {'☀️' if meteo == 'Soleggiato' else '🌧️'}")
        
        print("\n\nTORTOISE WINS! || VAY!!!\n")
    
    elif pos_l >= 70:
        
        pos_l = 70
        pista[-1] = "L"
        pista[pos_t - 1] = "T"
        
        print(*pista)
        
        print(f"\nPosizione tartaruga = {pos_t}               Posizione lepre = {pos_l}                Cicli = {cicli}                 Meteo = {meteo}  {'☀️' if meteo == 'Soleggiato' else '🌧️'}")
            
        print("\n\nHARE WINS || YUCH!!!\n")
    
    elif pos_l == pos_t:
        
        pista[pos_t - 1] = "OUCH!!!"
        
        print(*pista)
    
        print(f"\nPosizione tartaruga = {pos_t}               Posizione lepre = {pos_l}                Cicli = {cicli}                 Meteo = {meteo}  {'☀️' if meteo == 'Soleggiato' else '🌧️'}")
        
    else:
        
        pista[pos_t - 1] = "T"
        pista[pos_l - 1] = "L"
        
        print(*pista)
        
        print(f"\nPosizione tartaruga = {pos_t}               Posizione lepre = {pos_l}                Cicli = {cicli}                 Meteo = {meteo}  {'☀️' if meteo == 'Soleggiato' else '🌧️'}")
    

if __name__ == "__main__":

    print("\n'BANG !!!!! AND THEY'RE OFF !!!!!'\n")
    
    pos_t: int = 1
    pos_l: int = 1
    cicli: int = 1
    risultato: bool = False
    meteo: str = "Soleggiato"
    
    gara(pos_t, pos_l, cicli, meteo)
    print("\n" + "#" * 140 + "\n")
    
    while risultato == False:
        
        time.sleep(1)
        
        cicli += 1
        
        pos_t, meteo = tartaruga(pos_t, cicli, meteo)
        pos_l, meteo = lepre(pos_l, cicli, meteo) 
        
        gara(pos_t, pos_l, cicli, meteo)
        
        print("\n" + "#" * 140 + "\n")
        
        if pos_t >= 70 or pos_l >= 70:
            
            risultato = True