import random

class Persona:

    #constantes
    LETRAS=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
    SEXO="H"

    #constructor
    def __init__(self):
        self.__dni=self.generaDNI()
        self.__nombre=""
        self.__edad=0
        self.__sexo=self.SEXO
        self.__peso=0
        self.__altura=0
    
    #calcula el IMC
    def calcularIMC(self):
        if self.__altura>0:
            imc=self.__peso/(self.__altura**2)
        else:
            print("La altura no puede ser 0")
            return 2
        if imc<20:
            return -1
        elif imc<=25:
            return 0
        return 1
    
    #devuelve si es mayor de edad o no
    def esMayorDeEdad(self):
        return self.__edad>17
    
    #devulve toda la informacion de la persona usando __str__() y un metodo toString()
    def __str__(self):
        return(f"{self.__nombre} con DNI {self.__dni} tiene {self.__edad} anios, es {self.__sexo}, mide {self.__altura}m y pesa {self.__peso}Kg")

    def toString(self):
        print(f"{self.__nombre} con DNI {self.__dni} tiene {self.__edad} anios, es {self.__sexo}, mide {self.__altura}m y pesa {self.__peso}Kg")


    #genera un dni con numeros aleatorios y pone su letra correspondiente
    def generaDNI(self):
        numero=""
        for i in range(1,9):
            numero=numero+str(random.randint(0,9))
        return numero+self.LETRAS[int(numero)%23]
    
    #set de nombre
    def setNombre(self,nombre):
        self.__nombre=nombre

    #set de edad
    def setEdad(self,edad):
        self.__edad=edad
    
    #set de sexo
    def setSexo(self,sexo):
        self.__sexo=sexo
    
    #set de altura
    def setAltura(self,altura):
        self.__altura=altura

    #set de peso
    def setPeso(self,peso):
        self.__peso=peso

    #get de nombre
    def getNombre(self):
        return self.__nombre

#pruebas comentadas por el ejercicio 8
#p1=Persona()
#print(p1)