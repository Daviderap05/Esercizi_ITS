# def classifica_numeri(lista: int) -> dict[str:list[int]]:
    
#     dizionario: dict[str:list[int]] = {'pari': [], 'dispari': []}
    
#     for i in lista:
        
#         if i % 2 == 0:
            
#             dizionario['pari'].append(i)
            
#         else:
            
#             dizionario['dispari'].append(i)
            
#     return dizionario



# def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    
#     dizionario: dict[str:list[int]] = {}
    
#     for key, value in tuples:
        
#         if key not in dizionario.keys():
            
#             dizionario[key] = []
            
#         dizionario[key].append(value)
        
#     return dizionario



# def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    
#     for key, value in da_rimuovere.items():
        
#         if key in lista and lista.count(key) >= value:

#             for i in range(value):
                    
#                 lista.remove(key)
                    
#     return lista



# def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    
#     new_voti: dict[str:list[int]] = {}
    
#     for p in voti:
        
#         if p['nome'] not in new_voti:   # .keys() non necessario per cercare se le chiavi ci sono
                
#             new_voti[p['nome']] = []
            
#         new_voti[p['nome']].append(p['voto'])
             
#     return new_voti

# print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))



# def filtra_e_mappa(prodotti: dict[str, float]) -> dict[str, float]:

#     new_diz: dict[str, float] = {}
    
#     for key, value in prodotti.items():
            
#         if value > 20.0:
                        
#             new_diz[key] = value * 0.9 # 0.9 perché ragiona al contrario -- 0.1 è il 10 per cento della cifra mentr4e 0.9 è gia il prezzo scontato
            
#     return new_diz


# from typing import Any
# def create_contact(name: str, email: str = None, telefono: int = None) -> dict:
    
#     new_diz: dict[Any, Any] = {}
    
#     new_diz['profile'] = name
    
#     if email != None:
        
#         new_diz['email'] = email
        
#     else:
        
#         new_diz['email'] = None
    
#     if telefono != None:

#         new_diz['telefono'] = telefono
        
#     else:
        
#         new_diz['telefono'] = None
        
#     return new_diz

# def update_contact(dictionary: dict, name: str, email: str = None, telefono: int = None) -> dict:
    
#     if email != None:
        
#         dictionary['email'] = email
    
#     if telefono != None:

#         dictionary['telefono'] = telefono
        
#     else:
        
#         dictionary['telefono'] = None
        
#     return dictionary