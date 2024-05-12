class Vehiculo:
        id_vehiculo= int
        marca= str
        modelo= str
        año= int
        placa= str
        color= str
        combustible= str
        transmision= str
        cilindraje= float
        kilometraje= float
        puertas= int
        alarma= bool
        sensor= bool
        precio = float

        def __init__(self, id_vehiculo, marca, modelo, año, placa, color, combustible, transmision, cilindraje, kilometraje, puertas, alarma, sensor, precio) -> None:
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