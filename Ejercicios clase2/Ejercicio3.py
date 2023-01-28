numeros=[1,2,3.5,4,True,"holas"]    #creacion de lista de numero
print(numeros[-1])                  #nos entrega el ultimo valor de la lista
print(len(numeros))                 #imrpimimos longitud de "lista"
print(type(numeros))                #clase 'list'

if 4 in numeros:                    #consulta si 4 esta dentro de la lista
    print('el 4 se encuentra contenido en la lista')
else:
    print('El caracter no existe en lista')
#/////////////////////////////////////////////////////////

#'reverse' revierte el orden de listado     numeros.reverse()
#'remove' remueve un elemento de la lista   numeros.remove(2)
#'index' brinda posicion de elemento en lista   numeros.index(2)

# Listas anidadas
a = ['abc','dfe',False]
b = [1,2,3]
c = ['dasd','hola','mundo']

d = [a,b,c]






""" Vlista=[10,23,45,322,'hello']   #lista(array) es [] diccionario {}

a=type(Vlista[-1])

if a==str:
    print('el ultimo elemento es string')
else:
    print('el elemento no es string')
Vlista.append(2) """