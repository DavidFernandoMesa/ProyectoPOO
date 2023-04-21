from autor import Autor
from libro import Libro
import time

class Autor_adulto(Autor):
    def crea_libro(self, titulo, sinopsis, genero, idioma, formato, fecha_publicacion):
        libro = Libro(titulo, sinopsis, genero, idioma,
                      formato, fecha_publicacion)
        self.obras_publicadas.append(libro)
        time.sleep(6)
        return libro
