class Food:
    
    def __init__(self, name: str, price: float, description: str) -> None:
        
        self.name = name
        self.price = price
        self.description = description


class Menu:
    
    def __init__(self, list_food: list[Food] = []) -> None:
        
        self.list_food = list_food
        
    def addFood(self) -> None:
        
        food: Food = Food (input("Inserisci il nome: ").capitalize(),
                           float(input("Inserisci il prezzo: ").capitalize()), 
                           input("Inserisci la descrizione: ").capitalize())
        
        print("")
        
        self.list_food.append(food)
        
        
    def removeFood(self, food_name: str) -> None:
        
        if self.list_food:
            
            for food in self.list_food:
                
                if food.name == food_name:
                
                    self.list_food.remove(food)
                    
                    print(f"\nPietanza '{food_name}' rimosso/a.\n")
                    
                    break
                
                else:
                
                    print("Elemento inesistente\n\n")
                
        else:
            
            print("Lista vuota")
            
            
    def printPrices(self) -> None:
        
        if self.list_food:
            
            for food in self.list_food:
                
                print(f"{food.name} = {food.price:.2f}")
                    
        else:
            
            print("Lista vuota")
            
            
    def getAveragePrice(self) -> None:

        print("")
        
        somma: float = 0        
        
        if self.list_food:
            
            for food in self.list_food:
                
                somma += food.price
        
            print(f"La media dei prezzi è: {(somma / len(self.list_food)):.2f}\n")
            
        else:
            
            print("Lista vuota")
            
    def mostraDati(self) -> None:
        
        for food in self.list_food:
        
            print(f"Nome: {food.name}\nPrezzo: {food.price}\nDescrizione: {food.description}\n")
            

if __name__ == "__main__":
    
    list_food: list[Food] = []
    
    pizza: Food = Food("Pizza margherita", 8.50, "Pizza con pomodoro, mozzarella e basilico")
    pasta: Food = Food("Pasta carbonara", 10.00, "Pasta con uova, guanciale e pecorino")
    gelato: Food = Food("Gelato al cioccolato", 5.00, "Gelato artigianale al cioccolato fondente")

    list_food.append(pizza)
    list_food.append(pasta)
    list_food.append(gelato)
    
    menu: Menu = Menu(list_food)
    
    menu.mostraDati()

    menu.addFood()
    
    menu.mostraDati()

    menu.printPrices()
    
    menu.removeFood("Pizza margherita")
    
    menu.mostraDati()
    
    menu.printPrices()

    menu.getAveragePrice()