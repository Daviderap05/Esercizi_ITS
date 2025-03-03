frase: str = input("Frase: ")

match frase[-1]:
    
    case "?" if len(frase) % 2 == 0:
        
        print("Si")
        
    case "?" if len(frase) % 2 == 1:
        
        print("No")
        
    case "!":
        
        print("Wow!")
        
    case _:
        
        print(f'Tu dici "{frase}"')




# match frase:     #frase[-1] per poi fare case "?" o "!" tanto il resto è dafault
    
#     case frase if frase[-1] == "?" and len(frase) % 2 == 0:
        
#         print("Si")
        
#     case frase if frase[-1] == "?" and len(frase) % 2 == 1:
        
#         print("No")
        
#     case frase if frase[-1] == "!":
        
#         print("Wow!")
        
#     case _:
        
#         print(f'Tu dici "{frase}"')