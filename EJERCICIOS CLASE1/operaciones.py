numero1=7
numero2=2

print('la suma es ',numero1+numero2)
print('la resta es ',numero1-numero2)
print('division ',numero1/numero2)
print('la division entera ',numero1//numero2)
print('el modulo es ',numero1%numero2)

#determina si un numero es multiplo de 2
numero3=123213213
numeroMultiplo=2
isMultiplo=numero3%2
isMultiplo=numero3%numeroMultiplo #maximo valor es numeroMultiplo -1
#para caso singular de 2 solo toma 0, 1 <> EL TIPO BOOLEANO 0 F y 1 T
print(isMultiplo)