X: int = int(input("Inserisci la coordinata X: "))
Y: int = int(input("Inserisci la coordinata Y: "))

coordinate: tuple = (X, Y)

print("")

match coordinate:
    
    case 0, 0:
        
        print("Il punto (0,0) si trova nell'origine.")
        
    case coordinate, 0:
        
        print(f"Il punto ({coordinate},0) si trova sull'asse X.")
        
    case 0, coordinate:
        
        print(f"Il punto (0,{coordinate}) si trova sull'asse Y.")
        
    case x, y if x > 0 and y > 0:
        
        print(f"Il punto ({(x,y)}) si trova nel primo quadrante.")
        
    case x, y if x < 0 and y > 0:
        
        print(f"Il punto ({(x,y)}) si trova nel secondo quadrante.")
        
    case x, y if x < 0 and y < 0:
        
        print(f"Il punto ({(x,y)}) si trova nel terzo quadrante.")
        
    case x, y if x > 0 and y < 0:
        
        print(f"Il punto ({(x,y)}) si trova nel quarto quadrante.")