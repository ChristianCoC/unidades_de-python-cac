# Clases
class auto:
    marca = "Fiat"
    modelo = "Palio"
    año = 2015


taxi = auto()

print(taxi.marca)
print(taxi.modelo)
print(taxi.año)


class auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año


taxi = auto("Renault", "Clio", 2010)
remis = auto("Volkswagen", "Golf", 2012)
uber = auto("Ford", "Focus", 2018)

print(taxi.marca)
print(remis.marca)
print(uber.marca)


# Herencias
class Auto:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color


class taxi(Auto):
    def __init__(self, marca, modelo, año, color, patente):
        super().__init__(marca, modelo, año, color)
        self.patente = patente

    def presentacion(self):
        return (
            f"Taxi: {self.marca} {self.modelo} {self.año} {self.color} {self.patente}"
        )


class remis(Auto):
    def __init__(self, marca, modelo, año, color, conductor):
        super().__init__(marca, modelo, año, color)
        self.conductor = conductor

    def presentacion(self):
        return f"Remis: {self.marca} {self.modelo} {self.año} {self.color} {self.conductor}"


class uber(Auto):
    def __init__(self, marca, modelo, año, color, dni):
        super().__init__(marca, modelo, año, color)
        self.dni = dni

    def presentacion(self):
        return f"Uber: {self.marca} {self.modelo} {self.año} {self.color} {self.dni}"


auto_taxi = taxi("Renault", "Clio", 2010, "Rojo", "ABC123")
print(auto_taxi.patente)

auto_remis = remis("Volkswagen", "Golf", 2012, "Blanco", "Jorge Peña")
print(auto_remis.conductor)

auto_uber = uber("Ford", "Focus", 2018, "Azul", "12345678")
print(auto_uber.dni)

print(auto_taxi.presentacion())

print(auto_remis.presentacion())

print(auto_uber.presentacion())


# Herencias Multiples
class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni


class Conductor:
    def __init__(self, licencia):
        self.licencia = licencia


class PasajeroConductor(Persona, Conductor):
    def __init__(self, nombre, dni, licencia):
        Persona.__init__(self, nombre, dni)
        Conductor.__init__(self, licencia)

    def presentacion(self):
        return f"Persona: {self.nombre} {self.dni} {self.licencia}"


pasajero_conductor = PasajeroConductor("Jorge", "12345678", "123456789")
print(pasajero_conductor.presentacion())
