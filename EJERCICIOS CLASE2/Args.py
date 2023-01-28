def indeterminados_posicion(*args):     #cuand pongo asterirsco esque desconozco la cantidad de datos a recibir
        print(args)

indeterminados_posicion(5,"Hola",[1,2,3,4,5],{'dia':'sabado'})

def indeterminados_nombre(**kwargs):
    print(kwargs,type(kwargs))          #proporciona en clase diccionario
    #for kwarg in kwargs:
    #    print(kwarg, "=>", kwargs[kwarg])

indeterminados_nombre(n=5, c="Hola", l=[1,2,3,4,5])   