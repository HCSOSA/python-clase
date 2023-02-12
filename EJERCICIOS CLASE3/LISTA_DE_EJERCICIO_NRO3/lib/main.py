__name__=='__main__'

msg="""Elija una de las siguientes opciones:
a)Ejecutar ejercicio2
b)Ejecutar ejercicio3
c)Ejecutar ejercicio4
d)Ejecutar ejercicio7
e)Ejecutar ejercicio5.1
f)Ejecutar ejercicio5.2"""
print(msg)

OpcionMenu=input("ingrese la opcion de menu: ")

if(OpcionMenu!='a' or OpcionMenu!='b' or OpcionMenu!='c' or OpcionMenu!='d' or OpcionMenu!='e'or OpcionMenu!='f'):
    if OpcionMenu=='a':
        from E2 import *
        print('ejecutando ejercicio2')

    elif OpcionMenu!='b':
        from E3 import *
        print('ejecutando ejercicio3')
    
    elif OpcionMenu!='c':
        print('ejecutando ejercicio4')
    
    elif OpcionMenu!='d':
        from E7 import *
        print('ejecutando ejercicio7')
    
    elif OpcionMenu!='e':
        from E51 import *
        print('ejecutando ejercicio 5.1')
    
    elif OpcionMenu!='f':
        from E52 import *
        print('ejecutando ejercicio 5.2')
else:
    print("digite caracter correcto")
