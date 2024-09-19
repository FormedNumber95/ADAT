lista=[]
sumatorio=0
for i in range(1,11):
    num=int(input(f"Dime el numero Nº{i} "))
    lista.append(num)
    sumatorio=sumatorio+num
media=sumatorio/len(lista)
print(lista)
print(f"El sumatorio es {sumatorio} y la media es {media}")