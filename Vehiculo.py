class Vehiculo:
        id_vehiculo = int
        marca = str
        modelo = str
        año = int
        placa = str
        color = str
        combustible = str
        transmision = str
        cilindraje = float
        kilometraje = float
        puertas = int
        alarma = bool
        sensor = bool
        precio = float
        lista_vehiculo = list

        def __init__(self, id_vehiculo=None, marca=None, modelo=None, año=None, placa=None, color=None, combustible=None, transmision=None, cilindraje=None, kilometraje=None, puertas=None, alarma=None, sensor=None, precio=None, lista_vehiculo=None):
            self.id_vehiculo = id_vehiculo
            self.marca = marca
            self.modelo = modelo
            self.año = año
            self.placa = placa
            self.color = color
            self.combustible = combustible
            self.transmision = transmision
            self.cilindraje = cilindraje
            self.kilometraje = kilometraje
            self.puertas = puertas
            self.alarma = alarma
            self.sensor = sensor
            self.precio = precio
            self.lista_vehiculo = lista_vehiculo

        def ingresar_vehiculo(self):
            print("-"*30)
            print("INGRESAR DATOS DEL VEHICULO:")
            self.id_vehiculo = int(input("Ingrese el id del vehiculo: \n"))
            self.marca = input("Ingrese la marca del vehiculo: \n")
            self.modelo = input("Ingrese el modelo del vehiculo: \n")
            self.año = int(input("Ingrese el año del vehiculo: \n"))
            self.placa = input("Ingrese la placa del vehiculo: \n")
            self.color = input("Ingrese el color del vehiculo: \n")
            self.combustible = input("Ingrese el tipo de combustible del vehiculo: \n")
            self.transmision = input("Ingrese el tipo de transmision del vehiculo \n (Manual, Automatica, CVT, Semiautomatica, Doble embrague): \n")
            self.cilindraje = float(input("Ingrese el cilindraje del vehiculo: \n"))
            self.kilometraje = float(input("Ingrese el kilometraje del vehiculo: \n"))
            self.puertas= int(input("Ingrese el numero de puertas del vehiculo: \n"))
            self.alarma = input("¿El vehiculo tiene alarma? (si/no): \n").lower() == "si"
            self.sensor = input("¿El vehiculo tiene sensores? (si/no): \n").lower() == "si"
            self.precio = float(input("Ingrese el precio del vehiculo: \n"))
            self.lista_vehiculo = []

        def mostrar_detalles_vehiculo(self):
            print("-"*30)
            print("DETALLES DEL VEHICULO")
            print("El id del vehiculo es: ",self.id_vehiculo)
            print("La marca del vehiculo es: ",self.marca)
            print("El modelo del vehiculo es: ",self.modelo)
            print("El año del vehiculo es: ",self.año)
            print("La placa del vehiculo es: ",self.placa)
            print("El color del vehiculo es: ",self.color)
            print("El tipo de combustible que utiliza el vehiculo es: ",self.combustible)
            print("El tipo de transmision del vehiculo es: ",self.transmision)
            print("el cilindraje del vehiculo es: ",self.cilindraje)
            print("El kilometraje del vehiculo es: ",self.kilometraje ,"km/h")
            print("El vehiculo tiene ",self.puertas ,"puertas")
            print("El vehiculo cuenta con alarma ",self.alarma)
            print("El vehiculo cuenta con sensor ",self.sensor)
            print("El vehiculo tiene un valor de ",self.precio ,"pesos")
            print("lista de vehiculos: ",self.lista_vehiculo)

        def borrar_vehiculo(self):
            pass 