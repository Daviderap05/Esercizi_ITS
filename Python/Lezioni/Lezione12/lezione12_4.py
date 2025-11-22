try:

    with open("/home/its/VsProject/Inglese/inglese_1", "r") as inglese:
    
        for line in inglese:
                    
            print(line.strip())
            
except IOError:
    
    print("File inesistente o non trovato")

    
    