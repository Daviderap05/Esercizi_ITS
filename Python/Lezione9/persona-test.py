'''# dal file persona.py impoprta la classe Persona
from persona import Persona

# creo una persona
fm:Persona = Persona("Federico", "March", 29)

# prima di aver definito la funzione __str__ nella classe Persona
#print(fm)

#print(fm.name, fm.lastname, fm.age)

# dopo aver definito la funzione __str__ nella classe Persona
print(fm)
'''
# dal file persona2 importa la classe Persona
from persona2 import Persona

fm:Persona = Persona()

# richiamo il metodo __str__ della classe Persona per mostrare in output le informazioni relative all'oggetto fm 
print(fm)

print("--------------")

msg = str(fm)
print(msg)

# modifico il nome della persona fm 
fm.setName("Federico")

print("--------------")

print(fm)

# modifico il cognome della persona fm
fm.setLastname("March")

# modifico l'età della persona fm
fm.setAge(29)

print("--------------")

print(fm)

print("--------------")
print(fm.getName(), fm.getLastname(), fm.getAge())

# provo a chiamare l'oggetto fm come una funzione (prima di aver creato il metodo __call__ nella classe persona) 
#fm() # .> Output: Errore

# provo a chiamare l'oggetto fm come se fosse una funzione (dopo aver creato il metodo __call__ nella classe Persona)
fm()

# scrivere fm() equivale a richiamare fm.__call__()
