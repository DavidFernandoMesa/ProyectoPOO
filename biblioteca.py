class Biblioteca:
    id = int
    lista_libros = []
    personas = []

    def __init__(self, lista_libros, personas):
        self.lista_libros = lista_libros
        self.personas = personas
