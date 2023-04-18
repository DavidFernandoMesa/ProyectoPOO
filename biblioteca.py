class Biblioteca:
    id = int
    lista_libros = []
    personas = []

    def __init__(self, lista_libros, personas):
        self.lista_libros = lista_libros
        self.personas = personas
        
    def agregar_libro(self, libro):
        self.lista_libros.append(libro)

    def eliminar_libro(self, libro):
        if libro in self.lista_libros:
            self.lista_libros.remove(libro)

    def agregar_persona(self, persona):
        self.personas.append(persona)

    def eliminar_persona(self, persona):
        if persona in self.personas:
            self.personas.remove(persona)
