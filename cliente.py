import re
import json


class Cliente:

    def __init__(
        self,
        id_cliente=None,
        nombre=None,
        apellidos=None,
        documento=None,
        edad=None,
        genero=None,
        direccion=None,
        email=None,
        celular=None,
    ):
        with open("./cliente.json", "r", encoding="utf-8") as archivo:
            clientes = json.load(archivo)
            if id_cliente is not None:
                self._id_cliente = id_cliente
            elif not clientes and (id_cliente is None):
                self._id_cliente = 0
            else:
                self._id_cliente = clientes[-1]["_id_cliente"] + 1
        self._nombre = nombre
        self._apellidos = apellidos
        self._documento = documento
        self._edad = edad
        self._genero = genero
        self._direccion = direccion
        self._email = email
        self._celular = celular
        self._vehiculos_comprados = (
            vehiculos_comprados if vehiculos_comprados is not None else []
        )

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        if 0 < value < 120:
            self._edad = value
        else:
            raise ValueError("La edad debe estar entre 1 y 119 años.")

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        if value.lower() in ["masculino", "femenino"]:
            self._genero = value.lower().capitalize()
        else:
            raise ValueError("El género debe ser 'Masculino' o 'Femenino'.")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if re.match(r"^\w+@\w+\.\w{2,3}$", value):
            self._email = value
        else:
            raise ValueError("El correo electrónico no es válido.")

    @property
    def celular(self):
        return self._celular

    @celular.setter
    def celular(self, value):
        if re.match(r"^\d{10}$", str(value)):
            self._celular = value
        else:
            raise ValueError("El número de celular debe tener 10 dígitos.")

    def ingresar_cliente(self):
        print("-" * 30)
        print("INGRESAR DATOS DEL CLIENTE:")
        self._nombre = input("Ingrese los nombres del cliente: \n")
        self._apellidos = input("Ingrese los apellidos del cliente: \n")
        self._documento = int(input("Ingrese el numero de documento del cliente: \n"))
        self._edad = int(input("Ingrese la edad del cliente: \n"))
        self._genero = input("Ingrese el genero del cliente : (Masculino/Femenino): \n")
        self._direccion = input("Ingrese la dirección del cliente: \n")
        self._email = input(
            "Ingrese la direccion de correo electronico del cliente: \n"
        )
        self._celular = int(input("Ingrese el número de celular del cliente: \n"))

        self._vehiculos_comprados = []

    def mostrar_detalles_cliente(self):
        print("/", "-" * 30, "/")
        print("DETALLES DEL CLIENTE:")
        print("ID del Cliente:", self._id_cliente)
        print("Nombre:", self._nombre)
        print("Apellidos:", self._apellidos)
        print("Documento:", self._documento)
        print("Edad:", self.edad)
        print("Género:", self.genero)
        print("Dirección:", self._direccion)
        print("Email:", self._email)
        print("Celular:", self._celular)
        print("Vehículos Comprados:", self._vehiculos_comprados)


def agregar_cliente():
    cliente = Cliente()
    cliente.ingresar_cliente()
    guardar_cliente(cliente)
    print("Cliente agregado exitosamente.")


def mostrar_todos_los_clientes(filename="./cliente.json"):
    with open(filename, "r", encoding="utf-8") as archivo:
        clientes = json.load(archivo)
        if not clientes:
            print("No hay ningún cliente registrado.")
            return
        for cliente in clientes:
            nuevo_cliente = Cliente(
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
            nuevo_cliente.mostrar_detalles_cliente()


def eliminar_cliente(filename="./cliente.json"):
    with open(filename, "r", encoding="utf-8") as f:
        clientes = json.load(f)
        if not clientes:
            print("No hay ningún cliente registrado para borrar.")
            return

        id_cliente = int(input("Ingrese la ID del cliente que desea eliminar: "))

        confirmacion = input(
            "¿Está seguro de que desea borrar este cliente? (s/n): "
        ).lower()

        if confirmacion == "s":
            for idx, obj in enumerate(clientes):
                if obj["_id_cliente"] == id_cliente:
                    clientes.pop(idx)
                    print("Cliente borrado exitosamente.")
                    break
            else:
                print("Cliente no encontrado.")
        else:
            print("Operación cancelada.")

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(clientes, f, indent=4)


def guardar_cliente(cliente, filename="./cliente.json"):
    with open(filename, "r+", encoding="utf-8") as archivo:
        try:
            archivo_datos = json.load(archivo)
        except json.JSONDecodeError:
            archivo_datos = []
        archivo_datos.append(cliente.__dict__)
        archivo.seek(0)
        json.dump(archivo_datos, archivo, indent=4)


def menu():
    while True:
        print("\n" + "-" * 50)
        print("MENÚ DE OPCIONES")
        print("1. Ingresar cliente")
        print("2. Mostrar detalles de todos los clientes")
        print("3. Eliminar cliente")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            mostrar_todos_los_clientes()
        elif opcion == "3":
            eliminar_cliente()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu()

#
