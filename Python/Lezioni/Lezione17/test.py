#dal modulo lezione17_1_1 importare la classe MovieCatalog
from lezione17_1 import MovieCatalog

#creare un oggetto della classe MovieCatalog
catalog: MovieCatalog = MovieCatalog()

#aggiungimao un regista e dei film al catalogo
catalog.add_movie("Steven Spielberg", ["Casper", "Ritorno al futuro"])

#visualizziamo il catalogo con metodo getter
print(catalog.getCatalog())

#visualizziamo il catalogo con metodo __set__
#print(catalog)

#aggiungere un altro film di Steven Spealberg al catalogo
catalog.add_movie("Steven Spielberg", ["E.T"])

#visualizziamo il catalogo con metodo getter
print(catalog.getCatalog())

#visualizziamo il catalogo con metodo __set__
#print(catalog)

#aggiungere un nuovo regista
catalog.add_movie("Quentin Tarantino", ["Pulp Fiction", "Kill Bill"])

#visualizziamo il catalogo con metodo getter
print(catalog.getCatalog())

#visualizziamo il catalogo con metodo __set__
#print(catalog)

#rimuovere il film E.T dal catalogo
catalog.remove_movie("Steven Spielberg", "E.T")

#visualizziamo il catalogo con metodo getter
print(catalog.getCatalog())

#visualizziamo il catalogo con metodo __set__
#print(catalog)

#rimuoviamo tutti i film di Steven Spielberg dal catalogo
catalog.remove_movie("Steven Spielberg", "Ritorno al futuro")
catalog.remove_movie("Steven Spielberg", "Casper")

#visualizziamo il catalogo con metodo getter
print(catalog.getCatalog())

#visualizziamo il catalogo con metodo __set__
#print(catalog)

#visualizzare solo una lista dei registi
print(catalog.list_director())

#visualizziamo il catalogo con metodo getter
print(catalog.getCatalog())

#visualizziamo il catalogo con metodo __set__
#print(catalog)

#Visualizziamo i film di un regista specifico
catalog.get_movies_by_director("Quentin Tarantino")

catalog.add_movie("Steven Spielberg", ["Casper", "Ritorno al futuro"])
print(catalog.getCatalog())

print(catalog.search_movies_by_title("l"))