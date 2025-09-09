class Verificacion:
    def leer_entero(self, mensaje):
        
        while True:
            try:
                entero = int(input(mensaje))
                if entero <0:
                    print("Error, el número debe ser positivo") 
                else:
                    return entero
            except ValueError:
                print("Carácter invalido")

        