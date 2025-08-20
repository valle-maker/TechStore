#Voy en el segundo requerimiento 
from Producto import Producto
import csv
class Inventario:
    def __init__(self):
        self.productos = []
        self.archivo_productos = "a_productos.csv"


    def agregar_productos(self):
        pro = Producto()
        pro.pedir_datos()
        self.productos.append(pro)


    #Proguntar si se pueden eliminar productos desde el archivo
    def eliminar_productos(self, id, cantidad):
        self.productos.remove()




        
obj=Inventario()
obj.agregar_productos()

