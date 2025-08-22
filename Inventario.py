
from Producto import Producto
import csv
class Inventario:
    def __init__(self):
        self.productos = []
        self.archivo_productos = "a_productos.csv"

    #Hacer la verificación de que no se puede agregar cero productos o negativos
    #Verificar que la lista no este vacia
    def agregar_productos(self):
        pro = Producto()
        pro.pedir_datos()
        self.productos.append(pro)
    
    #Método de busqueda
    #Mejorar este método con lo de los index
    
    def buscar_productos(self, id):
        pos = -1
        for i in range(len(self.productos)):
            if id == self.productos[i].id:
                pos = i
        if pos <0:
            print("No se encontro el producto")
        
        return pos




    #Preguntar si se pueden eliminar productos desde el archivo
    
    def eliminar_productos(self, id, cantidad):
        posicion = self.buscar_productos(id)

        if posicion >= 0:
            if self.productos[posicion].cantidad>0:
                if self.productosposicion[posicion].cantidad >= cantidad:
                    self.productos[posicion].cantidad -= cantidad
                else:
                    print(f"Quiere eliminar {cantidad}, pero solo hay {self.productos[posicion].cantidad}")
                    eliminar_todo = input("Eliminar todo (si/no)")
                    if eliminar_todo.lower()=='si':
                        self.productos[posicion].cantidad=0
                        return
                    else:
                        return
            else:
                print("Ya no quedan existencias del producto a eliminar")
        
#Mirar que métodos siguen 
#       

            
        
         



        




        
obj=Inventario()
obj.agregar_productos()
obj.buscar_productos(123)
obj.eliminar_productos(123, 8)
