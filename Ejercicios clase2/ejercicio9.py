#funciones

def myFunctionBasic():         #para crear funcion debemos escribir "def"
    print("Hello desde myFunctionBasic")

def myFunctionWithReturn():   
    return "Hello desde myFunctionWithReturn"

#myFunctionBasic()
#msg=myFunctionWithReturn()     #llamamos a una funcione escribiendo su nombre
#print(msg)                     #para llamar debemos asignarle una variable

def myFunctionWithParameters(a):
    print(a)

def myFunctionWithParametersV2(b):
    return b

def myFunctionWithParametersV3(c='default'):
    print(c)

def myFunctionWithParametersV4(a,b,c,d,e,f,g):
    print(a+b+c+d+e+f+g)

#el orden seguido es primero declarar la funcion y lueo implementar

myFunctionWithParameters(1)
x=myFunctionWithParametersV2(2)
print(x)
myFunctionWithParametersV3(3)
