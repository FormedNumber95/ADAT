def buscar_en_diccionario(diccionario,elemento):
    for i in range(len(diccionario)):
        if estadisticas.get(elemento):
            return True
    return False

estadisticas={"fuerza":15,"destreza":15,"constitucion":8,"inteligencia":8,"sabiduria":8,"carisma":15}
print(buscar_en_diccionario(estadisticas,"fuergza"))