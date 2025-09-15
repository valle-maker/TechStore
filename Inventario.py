
from Producto import Producto
import csv
class Inventario:
    #Constructor de la clase inventario
    def __init__(self):
        self.productos = [] # Lista dode se guarda la información de los porductos
        self.archivo_productos = "a_productos.csv" #Archivo donde se guarda de manera externa la información del producto
        self.actualizar_archivo() #Método que mantiene la información guardada en al archivo actualizada con la lista de productos

    #Método para agreagar productos
    def agregar_productos(self):
        pro = Producto(0, "", 0, 0) #Se inicializa una instancia de la clase con valores por defecto
        pro.pedir_datos() #Guardamos el objeto con los datos ingresados por el usuario
        self.productos.append(pro) #Guardamos el producto en la lista 
        self.guardar_archivo() #Sincronizamos la informacion de la lista y el archivo
        
    #Método para buscar productos por el atributo id   
    def buscar_productos(self, id):
        
        for i in range(len(self.productos)):
            if id == self.productos[i].id:
                return i
        print("No se encontró el producto")
        return None
    
    #Método que busca los productos por su nombre
    def buscar_productos_nombre(self, nombre):
        flag = False #Variable bandera que cambia su valor en caso de que se encuente
        for prod in self.productos: 
            if prod.nombre.lower()==nombre.lower():
                flag = True
                print("--Información del producto: ")
                print(f"Producto: {prod.nombre}\nPrecio: {prod.precio}\nExistencias: {prod.cantidad}")
        
        if not flag: #Si no se encuentra la variable no cambia su valor y podemos lanzar un mensaje de que no se encontró
            print("No se encontró el porducto")

    #Método que recorre la lista de productos y los muesta 
    def mostrar_prodcutos(self):
        i =0
        for pro in self.productos:
            i+=1
            print(f"Producto número: {i}")
            print(f"Nombre: {pro.nombre}\nPrecio: {pro.precio}\nExistencias: {pro.cantidad}\n")
    
    #Método que elimina los productos, requiere el id del producto a eliminar
    def eliminar_producto(self, id):
        pos = self.buscar_productos(id) #Se usa el métod de busqueda para encontrar el producto
        if pos is not None: # Se verifica que el producto a eliminar ocupe una posicion en la lista de prodcutos
            self.productos.pop(pos) #Los eliminamos de la lista con el método pop()
            print("Producto eliminado con exito!")
            self.guardar_archivo() #Sincronizamos los cambios de la lista y el archivo
        
        

    #Método no implementado por ahora
    # def eliminar_cantidad(self, id, cantidad):
    #     posicion = self.buscar_productos(id)

    #     if posicion >= 0:
    #         if self.productos[posicion].cantidad>0:
    #             if self.productos[posicion].cantidad >= cantidad:
    #                 self.actulizar_cantidad(id, self.productos[posicion].cantidad-cantidad)
    #             else:
    #                 print(f"Quiere eliminar {cantidad}, pero solo hay {self.productos[posicion].cantidad}")
    #                 eliminar_todo = input("Eliminar todo (si/no)")
    #                 #Acá se debe implementar el método del pop()
    #                 if eliminar_todo.lower()=='si':
    #                     self.productos[posicion].cantidad=0
    #                     return
    #                 else:
    #                     return
    #         else:
    #             print("Ya no quedan existencias del producto a eliminar")
    #     self.guardar_archivo()

    #Método que modifica el precio de los productos
    def actualizar_precio(self, id, n_precio): 
        pos = self.buscar_productos(id) #Busca la posicion del producto
        if pos is not None: #Verifica que el producto ocupe una posición en la lista 
            self.productos[pos].precio = n_precio #Y modifica el precio que tenia por el precio nuevo
        self.guardar_archivo() #Se sincroniza 

    #Método para actualizar la cantidad, funciona de manera similar al método de actulizar_precio
    def actulizar_cantidad(self, id, n_cantidad):
        pos = self.buscar_productos(id)
        if pos is not None:
            self.productos[pos].cantidad = n_cantidad
        
        self.guardar_archivo()

    #Método para guardar la información contenida de la lista en el archivo
    def guardar_archivo(self):
        with open(self.archivo_productos, "w", newline="") as f: #Abrimos el archivo en modo de escritura
            field_names = ['Id', 'Nombre' ,'Cantidad', 'Precio'] #como la información de los productos se guarda como diccionarios,
            #Creamos los valores de estos
            escritor = csv.DictWriter(f, fieldnames=field_names) 
            escritor.writeheader()
            for pro in self.productos: #ciclo que trae la información de la lista 
                escritor.writerow({ #Metodo para guardar diccionarios en archivos
                    #Cada elemento de la lista los guardamos con su respectivo valor 
                    'Id': pro.id,
                    'Nombre': pro.nombre,
                    'Cantidad': pro.cantidad,
                    'Precio': pro.precio
                })
        
    #Metodo para que la lista y el archivo siempre estan sincronizados 
    def actualizar_archivo(self):
        with open(self.archivo_productos, "r", newline="") as f: #ABrimos el archivo en modo lectura
            lector = csv.DictReader(f) #Usamos el método de lectura de archivos
            #Con el ciclo traemos cada elemeto del archvio
            for pro in lector:
                #Guardamos cada elemento en una variable con su tipo de datos
                id = int(pro['Id'])
                nombre = pro['Nombre']
                cantidad = int(pro['Cantidad'])
                precio = int(pro['Precio'])
                #Actualizamos la lista creando nuevamente los productos con la información contenida en el archivo
                self.productos.append(Producto(id, nombre, cantidad, precio))
        
        

