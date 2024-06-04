import json
from venta import Venta, guardar_venta, seleccionar_vehiculo, identificar_cliente, borrar_vehiculo
from pago import registrar_pago
from cliente import agregar_cliente, eliminar_cliente
from vehiculo import agregar_vehiculo, eliminar_vehiculo


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
        print("VENTA DE VEHICULOS --DATANEXUS--")
        print("1. Realizar compra")
        print("2. Realizar pago")
        print("3. Cancelar compra")
        print("4. Mostrar detalles de la venta")
        print("5. Agregar cliente")
        print("6. Eliminar cliente")
        print("7. Agregar vehículo")
        print("8. Eliminar vehículo")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            realizar_compra()
        elif opcion == "2":
            id_venta = int(input("Ingrese el ID de la venta para realizar el pago: "))
            with open("./venta.json", "r", encoding="utf-8") as archivo:
                ventas = json.load(archivo)
                venta_actual = next((v for v in ventas if v["_id_venta"] == id_venta), None)
                if venta_actual:
                    venta_obj = Venta(
                        id_venta=venta_actual["_id_venta"],
                        fecha=venta_actual["_fecha"],
                        estado=venta_actual["_estado"],
                        id_cliente=venta_actual["_id_cliente"],
                        id_vehiculo=venta_actual["_id_vehiculo"]
                    )
                    venta_obj.realizar_pago()
                else:
                    print("Venta no encontrada.")
        elif opcion == "3":
            id_venta = int(input("Ingrese el ID de la venta para cancelar: "))
            with open("./venta.json", "r", encoding="utf-8") as archivo:
                ventas = json.load(archivo)
                venta_actual = next((v for v in ventas if v["_id_venta"] == id_venta), None)
                if venta_actual:
                    venta_obj = Venta(
                        id_venta=venta_actual["_id_venta"],
                        fecha=venta_actual["_fecha"],
                        estado=venta_actual["_estado"],
                        id_cliente=venta_actual["_id_cliente"],
                        id_vehiculo=venta_actual["_id_vehiculo"]
                    )
                    venta_obj.cancelar_compra()
                else:
                    print("Venta no encontrada.")
        elif opcion == "4":
            id_venta = int(input("Ingrese el ID de la venta para mostrar detalles: "))
            with open("./venta.json", "r", encoding="utf-8") as archivo:
                ventas = json.load(archivo)
                venta_actual = next((v for v in ventas if v["_id_venta"] == id_venta), None)
                if venta_actual:
                    venta_obj = Venta(
                        id_venta=venta_actual["_id_venta"],
                        fecha=venta_actual["_fecha"],
                        estado=venta_actual["_estado"],
                        id_cliente=venta_actual["_id_cliente"],
                        id_vehiculo=venta_actual["_id_vehiculo"]
                    )
                    venta_obj.mostrar_detalles_venta()
                else:
                    print("Venta no encontrada.")
        elif opcion == "5":
            agregar_cliente()
        elif opcion == "6":
            eliminar_cliente()
        elif opcion == "7":
            agregar_vehiculo()
        elif opcion == "8":
            eliminar_vehiculo()
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu()
