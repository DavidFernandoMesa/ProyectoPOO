from libro import Libro
class Biblioteca:
    id = int
    libros = []
    __personas = []

    def __init__(self, libros, personas):
        self.libros = libros
        self.__personas = personas

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)

    def listar_personas(self):
        for persona in self.__personas:
            print(persona)

    def agregar_persona(self, persona):
        self.__personas.append(persona)

    def eliminar_persona(self, persona):
        if persona in self.__personas:
            self.__personas.remove(persona)

    def __str__(self):
        resultado = f"Nombre: {self.nombre}\n, Nacionalidad: {self.nacionalidad}\n Libros: {self.libros}"
        resultado += "Libros:\n"
        for libro in self.libros:
            resultado += f"\t{libro}\n"
        resultado += "Persona:\n"
        for persona in self.__personas:
            resultado += f"\t{persona}\n"
        return resultado