def sumaTres(n):        #primero def-nombreDeFuncion-valoriable
    print(n+3)


def tablaDeMultiplicar(n):          #tabla de multiplicar
     for i in range(1,11):          #valor incial 1 y final 11
        print(n,'*',i,'=',i*n)      #mostrara valor de n,numero de iteracion,multiplicacion de n*nro iteracion

def cadena():
    return 'cursoDePython'
print(cadena())

n=5
def funcion():
    print(n)



ejemplo=[3,7,9,5,8,3,7,12]       #creamos lista

def separarLista(lista):        #creamos funcion y creamos elemento lista
    lista.sort()                #usamos short para tener orden
    pares=[]                    #clasificamos en 2 pares de listas
    impares=[]
    for i in lista:             #para iterar entre cada uno de elementos de lista usamos for
        if i%2==0:               #condicion para elemento par
            pares.append(i)     
        else:
            impares.append(i)
    return pares,impares


pares,impares = separarLista(ejemplo)

print(pares)
print(impares)