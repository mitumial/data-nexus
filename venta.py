import pago
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

    def realizar_pago(self, filename="./venta.json"):
        pago.registrar_pago(self._id_cliente, self.id_vehiculo)
        with open(filename, "r", encoding="utf-8") as archivo:
            ventas = json.load(archivo)
            for venta in ventas:
                if venta["_id_venta"] == self.id_venta:
                    venta["_estado"] = "Pagado"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(ventas, f, indent=4)
        borrar_vehiculo(self._id_vehiculo, filename="./vehiculo.json")

    def mostrar_detalles_venta(self):
        with open("./cliente.json", "r", encoding="utf-8") as archivo:
            clientes = json.load(archivo)
            for cliente in clientes:
                if cliente["_id_cliente"] == self.id_cliente:
                    cliente_info = cliente
        with open("./vehiculo.json", "r", encoding="utf-8") as archivo:
            vehiculos = json.load(archivo)
            for vehiculo in vehiculos:
                if vehiculo["_id_vehiculo"] == self.id_vehiculo:
                    vehiculo_info = vehiculo
        print(
            f"""\n
                Cliente: {cliente_info["_nombre"]} {cliente_info["_apellidos"]}
                Vehiculo: {vehiculo_info["_marca"]} {vehiculo_info["_modelo"]}
                Fecha: {self._fecha}
                Estado: {self._estado}
                Por la suma total de: {vehiculo_info["_precio"]} pesos
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
        for cliente in clientes:
            while True:
                doc = int(input("Ingrese su numero de documento:\n"))
                cliente = next(
                    (c for c in clientes if c["_documento"] == doc),
                    None,
                )
                if cliente is None:
                    print("Cliente no encontrado.")
                    continue
                if cliente["_documento"] == doc:
                    es_cliente = input(
                        f'¿Esta seguro que se identifica como {cliente["_nombre"]} {cliente["_apellidos"]}? (Si/No)\n'
                    )
                    if es_cliente.lower() == "si":
                        id_cliente_seleccionado = cliente["_id_cliente"]
                        print("Cliente identificado exitosamente.")
                        return id_cliente_seleccionado
                    else:
                        continue


def mostrar_vehiculos_disponibles(
    marca=None, modelo=None, anio=None, precio=None, opcion=None
):
    if opcion is not None:
        filtro_valor = next(f for f in [marca, modelo, anio, precio] if f != None)
        if opcion == "anio" or opcion == "precio":
            filtro_valor = int(filtro_valor)
        with open("./vehiculo.json", "r", encoding="utf-8") as archivo:
            vehiculos = json.load(archivo)
            if not vehiculos:
                print("No hay ningún vehiculo disponible.")
                return
            flag = True
            for vehiculo in vehiculos:
                if opcion == "precio":
                    if vehiculo[f"_{opcion}"] <= filtro_valor:
                        print("-" * 50)
                        print(f'[{vehiculo["_id_vehiculo"]}] \t')
                        print(f'{vehiculo["_marca"]} {vehiculo["_modelo"]}')
                        print(f'{vehiculo["_kilometraje"]} km | {vehiculo["_anio"]}')
                        print(f'{vehiculo["_precio"]} pesos')
                        print("-" * 50)
                        flag = False
                else:
                    if vehiculo[f"_{opcion}"] == filtro_valor:
                        print("-" * 50)
                        print(f'[{vehiculo["_id_vehiculo"]}] \t')
                        print(f'{vehiculo["_marca"]} {vehiculo["_modelo"]}')
                        print(f'{vehiculo["_kilometraje"]} km | {vehiculo["_anio"]}')
                        print(f'{vehiculo["_precio"]} pesos')
                        print("-" * 50)
                        flag = False
            if flag:
                print("No se encontraron vehiculos disponibles que cumplan su filtro")
                seleccionar_vehiculo()
    else:
        with open("./vehiculo.json", "r", encoding="utf-8") as archivo:
            vehiculos = json.load(archivo)
            if not vehiculos:
                print("No hay ningún vehiculo disponible.")
                return
            for vehiculo in vehiculos:
                print("-" * 50)
                print(f'[{vehiculo["_id_vehiculo"]}] \t')
                print(f'{vehiculo["_marca"]} {vehiculo["_modelo"]}')
                print(f'{vehiculo["_kilometraje"]} km | {vehiculo["_anio"]}')
                print(f'{vehiculo["_precio"]} pesos')
                print("-" * 50)


def seleccionar_vehiculo():
    print("\nSeleccione el filtro:")
    print("0. Todos los vehiculos")
    print("1. Marca")
    print("2. Modelo")
    print("3. Año")
    print("4. Precio")
    filtro = int(input("Ingrese el numero a la opcion correspondiente: \n"))
    if filtro == 0:
        mostrar_vehiculos_disponibles()
    elif filtro == 1:
        opcion = "marca"
        filtro_valor = input(f"Ingrese valor de {opcion} que desea visualizar: \n")
        mostrar_vehiculos_disponibles(marca=filtro_valor, opcion=opcion)
    elif filtro == 2:
        opcion = "modelo"
        filtro_valor = input(f"Ingrese valor de {opcion} que desea visualizar: \n")
        mostrar_vehiculos_disponibles(modelo=filtro_valor, opcion=opcion)
    elif filtro == 3:
        opcion = "anio"
        filtro_valor = input(f"Ingrese valor de {opcion} que desea visualizar: \n")
        mostrar_vehiculos_disponibles(anio=filtro_valor, opcion=opcion)
    elif filtro == 4:
        opcion = "precio"
        filtro_valor = input(
            f"Ingrese valor máximo de {opcion} que desea visualizar: \n"
        )
        mostrar_vehiculos_disponibles(precio=filtro_valor, opcion=opcion)
    else:
        print("Opcion no valida. Por favor, intente de nuevo")
        return

    with open("./vehiculo.json", "r", encoding="utf-8") as archivo:
        vehiculos = json.load(archivo)
        while True:
            id_vehiculo_seleccionado = int(
                input("Ingrese el id correspondiente al vehiculo deseado: \n")
            )
            vehiculo = next(
                (v for v in vehiculos if v["_id_vehiculo"] == id_vehiculo_seleccionado),
                None,
            )
            if vehiculo is None:
                print("Vehiculo no encontrado.")
                continue
            else:
                return id_vehiculo_seleccionado


def borrar_vehiculo(id_vehiculo, filename="./vehiculo.json"):
    with open(filename, "r", encoding="utf-8") as f:
        vehiculos = json.load(f)
        if not vehiculos:
            print("No hay ningún vehiculo registrado para borrar.")
            return

    for idx, obj in enumerate(vehiculos):
        if obj["_id_vehiculo"] == id_vehiculo:
            vehiculos.pop(idx)
            print("Vehiculo borrado exitosamente.")
            break
    else:
        print("Vehiculo no encontrado.")

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(vehiculos, f, indent=4)


def realizar_compra():
    nueva_venta = Venta()
    nueva_venta.id_vehiculo = seleccionar_vehiculo()
    nueva_venta.id_cliente = identificar_cliente()
    guardar_venta(nueva_venta)
    print("Su transacción ha sido creada exitosamente")
    return nueva_venta


def menu():
    while True:
        print("\n" + "-" * 50)
        print("VENTA DE VEHICULOS")
        print("1. Realizar compra")
        print("2. Realizar pago")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            venta_actual = realizar_compra()
            venta_actual.mostrar_detalles_venta()
        elif opcion == "2":
            venta_actual.realizar_pago()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu()
