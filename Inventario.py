#Tareas:
#Actulizar precio o cantidada de producto existente 
#Hacer la verificación de que no se puede agregar cero productos o negativos(Ya sea hacer el método o la clase)
#Verificar que la lista no este vacia(Hacer que el método de verificacion funcione)
#Separar los inpus y los outputs
#Mirar si se puede usar el método de actulizar_cantidad en el de eliminar por ejemplo
#Para la parte del main, se guarda siempre un objeto, esto es para cuando lo este guardando en listas
#Ya esta melo y guardo en archivos, falta el método para actulizar 



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
        self.guardar_archivo()

    
    def verificar_lista_vacia(self):
        if self.productos == []:
            print("EL inventario esta vacio")
            return -1
        else:
            return 1
        
        
    def buscar_productos(self, id):
        verificacion_lista = self.verificar_lista_vacia()
        if verificacion_lista==1:
            pos = -1
            for i in range(len(self.productos)):
                if id == self.productos[i].id:
                    pos = i
            if pos <0:
                print("No se encontro el producto")
            
            return pos
        
        
    def buscar_productos_nombre(self, nombre):
        #Incluir la verificación de que la lista tenga datos
        for prod in self.productos: 
            if prod.nombre==nombre:
                print(f"Producto: {prod.nombre}\nPrecio: {prod.precio}\nExistencias: {prod.cantidad}")
            else:
                print("No se encontro el producto")


    def mostrar_prodcutos(self):
        for pro in self.productos:
            print(f"Nombre:{pro.nombre}\nPrecio:{pro.precio}\nExistencias: {pro.cantidad}")


    def eliminar_productos(self, id, cantidad):
        posicion = self.buscar_productos(id)

        if posicion >= 0:
            if self.productos[posicion].cantidad>0:
                if self.productos[posicion].cantidad >= cantidad:
                    self.actulizar_cantidad(id, self.productos[posicion].cantidad-cantidad)
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
        self.guardar_archivo()

    def actualizar_precio(self, id, n_precio):
        pos = self.buscar_productos(id)
        if pos >= 0:
            self.productos[pos].precio = n_precio
        self.guardar_archivo()


    def actulizar_cantidad(self, id, n_cantidad):
        #Hacer las verificaciones de ingresar nuevas cantidades
        pos = self.buscar_productos(id)
        if pos >=0:
            self.productos[pos].cantidad = n_cantidad
        self.guardar_archivo()

    def guardar_archivo(self):
        with open(self.archivo_productos, "w", newline="") as f:
            field_names = ['Id', 'Nombre' ,'Cantidad', 'Precio']
            escritor = csv.DictWriter(f, fieldnames=field_names)
            escritor.writeheader()
            for pro in self.productos:
                escritor.writerow({
                    'Id': pro.id,
                    'Nombre': pro.nombre,
                    'Cantidad': pro.cantidad,
                    'Precio': pro.cantidad
                })

        
       
        
obj=Inventario()
obj.agregar_productos()
#obj.actualizar_precio(123, 3000)
#obj.buscar_productos_nombre("dell")
#obj.buscar_productos(123)
obj.eliminar_productos(123, 8)
obj.mostrar_prodcutos()
