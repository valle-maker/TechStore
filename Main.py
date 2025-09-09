#Si ingreso una opción que no es, marca error
from Verificacion import Verificacion
from Inventario import Inventario

class Main:
    def __init__(self):
        self.inventario = Inventario()
        self.ver = Verificacion()
    def menu(self):
        
        
        while True:
            print("Menú")
            print("1. Añadir producto")
            print("2. Eliminar producto")
            print("3. Buscar productos por nombre")
            print("4. Mostrar la lista de los productos")
            print("5. Actualizar cantidad")
            print("6. Actulizar precio")
            print("7. Salir")
            opcion = self.ver.leer_entero("Ingrese la opcion del menú: ")
            match opcion:
                case 1:
                    self.inventario.agregar_productos()
                case 2:
                    id = self.ver.leer_entero("Ingrese el id del producto")
                    self.inventario.eliminar_producto(id)
                
                case 3:
                    nombre = input("Ingrese el nombre del producto que desea buscar: ")
                    self.inventario.buscar_productos_nombre(nombre)
                case 4:
                    self.inventario.mostrar_prodcutos()
                case 5: 
                    id_prodcuto = self.ver.leer_entero("Ingrese el id del producto: ")
                    n_cantidad = self.ver.leer_entero("Ingrese la nueva cantidad: ")
                    self.inventario.actulizar_cantidad(id_prodcuto, n_cantidad)

                case 6:
                    id_prodcuto = self.ver.leer_entero("Ingrese el id del producto: ")
                    n_cantidad = self.ver.leer_entero("Ingrese el nuevo precio: ")
                    self.inventario.actualizar_precio(id_prodcuto, n_cantidad)
                case 7:
                    print("Saliendo...")
                    break
                case _:
                    print("Opcion no valida")
                
            
                
menu = Main()
menu.menu()