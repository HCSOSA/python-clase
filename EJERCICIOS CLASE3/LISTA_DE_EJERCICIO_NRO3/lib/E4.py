""" 4. Una tienda de autopartes necesita un programa para catalogar sus productos ,crear la
clase Catálogo y producto ,realizar un objeto dentro de un catálogo productos el cual debe
tener un método para agregar productos y otra para mostrar toda la lista de productos. """

class Producto_Laptop:        #laptop
    def __init__(self,ram,pantalla,marca,almacenamiento):
        self.ram=ram
        self.pantalla=pantalla
        self.marca=marca
        self.almacenamiento=almacenamiento

    def __str__(self) -> str:
       return f"Notebook tiene siguientes especificaciones {self.ram} , {self.pantalla} , {self.almacenamiento} ,{self.marca}"

class Catalogo:
    listProductos=[]
    def __init__(self,listaProductos:list=[]):
        self.listProductos=listaProductos

    def agregar(self,p):
        self.listProductos.append(p)

    def mostrarCatalogo(self):          
        for i,p in enumerate(self.listProductos):  
            i+=1
            print(i,p)

try:
    p1=Producto_Laptop('8Gb','17inch','512Gb','MSI')
    p2=Producto_Laptop('16Gb','17inch','1Tb','ASUS')

    
    catalogo=Catalogo()
    catalogo.agregar(p1)
    catalogo.agregar(p2)
    catalogo.mostrarCatalogo()

except Exception as e:
    print("error al crear los productos")
