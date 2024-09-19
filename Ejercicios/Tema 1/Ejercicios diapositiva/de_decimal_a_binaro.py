def convertir_a_binario(numero,numero_entero,numero_fraccional):
  numero_final=''
  while numero!=0:
    if numero_entero>=1:
      while numero_entero>0:
        if numero_entero%2==0:
          numero_final="0"+numero_final
        else:
          numero_final="1"+numero_final
        numero_entero=int(numero_entero/2)
        if numero_entero==1:
          numero_entero=0
          numero_final="1"+numero_final
    if numero_fraccional!=0:
      numero_final=numero_final+"."
      while numero_fraccional!=0:
        numero_fraccional*=2
        if numero_fraccional>=1:
          numero_final=numero_final+"1"
          numero_fraccional=numero_fraccional-1
        else:
          numero_final=numero_final+"0"
    if numero_fraccional+numero_entero==0:
      numero=0
  return(numero_final)

numero=float(input("Pon el numero: "))
numero_entero=int(numero)
numero_fraccional=numero-numero_entero
print(convertir_a_binario(numero,numero_entero,numero_fraccional))