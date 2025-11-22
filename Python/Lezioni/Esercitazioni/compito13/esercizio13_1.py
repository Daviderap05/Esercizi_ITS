from abc import ABC, abstractmethod
import string



class CodificatoreMessaggio(ABC):
    
    @abstractmethod
    def codifica(self, testoInChiaro: str) -> str:
        pass
        


class DecodificatoreMessaggio(ABC):
    
    @abstractmethod
    def decodifica(self, testoCodificato: str) -> str:
        pass
    
    

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    
    def __init__(self, chiave: int):
        self.chiave = chiave
        super().__init__()
        
        
    def codifica(self, testoInChiaro: str) -> str:
        
        if not testoInChiaro or not isinstance(testoInChiaro, str):
            raise ValueError("Inserire un testo valido da codificare.")
        
        alphabet: str = string.ascii_lowercase
        testoCodificato: str = ""
        
        for letter in testoInChiaro.lower():
            
            if letter in alphabet:
                
                index_c: int = (alphabet.index(letter) + self.chiave) % 26
                letter_c = alphabet[index_c]
                testoCodificato += letter_c
                
            else:
                
                testoCodificato += letter
                
        return testoCodificato
      
                
    def decodifica(self, testoCodificato: str) -> str:
        
        if not testoCodificato or not isinstance(testoCodificato, str):
            raise ValueError("Inserire un testo valido da decodificare.")
        
        alphabet: str = string.ascii_lowercase
        testoInChiaro: str = ""
        
        for letter in testoCodificato.lower():
            
            if letter in alphabet:
                
                index_c: str = (alphabet.index(letter) - self.chiave) % 26
                letter_c = alphabet[index_c]
                testoInChiaro += letter_c
                
            else:
                
                testoInChiaro += letter
                
        return testoInChiaro
    
    
    def leggi_da_file(self, path: str) -> str:
        
        try:
            
            with open(path, "r", encoding="utf-8") as file:
                
                return file.read().strip()
            
        except FileNotFoundError:
            
            raise FileNotFoundError(f"File non trovato: '{path}'")


    def scrivi_su_file(self, path: str, testo: str) -> None:
        
        with open(path, "w", encoding="utf-8") as file:
            
            file.write(testo)

    
    
class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    
    def __init__(self, n: int):
        self.n: int = n
        super().__init__()
        
        
    def codifica(self, testoInChiaro: str) -> str:
        
        if not testoInChiaro or not isinstance(testoInChiaro, str):
            raise ValueError("Inserire un testo valido da codificare.")
        
        testoInChiaro = testoInChiaro.strip().lower()
        lunghezza: int = len(testoInChiaro)
        metà = lunghezza // 2
        prima_m: str = ""
        seconda_m: str = ""
        testoCodificato: str = testoInChiaro
        
        for _ in range (self.n):
            
            nuova_s: str = ""
            
            if lunghezza % 2 == 0:
                
                prima_m = testoCodificato[:metà]
                seconda_m = testoCodificato[metà:]
                
            else:
                
                prima_m = testoCodificato[:metà + 1]
                seconda_m = testoCodificato[metà + 1:]
            
                
            for lettera_pm, lettera_sm in zip(prima_m, seconda_m):
                nuova_s += lettera_pm + lettera_sm
                    
                                
            if len(prima_m) > len(seconda_m):
                nuova_s += prima_m[-1]
                
            testoCodificato = nuova_s
                
        return testoCodificato
    
    
    def decodifica(self, testoCodificato: str) -> str:
        
        if not testoCodificato or not isinstance(testoCodificato, str):
            raise ValueError("Inserire un testo valido da decodificare.")
        
        testoCodificato: str = testoCodificato.strip().lower()
    
        for _ in range(self.n):
            
            prima_m: str = ""
            seconda_m: str = ""

            for i in range(0, len(testoCodificato), 2):
                
                prima_m += testoCodificato[i]
                
                if i + 1 < len(testoCodificato):
                    seconda_m += testoCodificato[i + 1]

            testoCodificato = prima_m + seconda_m
            
        return testoCodificato
    
    
    def leggi_da_file(self, path: str) -> str:
        
        try:
            
            with open(path, "r", encoding="utf-8") as file:
                
                return file.read().strip()
            
        except FileNotFoundError:
            
            f"File non trovato: '{path}'"


    def scrivi_su_file(self, path: str, testo: str) -> None:
        
        with open(path, "w", encoding="utf-8") as file:
            
            file.write(testo)
            
            

def main1() -> None:
    
    cifratore: CifratoreAScorrimento = CifratoreAScorrimento(3)
    testo: str = cifratore.leggi_da_file("Esercitazioni/compito13/da_decriptare.txt")
    codificato: str = cifratore.codifica(testo)
    cifratore.scrivi_su_file("Esercitazioni/compito13/decriptato1.txt", codificato)
    print(codificato, end="\n\n")
    decodificato: str = cifratore.decodifica(codificato)
    print(decodificato, end="\n\n")


def main2() -> None:
    
    cifratore: CifratoreACombinazione = CifratoreACombinazione(3)
    testo: str = cifratore.leggi_da_file("Esercitazioni/compito13/da_decriptare.txt")
    codificato: str = cifratore.codifica(testo)
    cifratore.scrivi_su_file("Esercitazioni/compito13/decriptato2.txt", codificato)
    print(codificato, end="\n\n")
    decodificato: str = cifratore.decodifica(codificato)
    print(decodificato, end="\n\n")


if __name__ == "__main__":
    main1()
    main2()