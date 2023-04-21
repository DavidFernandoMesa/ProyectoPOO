from abc import abstractmethod
from persona import Persona
from libro import Libro
import time


class Autor(Persona):
    id = int
    nacionalidad = str
    genero = str
    obras_publicadas = []

    def __init__(self, nombre, edad, nacionalidad, obras_publicadas):
        super().__init__(nombre)
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.obras_publicadas = obras_publicadas

    @abstractmethod
    def crea_libro(self, titulo, sinopsis, genero, idioma, formato, fecha_publicacion):
        pass

    def __str__(self):
        return f"Nombre: {self.nombre}, Nacionalidad: {self.nacionalidad}, obras publicadas: {self.obras_publicadas}, edad {self.edad}"
