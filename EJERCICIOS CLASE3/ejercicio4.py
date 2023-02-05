#clase es estructura y objeto instancia
class Celular:      #creamos el objeto Celular. Para definir clase primero debemos definir una funcion
    def __init__(self,marca,pantalla,imei,camara):  #funcion que inicializa clase cuando se convierta en objeto
        self.marca=marca                            #con self.xxx=xxx definimos las caracteristicas que tendra el objeto
        self.pantalla=pantalla                      #self siempre se usa para hacer referencia a valor de una clases
        self.imei=imei                              #poner objetos para que celular tenga identidad
        self.camara=camara                          #creamos nuevo atributo del objeto
        self.activado=False 
        self.apagado=True
        self.pantallaBloque=False

    def __str__(self) -> str:   #los que tienen doble __ son privados, definimos que sera de tipo string
        return f"el celular tiene los siguientes atributos{self.marca} , {self.pantalla} , {self.imei} , {self.camara} y su estado de activacion es {self.activado} "
        #usamos f para fstring con este podemos poner variables en texto a mostrar
    def sizeDisplay(self)->float:
        description=self.pantalla.split(sep='-')    #devuelve lista con segmentos separados
        return float(description[1])            #DEVUELVE valor de la funcion al programa principal
    
    def camaraFrontal(self)->float:
        camaraFrontal=self.camara.split(sep='-')
        return camaraFrontal[0]
    
    def activar(self,name):           ##siempre usar self
        print(name) 
        self.activado=True
    
    def estadoActivacion(self):
        if self.activado:
            return 'el celular esta activado'
        else:
            return 'el celular no se encuentra activado'
    
    def estadoPantalla(self):
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

try:

    c1=Celular('nokia','retina-6.4','chi20232410','8,4,3')
    #print(c1)
    a=c1.estadoActivacion()
    print(a)
    c1.activar("gianmarco")
    print(c1)
    c1.estadoPantalla()
    if a:
        print("el celular esta prendiendo")
        c1.prender()
    
    c1.estadoPantalla()

except Exception as e:
    print("error al crear los objetos celulares")
    print(e)
