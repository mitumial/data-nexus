from vehiculo import Vehiculo
from cliente import Cliente
import json
from datetime import datetime as dt
import re


class Venta:
    _id_venta = int
    _fecha = str
    _estado = str
    _id_cliente = int
    _id_vehiculo = int

    def __init__(
        self, id_venta=None, fecha=None, estado=None, id_cliente=None, id_vehiculo=None
    ):
        with open("./venta.json", "r", encoding="utf-8") as archivo:
            ventas = json.load(archivo)
            if id_venta is not None:
                self._id_venta = id_venta
            elif not ventas and (id_venta is None):
                self._id_venta = 0
            else:
                self._id_venta = ventas[-1]["_id_venta"] + 1

        if fecha is not None:
            self._fecha = fecha
        else:
            self._fecha = dt.now().strftime("%d-%m-%Y")

        if estado is not None:
            self._estado = estado
        else:
            self._estado = "No pagado"

        self._id_cliente = id_cliente
        self._id_vehiculo = id_vehiculo

    @property
    def id_venta(self):
        return self._id_venta

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
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, value):
        self._id_cliente = value

    @property
    def id_vehiculo(self):
        return self._id_vehiculo

    @id_vehiculo.setter
    def id_vehiculo(self, value):
        self._id_vehiculo = value

    # def realizar_compra(self):
    #     if self.pago.cantidad < self.calcular_total():
    #         self._estado = "Pagado"
    #         self.tarjeta.fondos = self.tarjeta.fondos - self.vehiculo.precio

    def mostrar_detalles_venta(self):
        with open("./cliente.json", "r", encoding="utf-8") as archivo:
            clientes = json.load(archivo)
            for cliente in clientes:
                if cliente["_id_cliente"] == self.id_cliente:
                    cliente_info = Cliente(
                        id_cliente=cliente["_id_cliente"],
                        nombre=cliente["_nombre"],
                        apellidos=cliente["_apellidos"],
                        documento=cliente["_documento"],
                        edad=cliente["_edad"],
                        genero=cliente["_genero"],
                        direccion=cliente["_direccion"],
                        email=cliente["_email"],
                        celular=cliente["_celular"],
                        vehiculos_comprados=cliente["_vehiculos_comprados"],
                    )
            with open("./vehiculo.json", "r", encoding="utf-8") as archivo:
                vehiculos = json.load(archivo)
                for vehiculo in vehiculos:
                    if vehiculo["_id_vehiculo"] == self.id_vehiculo:
                        vehiculo_info = Vehiculo(
                            id_vehiculo=vehiculo["_id_vehiculo"],
                            marca=vehiculo["_marca"],
                            modelo=vehiculo["_modelo"],
                            anio=vehiculo["_anio"],
                            placa=vehiculo["_placa"],
                            color=vehiculo["_color"],
                            combustible=vehiculo["_combustible"],
                            transmision=vehiculo["_transmision"],
                            cilindraje=vehiculo["_cilindraje"],
                            kilometraje=vehiculo["_kilometraje"],
                            puertas=vehiculo["_puertas"],
                            alarma=vehiculo["_alarma"],
                            sensor=vehiculo["_sensor"],
                            precio=vehiculo["_precio"],
                        )
                print(
                    f"""\n
                        Cliente:{cliente_info.nombre} {cliente_info.apellidos}
                        Vehiculo:{vehiculo_info.marca} {vehiculo_info.modelo}
                        Fecha:{self._fecha}
                        Estado:{self._estado}
                        Por la suma total de: {vehiculo_info.calcular_total()}
                        \n
                    """
                )

    def cancelar_compra(self, filename="./venta.json"):
        with open(filename, "r", encoding="utf-8") as f:
            ventas = json.load(f)

            id_venta = self._id_venta

            confirmacion = input(
                "¿Está seguro de que desea cancelar su compra? (s/n): "
            ).lower()

            if confirmacion == "s":
                for idx, obj in enumerate(ventas):
                    if obj["_id_venta"] == id_venta:
                        ventas.pop(idx)
                        print("Compra cancelada exitosamente.")
                        break
            else:
                print("Operación cancelada.")

            with open(filename, "w", encoding="utf-8") as f:
                json.dump(ventas, f, indent=4)


def guardar_venta(venta, filename="./venta.json"):
    with open(filename, "r+", encoding="utf-8") as archivo:
        ventas = json.load(archivo)
        ventas.append(venta.__dict__)
        archivo.seek(0)
        json.dump(ventas, archivo, indent=4)


def identificar_cliente():
    with open("./cliente.json", "r", encoding="utf-8") as archivo:
        clientes = json.load(archivo)
        if not clientes:
            print("No hay ningún cliente registrado.")
            return
        doc = int(input("Ingrese su numero de documento:\n"))
        for cliente in clientes:
            if cliente["_documento"] == doc:
                while True:
                    es_cliente = input(
                        f'¿Esta seguro que se identifica como {cliente["_nombre"]} {cliente["_apellidos"]}? (Si/No)\n'
                    )
                    if es_cliente.lower() == "si":
                        break
                    doc = int(input("Por favor, ingrese su documento de nuevo:\n"))
                id_cliente_seleccionado = cliente["_id_cliente"]
        print("Cliente identificado exitosamente.")
        return id_cliente_seleccionado


def mostrar_vehiculos_disponibles():
    with open("./vehiculo.json", "r", encoding="utf-8") as archivo:
        vehiculos = json.load(archivo)
        if not vehiculos:
            print("No hay ningún vehiculo disponible.")
            return
        for vehiculo in vehiculos:
            print("\n" + "-" * 50)
            print(f'[{vehiculo["_id_vehiculo"]}] \t')
            print(f'{vehiculo["_marca"]} {vehiculo["_modelo"]}')
            print(f'{vehiculo["_kilometraje"]} km | {vehiculo["_anio"]}')
            print(f'{vehiculo["_precio"]} pesos')


def seleccionar_vehiculo():
    mostrar_vehiculos_disponibles()
    id_vehiculo_seleccionado = input(
        "Ingrese el id correspondiente al vehiculo deseado: \n"
    )
    with open("./vehiculo.json", "r", encoding="utf-8") as archivo:
        vehiculos = json.load(archivo)
        for vehiculo in vehiculos:
            if vehiculo["_id_vehiculo"] == id_vehiculo_seleccionado:
                break
    print("Vehiculo seleccionado exitosamente.")
    return id_vehiculo_seleccionado


def realizar_compra():
    nueva_venta = Venta()
    nueva_venta.id_vehiculo = seleccionar_vehiculo()
    nueva_venta.id_cliente = identificar_cliente()
    guardar_venta(nueva_venta)
    print("Su transacción ha sido creada exitosamente")


def menu():
    while True:
        print("\n" + "-" * 50)
        print("VENTA DE VEHICULOS")
        print("1. Realizar nueva compra")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            realizar_compra()
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu()
