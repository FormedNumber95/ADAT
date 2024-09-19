def sin_find(palabra,letra):
    palabra=str(palabra)
    letra=str(letra)
    palabra=palabra.lower()
    letra=letra.lower()
    for i in range(len(palabra)):
        if palabra[i]==letra:
            return i
    return -1

def con_find(palabra,letra):
    palabra=str(palabra)
    letra=str(letra)
    palabra=palabra.lower()
    letra=letra.lower()
    return(palabra.find(letra))

palabra=input("Di la palabra: ")
letra=input("Dime que letra quieres buscar: ")
print(f"Usando find:{con_find(palabra,letra)}")
print(f"Sin usar find: {sin_find(palabra,letra)}")