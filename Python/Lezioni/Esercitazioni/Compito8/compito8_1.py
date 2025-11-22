class Frazione:
    
    def __init__(self, numeratore: int = 13, denominatore: int = 5) -> None:
        
        self.setNumeratore(numeratore)
        self.setDenominatore(denominatore)
        
        
    def __str__(self) -> str:
        
        return f"{self.__numeratore} / {self.__denominatore}"
        
        
    def setNumeratore(self, numeratore: int) -> None:
    
        if isinstance(numeratore, int):
        
            self.__numeratore = numeratore
            
        else:
            
            print("Numeratore non valido inizializzato di default a 13\n")
            self.__numeratore = 13
        
        
    def getNumeratore(self) -> int:
        
        return self.__numeratore
        
        
    def setDenominatore(self, denominatore: int) -> None:
        
        if isinstance(denominatore, int) and denominatore != 0:
            
            self.__denominatore = denominatore
            
        else:
            
            print("Denominatore non valido inizializzato di default a 5\n")
            self.__denominatore = 5
        
    
    def getDenominatore(self) -> int:
        
        return self.__denominatore
        
        
    def value(self) -> float:
        
        return round((self.__numeratore / self.__denominatore), 3)
    
     
def mcd(x: int, y: int) -> int:
    
    divisori: list[int] = []
    div: int = 1
    
    while  div <= min(x, y):
        
        if x % div == 0 and y % div == 0:
            
            divisori.append(div)
                        
        div += 1
        
    if len(divisori) > 0:
        
        return max(divisori)
        
    return 1
    
    
def semplifica(frazioni: list[Frazione] = []) -> list[Frazione]:
    
    if frazioni == []:
        
        raise ValueError ("Inserire una lista di frazioni.")
    
    frazioni_semplificate: list[Frazione] = []
    
    for frazione in frazioni:
        
        mcdiv: int = mcd(frazione.getNumeratore(), frazione.getDenominatore())
        
        if mcdiv == 1:
            
            frazioni_semplificate.append(frazione)
            
        else:
            
            frazione_semplificata: Frazione = Frazione(frazione.getNumeratore() // mcdiv, frazione.getDenominatore() // mcdiv)
            frazioni_semplificate.append(frazione_semplificata)
            
    return frazioni_semplificate
        

def fractionCompare(frazioni: list[Frazione], frazioni_semplificate: list[Frazione]) -> None:
    
    i: int = 1
    
    for FrazioneNonSemplificata, FrazioneSemplificata in zip(frazioni, frazioni_semplificate):
        
        ris1: float = FrazioneNonSemplificata.value()
        ris2: float = FrazioneSemplificata.value()
        
        print(f"Il risultato della {i}° frazione non semplificata ({FrazioneNonSemplificata}) è: {ris1}")
        print(f"Il risultato della {i}° frazione semplificata ({FrazioneSemplificata}) è: {ris2}\n")
        
        i += 1
        
        

l: list[Frazione] = [
    
    Frazione(2.5, 0),  # Il metodo set imposterà i valore di default (13/5) # type: ignore
    Frazione(1, 2),
    Frazione(2, 4),
    Frazione(3, 5),
    Frazione(6, 9),
    Frazione(4, 7),
    Frazione(24, 36),
    Frazione(12, 36),
    Frazione(40, 60),
    Frazione(5, 11),
    Frazione(10, 45),
    Frazione(42, 78),
    Frazione(9, 15)
    
]

l_s: list[Frazione] = semplifica(l)

fractionCompare(l, l_s)