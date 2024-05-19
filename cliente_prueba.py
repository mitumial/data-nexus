import re
import uuid

class Cliente:
    def __init__(self, id_cliente=None, nombre=None, apellidos=None, documento=None, edad=None, genero=None, direccion=None, email=None, celular=None, vehiculos_comprados=None):
        self.id_cliente = id_cliente if id_cliente is not None else uuid.uuid4().int
        self.nombre = nombre
        self.apellidos = apellidos
        self.documento = documento
        self._edad = None
        self.edad = edad
        self._genero = None
        self.genero = genero
        self.direccion = direccion
        self._email = None
        self.email = email
        self._celular = None
        self.celular = celular
        self.vehiculos_comprados = vehiculos_comprados if vehiculos_comprados is not None else []

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        if value is not None:
            if 0 < value < 120:
                self._edad = value
            else:
                raise ValueError("La edad debe estar entre 1 y 119 años.")
        else:
            self._edad = value

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        if value is not None:
            if value.lower() in ["masculino", "femenino"]:
                self._genero = value.lower().capitalize()
            else:
                raise ValueError("El género debe ser 'Masculino' o 'Femenino'.")
        else:
            self._genero = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value is not None:
            if re.match(r"^\w+@\w+\.\w{2,3}$", value):
                self._email = value
            else:
                raise ValueError("El correo electrónico no es válido.")
        else:
            self._email = value

    @property
    def celular(self):
        return self._celular

    @celular.setter
    def celular(self, value):
        if value is not None:
            if re.match(r"^\d{10}$", str(value)):
                self._celular = value
            else:
                raise ValueError("El número de celular debe tener 10 dígitos.")
        else:
            self._celular = value

    def ingresar_cliente(self):
        print("-" * 30)
        print("INGRESAR DATOS DEL CLIENTE:")
        self.nombre = input("Ingrese los nombres del cliente: \n")
        self.apellidos = input("Ingrese los apellidos del cliente: \n")
        self.documento = int(input("Ingrese el numero de documento del cliente: \n"))
        try:
            self.edad = int(input("Ingrese la edad del cliente: \n"))
        except ValueError as e:
            print(f"Error: {e}")
            return

        try:
            self.genero = input("Ingrese el genero del cliente (Masculino/Femenino): \n")
        except ValueError as e:
            print(f"Error: {e}")
            return

        direccion_tipo = input("Ingrese el tipo de dirección (Calle/Carrera): \n")
        direccion_numero = input("Ingrese el número de la dirección: \n")
        self.direccion = f"{direccion_tipo} {direccion_numero}"

        try:
            self.email = input("Ingrese la direccion de correo electronico del cliente: \n")
        except ValueError as e:
            print(f"Error: {e}")
            return

        try:
            self.celular = int(input("Ingrese el número de celular del cliente: \n"))
        except ValueError as e:
            print(f"Error: {e}")
            return

        self.vehiculos_comprados = []

    def mostrar_detalles_cliente(self):
        print("/","-" * 30, "/")
        print("DETALLES DEL CLIENTE:")
        print("ID del Cliente:", self.id_cliente)
        print("Nombre:", self.nombre)
        print("Apellidos:", self.apellidos)
        print("Documento:", self.documento)
        print("Edad:", self.edad)
        print("Género:", self.genero)
        print("Dirección:", self.direccion)
        print("Email:", self.email)
        print("Celular:", self.celular)
        print("Vehículos Comprados:", self.vehiculos_comprados)


def agregar_cliente(clientes):
    cliente = Cliente()
    cliente.ingresar_cliente()
    if cliente.nombre and cliente.apellidos and cliente.documento and cliente.edad and cliente.genero and cliente.direccion and cliente.email and cliente.celular:
        clientes.append(cliente)
        print("Cliente agregado exitosamente.")
    else:
        print("Error: Datos del cliente incompletos o incorrectos.")


def mostrar_todos_los_clientes(clientes):
    if not clientes:
        print("No hay ningún cliente registrado.")
        return
    for cliente in clientes:
        cliente.mostrar_detalles_cliente()


def buscar_cliente_por_id(clientes, id_cliente):
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            return cliente
    return None


def eliminar_cliente(clientes):
    if not clientes:
        print("No hay ningún cliente registrado para borrar.")
        return

    id_cliente = int(input("Ingrese la ID del cliente que desea eliminar: "))
    cliente = buscar_cliente_por_id(clientes, id_cliente)
    
    if cliente:
        confirmacion = input("¿Está seguro de que desea borrar este cliente? (s/n): ").lower()
        if confirmacion == "s":
            clientes.remove(cliente)
            print("Cliente borrado exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print("Cliente no encontrado.")


def menu():
    clientes = []
    
    while True:
        print("\n" + "-" * 50)
        print("MENÚ DE OPCIONES")
        print("1. Ingresar cliente")
        print("2. Mostrar detalles de todos los clientes")
        print("3. Eliminar cliente")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente(clientes)
        elif opcion == "2":
            mostrar_todos_los_clientes(clientes)
        elif opcion == "3":
            eliminar_cliente(clientes)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


# Ejecutar el menú
menu()
