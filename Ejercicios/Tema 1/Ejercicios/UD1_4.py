lista=[]
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
print(lista)
print("¿Qué desea hacer con la lista?")
print("\t1.\tSumatorio")
print("\t2.\tMedia")
print("\t3.\tMáximo")
print("\t4.\tMínimo")
print("\t0.\tSalir")
resp=int(input())
while resp<0 or resp>4:
    resp=int(input("Has introducido un numero no valido, introduce un numero valido: "))
if resp==1:
    sumatorio=0
    for i in lista:
        sumatorio=sumatorio+i
    print(f"El sumatorio es {sumatorio}")
elif resp==2:
    sumatorio=0
    for i in lista:
        sumatorio=sumatorio+i
    print(f"La media es {sumatorio/len(lista)}")
elif resp==3:
    maximo=-9999999999
    for i in lista:
        if i>maximo:
            maximo=i
    print(f"El maximo es {maximo}")
elif resp==4:
    minimo=9999999999
    for i in lista:
        if i<minimo:
            minimo=i
    print(f"El minimo es {minimo}")
else:
    print("Has decidido salir del programa")