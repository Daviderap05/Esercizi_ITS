from movie_genre import *
from noleggio import Noleggio


film_list = [
    Azione(1, "Titanic Reloaded"),
    Azione(2, "Die Hard"),
    Azione(3, "Mad Max"),
    Azione(4, "John Wick"),
    Azione(5, "The Raid"),
    Commedia(6, "Una notte da leoni"),
    Commedia(7, "Scary Movie"),
    Commedia(8, "Zoolander"),
    Commedia(9, "Borat"),
    Drama(10, "Il miglio verde"),
]

store = Noleggio(film_list)

print("Quale film vuoi nolleggiare?")

# --- Simulazioni ---

cliente1 = 101
cliente2 = 202

film1 = film_list[0]    # Azione(1, "Titanic Reloaded"),
store.rentAMovie(film1, cliente1)

film2 = film_list[4]    # Commedia(6, "Una notte da leoni")
store.rentAMovie(film2, cliente1)

store.printRentMovies(cliente1)
print("\n\n-----------------------------------------------------")
store.printMovies()
print("-----------------------------------------------------\n\n")

store.rentAMovie(Commedia(6, "Una notte da leoni"), cliente1)

film3 = film_list[-1]
store.rentAMovie(film3, cliente2)

store.printRentMovies(cliente2)
print("\n\n-----------------------------------------------------")
store.printMovies()
print("-----------------------------------------------------\n\n")

store.giveBack(Commedia(6, "Una notte da leoni"), cliente1, 5)
print("\n\n-----------------------------------------------------")
store.printMovies()
print("-----------------------------------------------------\n\n")