class Criptografo:
   
    def encriptar(self,txt):
        texto_nuevo=""
        for i in range(len(txt)):
            texto_nuevo=texto_nuevo+chr(ord(txt[i])+1)
        return texto_nuevo

    def desencriptar(self,txt):
        texto_nuevo=""
        for i in range(len(txt)):
            texto_nuevo=texto_nuevo+chr(ord(txt[i])-1)
        return texto_nuevo

c1= Criptografo()
texto=input("Introduce el texto que quieras encriptar y luego desencriptar: ")
texto_encriptado=c1.encriptar(texto)
texto_desencriptado=c1.desencriptar(texto_encriptado)
print(texto)
print(texto_encriptado)
print(texto_desencriptado)