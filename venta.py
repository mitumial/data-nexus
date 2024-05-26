import json
from datetime import datetime as dt
import re


class Cliente:
    pass


class Vehiculo:
    interes = 0.19

    def calcular_total(self):
        precio_total = self.vehiculo.precio * (1 + self.interes)
        return precio_total

    pass


class Venta:
    _id_venta = int
    _fecha = str
    _estado = str
    _cliente = Cliente
    _vehiculo = Vehiculo
    ventas_inventario = []

    def __init__(self, cliente=None, vehiculo=None):
        if not self.ventas_inventario:
            self._id_venta = 0
        else:
            self._id_venta = self.ventas_inventario[-1]["_id_venta"] + 1
        self._fecha = dt.now().strftime("%d-%m-%Y")
        self._estado = "No pagado"
        self._cliente = cliente
        self._vehiculo = vehiculo
        self.ventas_inventario.append(self)

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        if not re.match(r"\d{2}-\d{2}-\d{4}", value):
            raise ValueError("La fecha debe estar en formato dd-mm-yyyy")
        else:
            self._fecha = value

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, value):
        self._cliente = value

    @property
    def vehiculo(self):
        return self._vehiculo

    @vehiculo.setter
    def vehiculo(self, value):
        self._vehiculo = value

    def realizar_compra(self):
        if self.pago.cantidad < self.calcular_total():
            self._estado = "Pagado"
            self.tarjeta.fondos = self.tarjeta.fondos - self.vehiculo.precio

    def mostrar_detalles_venta(self):

        print(
            f"""\n
                Cliente:{self._cliente.nombres} {self._cliente.apellidos}
                \n
                Vehiculo:{self._vehiculo.marca} {self._vehiculo.modelo}
                \n
                Fecha:{self._fecha}
                \n
                Estado:{self._estado}
                \n
                Por la suma total de: {self._vehiculo.precio}
                \n
            """
        )

    def cancelar_compra(self):
        pass


def cargar_ventas(filename="./venta.json"):
    with open(filename, "r") as archivo:
        ventas = json.load(archivo)

    for venta in ventas:
        Venta.ventas_inventario.append(venta)


def guardar_venta(venta, filename="./venta.json"):
    with open(filename, "r+") as archivo:
        ventas = json.load(archivo)
        ventas.append(venta.__dict__)
        archivo.seek(0)
        json.dump(ventas, archivo, indent=4)


def realizar_venta(lista_vehiculos, lista_clientes):
    nueva_venta = Venta()
    mostrar_vehiculos_disponibles(lista_vehiculos)
    id_carro_seleccionado = input(
        "Ingrese el id correspondiente al vehiculo deseado: \n"
    )
    vehiculo_informacion = list(
        filter(
            lambda vehiculo: vehiculo["id"] == id_carro_seleccionado,
            Vehiculo.vehiculos_inventario,
        )
    )
    nueva_venta.vehiculo = vehiculo_informacion

    id_cliente_seleccionado = identificar_cliente(lista_clientes)
    cliente_informacion = list(
        filter(
            lambda cliente: cliente["id"] == id_cliente_seleccionado,
            Cliente.clientes_inventario,
        )
    )
    nueva_venta.cliente = cliente_informacion
    guardar_venta(nueva_venta)


def identificar_cliente(lista_clientes):
    doc = int(input("Ingrese su numero de documento:\n"))
    for cliente in lista_clientes:
        if cliente.documento == doc:
            while True:
                es_cliente = input(
                    f"¿Esta seguro que se identifica como {cliente.nombre} {cliente.apellidos}? (Si/No)\n"
                )
                if es_cliente.lower() == "si":
                    break
                print(f"Por favor, ingrese su documento de nuevo.\n")
            id_cliente_seleccionado = cliente.id_cliente
    return id_cliente_seleccionado


def mostrar_vehiculos_disponibles(lista_vehiculos):
    for vehiculo in lista_vehiculos:
        print("\n" + "-" * 50)
        print(f"[{vehiculo.id_vehiculo}] \t")
        print(f"Promoción especial! \033[9m{vehiculo.calcular_total()} pesos\033[0m")
        print(f"{vehiculo.precio * 1.19 * 5} pesos")
        print(f"{vehiculo.marca} {vehiculo.modelo}")
        print(f"{vehiculo.kilometraje} km | {vehiculo.año}")
        print("\n" + "-" * 50)


# def menu(lista_clientes, lista_vehiculos):

#     while True:
#         print("\n" + "-" * 50)
#         print("VENTA DE VEHICULOS")
#         print("1. Mostrar lista de todos los vehiculos disponibles")
#         print("2. Identifiquese")
#         print("3. Elegir metodo de pago")
#         print("4. Cancelar compra")

#         opcion = input("Seleccione una opción: ")

#         if opcion == "1":
#             mostrar_vehiculos_disponibles(lista_vehiculos)
#             id_carro_seleccionado = input(
#                 "Ingrese el id correspondiente al vehiculo deseado: \n"
#             )
#         elif opcion == "2":
#             id_cliente_seleccionado = identificar_cliente(lista_clientes)
#         elif opcion == "3":
#             pass
#         elif opcion == "4":
#             print("Saliendo del programa...")
#             break
#         else:
#             print("Opción no válida. Por favor, intente de nuevo.")

#     compra_de_vehiculo = Venta()
cargar_ventas()

mi_nueva_venta = Venta("addfsad", "gdsadaf")

guardar_venta(mi_nueva_venta)
# Ejecutar el menú
# menu()
