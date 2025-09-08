from Inventario import Inventario

class Main:
    def __init__(self):
        self.inventario = Inventario()
    def menu(self):
        
        
        while True:
            print("Menú")
            print("1. Añadir producto")
            print("2. Eliminar producto")
            print("3. Salir")
            print("4. Buscar productos por nombre")
            opcion = int(input("Ingrese la opcion del menu: "))
            match opcion:
                case 1:
                    self.inventario.agregar_productos()
                case 2:
                    id = int(input("Ingrese el id del producto a eliminar: "))
                    self.inventario.eliminar_producto(id)
                case 3:
                    print("Saliendo...")
                    break
                case 4:
                    nombre = input("Ingrese el nombre del producto que desea buscar: ")
                    self.inventario.buscar_productos_nombre(nombre)
                case _:
                    print("Opcion no valida")
            
                
menu = Main()
menu.menu()