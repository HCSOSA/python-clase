msg="""Elija una de las siguientes opciones:

a)Realizar programa que dibuje cuadrado en consola con *
b)Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e
imprimir el número
c)Iterar una lista de elementos que contengan nombre y edad e imprimir solo los
mayores de edad.
"""
print(msg)

numeroOne=int(input("ingrese un valor: "))
OpcionMenu=input('ingrese la opcion de menu: ')

#menu

print(numeroOne,OpcionMenu)

if(OpcionMenu!='A' or OpcionMenu!='B' or OpcionMenu!='C'):
    if OpcionMenu=='A':
        for _ in range(4):
            print('****')
    elif OpcionMenu=='B':
            #Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e imprimir el número
            numeroIterar=[2,5,6,8,10,2.3]
    #elif OpcionMenu=='C':
            #Iterar una lista de elementos que contengan nombre y edad e imprimir solo los mayores de edad
else:
    print('ingrese otro valor')