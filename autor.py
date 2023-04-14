from persona import Persona

class Autor(Persona):
    id = int
    nacionalidad = str
    genero = str
    obras_publicadas = []
    
    def __init__(self, nombre, nacionalidad, obras_publicadas):
        super().__init__(nombre)
        self.nacionalidad = nacionalidad
        self.obras_publicadas = obras_publicadas
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Nacionalidad: {self.nacionalidad}, Obras publicadas: {self.obras_publicadas}"
