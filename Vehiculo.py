class Vehiculo:
        id_vehiculo= int
        marca= str
        modelo= str
        año= int
        placa= str
        color= str
        combustible= str
        transmision= str
        cilindraje= float
        kilometraje= float
        puertas= int
        alarma= bool
        sensor= bool
        precio = float

        def __init__(self, id_vehiculo, marca, modelo, año, placa, color, combustible, transmision, cilindraje, kilometraje, puertas, alarma, sensor, precio) -> None:
            self.id_vehiculo= id_vehiculo
            self.marca= marca
            self.modelo= modelo
            self.año= año
            self.placa= placa
            self.color= color
            self.combustible= combustible
            self.transmision= transmision
            self.cilindraje= cilindraje
            self.kilometraje= kilometraje
            self.puertas= puertas
            self.alarma= alarma
            self.sensor= sensor
            self.precio = precio
        
        def ingresar_vehiculo(self):
            print('-'*30)
            print('INGRESAR DATOS DEL VEHICULO:')
            self.id_vehiculo= int(input("Ingrese el id del vehiculo: \n"))
            self.marca= input("Ingrese la marca del vehiculo: \n")
            self.modelo= input("Ingrese el modelo del vehiculo: \n")
            self.año= int(input("Ingrese el año del vehiculo: \n"))
            self.placa= input("Ingrese la placa del vehiculo: \n")
            self.color= input("Ingrese el color del vehiculo: \n")
            self.combustible= input("Ingrese el tipo de combustible del vehiculo: \n")
            self.transmision= input("Ingrese el tipo de transmision del vehiculo \n (Manual, Automatica, CVT, Semiautomatica, Doble embrague): \n")
            self.cilindraje= float(input("Ingrese el cilindraje del vehiculo: \n"))
            self.kilometraje= float(input("Ingrese el kilometraje del vehiculo: \n"))
            self.puertas= int(input("Ingrese el numero de puertas del vehiculo: \n"))
            self.alarma= bool(input("¿El vehiculo tiene alarma? (si/no): \n"))
            '''if self.alarma.lower() == "sí":
                print("¡Genial!, el vehiculo tiene alarma")
            elif self.alarma.lower() == "no":
                print("El vehiculo no tiene alarma")
            else:
                print("Por favor, responde con 'sí' o 'no'.")'''
            self.sensor= bool(input("¿El vehiculo tiene sensores? (si/no): \n"))
            '''if self.sensor.lower() == "sí":
                print("¡Genial!, el vehiculo tiene sensor")
            elif self.sensor.lower() == "no":
                print("El vehiculo no tiene sensor")
            else:
                print("Por favor, responde con 'sí' o 'no'.")'''
            self.precio = float(input("Ingrese el precio del vehiculo: \n"))
            
        def mostrar_detalles_vehiculo(self):
            print('-'*30)
            print(f"El id del vehiculo es: {self.id_vehiculo}")
            print(f"La marca del vehiculo es: {self.marca}")
            print(f"El modelo del vehiculo es: {self.modelo}")
            print(f"El año del vehiculo es: {self.año}")
            print(f"La placa del vehiculo es: {self.placa}")
            print(f"El color del vehiculo es: {self.color}")
            print(f"El tipo de combustible que utiliza el vehiculo es: {self.combustible}")
            print(f"El tipo de transmision del vehiculo es: {self.transmision}")
            print(f"el cilindraje del vehiculo es: {self.cilindraje}")
            print
            pass

        def determinar_alarma(self):
            if self.alarma.lower() == "sí":
                print("¡Genial!, el vehiculo tiene alarma")
            elif self.alarma.lower() == "no":
                print("El vehiculo no tiene alarma")
            else:
                print("Por favor, responde con 'sí' o 'no'.")

        def determinar_sensor(self):
            if self.sensor.lower() == "sí":
                print("¡Genial!, el vehiculo tiene sensor")
            elif self.sensor.lower() == "no":
                print("El vehiculo no tiene sensor")
            else:
                print("Por favor, responde con 'sí' o 'no'.")
    
        def borrar_vehiculo():
            pass   