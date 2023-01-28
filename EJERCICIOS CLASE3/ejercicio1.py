import sys
argumentos=sys .argv
print(type(argumentos))

def leerArgumentos(*args):  
    for arg in args:
        print(arg)


leerArgumentos(*argumentos)