import random
import pickle

def generar_numeros(archivo):
    lista=[]
    for i in range(1000):
        lista.append(random.uniform(-100,100))
    archivo_escribir=open(archivo,'wb')
    pickle.dump(lista,archivo_escribir)
    archivo_escribir.close()

def promedio(archivo):
    archivo_promedio=open(archivo,'rb')
    lista=pickle.load(archivo_promedio)
    print(sum(lista)/1000)

generar_numeros("textos/texto_numero")
promedio("textos/texto_numero")