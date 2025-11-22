import random
import os
import time
import re


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
        i cui elementi sono numeri della sequenza 0, 1, 4, 9, 16, 25, 36, 49, ...
        
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

        if not re.fullmatch(r"^Robot-(?:[1-8][0-9]{4}|90000)$", nome):
            
            print('Attenzione! Tutti gli Alieni devono avere il nome "Robot" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!\n')
            
            nome_correttamente_formattato: str = f"Robot-{self.__matricola}"
            time.sleep(1)
            
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
        self.setVittoria(urlo_vittoria)
        self.setSconfitta(gemito_sconfitta)
        super().__init__(nome)
        
    
    def __str__(self) -> str:
        
        nome_aggiornato: str = ""
        
        for i, c in enumerate(self.getNome()):
            
            if c.isalpha():
                
                if i % 2 == 0:
                    
                    nome_aggiornato += c.lower()
                    
                else:
                    
                    nome_aggiornato += c.upper()
                
                continue
                    
            nome_aggiornato += c
                
        return f"Mostro: {nome_aggiornato}"
    
        
    def __setAssalto(self) -> None:
        
        self.__assalto: list[int] = random.sample(range(1, 101), 15)
        
        
    def setVittoria(self, urlo_vittoria: str) -> None:
        
        if isinstance(urlo_vittoria, str):
            
            self.__urlo_vittoria = urlo_vittoria
            
        else:
            
            self.__urlo_vittoria = "GRAAAHHH"
            
            
    def setSconfitta(self, gemito_sconfitta: str) -> None:
        
        if isinstance(gemito_sconfitta, str):
            
            self.__gemito_sconfitta = gemito_sconfitta
            
        else:
            
            self.__gemito_sconfitta = "Uuurghhh"
        
        
    def getAssalto(self) -> list[int]:
        
        return self.__assalto
    

    def getVittoria(self) -> str:
        
        return self.__urlo_vittoria
    
    
    def getSconfitta(self) -> str:
        
        return  self.__gemito_sconfitta
    
  
    
def pariUguali(a: list[int], b: list[int]) -> list[int]:
    

    '''
    
        Questo metodo riceve in input due liste a e b di interi positivi e deve restituire una lista c.
        Ogni elementi della lista c deve essere uguale a:
        
        - 1 se l'elemento i-esimo di a e l'elemento i-esimo di b sono sono entrambi pari
        - 0 altrimenti
    
    '''
    
    
    c: list[int] = []
    
    for i, j in zip(a, b):
        
        if i % 2 == 0 and j % 2 == 0:
            
            c.append(1)
            
        else:
            
            c.append(0)
            
    return c   # Alternativa una sola riga: return [1 if i % 2 == 0 and j % 2 == 0 else 0 for i, j in zip(a, b)]


def combattimento(a: Alieno, m: Mostro) -> Alieno|Mostro:
    
    
    '''
    
        Questo metodo riceve in input un oggetto della classe Alieno ed un oggetto della classe Mostro. 
        Il metodo deve controllare la validità di a e la validità di m. Se a non è un Alieno o se m non è un Mostro, 
        il combattimento deve essere interrotto, mostrare un opportuno messaggio e ritornare None. Altrimenti, se a e m sono oggetti validi, 
        il metodo deve simulare il combattimento tra Mostro e Alieno, restituendo la creatura vincitrice. 
        Il combattimento consiste nell'applicare la funzione pariUguali() alle munizioni dell'Alieno e all'assalto del Mostro. 
        Se la lista prodotta in output dal pariUguali() ha più di 4 elementi con valore 1, allora il vincitore è il mostro. Altrimenti, 
        il vincitore è l'alieno. Se vince il mostro, sullo schermo viene stampato per 3 volte l'urlo della vittoria, 
        altrimenti viene stampato il gemito della sconfitta.
    
    '''
    
    
    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        
        raise ValueError("Le creature non sono valide")
    
    lista_vincitore: list[int] = pariUguali(a.getMunizioni(), m.getAssalto())
    
    if lista_vincitore.count(1) > 4:    #vittoria mostro
        
        for i in range(3):
            
            print(m.getVittoria())
            
        return m
            
    else:                               #vittoria alieno
        
        print(m.getSconfitta())
        
        return a
    

def proclamaVincitore(c: Creatura) -> None:
    
    
    '''

        Questo metodo stampa a schermo se hanno vinto gli alieni o i mostri (a seconda dell'oggetto c) e, 
        mostra il vincitore all'interno di un rettangolo con contorno di *.

    '''
    
    
    larghezza: int = len(str(c)) + 10
    altezza: int = 5

    for i in range(altezza):
        
        if i == 0 or i == (altezza - 1):
            
            print("*" * larghezza)
            
        elif i == 2:
            
            spazi_totali: int = larghezza - 2 - len(str(c))
            spazi_sx: int = spazi_totali // 2
            spazi_dx: int = spazi_totali - spazi_sx
            
            print("*" + " " * spazi_sx + str(c) + " " * spazi_dx + "*")
            
        else:
            
            print("*" + " " * (larghezza - 2) + "*")
            
            
def pulisci_terminale():
    
  """Pulisce il terminale."""
  
  if os.name == 'nt': # Se il sistema operativo è Windows
      
    os.system('cls')
    
  else: # Se il sistema operativo è Unix-like
      
    os.system('clear')
            
            
def main():
    
    
    '''
    
        - Inizializza un mostro e un alieno e stampa i dati corrispondenti sullo schermo.
        - Esegue un combattimento tra i due oggetti creati.
        - Proclama il vincitore.
    
    '''
    
    
    pulisci_terminale()
    
    # Inizializzazione di un alieno
    alieno: Alieno = Alieno("Robot-44567")  # il nome verrà corretto automaticamente se serve
    
    print(alieno)
    print("Munizioni:", alieno.getMunizioni())
    print()

    # Inizializzazione di un mostro
    mostro: Mostro = Mostro("Gorthor", "GRAAAHHH", "Uuurghhh")
    
    print(mostro)
    print("Assalto:", mostro.getAssalto())
    print()

    print("Combattimento\n")

    # parte il combattimento
    vincitore: Alieno|Mostro = combattimento(alieno, mostro)
    print()

    # Proclamazione del vincitore con messaggio
    if isinstance(vincitore, Mostro):
        
        print("I Mostri hanno vinto!\n")
        
    elif isinstance(vincitore, Alieno):
        
        print("Gli Alieni hanno vinto!\n")

    # Visualizzazione grafica del vincitore
    proclamaVincitore(vincitore)
    
    
if __name__ == "__main__":
    
    main()