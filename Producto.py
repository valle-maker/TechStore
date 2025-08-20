class Producto:
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.precio = 0
        self.cantidad = ""
    def pedir_datos(self):
        self.id = int(input("Ingrese el id del producto: "))
        self.nombre = input("Ingrese el nombre del producto: ")
        self.precio = int(input("Ingrese el precio del producto: "))
        self.cantidad = int(input("Ingrese cuantos productos vas a añadir: "))
