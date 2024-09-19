frase_introducida=input("Di una frase: ")
cont_pal=0
i=0
cont=0
frase=frase_introducida.lower()
while i!=-1:
    i=frase.find(" ")
    subfrase=frase[0:i]
    if i==-1:
        subfrase=frase
    if "a" in subfrase:
        cont=cont+1
    cont_pal=cont_pal+1
    frase=frase[i+1:]
porcentaje=cont*100/cont_pal
print(f" palabras: {cont_pal}, palabras con a: {cont}, porcentaje de palabras con a: {porcentaje}")
