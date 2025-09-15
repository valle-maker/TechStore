from Verificacion import Verificacion #Se importa la clase verificación para manejar los tipos de datos de entrada
class Producto: 
    # Constructor de la clase producto
    def __init__(self, id, nombre, precio, cantidad):
        #Creamos una instancia de verificacion para usar el metodo de verificar los números enteros
        self.ver = Verificacion()
        #Definimos los atributos de la clase
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    #Creamos el método para pedir los datos al usuario 
    def pedir_datos(self):
        self.id = self.ver.leer_entero("Ingrese el id: ")
        self.nombre = input("Ingrese el nombre: ")
        self.precio = self.ver.leer_entero("Ingrese el precio: ")
        self.cantidad = self.ver.leer_entero("Ingrese la cantidad: ")
