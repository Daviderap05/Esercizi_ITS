import random
import time
import shutil


def tartaruga(pos: int, cont: int, meteo: str, energia: int):
    
    lancio: int = random.randint(1, 10)
    
    if (cont % 20) < 10:
        
        meteo = "Soleggiato"
        
        match lancio:
            
            case lancio if lancio <= 5:
                
                if 5 <= energia <= 100:
                    
                    energia -= 5
                    pos += 3
                    
                elif energia <= 4:
                    
                    energia += 10
                    
                else:
                    
                    energia = 100 
        
            case lancio if lancio == 6 or lancio == 7:
                
                if 10 <= energia <= 100:
                    
                    energia -= 10
                    pos -= 6
                    
                    if pos < 1:
                    
                        pos = 1
                    
                elif energia <= 9:
                    
                    energia += 10
                    
                else:
                    
                    energia = 100

            case lancio:
                
                if 3 <= energia <= 100:
                    
                    energia -= 3
                    pos += 1
                    
                elif energia <= 2:
                    
                    energia += 10
                    
                else:
                    
                    energia = 100
            
    else:
        
        meteo = "Piovoso"
        
        match lancio:
            
            case lancio if lancio <= 5:
                
                if 5 <= energia <= 100:
                    
                    energia -= 5
                    pos += 3 - 1
                    
                elif energia <= 4:
                    
                    energia += 10
                    
                else:
                    
                    energia = 100 
        
            case lancio if lancio == 6 or lancio == 7:
                
                if 10 <= energia <= 100:
                    
                    energia -= 10
                    pos -= 6 + 1
                    
                    if pos < 1:
                    
                        pos = 1
                    
                elif energia <= 9:
                    
                    energia += 10
                    
                else:
                    
                    energia = 100

            case lancio:
                
                if 3 <= energia <= 100:
                    
                    energia -= 3
                    pos += 1 - 1
                    
                elif energia <= 2:
                    
                    energia += 10
                    
                else:
                    
                    energia = 100
        
    return pos, meteo, energia


def lepre(pos: int, cont: int, meteo: str, energia: int):
    
    lancio: int = random.randint(1, 10)
    
    if (cont % 20) < 10:
        
        meteo = "Soleggiato"
        
        match lancio:
            
            case lancio if lancio <= 2:
                
                energia += 10
                
                if energia > 100:
                    
                    energia = 100
                    
            case lancio if lancio == 3 or lancio == 4:
            
                if 15 <= energia <= 100:
                    
                    energia -= 15
                    pos += 9
                        
            case 5:
            
                if 12 <= energia <= 100:
                    
                    energia -= 12
                    pos -= 20
                    
                    if pos < 1:
                        
                        pos = 1
                        
            case lancio if 6 <= lancio <= 8:
                
                if 5 <= energia <= 100:
                    
                    energia -= 5
                    pos += 1
                    
            case lancio:
                
                if 2 <= energia <= 100:
                    
                    energia -= 2
                    pos += 8
                    
                    if pos < 1:
                        
                        pos = 1
                
    else:
        
        meteo = "Piovoso"
        
        match lancio:
            
            case lancio if lancio <= 2:
                
                energia += 10
                
                if energia > 100:
                    
                    energia = 100
                    
            case lancio if lancio == 3 or lancio == 4:
            
                if 15 <= energia <= 100:
                    
                    energia -= 15
                    pos += 9 - 1
                        
            case 5:
            
                if 12 <= energia <= 100:
                    
                    energia -= 12
                    pos -= 20 + 1
                    
                    if pos < 1:
                        
                        pos = 1
                        
            case lancio if 6 <= lancio <= 8:
                
                if 5 <= energia <= 100:
                    
                    energia -= 5
                    pos += 1 - 1
                    
            case lancio:
                
                if 2 <= energia <= 100:
                    
                    energia -= 2
                    pos += 8 - 1
                    
                    if pos < 1:
                        
                        pos = 1
        
    return pos, meteo, energia


