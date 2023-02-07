import sys

def argumentosIngresados():
    nombre_archivo=sys.argv[0]    #obtenemos el nombre del scrip del primer argunmento
    longitud_argumentos=len(sys.argv) #calculamos la longitud
    nombre_archivo=str(sys.argv)  #obtenemos la representacion como str de la lista

    print('NOMBRE scrip: {}'.format(nombre_archivo))
    print('CANTIDAD de argumentos: {}'.format(longitud_argumentos))
    print('LISTA de argumentos: {}'.format(nombre_archivo))


argumentosIngresados()