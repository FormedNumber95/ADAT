#Elegir la clave
clave="sorcerer"
clave=clave.upper()

#abrir el archivo que se va a encriptar para leerlo, eliminar los espacios y 
# caracteres especiales y ponerlo todo en mayusculas
archivo=open("carpeta/pako.txt","r")
textoParaCifrar=""
for i in archivo:
    i.upper()
    for j in range(len(i)):
        if ord(i[j])>=ord("A") and ord(i[j])<=ord("Z"):
            print("Hola")
