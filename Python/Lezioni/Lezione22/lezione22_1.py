class Documento():  
    
    '''
    
        Classe Documento che continene una variabile di tipo stringa chiamata testo e che 
        memorizza qualsiasi contenuto testuale per il documento
        
        Metodo getText() che restituisca il testo.
        
        Metodo setText() per impostare il testo. 
        
        Metodo isInText() che restituisce True se un documento contiene la parola chiave specificata.
    
    '''
      
    def __init__(self, testo_passato: str) -> None:
        self.setText(testo_passato)
    
    
    def setText(self, testo_passato: str) -> None:
        self.testo: str = testo_passato
    
    
    def getText(self) -> str:
        return self.testo
    
    
    def isInText(self, parola_da_cercare: str) -> bool:
        return True if parola_da_cercare.lower() in self.getText().lower().split() else False
    
    
    
class Email(Documento):
    
    '''
    
        Classe Email che deriva da Documento e include le variabili per il mittente, il destinatario e il titolo del messaggio.
        
        Metodi get() e set() appropriati per tali variabili. 
        
        Il corpo del messaggio dell’e-mail è memorizzato nella variabile ereditata testo.
        
        Metodo getText() ridefinito per concatenare e ritornare tutti i campi di testo (mittente, destinatario, titolo del messaggio, e messaggio) come di seguito:
        Da: alice@example.com, A: bob@example.com
        Titolo: Incontro
        Messaggio: Ciao Bob, possiamo incontrarci domani?
        
        Metodo writeToFile() per scrivere il risultato del metodo getText() in un file di testo e in un percorso specificato.
 
    '''
     
    def __init__(self, testo_passato: str, mittente: str, destinatario: str, titolo_messaggio: str)  -> None:
        super().__init__(testo_passato)
        self.setMittente(mittente)
        self.setDestinatario(destinatario)
        self.setTitolo_messaggio(titolo_messaggio)
        
        
    def setMittente(self, mittente: str) -> None:
        self.mittente: str = mittente
    
    
    def getMittente(self) -> str:
        return self.mittente
    
    
    def setDestinatario(self, destinatario: str) -> None:
        self.destinatario: str = destinatario
    
    
    def getDestinatario(self) -> str:
        return self.destinatario
    
    
    def setTitolo_messaggio(self, titolo_messaggio: str) -> None:
        self.titolo_messaggio: str = titolo_messaggio
    
    
    def getTitolo_messaggio(self) -> str:
        return self.titolo_messaggio
    
    
    def getText(self) -> str:
        return f"Da: {self.getMittente()}, A: {self.getDestinatario()}\nTitolo: {self.getTitolo_messaggio().capitalize()}\nMessaggio: {super().getText()}"
    
    
    def writeToFile(self) -> None:
        
        try:
            
            # Apre il file in modalità scrittura (se non esiste, lo crea)
            with open("Python/Lezioni/Lezione22/email1.txt", mode="w", encoding="utf-8") as file:
                file.write(self.getText())

        except Exception as e:
            print(f"Si è verificato un errore: {e}")
            
            

class File(Documento):
    
    '''

    Classe File che sia derivata da Documento e include una variabile per il nomePercorso.
    
    Crea un file document.txt con all'interno la stringa "Questo e' il contenuto del file." e 
    salvalo in una directory a tua scelta e che sarà indicata in nomePercorso.
    
    I contenuti testuali del file dovrebbero essere letti da questo file di testo al percorso specificato in 
    nomePercorso e memorizzati nella variabile ereditata testo tramite un metodo leggiTestoDaFile().
    
    Si ridefinisca il metodo getText() che concateni e ritorni il nome del percorso e il testo, come di seguito:
    - Percorso: nomePercorso/document.txt
    - Contenuto: Questo e' il contenuto del file.

    '''
    
    # Nella versione prof non c'è testo_passato: str = ""
    def __init__(self, testo_passato: str = "", nomePercorso: str = "Python/Lezioni/Lezione22/document.txt"): 
        self.nomePercorso: str = nomePercorso
        #super().__init__(self.leggiTestoDaFile()) Versione prof 
        super().__init__(testo_passato)
        
            
    def leggiTestoDaFile(self):
        
        try:
                
            with open(self.nomePercorso, mode="r", encoding="utf-8") as file:
                messaggio: str = file.read()
                
            return messaggio

        except Exception as e:
            print(f"Si è verificato un errore: {e}")
    
    
    def getText(self) -> str:
        #return f"Percorso: {self.nomePercorso}\nContenuto: {super().getText()}" Versione prof
        return f"Percorso: {self.nomePercorso}\nContenuto: {self.leggiTestoDaFile()}"
        
    

def main() -> None:
    
    '''
    
    Creazione degli oggetti:\n
    
    - Email: Viene creato un oggetto Email con mittente, destinatario, oggetto e corpo del messaggio.
    - File: Viene creato un oggetto File specificando il percorso di un file esistente.\n
    
    Prova dei metodi:\n
    
    - Stampa del testo dell'email: Viene stampato il testo del messaggio dell'email utilizzando il metodo getText().
    - Stampa del testo del file: Viene stampato il contenuto del file utilizzando il metodo getText().\n
    
    Scrittura del contenuto dell'email su un file:\n
    
    - Scrittura su file: Il contenuto dell'email viene scritto su un nuovo 
        file chiamato email1.txt utilizzando il metodo writeToFile().\n
    
    Verifica della presenza di parole chiave:\n
    
    - Email: Utilizzo del metodo isInText() per verificare se la parola 'incontrarci' 
        è presente nel testo dell'email. Il risultato atteso è True.
    - File: Utilizzo del metodo isInText() per verificare se la parola 'percorso' 
        è presente nel testo del file. Il risultato atteso è False.

    '''
     
    email: Email = Email("Ciao Bob, possiamo incontrarci domani?", "alice@example.com", "bob@example.com", "Incontro")
    file: File = File()
        
    print(email.getText(), end="\n\n")
    print(file.getText())
    
    email.writeToFile()
    
    print(f"\n{email.isInText('incontrarci')}")
    print(email.isInText('percorso'))
    
    
if __name__ == "__main__":
    main()