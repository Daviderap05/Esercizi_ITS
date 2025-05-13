from curses.ascii import isalnum
from multiprocessing import Value
from os import name
from typing import Any

from networkx import expected_degree_graph


def item(code: str, name: str, quantity: int, price: float) -> dict:
    
    if quantity > 0 and price >= 0:
        
        return {"code" : code, "name" : name, "quantity": quantity, "price" : price}
    
    else:
        
        print("Valori non validi.")


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
        
        if item_to_remove:
            
            for product in items[:]:
                
                if product["name"] == item_to_remove:
                    
                    items.remove(product)
                    print(f"Prodotto '{item_to_remove}' rimosso dal carrello.\n")
                    
                    return
                
            print(f"Prodotto '{item_to_remove}' non trovato nel carrello.\n")
        
        else:
            
            print("Il campo deve essere pieno")        
    else:
        
        print("Il carrello è vuoto")
        
        
        
def view_items(items: list[dict[str, Any]]) -> None:
    
    cont: int = 1
    
    if not items:
        
        print("Il carrello è vuoto")
        
    else:
        
        print("Prodotti nell'inventario:\n")
        
        for item in items:
            
            print(f"{cont}) {item['name']} ({item['code']}): €{item['price']:.2f} x {item['quantity']}")
            cont += 1
            
        print("")
        
        
def search_item(items: list[dict[str, Any]]):
    
    if not items:
        
        print("Il carrello è vuoto")
        
    else:   
        
        while True:
            
            try:
                
                code: str = input("Inserire il codice dell'elemento da ricercare nell'inventario: ")
                
                if not code.isalnum() or len(code) > 6:
                    
                    raise ValueError("Il codice deve essere un alfanumerico di massimo 6 cifre... riprova")
                
                else:
                    
                    break
                
            except ValueError as e:
        
                print(e)
        
        while True:
                
            ris: str = input("\nVuoi inserire anche il nome per una ricerca più accurata? [s/n]: ")
            match: bool = False
            
            match ris.lower():
                
                case "n":
                    
                    for item in items:
                    
                        if item["code"] == code:
                            
                            print(f"- {item['name']} ({item['code']}): €{item['price']:.2f} x {item['quantity']}")
                            match = True
                            
                    if not match:
                        
                        print("Nessuna corrispondenza")
                        
                    break
                                
                case "s": 
                    
                    try:
                        
                        name: str = input("\nInserire il nome dell'elemento da ricercare nell'inventario: ")
            
                        if not name.isalpha():
                
                            raise ValueError("Il nome deve contenere solo caratteri... riprova")
                        
                        else:
                            
                            for item in items:
                            
                                if item["code"] == code and item["name"].lower() == name.lower():
                                    
                                    print(f"- {item['name']} ({item['code']}): €{item['price']:.2f} x {item['quantity']}")
                                    match = True
                                    
                            if not match:
                        
                                print("Nessuna corrispondenza")
                                    
                            break
                                        
                    except ValueError as e:
            
                        print(e) 
                    
                case _:
                    
                    print("Scelta non valida... riprova")
                    
                    
def update_item(items: list[dict[str, Any]]):
    
    view_items(items):
    
    
            
        
             
    
    
    
    
    
    
    
    
    
    
    
            
# def update_item(items: list[dict[str, Any]], code: str, name: str, quantity: int, price: float):
    
#     if not items:
        
#         print("Il carrello è vuoto")
        
#     else:
        