class Restaurant:   #esercizio 1, 2 e 4
    
    def __init__(self, restaurant_name: str, cuisine_type: str, number_served: int = 0):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        
    def describe_restaurant(self):
        
        print(f"Il nome del ristorante è: {self.restaurant_name}. Il suo tipo di cucina è: {self.cuisine_type}")
    
    
    def open_restaurant(self):
        
        print(f"Il ristorante {self.restaurant_name} è aperto")
        
restaurant: Restaurant = Restaurant("Stella", "Italiano")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type   )

print("")

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("")

restaurant1 = Restaurant("Stella", "Italiano")
restaurant2 = Restaurant("Sakura", "Giapponese")
restaurant3 = Restaurant("El Sol", "Messicano")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()