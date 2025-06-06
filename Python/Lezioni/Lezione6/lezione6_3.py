voto: int = int(input("Inserisci il voto di laurea: "))

match voto:
    
    case _ if 106 <= voto <= 110:
        
        print("GPA 4.0")
        
    case _ if 101 <= voto <= 105:
        
        print("GPA 3.7")
        
    case _ if 96 <= voto <= 100:
        
        print("GPA 3.3")
        
    case _ if 91 <= voto <= 95:
        
        print("GPA 3.0")
        
    case _ if 86 <= voto <= 90:
        
        print("GPA 2.7")
        
    case _ if 81 <= voto <= 85:
        
        print("GPA 2.3")
        
    case _ if 76 <= voto <= 80:
        
        print("GPA 2.0")
        
    case _ if 70 <= voto <= 75:
        
        print("GPA 1.7")
        
    case _ if 66 <= voto <= 69:
        
        print("GPA 1.0")
        
    case _:
        
        print("Voto non valido")