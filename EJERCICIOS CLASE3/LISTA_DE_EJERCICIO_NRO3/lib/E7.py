""" Programa que tenga una "CLASE" Producto el cual solo tiene el 
"ATRIBUTO" de nombre ,codigo el cual tiene la siguiente estructura
 ‘PAIS-LOTE-AÑO’ ejemplo : ‘PERU-0001-2023’ crear un "METODO" que permita 
 imprimir el objeto de forma literal (__str__) y que me permita 
 identificar el país  de origen , el numero de lote """

class Producto:
    def __init__(self,nombre,codigo,stock):
        self.nombre=nombre
        self.codigo=codigo
        self.stock=True
        #self.año=año
    def __str__(self)->str:
        return f'El pais de origen es {self.nombre}, el numero de lote {self.codigo}'

    def disponible(self,name):
        print(name)
        self.stock=False
    
    def estadoStock(self):
        if self.stock:
            return 'el producto tiene stock en estos paises'
        else:
            return 'el producto no tiene stock'
   
class Catalogo:
    listProductos=[]
    def __init__(self,listaProductos:list=[]):
        self.listProductos=listaProductos
    
    def agregar(self,p):
        self.listProductos.append(p)

    def mostrarCatalogo(self):          
        for i,p in enumerate(self.listProductos):        #para tener mas orden usamos enumerate
            i+=1
            print(i,p)

try:
    p1=Producto('PR','2410','2001')
    p2=Producto('BR','0708','2003')
    p3=Producto('EEUU','1012','2012')

    a=p1.estadoStock()
    print(a)

    print(p3)
    
    #agregamos variables a catalogo
    catalogo=Catalogo()
    catalogo.agregar(p1)
    catalogo.agregar(p2)
    catalogo.agregar(p3)
    catalogo.mostrarCatalogo()


except Exception as e:
    print("error al crear los productos")
    print(e)