#msg abreviatura de mensaje
msg="""Elija una de las siguientes opciones:    

a)mostrar la suma de los dos numeros
b)mostrar la rsta de los dos numeros (1ro menos 2do)
c)mostrar la multiplicacion de los dos numeros
"""
print(msg)
#obtener inputs desde teclado
numeroOne=int(input("ingrese un valor: "))
numeroTwo=int(input('ingrese segundo valor:'))
opcionMenu=input('ingrese la opcion de menu: ')
#menu

print('V1: ',numeroOne,'V2: ',numeroTwo,'Op: ',opcionMenu)

if(opcionMenu!='A' or opcionMenu!='B'or opcionMenu!='C'): #si opcion de menu es distinto de A,B o C
    if opcionMenu=='A':                 #si letra digitada es igual 'A'
        print(numeroOne+numeroTwo)
    elif opcionMenu=='B':               #si letra digitada es igual 'B'
        print(numeroOne-numeroTwo)
    elif opcionMenu=='C':               #si letra digitada es igual 'C'
        print(numeroOne*numeroTwo)
    else:
        print('esta opcion no es valida')   #sino

else:
        print('elija una opcion correcta')  #sino


if True:
    pass
elif True:  #tomara el primer True
    pass
elif True:
    pass
else:
    pass