
"""
for x in range(1,11,2):
    print(x)
    for (int i=1;i<11;i+=2) # en otros lenguajes"""


numeroIteraciones=int(input("ingresar numeros a iterar"))
numeros=list()

for i in range(1,numeroIteraciones+1):
    if i%2==0 and i%3==0 and i%5!=0:
        numeroAgregar=int(input("ingrese numero"))
        numeros.append(numeroAgregar)
        #numeros.append(i)
print(numeros)