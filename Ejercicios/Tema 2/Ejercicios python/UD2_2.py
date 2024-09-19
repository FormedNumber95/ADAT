import random

frase=input("Dime una frase y elegire 2 palabras aleatroias y las mezclare de marera aleatoria formando una sola palabra con todas las letras: ")
frase=frase.strip()
lista_frase=frase.split(" ")
lista_palabras=[]
for i in range(0,2):
    palabra=random.choice(lista_frase)
    lista_palabras.append(palabra)
    lista_frase.remove(palabra)
print(lista_palabras)
lista_palabras[0]=list(lista_palabras[0])
lista_palabras[1]=list(lista_palabras[1])
lista_letras=[]
i=0
j=0
while i<len(lista_palabras[0]) and j<len(lista_palabras[1]):
    palabra_elegir=random.randint(0,1)
    if palabra_elegir==0:
        lista_letras.append(lista_palabras[0][i])
        i=i+1
    else:
        lista_letras.append(lista_palabras[1][j])
        j=j+1
while i<len(lista_palabras[0]):
    lista_letras.append(lista_palabras[0][i])
    i=i+1
while j<len(lista_palabras[1]):
    lista_letras.append(lista_palabras[1][j])
    j=j+1
frase_final=""
for i in range(len(lista_letras)):
    frase_final=frase_final+lista_letras[i]
print(frase_final)
