def ingresar_libros(archivo):
    resp='S'
    lista_libros=[]
    while resp!='N' and resp!="NO":
        titulo=input("Titulo del libro: ")
        autor=input("Autor: ")
        precio=float(input("Precio original: "))
        while precio<=0.01:
            precio=int(input("El precio no puede ser 0 o menor\nIntroduce el precio correcto: "))
        precio_con_descuento=float(input("Precio con descuento: "))
        while precio_con_descuento>=precio or precio_con_descuento<=0:
            precio_con_descuento=float(input("el precio con descuento no puede ser mayor o igual al precio ni 0 ni negativo\nIntroduce el precio con descuento correcto: "))
        cant_pag=int(input("Cantidad de paginas: "))
        libro=[titulo,autor,precio,precio_con_descuento,cant_pag]
        lista_libros.append(libro)
        resp=input("Deseas introducir otro libro? (S/N) ")
        resp=resp.upper()
    bbdd=open(archivo,'a')
    for i in range(len(lista_libros)):
        bbdd.write(repr(lista_libros[i])+"\n")
    bbdd.close()

def mas_descuento(archivo):
    bbdd=open(archivo,"r")
    linea=bbdd.readline()
    porcentaje_mayor=0
    libro=[]
    while linea!="":
        libro_recuperado=eval(linea)
        precio=int(libro_recuperado[2])
        precio_con_descuento=int(libro_recuperado[3])
        porcentaje=100-(precio_con_descuento*100/precio)
        print(porcentaje)
        if porcentaje>porcentaje_mayor:
            porcentaje_mayor=porcentaje
            libro=libro_recuperado
        linea=bbdd.readline()
    bbdd.close()
    print(f"El libro con mayor porcentaje de descuento es {libro[0]} y tiene un descuento de {porcentaje_mayor}%")

    
#ingresar_libros("textos/libreria")
mas_descuento("textos/libreria")