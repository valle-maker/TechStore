class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def pedir_datos(self):
        self.id = int(input("Ingrese el id del producto: "))
        self.nombre = input("Ingrese el nombre del producto: ")
        self.precio = int(input("Ingrese el precio del producto: "))
        self.cantidad = int(input("Ingrese cuantos productos vas a añadir: "))
