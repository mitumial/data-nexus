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
    def __init__(
        self, cantidad, id_cliente, nro_cuenta, tipo, fecha_expiracion, fondos, contraseña
    ):
        super().__init__(cantidad, id_cliente)
        self.nro_cuenta = nro_cuenta
        self.tipo = tipo
        self.fecha_expiracion = fecha_expiracion
        self.fondos = fondos
        self.contraseña = contraseña

    def verificar_validez(self):
        # Verificar longitud del número de tarjeta (debe ser 16 dígitos)
        if not re.match(r"^\d{16}$", str(self.nro_cuenta)):
            print("El número de tarjeta no es válido. Debe tener 16 dígitos.")
            return False

        # Verificar la fecha de expiración
        try:
            fecha_expiracion_dt = datetime.strptime(self.fecha_expiracion, "%m-%Y")
            if fecha_expiracion_dt < datetime.now():
                print("La tarjeta está expirada.")
                return False
        except ValueError:
            print("La fecha de expiración no tiene un formato válido (MM-AAAA).")
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
            raise ValueError(
                "El efectivo operado no es suficiente para realizar el pago"
            )


def registrar_pago(id_cliente, id_vehiculo):
    # Verificar si el cliente existe
    with open("./cliente.json", "r", encoding="utf-8") as archivo:
        clientes = json.load(archivo)
        cliente = next((c for c in clientes if c["_id_cliente"] == id_cliente), None)

    if cliente is None:
        print("Cliente no encontrado.")
        return

    with open("./vehiculo.json", "r", encoding="utf-8") as archivo:
        vehiculos = json.load(archivo)
        vehiculo = next(
            (v for v in vehiculos if v["_id_vehiculo"] == id_vehiculo), None
        )

    if vehiculo is None:
        print("Vehiculo no encontrado.")
        return

    print(f"\nCliente seleccionado: {cliente['_nombre']} {cliente['_apellidos']}")
    print("\nSeleccione el método de pago:")
    print("1. Tarjeta")
    print("2. Efectivo")
    metodo_pago = input("Ingrese la opción de pago: ")

    cantidad = vehiculo["_precio"]
    if metodo_pago == "1":
        nro_cuenta = input("Número de cuenta (16 dígitos): ")
        if metodo_pago == "1":
            print("Seleccione el tipo de tarjeta:")
            print("1. Débito")
            print("2. Crédito")
            tipo_tarjeta = input("Ingrese el tipo de tarjeta: ")

        if tipo_tarjeta == "1":
            tipo = "Débito"
        elif tipo_tarjeta == "2":
            tipo = "Crédito"
        else:
            print("Tipo de tarjeta no válido.")
            return
        fecha_expiracion = input("Fecha de expiración (MM-AAAA): ")
        
        while True:
            contraseña = (input("Ingrese su contraseña (Debe ser de 3 digitos): "))
            if contraseña.isdigit() and len(contraseña) == 3:
                break
            else:
                print("Error: La contraseña debe de contener 3 digitos númericos.")   
        fondos = float(input("Fondos disponibles en la tarjeta: "))

        pago_tarjeta = Tarjeta(
            cantidad, id_cliente, nro_cuenta, tipo, fecha_expiracion, fondos, contraseña
        )

        if pago_tarjeta.verificar_validez():
            if pago_tarjeta.verificar_fondos():
                pago_tarjeta.fondos = pago_tarjeta.fondos - vehiculo["_precio"]
                print(
                    f"Pago con tarjeta realizado con éxito. Sus saldo restante es de: {pago_tarjeta.fondos} pesos"
                )
                return
            else:
                print("Fondos insuficientes en la tarjeta.")
                return
        else:
            print("La tarjeta no es válida.")

    elif metodo_pago == "2":
        efectivo_operado = float(input("Ingrese el efectivo operado: "))
        pago_efectivo = Efectivo(cantidad, id_cliente, efectivo_operado)
        try:
            cambio = pago_efectivo.devolver_cambio()
            print(
                f"Pago en efectivo realizado con éxito. Le devolvemos su cambio de: {cambio}"
            )
            return
        except ValueError as e:
            print(e)
    else:
        print("Opción de pago no válida.")
        return


# Ejemplo de uso:
if __name__ == "__main__":
    registrar_pago()
    #