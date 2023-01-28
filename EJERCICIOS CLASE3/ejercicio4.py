#clase es estructura y objeto instancia
class Celular:      #para definir clase primero debemos definir una funcion
    def __init__(self,marca,pantalla,imei,camara):  #funcion que inicializa clase cuando se convierta en objeto
        self.marca=marca        
        self.pantalla=pantalla
        self.imei=imei
        self.camara=camara
        self.activado=False
    def __str__(self) -> str:   #creamos otra funcion 
        return f"el celular tiene los siguientes atributos{self.marca},{self.pantalla},{self.imei},{self.camara} y su estado de activacion es activado  "
    
    def sizeDisplay(self)->float:
        description=self.pantalla.split(sep='-')
        return float(description[1])
    
    def camaraFrontal(self)->float:
        camaraFrontal=self.camara.split(sep='-')
        return camaraFrontal[0]
    
    def activar(self,name):           ##siempre usar self
        print(name) 
        self.activado=True
    
    def estado(self):
        if self.activado:
            return 'el celular esta activado'
        else:
            return 'el celular no se encuentra activado'


try:
    c1=Celular('nokia','retina-6.4','chi20232410','8,4,3')
    print(c1)
    c1.estado()
    c1.activar("gianmarco")
    print(c1)
except Exception as e:
    print("error al crear los objetos celulares")
    print(e)
