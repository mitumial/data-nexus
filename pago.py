import json
import re
from datetime import datetime

class Pago:
    def __init__(self, cantidad, id_cliente):
        self.cantidad = cantidad
        self.id_cliente = id_cliente

    def verificar_fondos(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def obtener_cliente(self):
        with open("./cliente.json", "r", encoding="utf-8") as archivo:
            clientes = json.load(archivo)
            for cliente in clientes:
                if cliente["_id_cliente"] == self.id_cliente:
                    return cliente
        return None

class Tarjeta(Pago):
    def __init__(self, cantidad, id_cliente, nro_cuenta, tipo, fecha_expiracion, fondos):
        super().__init__(cantidad, id_cliente)
        self.nro_cuenta = nro_cuenta
        self.tipo = tipo
        self.fecha_expiracion = fecha_expiracion
        self.fondos = fondos

    def verificar_validez(self):
        # Verificar longitud del número de tarjeta (debe ser 16 dígitos)
        if not re.match(r'^\d{16}$', str(self.nro_cuenta)):
            print("El número de tarjeta no es válido. Debe tener 16 dígitos.")
            return False
        
        # Verificar la fecha de expiración
        try:
            fecha_expiracion_dt = datetime.strptime(self.fecha_expiracion, "%Y-%m-%d")
            if fecha_expiracion_dt < datetime.now():
                print("La tarjeta está expirada.")
                return False
        except ValueError:
            print("La fecha de expiración no tiene un formato válido (AAAA-MM-DD).")
            return False

        return True

    def verificar_fondos(self):
        return self.fondos >= self.cantidad

class Efectivo(Pago):
    def __init__(self, cantidad, id_cliente, efectivo_operado):
        super().__init__(cantidad, id_cliente)
        self.efectivo_operado = efectivo_operado

    def devolver_cambio(self):
        if self.efectivo_operado >= self.cantidad:
            return self.efectivo_operado - self.cantidad
        else:
            raise ValueError("El efectivo operado no es suficiente para realizar el pago")

def registrar_pago():
    id_cliente = int(input("Ingrese la ID del cliente: "))

    # Verificar si el cliente existe
    with open("./cliente.json", "r", encoding="utf-8") as archivo:
        clientes = json.load(archivo)
        cliente = next((c for c in clientes if c["_id_cliente"] == id_cliente), None)
    
    if cliente is None:
        print("Cliente no encontrado.")
        return

    print(f"\nCliente seleccionado: {cliente['_nombre']} {cliente['_apellidos']}")
    print("\nSeleccione el método de pago:")
    print("1. Tarjeta")
    print("2. Efectivo")
    metodo_pago = input("Ingrese la opción de pago: ")

    cantidad = float(input("Ingrese la cantidad a pagar: "))

    if metodo_pago == "1":
        nro_cuenta = input("Número de cuenta (16 dígitos): ")
        tipo = input("Tipo de tarjeta (por ejemplo, Visa, MasterCard): ")
        fecha_expiracion = input("Fecha de expiración (AAAA-MM-DD): ")
        fondos = float(input("Fondos disponibles en la tarjeta: "))

        pago_tarjeta = Tarjeta(cantidad, id_cliente, nro_cuenta, tipo, fecha_expiracion, fondos)

        if pago_tarjeta.verificar_validez():
            if pago_tarjeta.verificar_fondos():
                print("Pago con tarjeta realizado con éxito.")
            else:
                print("Fondos insuficientes en la tarjeta.")
        else:
            print("La tarjeta no es válida.")
    
    elif metodo_pago == "2":
        efectivo_operado = float(input("Ingrese el efectivo operado: "))
        pago_efectivo = Efectivo(cantidad, id_cliente, efectivo_operado)
        try:
            cambio = pago_efectivo.devolver_cambio()
            print(f"Pago en efectivo realizado con éxito. El cambio a devolver es: {cambio}")
        except ValueError as e:
            print(e)
    else:
        print("Opción de pago no válida.")

# Ejemplo de uso:
if __name__ == "__main__":
    registrar_pago()