def gara(pos_t: int, pos_l: int, cicli: int, meteo: str, energia_t: int, energia_l: int):
    
    pista: list[str] = ["_"] * 70
    
    dizionario_malus: dict[int, int] = {15 : 3, 30 : 5, 45 : 7}
    dizionario_bonus: dict[int, int] = {5 : 5, 20 : 3, 50 : 10}

    messaggio_bonus: str = ""
    messaggio_malus: str = ""
    
    for pos in dizionario_bonus:
        
        if 0 < pos <= 70:
            
            pista[pos-1] = "B"
            
    for pos in dizionario_malus:
        
        if 0 < pos <= 70:
            
            pista[pos-1] = "M"
            
    if pos_t >= 70 and pos_l >= 70:
        
        pos_t = pos_l = 70
        pista[-1] = "OUCH!!!"
        
        print(*pista)
        
        print(f"\nPosizione tartaruga = {pos_t} (energia = {energia_t})               Posizione lepre = {pos_l} (energia = {energia_l})                Meteo = {meteo} {'☀️' if meteo == 'Soleggiato' else '🌧️'}                {cicli} secondi")
        
        print("\n\nIT'S A TIE.\n")
    
    elif pos_t >= 70:
        
        pos_t = 70
        pista[-1] = "T"
        pista[pos_l - 1] = "L"
        
        print(*pista)
        
        print(f"\nPosizione tartaruga = {pos_t} (energia = {energia_t})               Posizione lepre = {pos_l} (energia = {energia_l})                Meteo = {meteo} {'☀️' if meteo == 'Soleggiato' else '🌧️'}                {cicli} Secondi")
        
        print("\n\nTORTOISE WINS! || VAY!!!\n")
    
    elif pos_l >= 70:
        
        pos_l = 70
        pista[-1] = "L"
        pista[pos_t - 1] = "T"
        
        print(*pista)
        
        print(f"\nPosizione tartaruga = {pos_t} (energia = {energia_t})               Posizione lepre = {pos_l} (energia = {energia_l})                Meteo = {meteo} {'☀️' if meteo == 'Soleggiato' else '🌧️'}                {cicli} Secondi")
            
        print("\n\nHARE WINS || YUCH!!!\n")
    
    elif pos_l == pos_t:
        
        for key, value in dizionario_malus.items():
            
            if pos_t == key:
                
                pos_t -= value
                pos_l -= value

                messaggio_bonus = f"MALUS alla casella {key}! Entrambi arretrano di {value} posizioni"
                    
        for key, value in dizionario_bonus.items():
            
            if pos_t == key:
                
                pos_t += value
                pos_l += value

                messaggio_bonus = f"BONUS alla casella {key}! Entrambi avanzano di {value} posizioni"
        
        pista[pos_t - 1] = "OUCH!!!"
        
        print(*pista)
    
        print(f"\nPosizione tartaruga = {pos_t} (energia = {energia_t})               Posizione lepre = {pos_l} (energia = {energia_l})                Meteo = {meteo} {'☀️' if meteo == 'Soleggiato' else '🌧️'}                {cicli} Secondi")
        
        if messaggio_bonus:
        
            print(f"\n{messaggio_bonus}")
        
    else:
        
        for key, value in {**dizionario_malus, **dizionario_bonus}.items():
                
            if pos_t == key:
                
                if key in dizionario_malus:
                    
                    pos_t -= value
                    messaggio_bonus = f"MALUS alla casella {key}! Tartaruga arretra di {value} posizioni"
                    
                elif key in dizionario_bonus:
                    
                    pos_t += value
                    messaggio_bonus = f"BONUS alla casella {key}! Tartaruga avanza di {value} posizioni"
                    
            if pos_l == key:
                
                if key in dizionario_malus:
                    
                    pos_l -= value
                    messaggio_malus = f"MALUS alla casella {key}! Lepre arretra di {value} posizioni"
                    
                elif key in dizionario_bonus:
                    
                    pos_l += value
                    messaggio_malus = f"BONUS alla casella {key}! Lepre avanza di {value} posizioni"
        
        pista[pos_t - 1] = "T"
        pista[pos_l - 1] = "L"
        
        print(*pista)
        
        print(f"\nPosizione tartaruga = {pos_t} (energia = {energia_t})               Posizione lepre = {pos_l} (energia = {energia_l})                Meteo = {meteo} {'☀️' if meteo == 'Soleggiato' else '🌧️'}                {cicli} Secondi")
        
        if messaggio_bonus and messaggio_malus:
        
            print(f"\n{messaggio_bonus}\n{messaggio_malus}")
            
        elif messaggio_bonus:
        
            print(f"\n{messaggio_bonus}")
            
        elif messaggio_malus:
        
            print(f"\n{messaggio_malus}")

    return pos_t, pos_l


if __name__ == "__main__":

    print("\n" * shutil.get_terminal_size().lines)
    
    print("\n'BANG !!!!! AND THEY'RE OFF !!!!!'\n")
    
    pos_t: int = 1
    pos_l: int = 1
    cicli: int = 1
    energia_t: int = 100
    energia_l: int = 100
    risultato: bool = False
    meteo: str = "Soleggiato"
    
    while risultato == False:
        
        time.sleep(1)
        
        cicli += 1
        
        pos_t, meteo, energia_t = tartaruga(pos_t, cicli, meteo, energia_t)
        pos_l, meteo, energia_l = lepre(pos_l, cicli, meteo, energia_l) 
        
        pos_t, pos_l = gara(pos_t, pos_l, cicli, meteo, energia_t, energia_l)
        print("\n" + "#" * 155 + "\n")
        
        if pos_t >= 70 or pos_l >= 70:
            
            risultato = True