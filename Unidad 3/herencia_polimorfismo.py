# Herencia y Polimorfismo
class Empleado:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
    def salario(self):
        pass
    
class EmpleadoFullTime(Empleado):
    def __init__(self, nombre, apellido, sueldo):
        super().__init__(nombre, apellido)
        self.sueldo = sueldo
    
    def salario(self):
        return self.sueldo
    
class EmpleadoPartTime(Empleado):
    def __init__(self, nombre, apellido, horas, valor_hora):
        super().__init__(nombre, apellido)
        self.horas = horas
        self.valor_hora = valor_hora
    
    def salario(self):
        return self.horas * self.valor_hora
    
empleado_1 = EmpleadoFullTime("Carlos", "Perez", 2000)
empleado_2 = EmpleadoPartTime("Andres", "Lara", 30, 15)

print(empleado_1.salario())
print(empleado_2.salario())
    
    