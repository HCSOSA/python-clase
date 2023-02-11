""" Programa que tenga una "CLASE" Producto el cual solo tiene el 
"ATRIBUTO" de nombre ,codigo el cual tiene la siguiente estructura
 ‘PAIS-LOTE-AÑO’ ejemplo : ‘PERU-0001-2023’ crear un "METODO" que permita 
 imprimir el objeto de forma literal (__str__) y que me permita 
 identificar el país  de origen , el numero de lote """

class Producto:
    def __init__(self,nombre,codigo):
        self.nombre=nombre
        self.codigo=codigo
        self.stock=False
    

    def disponible(self,name):
        print(name)
        self.stock=True
    
    def estadoStock(self):
        if self.stock:
            return 'el producto tiene stock'
        else:
            return 'el producto no tiene stock'

    def __str__(self)->str:
        return f'El pais de origen es {self.nombre} y el numero de lote {self.codigo}'


class Catalogo:
    listProductos=[]
    def __init__(self,listaProductos:list=[]):
        self.listProductos=listaProductos
    
    def agregar(self,p):
        self.listProductos.append(p)

    def mostrarCatalogo(self):          
        for i,p in enumerate(self.listProductos):        #para tener mas orden usamor enumerate
            i+=1
            print(i,p)

try:
    p1=Producto('PERU','2410','2023')

    a=p1.estadoStock()
    print(a)


except Exception as e:
    print("error al crear los productos")
    print(e)