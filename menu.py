import json
from venta import Venta, guardar_venta, seleccionar_vehiculo, identificar_cliente, borrar_vehiculo
from pago import registrar_pago
from cliente import agregar_cliente, eliminar_cliente, mostrar_todos_los_clientes
from vehiculo import agregar_vehiculo, eliminar_vehiculo, mostrar_todos_los_vehiculos


def realizar_compra():
    nueva_venta = Venta()
    nueva_venta.id_vehiculo = seleccionar_vehiculo()
    nueva_venta.id_cliente = identificar_cliente()
    guardar_venta(nueva_venta)
    print("Su transacción ha sido creada exitosamente")
    return nueva_venta


def manejo_clientes():
    while True:
        print("\n" + "-" * 50)
        print("MANEJO DE CLIENTES")
        print("1. Agregar cliente")
        print("2. Eliminar cliente")
        print("3. Mostrar todos los clientes")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            eliminar_cliente()
        elif opcion == "3":
            mostrar_todos_los_clientes()
        elif opcion == "4":    
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


def manejo_vehiculos():
    while True:
        print("\n" + "-" * 50)
        print("MANEJO DE VEHÍCULOS")
        print("1. Agregar vehículo")
        print("2. Eliminar vehículo")
        print("3. Mostras todos los vehiculos")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_vehiculo()
        elif opcion == "2":
            eliminar_vehiculo()
        elif opcion == "3":
            mostrar_todos_los_vehiculos()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


def manejo_ventas():
    while True:
        print("\n" + "-" * 50)
        print("MANEJO DE VENTAS")
        print("1. Realizar compra")
        print("2. Realizar pago")
        print("3. Cancelar compra")
        print("4. Mostrar detalles de la venta")
        print("5. Volver al menú principal")

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
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


def menu_principal():
    while True:
        print("\n" + "-" * 50)
        print("MENÚ PRINCIPAL")
        print("1. Manejo de clientes")
        print("2. Manejo de vehículos")
        print("3. Manejo de ventas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            manejo_clientes()
        elif opcion == "2":
            manejo_vehiculos()
        elif opcion == "3":
            manejo_ventas()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu_principal()
