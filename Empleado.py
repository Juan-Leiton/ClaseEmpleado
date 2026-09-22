class Empleado:
    def __init__(self, Nombre, Cargo):
        self.Nombre = Nombre
        self.Cargo = Cargo
        
class Tarea:
    def __init__(self, Nombre, Responsable):
        self.Nombre = Nombre
        self.Responsable = Responsable
        
Empleado = Empleado("Juan Diego","Ing de Soporte")
Tarea = Tarea("Soporte Nivel 3 con su usuario","Juan Diego")
print(Empleado.Nombre, "-", "Tarea.Nombre")

Empleado = Empleado("Juan Camilo","Ing ML")
Tarea = Tarea("General Datasets","Juan Camilo")
print(Empleado.Nombre, "-", "Tarea.Nombre")