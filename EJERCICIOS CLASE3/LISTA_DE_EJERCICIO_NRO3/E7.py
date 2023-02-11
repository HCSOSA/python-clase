""" crear un método que permita imprimir el objeto de forma literal (__str__) y que me permita identificar
el país de origen , el numero de lote . """

class Producto:
    def __init__(self,nombre,codigo):
        self.nombre=nombre      #PERU
        self.codigo=codigo      #0001-2023


    def __str__(self)->str:
        return f'El pais de origen es {self.nombre} y el numero de lote es {self.codigo}'       #cuando se usa return tenemos que agregar una variable

#///////////////////////////////////////////////////////////

class Catalogo:
    listProductos=[]
    def __init__(self,listaProductos:list=[]):      #por defecto la lista siempre estara vacia   
        self.listProductos=listaProductos
    

    def agregar(self,c):
        self.listProductos.append(c)
    #para enumerar
    def mostrarCatalogo(self):          
        for i,c in enumerate(self.listProductos):        #para tener mas orden usamos enumerate
            i+=1
            print(i,c)    

#///////////////////////////////////////////////////////////

try:
    pro1=Producto('ARGENTINA','2315-2023')
    pro2=Producto('BRASIL','4523-2023')

    catalogo=Catalogo()
    catalogo.agregar(pro1)
    catalogo.agregar(pro2)
    catalogo.mostrarCatalogo()

except Exception as e:
    print("error al crear los objetos celulares")
    print(e)