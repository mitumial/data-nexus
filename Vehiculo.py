import re
from datetime import datetime
import json

class Vehiculo:
        vehiculo_inventario = []

        def __init__(self, marca=None, modelo=None, año=None, placa=None, color=None, combustible=None, transmision=None, cilindraje=None, kilometraje=None, puertas=None, alarma=None, sensor=None, precio=None, lista_vehiculo=None):
            if not self.vehiculo_inventario:
                self._id_vehiculo = 0
            else:
                self._id_vehiculo = self.vehiculo_inventario[-1]["_id_vehiculo"] + 1
            self._marca = marca
            self._modelo = modelo
            self._año = año
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
            self._vehiculo_inventario.append(self)

        @property
        def año(self):
            return self._año

        @año.setter
        def año(self, value):
            current_year = datetime.now().year
            if value is not None:
                 if 1800 <= value <=current_year:
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
        def combustible(self):
            return self._combustible

        @combustible.setter
        def combustible(self, value):
            tipos_validos_combustible = {'gasolina', 'diésel', 'eléctrica'}
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
            if not isinstance(value, int) or value < 0 or value > 2000:
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
        def precio(self):
            return self._precio
        
        @precio.setter
        def precio(self, value):
            if not isinstance(value, int, float) or value < 0:
                raise ValueError("El precio debe ser un numero entero o decimal no negativo y mayor a cero.")
            else:
                self._precio = value


        def ingresar_vehiculo(self):
            print("-"*30)
            print("INGRESAR DATOS DEL VEHICULO:")
            self.id_vehiculo = int(input("Ingrese el id del vehiculo: \n"))
            self.marca = input("Ingrese la marca del vehiculo: \n")
            self.modelo = input("Ingrese el modelo del vehiculo: \n")
            self.año = int(input("Ingrese el año del vehiculo: \n"))
            self.año = int(input("Ingrese el año del vehiculo: \n"))
            self.placa = input("Ingrese la placa del vehiculo: \n")
            self.color = input("Ingrese el color del vehiculo: \n")
            self.combustible = input("Ingrese el tipo de combustible del vehiculo: \n")
            self.transmision = input("Ingrese el tipo de transmision del vehiculo \n (Manual, Automatica, CVT, Semiautomatica): \n")
            self.cilindraje = float(input("Ingrese el cilindraje del vehiculo: \n"))
            self.kilometraje = float(input("Ingrese el kilometraje del vehiculo: \n"))
            self.puertas= int(input("Ingrese el numero de puertas del vehiculo: \n"))
            self.alarma = input("¿El vehiculo tiene alarma? (si/no): \n").lower() == "si"
            self.sensor = input("¿El vehiculo tiene sensores? (si/no): \n").lower() == "si"
            self.precio = float(input("Ingrese el precio del vehiculo: \n"))
                
            self.vehiculo_inventario = []

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

def agregar_vehiculo():
    vehiculo = Vehiculo()
    vehiculo.ingresar_vehiculo()
    #if vehiculo.marca and vehiculo.modelo and vehiculo.año and vehiculo.placa and vehiculo.color and vehiculo.combustible and vehiculo.transmision and vehiculo.cilindraje and vehiculo.kilometraje and vehiculo.puertas and vehiculo.alarma and vehiculo.sensor and vehiculo.precio:
    Vehiculo.vehiculo_inventario.append(vehiculo)
    guardar_vehiculo(vehiculo)
    print("Vehiculo agregado exitosamente.")
    #else:
       # print("Error: Datos del vehiculo incompletos o incorrectos.")


def mostrar_todos_los_vehiculos():
    if not Vehiculo.vehiculo_inventario:
        print("No hay ningún vehiculo registrado.")
        return
    for vehiculo in Vehiculo.vehiculo_inventario:
        vehiculo.mostrar_detalles_vehiculo()

def buscar_vehiculo_por_id(id_vehiculo):
    for vehiculo in Vehiculo.vehiculo_inventario:
        if vehiculo.id_vehiculo == id_vehiculo:
            return vehiculo
    return None
    
def eliminar_vehiculo():
    if not Vehiculo.vehiculo_inventario:
        print("No hay ningún vehiculo registrado para borrar.")
        return

    id_vehiculo = int(input("Ingrese la ID del vehiculo que desea eliminar: "))
    Vehiculo = buscar_vehiculo_por_id(id_vehiculo)

    if Vehiculo:
        confirmacion = input("¿Está seguro de que desea borrar este vehiculo? (s/n): ").lower()
        if confirmacion == "s":
            Vehiculo.vehiculo_inventario.remove(Vehiculo)
            print("vehiculo borrado exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print("Vehiculo no encontrado.")

def cargar_vehiculo(filename="./vehiculo.json"):
    with open(filename, "r") as archivo:
        vehiculos = json.load(archivo)

    for vehiculo in vehiculos:
        Vehiculo.vehiculo_inventario.append(Vehiculo(vehiculo["_marca"], vehiculo["_modelo"], vehiculo["_año"], vehiculo["_placa"], vehiculo["_color"], vehiculo["_combustible"], vehiculo["_transmision"], vehiculo["_cilindraje"], vehiculo["_kilometraje"], vehiculo["_puertas"], vehiculo["_alarma"], vehiculo["_sensor"], vehiculo["_precio"], vehiculo["_vehiculo_inventario"]))         #modificar y agg los atributos a usar como aleja - que se ingresan

def guardar_vehiculo(vehiculo, filename="./vehiculo.json"):
    with open(filename, "r+") as archivo:
        archivo_datos = json.load(archivo)
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


cargar_vehiculo()
menu()
