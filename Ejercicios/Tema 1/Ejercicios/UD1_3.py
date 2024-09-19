lista=[]
sumatorio=0
i=0
while i <10:
    try:
        num=int(input(f"Dime el numero Nº{i} "))
        while num%2==0:
            num=int(input("El numero introducido deve ser impar, introduce un numero valido: "))
        lista.append(num)
        sumatorio=sumatorio+num
        i=i+1
    except ValueError:
        print("el valor introducido debe ser un numero")
media=sumatorio/len(lista)
print(lista)
print(f"El sumatorio es {sumatorio} y la media es {media}")