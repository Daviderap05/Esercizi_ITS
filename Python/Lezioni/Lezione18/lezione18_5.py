from tkinter import N
from typing import Any


def item(code: str, name: str, quantity: int, price: float) -> dict[str, Any]:
    
    if quantity > 0 and price >= 0:
        
        return {"code" : code.lower(), "name" : name.lower(), "quantity" : quantity, "price" : price}
    
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
                
                code: str = input("Inserire il codice dell'elemento da ricercare nell'inventario: ").lower()
                
                if not code.isalnum() or len(code) > 6:
                    
                    raise ValueError("Il codice deve essere un alfanumerico di massimo 6 cifre... riprova")
                
                else:
                    
                    break
                
            except ValueError as e:
        
                print(e)
        
        while True:
                
            ris: str = input("\nVuoi inserire anche il nome per una ricerca più accurata? [s/n]: ").lower()
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
                        
                        name: str = input("\nInserire il nome dell'elemento da ricercare nell'inventario: ").lower()
            
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
    
    view_items(items)
    
    while True:
        
        try:
            
            select: int = int(input("\nInserisci il numero corrispondente all'oggetto da modificare: "))
            
            if not 1 <= select <= len(items):
                
                print("Il numero inserito non corrisponde a nessun oggetto")
                continue
    
            break
                
        except ValueError:
            
            print("Inserire un valore valido... riprova")
    
    item = items[select - 1]
            
    while True:
        
        try:
            
            code: str = str(input("\nInserisci il nuovo codice: "))
            
            if not code.isalnum() or len(code) > 6:
                
                raise ValueError("Il codice deve essere un alfanumerico di massimo 6 cifre... riprova")
            
            item['code'] = code
            
            break
                
        except ValueError as e:
            
            print(e)
            
    while True:
        
        try:
            
            name: str = str(input("\nInserisci il nuovo nome: "))
            
            if not name.isalpha():
                
                raise ValueError("Il nome deve contenere solo caratteri... riprova")
            
            item['name'] = name
            
            break
                
        except ValueError as e:
            
            print(e)
            
    while True:
        
        try:
            
            price: float = float(input("\nInserisci il nuovo prezzo: "))
            
            if price < 0:
                
                print("Il prezzo non può essere negativo")
                continue
            
            item['price'] = price
            
            break
        
        except ValueError:
            
            print("Inserire un valore valido... riprova")
            
    while True:
        
        try:
            
            quantity: int = int(input("\nInserisci la nuova quantità: "))
            
            if quantity < 0:
                
                print("La quantità non può essere negativa")
                continue
            
            item['quantity'] = quantity
            
            break   
         
        except ValueError:
            
            print("Inserire un valore valido... riprova")
            
    print(f"Prodotto aggiornato: {item['name']} ({item['code']}): €{item['price']:.2f} x {item['quantity']}")
    
def main():
    
    # Lista per memorizzare i prodotti del carrello
    items: list[dict[str, Any]] = []

    # Creazione di oggetti di esempio
    print("Creazione di oggetti di esempio...")
    
    item1 = item("ABC123", "MartelloA", 5, 10.50)
    item2 = item("ABC123", "MartelloB", 3, 20.00)
    item3 = item("GHI789", "Cacciavite", 10, 5.00)

    # Aggiunta degli oggetti al carrello
    if item1:
        
        add_item(items, item1)
        
    if item2:
        
        add_item(items, item2)
        
    if item3:
        
        add_item(items, item3)

    # Visualizzazione degli oggetti nel carrello
    print("\nVisualizzazione degli oggetti nel carrello:")
    view_items(items)

    # Ricerca di un prodotto per codice
    print("\nRicerca di un prodotto per codice:")
    search_item(items)

    # Modifica di un prodotto
    print("\nModifica di un prodotto:")
    update_item(items)

    # Visualizzazione degli oggetti dopo la modifica
    print("\nVisualizzazione degli oggetti dopo la modifica:")
    view_items(items)

    # Rimozione di un prodotto
    print("\nRimozione di un prodotto:")
    remove_item(items, "Prodotto2")

    # Visualizzazione degli oggetti dopo la rimozione
    print("\nVisualizzazione degli oggetti dopo la rimozione:")
    view_items(items)

    # Test con carrello vuoto
    print("\nTest con carrello vuoto:")
    remove_item(items, "Cacciavite")  # Prova a rimuovere un prodotto non presente
    search_item(items)  # Prova a cercare un prodotto con carrello vuoto
    update_item(items)  # Prova a modificare un prodotto con carrello vuoto
    view_items(items)  # Visualizza il carrello vuoto


if __name__ == "__main__":
    main()