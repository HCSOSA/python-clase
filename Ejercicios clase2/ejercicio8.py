# numeros primos 2,3,5,7

numero=int(input("ingrese un numero"))
isPrimo=False
for i in range(2,numero+1):
    if numero%i==0:
        isPrimo=True
        break

if isPrimo:
    print("el numeor es primo")
else:
    print("el numero no es primo")
