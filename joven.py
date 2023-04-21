from autor import Autor
from libro import Libro
import time

class Autor_joven(Autor):
    def crea_libro(self, titulo, sinopsis, genero, idioma, formato, fecha_publicacion):
        libro = Libro(titulo, sinopsis, genero, idioma,
                      formato, fecha_publicacion)
        self.obras_publicadas.append(libro)
        time.sleep(8)
        return libro
