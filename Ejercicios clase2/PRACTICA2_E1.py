msg="""Elija una de las siguientes opciones:

a)Realizar programa que dibuje cuadrado en consola con *
b)Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e
imprimir el número
c)Iterar una lista de elementos que contengan nombre y edad e imprimir solo los
mayores de edad.
"""
print(msg)

numeroDigitado=int(input("ingrese un valor entero: "))
OpcionMenu=input("ingrese la opcion de menu: ")

#menu

print(numeroDigitado,OpcionMenu)

if(OpcionMenu!='a' or OpcionMenu!='b' or OpcionMenu!='c'):
    if OpcionMenu=='a':
        for i in range(1,numeroDigitado+1):
            for e in range(1,numeroDigitado+1):
                print("*",end="")
            print("")   #para cambiar de renglon

    elif OpcionMenu=='b':
        listaIterar=[5,32,5,44,8,'hola',7,9]
        numeroMultiploDos=[]
        for n1 in range(listaIterar):
            if n2 %2==0:
                numeroMultiploDos.append()
                print(numeroMultiploDos)

else:
    print("digite numero correcto")
