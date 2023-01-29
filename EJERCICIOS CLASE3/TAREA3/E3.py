#Realizar una función que pase un entero por valor y lo multiplique por 2 y otra función
#VALOR  copia local de variable dentro de funcion
#REFERENCIA manejo directo de la variable cambio dentro de funcion afectaran fuera

def enteroToValor(a):      #definimos funcion entero
    a = a*2*otraFuncion
    print('valor de a dentro de la funcion "enteroToValor" es ', a)
    return a

def otraFuncion(b):
    b = 4
    return b

a = 10
print('valor de a a nivel global es ', a)