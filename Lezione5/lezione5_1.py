pizzas: list[str] = ["Margherita", "Boscaiola", "Bufala"]

for i in pizzas:
    
    print(i)

for i in range(len(pizzas)):
    
    print(f"La mia {i + 1}° pizza preferita è: {pizzas[i]}")
    
print(f"A me piace la {pizzas[0]}")
print(f"A me piace la {pizzas[1]}")
print(f"A me piace la {pizzas[2]}")

print(f"A me piace tanto la pizza!")