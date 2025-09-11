from Verificacion import Verificacion
class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.ver = Verificacion()
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def pedir_datos(self):
        self.id = self.ver.leer_entero("Ingrese el id: ")
        self.nombre = input("Ingrese el nombre: ")
        self.precio = self.ver.leer_entero("Ingrese el precio: ")
        self.cantidad = self.ver.leer_entero("Ingrese la cantidad: ")
