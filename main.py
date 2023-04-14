from libro import Libro
from persona import Persona
from autor import Autor
from prestamo import Prestamo
from biblioteca import Biblioteca
import datetime


if __name__ == "__main__":

    fecha = datetime.date(1932, 6, 18)
    libro = Libro("Viaje al fin de la noche",
                  "Louis-Ferdinand Céline", "Novela", "Frances", "Digital", fecha)

    fecha1 = datetime.date(2500, 1, 1)
    libro1 = Libro("Poema de Gilgamesh",
                   "Anonimo", "Epopeya, Poesia", "Acadio", "Fisico", fecha1)

    fecha2 = datetime.date(1957, 6, 12)
    libro2 = Libro("De un castillo a otro",
                   "Louis-Ferdinand Céline", "Novela, Ficcion", "Frances, Ingles", "Digital", fecha2)

    fecha3 = datetime.date(1847, 10, 19)
    libro3 = Libro("Jane Eyre",
                   "Charlotte Brontë", "Novela", "Ingles", "Fisico", fecha3)

    autor = Autor("Louis-Ferdinand Céline", "Francesa", [libro, libro2])

    autor1 = Autor("Charlotte Brontë", "Britanica", [libro3])

    fecha4 = datetime.date(1813, 1, 28)
    libro4 = Libro("The works of Charlotte Brontë",
                   "Charlotte Brontë", "Drama", "Ingles", "Digital", fecha4)

    autor.obras_publicadas.append(libro4)

    fecha5 = datetime.date(1827, 12, 1)
    libro5 = Libro("Glass Town",
                   "Charlotte Brontë", "Novela", "Ingles", "Digital", fecha5)

    autor1.obras_publicadas.append(libro5)

    print("AUTOR")
    for libro in autor.obras_publicadas:
        print(vars(libro))

    print("AUTOR1")
    for libro1 in autor1.obras_publicadas:
        print(vars(libro1))

    print("PRESTAMO")

    fecha_prestamo = datetime.date(2023, 4, 14)
    fecha_vencimiento = datetime.date(2023, 6, 14)
    prestamo = Prestamo([libro4, libro3], autor,
                        fecha_prestamo, fecha_vencimiento)

    for prestamos in prestamo.libros:
        print(vars(prestamos))
