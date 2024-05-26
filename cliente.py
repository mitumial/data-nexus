import re
import json

class Cliente:
    
    clientes_inventario = []

    def __init__(self, nombre=None, apellidos=None, documento=None, edad=None, genero=None, direccion=None, email=None, celular=None, vehiculos_comprados=None):
        if not self.clientes_inventario:
            self._id_cliente = 0
        else:
            self._id_cliente = self.clientes_inventario[-1]._id_cliente + 1  
        self._nombre = nombre
        self._apellidos = apellidos
        self._documento = documento
        self._edad = edad
        self._genero = genero
        self._direccion = direccion
        self._email = email
        self._celular = celular
        self._vehiculos_comprados = vehiculos_comprados if vehiculos_comprados is not None else []

        self.clientes_inventario.append(self)

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
        self._direccion = input("Ingrese la dirección dle cliente: \n")
        self._email = input("Ingrese la direccion de correo electronico del cliente: \n")
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
   # if cliente.nombre and cliente.apellidos and cliente.documento and cliente.edad and cliente.genero and cliente.direccion and cliente.email and cliente.celular:
    Cliente.clientes_inventario.append(cliente)
    guardar_cliente(cliente)
    print("Cliente agregado exitosamente.")
    #else:
        #print("Error: Datos del cliente incompletos o incorrectos.")

    

def mostrar_todos_los_clientes():
    if not Cliente.clientes_inventario:
        print("No hay ningún cliente registrado.")
        return
    for cliente in Cliente.clientes_inventario:
        cliente.mostrar_detalles_cliente()


def buscar_cliente_por_id(id_cliente):
    for cliente in Cliente.clientes_inventario:
        if cliente.id_cliente == id_cliente:
            return cliente
    return None


def eliminar_cliente():
    if not Cliente.clientes_inventario:
        print("No hay ningún cliente registrado para borrar.")
        return

    id_cliente = int(input("Ingrese la ID del cliente que desea eliminar: "))
    cliente = buscar_cliente_por_id(id_cliente)

    if cliente:
        confirmacion = input("¿Está seguro de que desea borrar este cliente? (s/n): ").lower()
        if confirmacion == "s":
            Cliente.clientes_inventario.remove(cliente)
            print("Cliente borrado exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print("Cliente no encontrado.")

def cargar_cliente(filename="./cliente.json"):
    with open(filename, "r") as archivo:
        clientes = json.load(archivo)

    for cliente in clientes:
        Cliente.clientes_inventario.append(Cliente(cliente["_nombre"], cliente["_apellidos"], cliente["_documento"], cliente["_edad"], cliente["_genero"], cliente["_direccion"], cliente["_email"], cliente["_celular"], cliente["_vehiculos_comprados"]))       
def guardar_cliente(cliente, filename="./cliente.json"):
    with open(filename, "r+") as archivo:
        archivo_datos = json.load(archivo)
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


cargar_cliente()
menu()

