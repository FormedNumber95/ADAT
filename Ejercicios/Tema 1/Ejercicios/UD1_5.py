def sumatorio(lista):
    sumatorio=0
    for i in lista:
        sumatorio=sumatorio+i
    return sumatorio

def media(lista):
    return (sumatorio(lista)/len(lista))

def maximo(lista):
    maximo=-9999999999
    for i in lista:
        if i>maximo:
            maximo=i
    return maximo

def minimo(lista):
    minimo=9999999999
    for i in lista:
        if i<minimo:
            minimo=i
    return minimo

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
    print(f"El sumatorio es {sumatorio(lista)}")
elif resp==2:
    print(f"La media es {media(lista)}")
elif resp==3:
    print(f"El maximo es {maximo(lista)}")
elif resp==4:
    print(f"El minimo es {minimo(lista)}")
else:
    print("Has decidido salir del programa")