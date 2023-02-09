import sys
argumentosIngresados=sys.argv
print(type(argumentosIngresados))

def leerArgumentos(*args):
    for arg in args:
        print(arg)

    nombre_archivo=sys.argv[0]    #obtenemos el nombre del scrip del primer argunmento
    longitud_argumentos=len(sys.argv) #calculamos la longitud
    nombre_archivo=str(sys.argv)  #obtenemos la representacion como str de la lista

    print(f'NOMBRE scrip: {nombre_archivo}')
    print(f'CANTIDAD de argumentos: {longitud_argumentos}')
    print(f'LISTA de argumentos: {nombre_archivo}')

leerArgumentos(*argumentosIngresados)