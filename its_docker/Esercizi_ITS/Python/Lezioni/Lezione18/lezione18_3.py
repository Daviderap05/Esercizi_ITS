from typing import Any


def defines_product(name: str, price: float, quantity: int) -> dict[str, Any]:
    
    return {"name" : name, "price" : price, "quantity" : quantity}


def add_product(cart: list[dict[str, Any]], new_product: dict[str, Any]) -> None:
    
    if not cart:
        
        cart.append(new_product)
        print("Primo prodotto inserito nel carrello")
        
    else:
        
        for product in cart:
            
            if product["name"] == new_product["name"] and product["price"] == new_product["price"]:
                
                product["quantity"] += new_product["quantity"]
                print(f"quantità di '{product['name']}' aggiornata a: {product['quantity']}")
                
                return
                  
        cart.append(new_product)
        print("Prodotto inserito nel carrello")
      
        
def remove_product(cart: list[dict[str, Any]], product_to_remove: str) -> None:
    
    if cart:
        
        for product in cart[:]:
            
            if product["name"] == product_to_remove:
                
                cart.remove(product)
                print(f"Prodotto '{product_to_remove}' rimosso dal carrello.\n")
                
                return
            
        print(f"Prodotto '{product_to_remove}' non trovato nel carrello.\n")\
                
    else:
        
        print("Il carrello è vuoto")
           
            
def view_cart(cart: list[dict[str, Any]]) -> None:
    
    if not cart:
        
        print("Il carrello è vuoto")
        
    else:
        
        print("Prodotti nel carrello:\n")
        
        for product in cart:
            
            print(f"- {product['name']}: €{product['price']:.2f} x {product['quantity']}")
            
        print("")
            
            
def cart_total(cart: list[dict[str, Any]], discount: float = 0.0, tax: float = 0.22) -> float:
    
    if cart:
        
        somma: float = 0.0
        
        for product in cart:
            
            somma += product["price"] * product["quantity"]
            
        somma -= somma * discount
        
        somma += somma * tax
        
        return somma
    
    else:
        
        print("Il carrello è vuoto")
        return 0.0
        

def detailed_summary(cart: list[dict[str, Any]], discount: float = 0.0, tax: float = 0.22):
    
    if cart:
        
        view_cart(cart)
        print(f"Il totale, incluse tasse e sconti è di €{cart_total(cart, discount, tax):.2f}")
    
    else:
        
        print("Il carrello è vuoto")
        
if __name__ == "__main__":
        
    cart: list[dict] = []

    add_product(cart, defines_product("Laptop", 1000.0, 1))
    add_product(cart, defines_product("Mouse", 25.0, 2))
    add_product(cart, defines_product("Keyboard", 50.0, 1))

    view_cart(cart)

    remove_product(cart, "Mouse")

    view_cart(cart)

    detailed_summary(cart, 0.1)