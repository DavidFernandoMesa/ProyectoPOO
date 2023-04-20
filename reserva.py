import datetime
from libro import Libro


class Reserva_de_libros(Libro):
    id = int
    libros = []
    persona = str
    fecha_prestamo = datetime.date
    fecha_vencimiento = datetime.date
    reservado = False

    def __init__(self, libros, persona, fecha_prestamo, fecha_vencimiento):
        self.libros = libros
        self.persona = persona
        self.fecha_prestamo = fecha_prestamo
        self.fecha_vencimiento = fecha_vencimiento
        
    def reservar(self):
        self.reservado = True

    def cancelar_reserva(self):
        self.reservado = False
    
    def registrar_devolucion(self):
        if self.reservado:
            print("El libro {} de {} ha sido devuelto".format(
                self.titulo, self.autor))
            self.reservado = False
        else:
            print("El libro {} de {} no ha sido reservado".format(
                self.titulo, self.autor))
