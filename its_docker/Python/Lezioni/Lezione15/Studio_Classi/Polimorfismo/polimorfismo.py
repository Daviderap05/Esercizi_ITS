from persona2 import Persona
from alieno import Alieno

p: Persona = Persona("Davide", "Raponi", 19)

print(p)

et: Alieno = Alieno("Andromeda")

print(et)

p.speak()
et.speak()