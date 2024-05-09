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
        
    def ingresar_cliente():
        pass
    
    def mostrar_detalles_cliente():
        pass
    
    def borrar_cliente():
        pass    
        
        