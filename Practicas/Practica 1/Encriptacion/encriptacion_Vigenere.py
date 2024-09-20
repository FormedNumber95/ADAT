#Cifrado del texto

#Elegir la clave
clave="sorcerer"
clave=clave.upper()

#abrir el archivo que se va a encriptar para leerlo, eliminar los espacios y 
# caracteres especiales y ponerlo todo en mayusculas
archivo=open("carpeta/pako.txt","r")
textoParaCifrar=""
for i in archivo:
    i=i.upper()
    for j in range(len(i)):
        if ord(i[j])>=ord("A") and ord(i[j])<=ord("Z"):
            textoParaCifrar=textoParaCifrar+i[j]
archivo.close()

#Fijar el tamanio de la clave para que sea igual que el de textoParaCifrar o
#superior en caso de que la clave original fuera mas grande que el 
#textoParaCifrar
claveUsar=""
if(len(clave)<len(textoParaCifrar)):
    for i in range(len(textoParaCifrar)):
        if(i>=len(clave)):
            letra=i%len(clave)
        else:
            letra=i
        claveUsar=claveUsar+clave[letra]
else:
    claveUsar=clave

#Cifrar el texto con la suma de las letras
textoCifrado=""
for i in range(len(textoParaCifrar)):
    numLetra=ord(textoParaCifrar[i])+ord(claveUsar[i])-ord("A")-ord("A")
    letra=chr(numLetra%26+ord("A"))
    textoCifrado=textoCifrado+letra
print(f"El texto cifrado es: {textoCifrado}")
#Hasta aqui el cifrado

#Descifrar
textoDescifrado=""
for i in range(len(textoCifrado)):
    numLetra=ord(textoCifrado[i])-ord(claveUsar[i])-ord("A")-ord("A")
    letra=chr((numLetra+26)%26+ord("A"))
    textoDescifrado=textoDescifrado+letra
print(f"El texto descifrado es: {textoDescifrado}")