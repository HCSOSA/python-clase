msg="""Elija una de las siguientes opciones:

a)mostrar la suma de los dos numeros
b)mostrar la rsta de los dos numeros (1ro menos 2do)
c)mostrar la multip licacion de los dos numeros
"""
print(msg)
#obtner inputs de sde teclado
numeroOne=int(input("ingrese un valor: "))
numeroTwo=int(input('ingrese segundo valor :'))
opncionMenu=input('ingrese la opcion de menu: ')
#menu

print(numeroOne,numeroTwo,opncionMenu)

if(opncionMenu!='A' or opncionMenu!='B'or opncionMenu!='C'):
    if opncionMenu=='A':
        print(numeroOne+numeroTwo)
    elif opncionMenu=='B':
        print(numeroOne-numeroTwo)
    elif opncionMenu=='C':
        print(numeroOne*numeroTwo)
    else:
        print=('esta opcion no es valida')

else:
        print('elija una opcion correcta')