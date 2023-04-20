import datetime

class Libro:
    id = int
    titulo = str
    autor = str
    genero = str
    sinopsis = str
    idioma = str
    formato = str
    anio_publicacion = datetime.date

    def __init__(self, titulo, autor, genero, idioma, formato, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.idioma = idioma
        self.formato = formato
        self.anio_publicacion = anio_publicacion
        
    def __str__(self):
        if self.sinopsis:
            return f"Título: {self.titulo}, Sinopsis: {self.sinopsis}, Genero: {self.genero}, Idioma: {self.idioma}, Formato: {self.formato}, Anio publicacion: {self.anio_publicacion}"
        else:
            return f"Título: {self.titulo}, Autor: {self.autor}, Genero: {self.genero}, Idioma: {self.idioma}, Formato: {self.formato}, Anio publicacion: {self.anio_publicacion}"
