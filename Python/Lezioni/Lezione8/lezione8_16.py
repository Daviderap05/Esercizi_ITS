def make_album(artist: str, title: str, num_song = None) -> dict:
    
    album: dict = {artist : title}
    
    while True:
    
        opzione: str = input("\nVuoi inserire il numero di canzoni [y, n]: ").lower()
            
        if opzione == "n":
                
            break
                
        elif opzione == "y":
            
            while True:
            
                try:
                        
                    num_song: int = int(input("\nInserisci il numero di canzoni: "))
                        
                    album["num"] = num_song
                                        
                    break
                    
                except ValueError:
                
                    print("Inserimento non valido... riprovare.")
                    
            break
            
        else:
                
            print("Inserire solo y o n, riprova.")
        
    return album


def ordinamento(lista: list):
    
    if not len(lista):
            
        print("Non hai inserito nulla.\n")
    
    count: int = 0
    
    for dictionary in lista:

        for key, value in dictionary.items():
            
            if key == "" or value == "":
                
                print("Inserimenti non validi, hai lasciato uno o più campi vuoti.")
                break
            
            if count != 1:
                
                print(f"L'album dell'artista: {key}, si chiama '{value}'.")
            
                count += 1
            
            else:
                
                print(f"Il numero di canzoni è: {value}.")
        
        print("")
        
        count = 0