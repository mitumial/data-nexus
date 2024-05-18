class Cliente:
    def __init__(self, id_cliente=None, nombre=None, apellidos=None, documento=None, edad=None, genero=None, direccion=None, email=None, celular=None, vehiculos_comprados=None):
        # Inicializa los atributos del cliente
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellidos = apellidos
        self.documento = documento
        self.edad = edad
        self.genero = genero
        self.direccion = direccion
        self.email = email
        self.celular = celular
        # Inicializa vehiculos_comprados como una lista vacía si no se proporciona
        self.vehiculos_comprados = vehiculos_comprados if vehiculos_comprados is not None else []

    def ingresar_cliente(self):
        print("-" * 30)
        print("INGRESAR DATOS DEL CLIENTE:")
        self.id_cliente = int(input("Ingrese la id del cliente: \n"))
        self.nombre = input("Ingrese los nombres del cliente: \n")
        self.apellidos = input("Ingrese los apellidos del cliente: \n")
        self.documento = int(input("Ingrese el numero de documento del cliente: \n"))
        self.edad = int(input("Ingrese la edad del cliente: \n"))
        self.genero = input("Ingrese el genero del cliente: (Masculino/Femenino): \n")
        self.direccion = input("Ingrese la dirección del cliente: \n")
        self.email = input("Ingrese la direccion de correo electronico del cliente: \n")
        self.celular = int(input("Ingrese el número de celular del cliente: \n"))
        self.vehiculos_comprados = []  # Inicializa como lista vacía al ingresar un cliente

    def mostrar_detalles_cliente(self):
        print("-" * 30)
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
    clientes.append(cliente)
    print("Cliente agregado exitosamente.")


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
