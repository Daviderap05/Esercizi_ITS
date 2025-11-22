with open("Python/Lezioni/Lezione19/example.txt", mode="w", encoding="utf-8") as file:
    
    message: str = "Hello, world!\n"
    written_chart: int = file.write(message)    #la funzione write ritorna un intero perché restituisce il numero di caratteri inseriti
    print(f"Written characters: {written_chart}")
#con questo metodo il file viene chiuso in automatico senza file.close()

import time
class StopWatch:
    
    def __init__(self): #il costruttore della classe per inizializzare gli attributi

        self.__start_time = None
        self.__end_time = None
        
    def __enter__(self):
        
        self.__start_time = time.time() #la funzione time.time() restituisce il tempo attuale in secondi 
        
        return self
    
    def __exit__(self, exc_type, exc_val, traceback):  #la funzione __exit__ viene chiamata quando il blocco with termina
        
        #self.__end_time = time.time() #la funzione time.time() restituisce il tempo attuale in secondi
        self.__end_time = time.time()
        
        # Calcola il tempo trascorso
        elapsed_time: float = self.__end_time - self.__start_time
        print(f"Elapsed time: {elapsed_time:.8f} seconds")
        
        # Se si verifica un'eccezione, i parametri exc_type, exc_val e traceback conterranno informazioni sull'eccezione
        # Se non si verifica alcuna eccezione, questi parametri saranno None
        # Puoi usarli per gestire l'eccezione o semplicemente stamparli
        if exc_type is not None:
            
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_val}")
            print(f"Exception traceback: {traceback}")
            
        return False  #False per propagare l'eccezione, True per sopprimerla
#la funzione __exit__ può anche restituire True per sopprimere l'eccezione

pass

# Esempio di utilizzo della classe StopWatch
# con il costruttore __enter__ e __exit__ possiamo usare la classe StopWatch come un contesto
with StopWatch():

    print("Hello, world!")
    #time.sleep(2)
    print("Goodbye, world!")  
    