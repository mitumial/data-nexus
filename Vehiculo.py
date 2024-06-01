import re
from datetime import datetime
import json

class Vehiculo:

        def __init__(
                self, 
                id_vehiculo=None, 
                marca=None, 
                modelo=None, 
                anio=None, 
                placa=None, 
                color=None, 
                combustible=None, 
                transmision=None, 
                cilindraje=None, 
                kilometraje=None, 
                puertas=None, 
                alarma=bool, 
                sensor=bool, 
                precio=None, 
                ):
            with open("./vehiculo.json", "r", encoding="utf-8") as archivo:
                vehiculos = json.load(archivo)
                if id_vehiculo is not None:
                  self._id_vehiculo = id_vehiculo
                elif  not self.vehiculo_inventario and (id_vehiculo is None):
                    self._id_vehiculo = 0     
                else:
                    self._id_vehiculo = vehiculos[-1]['_id_vehiculo'] + 1 
            self._marca = marca
            self._modelo = modelo
            self._anio = anio
            self._placa = placa
            self._color = color
            self._combustible = combustible
            self._transmision = transmision
            self._cilindraje = cilindraje
            self._kilometraje = kilometraje
            self._puertas = puertas
            self._alarma = alarma
            self._sensor = sensor
            self._precio = precio
            self.vehiculo_inventario.append(self)

        @property
        def marca(self):
            return self._marca

        @marca.setter
        def marca(self, value):
            self._marca = value

        @property
        def modelo(self):
            return self._modelo

        @modelo.setter
        def modelo(self, value):
            self._modelo = value

        @property
        def anio(self):
            return self._anio

        @anio.setter
        def anio(self, value):
            current_year = datetime.now().year
            if value is not None:
                 if 1800 <= value <= current_year:
                      self._anio = value
                 else:
                      raise ValueError(f"El año debe estar entre 1900 y {current_year}.")
            else:
                 self._anio = value       

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
        def color(self):
            return self._color

        @color.setter
        def color(self, value):
            self._color = value
        
        @property
        def combustible(self):
            return self._combustible

        @combustible.setter
        def combustible(self, value):
            tipos_validos_combustible = {'gasolina', 'diesel', 'electrica'}
            if value.lower() in tipos_validos_combustible:
                self._combustible = value.lower()
            else:
                raise ValueError(f"Tipo de combustible '{value}' no es válido. Debe ser 'gasolina', 'diésel' o 'eléctrica'.")

        @property
        def transmision(self):
            return self._transmision
        
        @transmision.setter
        def transmision(self,value):
            tipos_validos = {'manual', 'automatica', 'semiautomatica', 'cvt'}
            if value.lower() in tipos_validos:
                self._transmision = value.lower()
            else:
                raise ValueError(f"Tipo de transmisión '{value}' no es válido. Debe ser 'manual', 'automatica', 'semiautomatica' o 'cvt'.")

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
            if not isinstance(value, (int, float)) or value < 0 or value > 2000:
                raise ValueError("El kilometraje debe ser un número entero no negativo que debe estar entre cero y 2000 km.")
            else:
                 self._kilometraje = value
        
        @property
        def puertas(self):
            return self._puertas

        @puertas.setter
        def puertas(self, value):
             if value is not None:
                  if 0 < value <= 5:
                    self._puertas = value
                  else:
                      raise ValueError("el numero de puertas debe ser inferior a 5.")
             else:
                 self._puertas = value

        @property
        def alarma(self):
            return self._alarma

        @alarma.setter
        def alarma(self, value):
            if value.lower() == "si":
                self._alarma = True
            elif value.lower() == "no":
                self._alarma = False
            else:
                raise ValueError("Valor para alarma debe ser 'si' o 'no'.")

        @property
        def sensor(self):
            return self._sensor

        @sensor.setter
        def sensor(self, value):
            if value.lower() == "si":
                self._sensor = True
            elif value.lower() == "no":
                self._sensor = False
            else:
                raise ValueError("Valor para sensor debe ser 'si' o 'no'.")

        @property
        def precio(self):
            return self._precio
        
        @precio.setter
        def precio(self, value):
            if not isinstance(value, (int)) or value < 0:
                raise ValueError("El precio debe ser un numero entero mayor a cero, en formato (000_000_000).")
            else:
                self._precio = value


        def ingresar_vehiculo(self):
            print("-"*30)
            print("INGRESAR DATOS DEL VEHICULO:")
            self.marca = input("Ingrese la marca del vehiculo: \n")
            self.modelo = input("Ingrese el modelo del vehiculo: \n")
            self.anio = int(input("Ingrese el año del vehiculo: \n"))
            self.placa = input("Ingrese la placa del vehiculo: \n")
            self.color = input("Ingrese el color del vehiculo: \n")
            self.combustible = input("Ingrese el tipo de combustible del vehiculo \n (gasolina, diesel, electrica): \n")
            self.transmision = input("Ingrese el tipo de transmision del vehiculo \n (Manual, Automatica, CVT, Semiautomatica): \n")
            self.cilindraje = float(input("Ingrese el cilindraje del vehiculo \n(El cilindraje debe ser un número (entero o decimal entre 1 y 8.0)): \n"))
            self.kilometraje = float(input("Ingrese el kilometraje del vehiculo: \n"))
            self.puertas = int(input("Ingrese el numero de puertas del vehiculo: \n"))
            self.alarma = input("¿El vehiculo tiene alarma? (si/no): \n")
            self.sensor = input("¿El vehiculo tiene sensores? (si/no): \n")
            self.precio = float(input("Ingrese el precio del vehiculo: \n"))
                    

        def mostrar_detalles_vehiculo(self):
            print("-"*30)
            print("DETALLES DEL VEHICULO")
            print("El id del vehiculo es: ",self._id_vehiculo)
            print("La marca del vehiculo es: ",self._marca)
            print("El modelo del vehiculo es: ",self._modelo)
            print("El año del vehiculo es: ",self._anio)
            print("La placa del vehiculo es: ",self._placa)
            print("El color del vehiculo es: ",self._color)
            print("El tipo de combustible que utiliza el vehiculo es: ",self._combustible)
            print("El tipo de transmision del vehiculo es: ",self._transmision)
            print("el cilindraje del vehiculo es: ",self._cilindraje)
            print("El kilometraje del vehiculo es: ",self._kilometraje ,"km/h")
            print("El vehiculo tiene ",self._puertas ,"puertas")
            print("El vehiculo cuenta con alarma ",self._alarma)
            print("El vehiculo cuenta con sensor ",self._sensor)
            print("El vehiculo tiene un valor de ",self._precio ,"pesos")
            

