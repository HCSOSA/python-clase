#Una función recursiva de suma de los n primeros números
#try    necestit un except
#excep
try:  
    def sumaRecursiva(n:int):
        
        if n==1:
            return 1
        else:
            return n + sumaRecursiva(n-1)
    n=5
            
    print(sumaRecursiva(n))

except:
        print('corrio un error')