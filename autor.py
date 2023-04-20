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

    def crea_libro(self, titulo, sinopsis, genero, idioma, formato, fecha_publicacion):
        libro = Libro(titulo, self.nombre, sinopsis, genero, idioma,
                      formato, fecha_publicacion)
        self.obras_publicadas.append(libro)

        if self.edad < 12:
            time.sleep(10)
            return libro
        elif self.edad >= 12 and self.edad < 20:
            time.sleep(7)
            return libro
        elif self.edad >= 20 and self.edad < 40:
            time.sleep(5)
            return libro
        else:
            time.sleep(2)
            return libro

    def __str__(self):
        return f"Nombre: {self.nombre}, Nacionalidad: {self.nacionalidad}, obras publicadas: {self.obras_publicadas}, edad {self.edad}"
