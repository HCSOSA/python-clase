# numeros primos 2,3,5,7

numero=int(input("ingrese numero: "))
isPrimo=False

#ejm si pones 7, itera 2,3,4,5,6
for i in range(2,numero+1):   #recorrer numero con for, desde 2 
    if numero%i==0:           #verificamos si el numero que ingresa es multiplo
        isPrimo=False         #si es numero primo se detiene
        break

if isPrimo:
    print("el numero es primo")
else:
    print("el numero no es primo")


#2:55:00