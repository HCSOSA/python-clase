""" Restaurante: haz una clase llamada Restaurante. El método __init __() para Restaurant debe almacenar dos atributos: 
un restaurant_name y un cuisine_type. Cree un método llamado describe_restaurant() que imprima estas dos piezas de información, 
y un método llamado open_restaurant () que imprima un mensaje indicando que el restaurante está abierto. """

class Restaurante:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant():
        print(f"el nombre del restaurante es: {self.restaurant_name} y el tipo de comida {self.cuisine_type}")

    def open_restaurant ():
        print(f"el restaurante {self.restaurant_name} esta abierto:")

    def __str__(self):
        return f"el restaurante{self.restaurant_name}"


""" Tres restaurantes: comience con su clase desde el ejercicio 1. Cree tres instancias diferentes de la clase y llame a 
describe_restaurant() para cada instancia. "restaurant_name"""
try:
        Restaurante1=Restaurante("rockys", "industrial")
        Restaurante1.describe_restaurant()
        a=Restaurante1
        print(Restaurante1)

except Exception as e:
        print("Error!!",e)


"""Usuarios: crea una clase llamada Usuario. Cree dos atributos llamados first_name y last_name, y luego cree varios 
otros atributos que normalmente se almacenan en un perfil de usuario. Cree un método llamado describe_user() 
que imprima un resumen de la información del usuario. Cree otro método llamado greet_user() que imprima un 
saludo personalizado para el usuario.

Cree varias instancias que representen a diferentes usuarios y llame a ambos métodos para cada usuario."""