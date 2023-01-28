""" def unafuncion(arg1,arg2,arg3,arg4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)

unafuncion("hola","i","o","y") """
#/////////////////////////////////////////////////////
""" def unafuncion(*args):     #puede recibir cuantos argumentos quiera ya que no sabemos cuantos agregaremos
    print(args)            #el * indica a python que le madnaran variables y las almacenara

unafuncion("hola","i","o","y","como",)  #todo se guardara dentro de tupla(no cambia) """
#/////////////////////////////////////////////////////
def total(*args):
    total=sum(args)
    print(total)
total(300,500,433,425424,324)