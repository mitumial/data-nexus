from datetime import datetime as dt
import uuid
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

    def __init__(self, cliente=None, vehiculo=None):
        self._id_venta = str(uuid.uuid4())
        self._fecha = dt.now().strftime("%d-%m-%Y")
        self._estado = "No pagado"
        self.cliente = cliente
        self.vehiculo = vehiculo

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
        self.cliente
        self.vehiculo

    def generar_factura(self):
        pass

    def calcular_total(self):
        pass

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

    def cancelar_venta(self):
        pass


mySale = Venta()

mySale.fecha = "11-15-20"
print(mySale.fecha)
