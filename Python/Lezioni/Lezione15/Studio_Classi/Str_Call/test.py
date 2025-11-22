from persona2 import Persona
from studente import Studente

# Creo un oggetto della classe Persona
fm: Persona = Persona("Federico", "March", 29)

#stampo le informazioni relative all'oggetto fm
print(fm)

# Creo un oggetto della classe Studente
studente1: Studente = Studente("Mario", "Rossi", 20, "012345") #se si lascia vuoto ad es. il campo matricola stampa l'errore scritto da noi

print(studente1) #va a rischiamare il metodo __str__ della classe Persona

#isistance(obj, class) verifica che l'oggetto sia istanza della classe che gli passiamo
#ritorna True o False
if isinstance(studente1, Studente):
    
    print("Studente1 è istanza della classe Studente") #ritornerà True
    
if isinstance(studente1, Persona):
    
    print("Studente1 è istanza della classe Persona") #ritornerà True perchè eredità da Persona
    
if isinstance(fm, Persona):
    
    print("fm è istanza della classe Persona") #ritornerà True
    
if isinstance(fm, Studente):
    
    print("fm è istanza della classe Studente") #ritornerà False
    
else:
    
    print("fm è istanza della classe Studente ma solo di persona") #ritornerà True
    
#controllare che la classe Studente sia sottoclasse della classe Persona
#issubclass(Class1, Class2) contrlla se Class1, sia sottoclasse di Class2
#ritorna True o False

if issubclass(Studente, Persona):
    
    print("La classe Studente è sottoclasse della classe Persona") #ritornerà True
    
if issubclass(Persona, Studente):
    
    print("La classe Persona è sottoclasse della classe Studente") #ritornerà False
    
else:
    
    print("La classe Persona non è sottoclasse della classe Studente") #ritornerà True