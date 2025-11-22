while True:
    
    try:
    
        position: int = int(input("Ciao inserisci la tua posizione: "))
        print("")
        
        if 1 <= position <= 12:
            
            match position:
                
                case 1:
                    
                    print(f"Finishing position: 1st!")
                    
                case 2:
                    
                    print(f"Finishing position: 2nd!")
                    
                case 3:
                    
                    print(f"Finishing position: 3rd!")
                    
                case _: 
                    
                    print(f"Finishing position: {position}th!")
            
            break
    
    except(ValueError):
        
        print("Inserire numeri interi e positivi.\n")



# if position == 1:
    
#     print(f"Finishing position: {position}st!")
    
# elif position == 2:
    
#     print(f"Finishing position: {position}nd!")
    
# elif position == 3:
    
#     print(f"Finishing position: {position}rd!")
    
# else:
    
#     print(f"Finishing position: {position}th!")