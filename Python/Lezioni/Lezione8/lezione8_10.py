def send_messages(lista: list):
    
    list2: list = []
    
    print(", ".join(lista))
    
    for i in lista:
        
        list2.append(i)
        
    print(*list2, sep = ", ", end = " ")
    

lista: list[str] = ["Ciao", "come", "stai"]

send_messages(lista)