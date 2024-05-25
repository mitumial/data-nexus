import re
from datetime import datetime
class Vehiculo:
        id_vehiculo = int
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

        @property
        def año(self):
            return self._año

        @año.setter
        def año(self, value):
            current_year = datetime.now().year
            if value is not None:
                 if 1900 <= value <=current_year:
                      self.año = value
                 else:
                      raise ValueError(f"El año debe estar entre 1900 y {current_year}.")
            else:
                 self._año = value       

        @property
        def placa(self):
             return self._placa

        @placa.setter
        def placa(self, value):
             if not re.match(r"\w{3}-\d{3}", value):
                  raise ValueError("La placa debe estar en formato aaa-000") 
             else:
                  self._placa = value 

        @property
        def cilindraje(self):
            return self._cilindraje

        @cilindraje.setter
        def cilindraje(self, value):
            if not isinstance(value, (int, float)):
                raise ValueError("El cilindraje debe ser un número (entero o decimal)")
            if value <= 0 or value > 8.0:
                raise ValueError("El cilindraje debe ser un número positivo y razonable (por ejemplo, entre 0.5L y 8.0L)")
            else:
                self._cilindraje = value 
            
        @property
        def kilometraje(self):
            return self._kilometraje

        @kilometraje.setter
        def kilometraje(self, value):
            if not isinstance(value, int) or value < 0 or value > 2000:
                raise ValueError("El kilometraje debe ser un número entero no negativo que debe estar entre cero y 2000 km.")
            else:
                 self._kilometraje = value

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