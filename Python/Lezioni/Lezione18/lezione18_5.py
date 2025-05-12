from curses.ascii import isalnum
from multiprocessing import Value
from typing import Any

from networkx import expected_degree_graph


def item(code: str, name: str, quantity: int, price: float) -> dict:
    
    return {"code" : code, "name" : name, "quantity": quantity, "price" : price}


def add_item(items: list[dict[str, Any]], new_item: dict[str, Any]) -> None:
    
    if not items:
        
        items.append(new_item)
        print("Primo prodotto inserito nel carrello")
        
    else:
        
        for product in items:
            
            if product["name"] == new_item["name"] and product["price"] == new_item["price"] and product["code"] == new_item["code"]:
                
                product["quantity"] += new_item["quantity"]
                print(f"quantità di '{product['name']}' aggiornata a: {product['quantity']}")
                
                return
                  
        items.append(new_item)
        print("Prodotto inserito nel carrello")
        
        

def remove_item(items: list[dict[str, Any]], item_to_remove: str) -> None:
    
    if items:
        
        for product in items[:]:
            
            if product["name"] == item_to_remove:
                
                items.remove(product)
                print(f"Prodotto '{item_to_remove}' rimosso dal carrello.\n")
                
                return
            
        print(f"Prodotto '{item_to_remove}' non trovato nel carrello.\n")\
                
    else:
        
        print("Il carrello è vuoto")
        
        
        
def view_items(items: list[dict[str, Any]]) -> None:
    
    if not items:
        
        print("Il carrello è vuoto")
        
    else:
        
        print("Prodotti nell'inventario:\n")
        
        for item in items:
            
            print(f"- {item['name']} ({item['code']}): €{item['price']:.2f} x {item['quantity']}")
            
        print("")
        
        
def search_item(items: list[dict[str, Any]]):
    
    if not items:
        
        print("Il carrello è vuoto")
        
    else:   
        
        while True:
            
            try:
                
                code: str = input("Inserire il codice dell'elemento da ricercare nell'inventario: ")
                
                if not code.isalnum():
                    
                    raise ValueError("Il codice deve essere alfanumerico... riprova")
                
                else:
                    
                    ris: str = input("\nVuoi inserire anche il nome per una ricerca più accurata? [s/n]: ")
                    
                    match ris.lower():
                        
                        case "n":
                            
                            for item in items:
                
                                for key in item.keys():
                            
                                    if key == code:
                                        
                                        print(f"- {item['name']} ({item['code']}): €{item['price']:.2f} x {item['quantity']}")
                                        
                                    else:
                                        
                                        print("Nessuna corrispondenza")
                                        
                            break
                            
                        case "s": 
                            
                            nome: str = input("Inserire il nome dell'elemento da ricercare nell'inventario: ")
                
                            if not nome.isalpha():
                    
                                raise ValueError("Il nome deve contenere solo caratteri... riprova")
                            
                            else:
                                
                                for item in items:
                    
                                    for key in item.keys():
                                
                                        if key == code and key == nome:
                                            
                                            print(f"- {item['name']} ({item['code']}): €{item['price']:.2f} x {item['quantity']}")
                                            
                                        else:
                                            
                                            print("Nessuna corrispondenza")
                                        
                            
                            
                        case _:
                            
                            print("Scelta non valida... riprova")   
                    
                    break         
                    
                            
            except ValueError as e:
            
                print(e)
                
            
        
             
    
    
    
    
    
    
    
    
    
    
    
            
# def update_item(items: list[dict[str, Any]], code: str, name: str, quantity: int, price: float):
    
#     if not items:
        
#         print("Il carrello è vuoto")
        
#     else:
        