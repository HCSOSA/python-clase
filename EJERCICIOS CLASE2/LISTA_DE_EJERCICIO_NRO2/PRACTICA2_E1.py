msg="""Elija una de las siguientes opciones:

a)Realizar programa que dibuje cuadrado en consola con *
b)Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e
imprimir el número
c)Iterar una lista de elementos que contengan nombre y edad e imprimir solo los
mayores de edad.
"""
print(msg)


OpcionMenu=input("ingrese la opcion de menu: ")

#opciones menu

if(OpcionMenu!='a' or OpcionMenu!='b' or OpcionMenu!='c'):
    if OpcionMenu=='a':
        numeroDigitado=int(input("ingrese un valor entero: "))
        for i in range(1,numeroDigitado+1):
            for e in range(1,numeroDigitado+1):
                print("*",end="")
            print("")   #para cambiar de renglon

    elif OpcionMenu=='b':
        listaIterar=[5,9,10,6,33,8]
        numeroMultiploDos=[]
        for n1 in listaIterar:
            if n1%2==0:
                numeroMultiploDos.append(n1)
                print(numeroMultiploDos)

    elif OpcionMenu=='c':
        nombresEdad=[["Juan",42],["Alexia",9],["Jenny",40]]
        Edades=[]
        mayoresEdad=[]
        Edades.append(nombresEdad[0][1])
        Edades.append(nombresEdad[1][1])
        Edades.append(nombresEdad[2][1])

        #print(Edades)
        for edad in Edades:
            if edad>=18:
                mayoresEdad.append(edad)
                print(mayoresEdad)
else:
    print("digite numero correcto")