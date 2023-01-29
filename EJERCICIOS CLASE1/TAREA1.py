#ALUMNO: CONTRERAS SOSA HECTOR 
#EJERCICIO1
"""
n = input("ingrese primer nombre: ")
a = input("ingrese primer apellido: ")
e = int(input("ingrese edad: "))
c = input("Estado civil: ")

print(n)
print(a)
print(e)
print(c)"""

#EJERCICIO2
"""
r=float(input("Ingrese radio: "))
b=float(input("Ingrese base: "))
h=float(input("Ingrese altura: "))
pi=3.14
a1=r*pi
a2=(b*h)/2
a3=(r*2)*(r*2)

print("Area circulo",a1)
print("Area triangulo",a2)
print("Area cuadrado",a3)"""

#EJERCICIO3
"""
v1=int(input("Ingrese valor1 "))
v2=int(input("Ingrese valor2 "))
v3=int(input("Ingrese valor3 "))

print("la suma es",v1+v2+v3)
print("la resta es",v1-v2-v3)
print("la multiplicacion es",v1*v2*v3) 
print("la divicion es",v1/v2/v3)
print("la divicion entera es,",v1//v2//v3)"""

#EJERCICIO4
"""
a=int(input("Ingrese valor "))#puede ser INT,STR, FLOAT, etc
print(type(a))"""

#EJERCICIO5
"""
import sys
print(sys.argv)"""

#EJERCICIO6
"""
a=int(input("Ingrese valor final"))
b=0

for i in range(1, a+1):
    print(i)
    b=b+i
print("La suma es: ",b)"""

#EJERCICIO7
"""
numero1=input("Ingrese nro1: ")
numero2=input("Ingrese nro2: ")

print("son iguales: ", numero1==numero2)
print("son diferentes: ", numero1!=numero2)
print("el primero es mayor que el segundov", numero1>numero2)
print("el segundo es mayor o igual que el primero: ", numero1<=numero2)"""

#EJERCICIO8
"""
C1=str("contraseña")

C2=str(input("Digite contraseña: "))

print("Contraseña coincide: ", C2==C1)
print("Contraseña diferente: ", C2!=C1)"""