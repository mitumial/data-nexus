class Pago:
    cantidad = float

    def __init__(self, cantidad):
        self.id_venta = cantidad

    def verificar_fondos():
        pass


class Tarjeta(Pago):
    cliente = Cliente
    nro_cuenta = int
    tipo = str
    fecha_expiracion = str
    fondos = int

    def __init__(self, cliente, nro_cuenta, tipo, fecha_expiracion):
        self.cliente = cliente
        self.nro_cuenta = nro_cuenta
        self.tipo = tipo
        self.fecha_expiracion = fecha_expiracion

    def verificar_validez():
        pass


class Efectivo(Pago):
    efectivo_operado = float

    def __init__(self, efectivo_operado):
        self.efectivo_operado = efectivo_operado

    def devolver_cambio():
        pass
