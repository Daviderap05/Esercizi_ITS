from custom_types import Telefono, Indirizzo, CAP


class Dipartimento:
    
    _nome: str
    _telefono: set[Telefono]
    _indirizzo: Indirizzo

    def __init__(self, nome: str, telefono: set[Telefono], indirizzo: Indirizzo|None = None) -> None:
    
        self._nome = nome

        if len(telefono) >= 1:
    
            self._telefono = telefono
    
        else:
    
            raise ValueError("Deve avere 1 o più numeri")
        
        if isinstance(indirizzo, Indirizzo):
            
            self._indirizzo = indirizzo


    def __str__(self) -> str:

        return f"Nome: {self._nome}, Telefono: {self._telefono}, Indirizzo: {self._indirizzo}"


    def set_nome(self, new_nome: str) -> None:
    
        self._nome = new_nome
        
        
    def get_nome(self) -> str:
        
        return self._nome
    
    
    def set_telefono(self, new_telefono: set[Telefono]) -> None:
        
        if len(new_telefono) >= 1:
            
            self._telefono = new_telefono
            
        else:
            
            raise ValueError("Deve avere 1 o più numeri")
        
        
    def get_telefono(self) -> set[Telefono]:
        
        return self._telefono
    
    
    def add_telefono(self, telefono: Telefono) -> None:

        self._telefono.add(telefono)


    def remove_telefono(self, telefono: Telefono) -> None:
        
        if telefono in self._telefono:
            
            self._telefono.remove(telefono)
            
        else:
            
            raise ValueError("Il numero di telefono non esiste nel set")
    
    
    def set_indirizzo(self, new_indirizzo: Indirizzo) -> None:
        
        if isinstance(new_indirizzo, Indirizzo):
            
            self._indirizzo = new_indirizzo
            
        else:
            
            raise TypeError("Indirizzo non valido")
        
        
    def get_indirizzo(self) -> Indirizzo|None:
        
        return self._indirizzo
    

d = Dipartimento("Bianco", {Telefono("+393493218793"), Telefono("333498793")}, Indirizzo("Viale Guglielmo Marconi", "451", CAP("00146")))
print(d)

d.add_telefono(Telefono("33333333333"))
print(d)

d.remove_telefono(Telefono("33333333333"))
print(d)