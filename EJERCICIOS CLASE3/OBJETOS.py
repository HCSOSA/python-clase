"""CLASE	plantilla o molde del cual provienen objeto  

persona,carro			        clase
caracteristicas objeto		    atributos del objeto
acciones que puede realizar	    metodos

EJEMPLO
objeto			    humano
atributos		    color de piel,piel,nacionalidad,estatura
acciones,metodos	caminar,correr,levantarse,dormir"""

#////////////////////////////////////////////////////////////////////

class Humano:                                #CLASE
    def __init__(self,edad):                    
        self.edad=edad                       #ATRIBUTO  

    def hablar(self,mensaje):                #METODO
        print(mensaje)                      

Pedro=Humano(26)  #OBJETO
Raul=Humano(21)   #creamos objeto que tiene como plantilla a clase humano
#podra acceder a todos los metodos y atributos que tenga dentro de objeto

print(f'Soy Raul y tengo {Raul.edad}')
print(f'Soy Pedro y tengo {Pedro.edad}')

Pedro.hablar('Hola')        #
Raul.hablar('hola,Pedro!')  #