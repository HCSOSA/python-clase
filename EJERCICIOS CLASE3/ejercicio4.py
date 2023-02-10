#clase es estructura y objeto instancia
class Celular:      #creamos el objeto Celular. Para definir clase primero debemos definir una funcion
    def __init__(self,marca,pantalla:float,imei,camara):  #funcion que inicializa clase cuando se convierta en objeto 
        self.marca=marca                            #con self.xxx=xxx definimos las caracteristicas que tendra el objeto
        self.pantalla=pantalla                      #self siempre se usa para hacer referencia a valor de una clases
        self.imei=imei                              #poner objetos para que celular tenga identidad
        self.camara=camara                          #creamos nuevo atributo del objeto
        self.activado=False 
        self.apagado=True
        self.pantallaBloque=False

    def __str__(self) -> str:   #los que tienen doble __ son privados, definimos que sera de tipo string
                                #se usa ___str__ para poder escribir facilmente,si no usamos nos aparecera codigos abstractos
        return f"el celular tiene los siguientes atributos {self.marca} , {self.pantalla} , {self.imei} , {self.camara} y su estado de activacion es {self.activado} "
        #usamos f para fstring con este podemos poner variables en texto a mostrar

    def sizeDisplay(self)->float:                   #PANTALLA
        description=self.pantalla.split(sep='-')    #devuelve lista con segmentos separados
        return float(description[1])                #DEVUELVE valor de la funcion al programa principal
    
    def camaraFrontal(self)->float:                 #CAMARA
        camaraFrontal=self.camara.split(sep=',')    #para poner separacion ','
        return camaraFrontal[0]
    
    def activar(self,name):                         #siempre usar self
        print(name) 
        self.activado=True
    
    def estadoActivacion(self):         #lo usa asi ya que es un booleano
        if self.activado:
            return 'el celular esta activado'
        else:
            return 'el celular no se encuentra activado'
    
    def estadoPantalla(self):                       #c1 es el objeto,necesitamos la clase
        if self.apagado:
            print("el celular se encuentra apagado")
            return True
        else:
            print("el celular se ecuentra prendido")
            return False

    def bloquearPantalla(self):
        self.bloquearPantalla=True

    def prender(self):
        self.apagado=False  

    def apagar(self):
        self.apagado=True 

class Catalogo:
    listCelulares=[]
    def __init__(self,listaCelulares:list=[]):      #por defecto la lista siempre estara vacia   
        self.listCelulares=listaCelulares
    
    def agregar(self,c):
        self.listCelulares.append(c)
    
    def mostrarCatalogo(self):          
        for i,c in enumerate(self.listCelulares):        #para tener mas orden usamor enumerate
            i+=1
            print(i,c)

try:

    c1=Celular('nokia','retina-6.4','chi20232410','8,4,3')      ##OBJETO
    c2=Celular('lg','hd-6.2','thai2023123','7,2,3')
    #print(c1)
    a=c1.estadoActivacion()     #line28
    print(a)
    c1.activar("gianmarco")     #line24
    print(c1)
    a=c1.estadoPantalla()       #line34
    print(a)
    
    if a:
        print("el celular esta prendiendo")
        c1.prender()
    c1.estadoPantalla()

#definimos una listad de objetos celulares    
#    catalogo=[c1,c2]
#    for i in catalogo:
#        print(i)
    catalogo=Catalogo()
    catalogo.agregar(c1)
    catalogo.agregar(c2)
    catalogo.mostrarCatalogo()
    
    

except Exception as e:
    print("error al crear los objetos celulares")
    print(e)


#2:00:00