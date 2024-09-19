diccionario={}
for i in range(0,128):
    diccionario.setdefault(i,chr(i))
print(diccionario)