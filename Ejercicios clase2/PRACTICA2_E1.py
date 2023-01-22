msg="""Elija una de las siguientes opciones:

a)Realizar programa que dibuje cuadrado en consola con *
b)Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e
imprimir el número
c)Iterar una lista de elementos que contengan nombre y edad e imprimir solo los
mayores de edad.
"""

#OPCION A
#OPCION B
#OPCION C

print(msg)
numeroOne=int(input("ingrese un valor: "))
numeroTwo=int(input('ingrese segundo valor :'))
OpcionMenu=input('ingrese la opcion de menu: ')

#menu

print(numeroOne,numeroTwo,OpcionMenu)

if(OpcionMenu!='A' or OpcionMenu!='B'or OpcionMenu!='C'):
    if OpcionMenu=='A':
        for _ in range(4):
            print('****')
    elif OpcionMenu=='B':
            #Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e imprimir el número
            a=int(input("Ingresa numero1"))
            b=int(input("Ingresa numero2"))
            if numero%2==0
                print("Es multiplo de 2")
            else:
                print('No es multiplo de 2')
    elif OpcionMenu=='C':
            #Iterar una lista de elementos que contengan nombre y edad e imprimir solo los mayores de edad
else:
        print('elija una opcion correcta')