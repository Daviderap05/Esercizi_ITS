from curses.ascii import isalpha
import random


class Creatura():
    
    
    '''

        Creatura con le seguenti proprietà:
        
        - attributi: nome (di tipo stringa, per indicare il nome della creatura)
        - metodi: tutti i metodi standard, ovvero __init__, setter, getter e __str__
        
        In particolare:
        
        il metodo setNome() deve fare un controllo se il nome inserito sia una stringa valida. In caso contrario, 
        impostare il nome della creatura con il valore di "Creatura Generica".
        
        il metodo __str__ deve mostrare in output: "Creatura: nome creatura"


    '''
    
    
    def __init__(self, nome: str) -> None:
        
        self.setNome(nome)
        
    
    def __str__(self) -> str:
        
        return f"Creatura: {self.__nome}"
    
    
    def setNome(self, nome: str) -> None:
        
        if isinstance(nome, str):
            
            self.__nome = nome
            
        else:
            
            self.__nome = "Creatura Generica"
        
        
    def getNome(self) -> str:
        
        return self.__nome
    
    
    
class Alieno(Creatura):
    
    
    '''
    
        Alieno (che eredita da Creatura) con le seguenti proprietà:
        
        - attributi: matricola (di tipo intero positivo), munizioni (una lista di 15 interi positivi)
        - metodi: setter, getter, __str__
        
        In particolare:
        
        il metodo setMatricola() (privato), non riceve argomenti in input e deve inizializzare l'attributo matricola con un numero intero positivo casuale tra 10000 e 90000.
        Per generare un numero intero casuale nell'intervallo [a, b] (ovvero estremi inclusi), importare il modulo random e usare la funzione randint(a,b) del modulo;
        
        il metodo setMunizioni() (privato) non riceve argomenti in input e deve inizializzare l'attributo munizioni con una lista di 15 numeri interi positivi 
        i cui elementi sono numeri della sequenza 0, 1, 4, 9, 16, 25, 36, 49, ... Usare le list comprehension.
        
        il metodo __init__ deve inizializzare la superclasse, inizializzare la matricola e le munizioni.
        Inoltre, i nomi di tutti gli alieni devono essere "Robot-" + matricola (ad esempio, "Robot-16326", scritto con la R maiuscola).
        Pertanto, nel metodo __init__ impostare il nome dell'Alieno come richiesto, effettuando opportuni controlli. 
        Nel caso in cui il nome dell'alieno non sia conforme, mostrare il seguente messaggio e re-impostare il nome in modo corretto: 
        "Attenzione! Tutti gli Alieni devono avere il nome "Robot" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!".
        
        il metodo __str__ deve mostrare in output: "Alieno: nome alieno" (ad esempio: Alieno: Robot-16326)
    
    '''
    
    
    def __init__(self, nome: str) -> None:
        
        self.__setMatricola()
        self.__setMunizioni()
        
        nome_correttamente_formattato: str = f"Robot-{self.__matricola}"
    
        if nome != nome_correttamente_formattato:
            
            print('Attenzione! Tutti gli Alieni devono avere il nome "Robot" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!')
            nome = nome_correttamente_formattato
        
        super().__init__(nome)
        
        
    def __str__(self) -> str:
        
        return f"Alieno: {self.getNome()}"
    
    
    def __setMatricola(self) -> None:
        
        self.__matricola: int = random.randint(10000, 90000)
        
        
    def __setMunizioni(self) -> None:
        
        self.__munizioni: list[int] = [x**2 for x in range(0, 15)]
        
        
    def getMatricola(self) -> int:
        
        return self.__matricola
    
    
    def getMunizioni(self) -> list[int]:
        
        return self.__munizioni
    
    
    
class Mostro(Creatura): 

    
    '''
    
        Mostro (che eredita da Creatura) con le seguenti proprietà:
        
        - attributi: urlo_vittoria (di tipo stringa), gemito_sconfitta (di tipo stringa), assalto (una lista di 15 interi positivi)
        - metodi: setter, getter, __str__
        
        In particolare:
        
        il metodo __init__ deve ricevere il nome del mostro, il suo urlo della vittoria ed il suo gemito sconfitta. Inoltre, deve inizializzare assalto.
        
        il metodo setAssalto() (privato) non riceve argomenti in input e deve inizializzare l'attributo assalto con una lista di 
        15 numeri interi positivi casuali tra 1 e 100, estremi inclusi, tutti diversi tra loro.
        
        i metodi setVittoria(vittoria: str) e setSconfitta(sconfitta: str) (privati), devono controllare se i valori di vittoria e sconfitta siano valori validi. 
        In caso contrario, devono impostare gli attributi urlo_vittoria a "GRAAAHHH" e gemito sconfitta a "Uuurghhh".
        
        Ad esempio, se il nome del mostro è "Godzilla", il metodo __str__ dovrà mostrare a schermo: Mostro: gOdZiLlA, 
        ovvero il nome del mostro scritto con i caratteri alternati minuscolo-maiuscolo.

    
    '''
    
    
    def __init__(self, nome: str, urlo_vittoria: str, gemito_sconfitta: str) -> None:   
        
        self.__setAssalto()
        super().__init__(nome)
        
    
    def __str__(self) -> str:
        
        nome_aggiornato: str = ""
        
        for i, c in enumerate(self.__nome):
            
            if c != " " or c.isalpha():
                
                if i % 2 == 0:
                    
                    nome_aggiornato += c.lower()
                    continue
                    
                else:
                    
                    nome_aggiornato += c.upper()
                    continue
                    
            nome_aggiornato += c
                
        return f"Mostro: {nome_aggiornato}"
    
        
    def __setAssalto(self) -> None:
        
        self.__assalto: list[int] = [random.randint(1, 100) for x in range(0, 15)]
        
        
    def getAssalto(self) -> list[int]:
        
        return self.__assalto