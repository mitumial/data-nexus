class Cliente:
    id_cliente = int
    nombre = str
    apellidos = str
    documento = int
    edad = int
    genero = str
    direccion = str
    email = str
    celular = int
    vehiculos_comprados = list
    
    def __init__(self, id_cliente, nombre, apellidos, documento, edad, genero, direccion, email, celular, vehiculos_comprados) -> None:
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellidos = apellidos
        self.documento = documento
        self.edad = edad
        self.genero = genero
        self.direccion = direccion
        self.email = email
        self.celular = celular
        self.vehiculos_comprados = vehiculos_comprados
        
    def ingresar_cliente(self):
        print("-"*30)
        print("INGRESAR DATOS DEL CLIENTE:")
        self.id_cliente = int(input("Ingrese la id del cliente: \n"))
        self.nombre = input("Ingrese los nombres del cliente: \n")
        self.apellidos = input("Ingrese los apellidos del cliente: \n")
        self.documento = int(input("Ingrese el numero de documento del cliente: \n"))
        self.edad = int(input("Ingrese la edad del cliente: \n"))
        self.genero = input("Ingrese el genero del cliente : (Masculino/Femenino): \n")
        self.direccion = int(input("Ingrese la dirección dle cliente: \n"))
        self.email = input("Ingrese la direccion de correo electronico del cliente: \n")
        self.celular = int(input("Ingrese el número de celular del cliente: \n"))
        self.vehiculos_comprados = []
        
    def mostrar_detalles_cliente():
        pass
    
    def borrar_cliente():
        pass    
        
        