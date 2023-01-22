Vlista=[10,23,45,322,'hello']

a=type(Vlista[-1])

if a==str:
    print('el ultimo elemento es string')
else:
    print('el elemento no es string')
Vlista.append(2)