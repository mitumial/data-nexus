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

  def __init__(self, cliente, nro_cuenta, tipo, fecha_expiracion):
    self.cliente = cliente
    self.nro_cuenta = nro_cuenta
    self.tipo = tipo
    self.fecha_expiracion = fecha_expiracion

  def verificar_validez():
    pass