def agregar_vehiculo():
    vehiculo = Vehiculo()
    vehiculo.ingresar_vehiculo()
    guardar_vehiculo(vehiculo)
    print("Vehiculo agregado exitosamente.")
   

def mostrar_todos_los_vehiculos(filename="./vehiculo.json"):
    with open(filename, "r", encoding="utf-8") as archivo:
        vehiculos = json.load(archivo)
        if not vehiculos:
            print("No hay ningún vehiculo registrado.")
            return
    for vehiculo in vehiculos:
        nuevo_vehiculo = Vehiculo(
            id_vehiculo= vehiculo["_id_vehiculo"],
            marca = vehiculo["_marca"],
            modelo = vehiculo["_modelo"],
            anio = vehiculo["_anio"],
            placa = vehiculo["_placa"],
            color = vehiculo["_color"],
            combustible = vehiculo["_combustible"],
            transmision = vehiculo["_transmision"],
            cilindraje = vehiculo["_cilindraje"],
            kilometraje = vehiculo["_kilometraje"],
            puertas = vehiculo["_puertas"],
            alarma = vehiculo["_alarma"],
            sensor = vehiculo["_sensor"],
            precio = vehiculo["_precio"],
        )
        nuevo_vehiculo.mostrar_detalles_vehiculo()
   
def eliminar_vehiculo(filename="./vehiculo.json"):
    with open(filename, "r", encoding="utf-8") as f:
        vehiculos = json.load(f)
        if not vehiculos:
            print("No hay ningún vehiculo registrado para borrar.")
            return

    id_vehiculo = int(input("Ingrese la ID del vehiculo que desea eliminar: "))

    confirmacion = input("¿Está seguro de que desea borrar este vehiculo? (s/n): ").lower()

    if confirmacion == "s":
        for idx, obj in enumerate(vehiculos):
            if obj["_id_vehiculo"] == id_vehiculo:
                vehiculos.pop(idx)
                print("Vehiculo borrado exitosamente.")
                break
        else:
            print("Vehiculo no encontrado.")
    else:
        print("Operación cancelada.")

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(vehiculos, f, indent=4)


def guardar_vehiculo(vehiculo, filename="./vehiculo.json"):
    with open(filename, "r+", encoding="utf-8") as archivo:
        try:
            archivo_datos = json.load(archivo)
        except json.JSONDecodeError:
            archivo_datos = []
        archivo_datos.append(vehiculo.__dict__)
        archivo.seek(0)
        json.dump(archivo_datos, archivo, indent=4)

def menu():
    while True:
        print("\n" + "-" * 50)
        print("MENÚ DE OPCIONES")
        print("1. Ingresar Vehiculo")
        print("2. Mostrar detalles de todos los vehiculos")
        print("3. Eliminar vehiculo")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_vehiculo()
        elif opcion == "2":
            mostrar_todos_los_vehiculos()
        elif opcion == "3":
            eliminar_vehiculo()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu()
