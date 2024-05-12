class Vehiculo:
    
    def __init__(self, id_vehiculo=None, marca=None, modelo=None, año=None, placa=None, color=None, combustible=None, transmision=None, cilindraje=None, kilometraje=None, puertas=None, alarma=bool, sensor=bool, precio=None):
        self.id_vehiculo= id_vehiculo
        self.marca= marca
        self.modelo= modelo
        self.año= año
        self.placa= placa
        self.color= color
        self.combustible= combustible
        self.transmision= transmision
        self.cilindraje= cilindraje
        self.kilometraje= kilometraje
        self.puertas= puertas
        self.alarma= alarma
        self.sensor= sensor
        self.precio = precio
        pass
