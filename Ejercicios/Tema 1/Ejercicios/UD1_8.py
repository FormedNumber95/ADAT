from UD1_7 import Persona

#crear las personas
p1=Persona()
p2=Persona()
p3=Persona()

#configurar las personas
p1.setAltura(1.3)
p1.setEdad(17)
p1.setNombre("Pako")
p1.setPeso(40)
p1.setSexo("H")

p2.setAltura(1.8)
p2.setEdad(20)
p2.setNombre("Paka")
p2.setPeso(40)
p2.setSexo("M")

p3.setAltura(1.5)
p3.setEdad(18)
p3.setNombre("Juan")
p3.setPeso(40)
p3.setSexo("H")

#comprobar IMC
if p1.calcularIMC()==-1:
    print(f"El peso de {p1.getNombre()} es bajo")
elif p1.calcularIMC()==0:
    print(f"El peso de {p1.getNombre()} es bueno")
else:
    print(f"El peso de {p1.getNombre()} es demasiado alto")

if p2.calcularIMC()==-1:
    print(f"El peso de {p2.getNombre()} es bajo")
elif p2.calcularIMC()==0:
    print(f"El peso de {p2.getNombre()} es bueno")
else:
    print(f"El peso de {p2.getNombre()} es demasiado alto")

if p3.calcularIMC()==-1:
    print(f"El peso de {p3.getNombre()} es bajo")
elif p3.calcularIMC()==0:
    print(f"El peso de {p3.getNombre()} es bueno")
else:
    print(f"El peso de {p3.getNombre()} es demasiado alto")

#comprobar que son mayores de edad
if p1.esMayorDeEdad():
    print(f"{p1.getNombre()} es mayor de edad")
else:
    print(f"{p1.getNombre()} no es mayor de edad")
if p2.esMayorDeEdad():
    print(f"{p2.getNombre()} es mayor de edad")
else:
    print(f"{p2.getNombre()} no es mayor de edad")
if p2.esMayorDeEdad():
    print(f"{p3.getNombre()} es mayor de edad")
else:
    print(f"{p3.getNombre()} no es mayor de edad")

print(p1)
print(p2)
print(p3)