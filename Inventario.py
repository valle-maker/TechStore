
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
    
    #Método de busqueda
    def buscar_productos(self, id):
        pos = -1
        for i in range(len(self.productos)):
            if id == self.productos[i].id:
                pos = i
        if pos < 0:
            print("No hay un prodcuto con ese id")
        return pos




    #Proguntar si se pueden eliminar productos desde el archivo
    def eliminar_productos(self, id, cantidad):
        self.buscar_productos(id)#creo que la parte de poner la bandera para ver si se encontro se debe hacer el main
        #Algo como si flag entonces preguntar por la cantidad que desea eliminar, seria hacer un condicional como, si inv.buscar_productos()==-1 flag=False...
        #Lo hice en este método pero en el metodo de main tambien debo hacer algo parecido

        #Hacer las validaciones, aparte de la de los tipos, tambien la de exitencias para eliminar 
        if self.buscar_producto() >= 0:
            self.lista[self.buscar_productos()].cantidad -= cantidad

            
        
         



        




        
obj=Inventario()
obj.agregar_productos()
obj.buscar_productos(123)
#obj.eliminar_productos(123, 0)
