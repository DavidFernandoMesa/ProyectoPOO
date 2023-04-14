import datetime


class Prestamo:
    id = int
    libros = []
    persona = str
    fecha_prestamo = datetime.date
    fecha_vencimiento = datetime.date

    def __init__(self, libros, persona, fecha_prestamo, fecha_vencimiento):
        self.libros = libros
        self.persona = persona
        self.fecha_prestamo = fecha_prestamo
        self.fecha_vencimiento = fecha_vencimiento
