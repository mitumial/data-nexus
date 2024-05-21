from datetime import datetime as dt
import re


class Cliente:
    pass


class Vehiculo:
    pass


class Venta:
    _id_venta = str
    _fecha = str
    _estado = str
    cliente = Cliente
    vehiculo = Vehiculo
    interes = 0.19
    lista_ventas = []

    def __init__(self, cliente=None, vehiculo=None):
        if not self.lista_ventas:
            self._id_venta = 0
        else:
            self._id_venta = self.lista_ventas[-1]._id_venta + 1
        self._fecha = dt.now().strftime("%d-%m-%Y")
        self._estado = "No pagado"
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.lista_ventas.append(self)

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        if not re.match(r"\d{2}-\d{2}-\d{4}", value):
            raise ValueError("La fecha debe estar en formato dd-mm-yyyy")
        else:
            self._fecha = value

    def realizar_compra(self):
        if self.pago.cantidad < self.calcular_total():
            self._estado = "Pagado"
            self.tarjeta.fondos = self.tarjeta.fondos - self.vehiculo.precio

    def calcular_total(self):
        precio_total = self.vehiculo.precio * (1 + self.interes)
        return precio_total

    def mostrar_detalles_venta(self):
        print(
            f"""\n
                Cliente:{self.cliente.nombres} {self.cliente.apellidos}
                \n
                Vehiculo:{self.vehiculo.marca} {self.vehiculo.modelo}
                \n
                Fecha:{self._fecha}
                \n
                Estado:{self._estado}
                \n
                Por la suma total de: {self.vehiculo.precio}
                \n
            """
        )

    def cancelar_compra(self):
        pass


def identificar_cliente(lista_clientes):
    doc = int(input("Ingrese su numero de documento:\n"))
    for cliente in lista_clientes:
        if cliente.documento == doc:
            while True:
                es_cliente = input(
                    f"¿Esta seguro que se identifica como {cliente.nombre} {cliente.apellidos}?\n"
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
        print(f"Promoción especial! \033[9m{5_000_000 * 1.19} pesos\033[0m")
        print(f"{vehiculo.precio * 1.19 * 5} pesos")
        print(f"{vehiculo.marca} {vehiculo.modelo}")
        print(f"{vehiculo.kilometraje} km | {vehiculo.año}")
        print("\n" + "-" * 50)


def menu(lista_clientes, lista_vehiculos):

    while True:
        print("\n" + "-" * 50)
        print("VENTA DE VEHICULOS")
        print("1. Mostrar lista de todos los vehiculos disponibles")
        print("2. Identifiquese")
        print("3. Elegir metodo de pago")
        print("4. Cancelar compra")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_vehiculos_disponibles(lista_vehiculos)
            id_carro_seleccionado = input(
                "Ingrese el id correspondiente al vehiculo deseado: \n"
            )
        elif opcion == "2":
            id_cliente_seleccionado = identificar_cliente(lista_clientes)
        elif opcion == "3":
            pass
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


# Ejecutar el menú
# menu()


mySale = Venta()
mySale.fecha = "08-07-2025"
print(mySale.fecha)
