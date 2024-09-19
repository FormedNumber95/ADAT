estadisticas={"fuerza":15,"destreza":15,"constitucion":8,"inteligencia":8,"sabiduria":8,"carisma":15}

#copy
estadisticas2=estadisticas.copy()
print(estadisticas2)

#fromkeys
nueva=["pako","Fred","tu"]
llave=dict.fromkeys(nueva)
print(llave)

#update
estadisticas.update(llave)
print(estadisticas)

#get
print(estadisticas.get("fuerza"))

#setdefault
estadisticas.setdefault(3,5)
print(estadisticas)

#pop
estadisticas.pop(3)
print(estadisticas)

#popitem
estadisticas.popitem()
print(estadisticas)