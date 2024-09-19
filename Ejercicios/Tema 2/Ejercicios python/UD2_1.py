import random

def rnd_word(archivo1,archivo2):
    lista_palabras=[]
    ar1=open(archivo1,'r')
    for linea in ar1:
        linea_bien=linea.strip()
        lista_palabras_linea=linea_bien.split(" ")
        lista_palabras.append(random.choice(lista_palabras_linea))
    ar1.close()
    ar2=open(archivo2,'w')
    for i in range(len(lista_palabras)):
        ar2.write(lista_palabras[i]+" ")

rnd_word('textos/texto1','textos/texto2')