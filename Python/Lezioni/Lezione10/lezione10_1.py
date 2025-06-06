class Restaurant:   #esercizio 1, 2 e 4
    
    def __init__(self, restaurant_name: str, cuisine_type: str, number_served: int = 0):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        
    def describe_restaurant(self):
        
        print(
            
            f"Il nome del ristorante è: {self.restaurant_name}. "
            f"Il suo tipo di cucina è: {self.cuisine_type}. "
            f"Il numero dei clienti serviti è: {self.number_served}."
        )
        
    def describe_number_served(self):
        
        print(f"Il ristorante {self.restaurant_name} ha servito {self.number_served} persone. ")
        
    def set_number_served(self):
        
        n: int = int(input("Inserisci il numero dei clienti serviti: "))

        self.number_served = n
        
        return self.number_served
    
    def open_restaurant(self):
        
        print(f"Il ristorante {self.restaurant_name} è aperto")
        
    def increment_number_served(self):
        
        n: int = int(input("Inserisci il numero dei nbuovi clienti da incrementare: "))

        self.number_served += n
        
        return self.number_served

if __name__ == "__main__":

    restaurant: Restaurant = Restaurant("Stella", "Italiano")

    print(restaurant.restaurant_name)
    print(restaurant.cuisine_type)

    print("")

    restaurant.describe_restaurant()
    restaurant.open_restaurant()

    print("")

    restaurant1: Restaurant = Restaurant("Stella", "Italiano")
    restaurant2: Restaurant = Restaurant("Sakura", "Giapponese")
    restaurant3: Restaurant = Restaurant("El Sol", "Messicano")

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

    print("")

    restaurant4: Restaurant = Restaurant("Macigno", "Indiano")
    restaurant4.describe_number_served()
    restaurant4.set_number_served()
    restaurant4.describe_number_served()
    restaurant4.describe_restaurant()
    restaurant4.increment_number_served()
    restaurant4.describe_number_served()